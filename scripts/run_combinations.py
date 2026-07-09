#!/usr/bin/env python3
"""
Combination engine: filter parts against config constraints AND compute the
derived metrics + cost for a combination.

Loads the parts data (data/parts/*.json), the config table (data/configs.json),
the conditions (data/scenario.json), the derived-parameter definitions/constants
(data/metrics.json), and cost adders (data/costs.json).

- Constraint filtering: which parts qualify for each config slot (`null` = none).
- Metrics: for a chosen combination, compute thermal load, AC power/duty (from the
  AC part + thermal load), daily energy, array/battery sizing, autonomy, and a
  PASS/WARN/FAIL feasibility verdict.
- Cost: total system cost from part prices x quantities + cost adders.

This module is the shared engine imported by solve.py and rank.py.

Usage:
  python3 scripts/run_combinations.py                 # qualifying parts + combo count per config
  python3 scripts/run_combinations.py --table         # config x category constraint table
  python3 scripts/run_combinations.py --metrics       # metrics + cost for each config's representative combo
  python3 scripts/run_combinations.py --config C6 --enumerate 5
  python3 scripts/run_combinations.py --check         # validate constraint fields against spec definitions

Standard library only (Python 3.8+).
"""
import argparse
import json
import itertools
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PARTS_DIR = DATA / "parts"
SERIES_FOR_BUS = {12: 4, 24: 8, 48: 16}


# ---------- loading ----------

def load_json(name):
    return json.loads((DATA / name).read_text())


def load_categories():
    cats = {}
    for f in sorted(PARTS_DIR.glob("*.json")):
        obj = json.loads(f.read_text())
        cats[obj["category"]] = {"specs": obj.get("specs", {}), "parts": obj.get("parts", [])}
    return cats


def load_configs():
    return load_json("configs.json")


def load_scenario():
    return load_json("scenario.json")


def load_metric_constants():
    return {k: v["value"] for k, v in load_json("metrics.json")["constants"].items()}


def load_costs():
    return load_json("costs.json")


def sval(scenario, path):
    section, field = path.split(".")
    return scenario[section][field]["value"]


# ---------- constraint matching ----------

def _as_number(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _scalar_eq(a, b):
    na, nb = _as_number(a), _as_number(b)
    if na is not None and nb is not None:
        return na == nb
    return a == b


def match_field(part_value, requirement):
    if isinstance(requirement, dict):
        for op, want in requirement.items():
            if op == "min":
                n = _as_number(part_value)
                if n is None or n < want:
                    return False
            elif op == "max":
                n = _as_number(part_value)
                if n is None or n > want:
                    return False
            elif op == "eq":
                if not _scalar_eq(part_value, want):
                    return False
            elif op == "ne":
                if _scalar_eq(part_value, want):
                    return False
            elif op == "in":
                if not any(_scalar_eq(part_value, w) for w in want):
                    return False
            elif op == "contains":
                seq = part_value if isinstance(part_value, list) else [part_value]
                if want not in seq:
                    return False
            else:
                raise ValueError(f"unknown operator '{op}'")
        return True
    if isinstance(part_value, list):
        return requirement in part_value
    return _scalar_eq(part_value, requirement)


def matches(part, constraints):
    for field, req in constraints.items():
        if field not in part:
            return False
        if not match_field(part[field], req):
            return False
    return True


def qualifying_parts(category_parts, constraints):
    return [p for p in category_parts if matches(p, constraints)]


# ---------- combinations ----------

def slot_options(cfg, cats):
    """{category: [qualifying parts]} for non-null slots; None for null slots."""
    out = {}
    for cat in load_configs()["part_categories"]:
        cell = cfg["constraints"].get(cat)
        out[cat] = None if cell is None else qualifying_parts(cats.get(cat, {}).get("parts", []), cell)
    return out


def pick_combo(cfg, cats, overrides=None):
    """First qualifying part per slot (or an override id); None for null slots."""
    overrides = overrides or {}
    combo = {}
    for cat, opts in slot_options(cfg, cats).items():
        if opts is None:
            combo[cat] = None
        elif cat in overrides:
            combo[cat] = next((p for p in opts if p["id"] == overrides[cat]), None)
        else:
            combo[cat] = opts[0] if opts else None
    return combo


def iter_combos(cfg, cats):
    """Yield every full combination (dict cat->part or None) for a config."""
    opts = slot_options(cfg, cats)
    active = [(c, v) for c, v in opts.items() if v is not None]
    cats_order = [c for c, _ in active]
    for tup in itertools.product(*[v for _, v in active]):
        combo = {c: None for c in opts}
        for c, p in zip(cats_order, tup):
            combo[c] = p
        yield combo


# ---------- metrics ----------

def compute_metrics(cfg, combo, scenario, K, costs=None):
    """Return (metrics dict, checks list). metrics has key 'incomplete' if unsizable.
    If costs is given, also computes the objective metrics total_construction_cost /
    array_area_m2 / system_mass_kg."""
    g = lambda p: sval(scenario, p)
    ac, inv, conv = combo["ac_unit"], combo["inverter"], combo["dc_dc_converter"]
    cc, pan, bat, bms = combo["charge_controller"], combo["solar_panel"], combo["battery"], combo.get("bms")
    bus = cfg["bus_voltage"]
    m = {}

    dT = g("site.outside_temp_day") - g("thermal_conditions.target_indoor_temp")
    m["thermal_load_w"] = (g("thermal_conditions.envelope_ua") * dT
                           + g("thermal_conditions.solar_gain")
                           + g("thermal_conditions.occupancy_gain") * g("space.occupancy_count"))

    if not ac.get("cooling_btu") or ac.get("running_w") is None:
        return {"incomplete": f"ac_unit '{ac['id']}' missing cooling_btu/running_w"}, \
               [("ac_data_complete", "FAIL", False)]

    m["ac_cooling_w"] = ac["cooling_btu"] * K["btu_h_to_w"]
    m["ac_duty_cycle"] = min(1.0, m["thermal_load_w"] / m["ac_cooling_w"])
    m["ac_avg_power_w"] = ac["running_w"] * m["ac_duty_cycle"]
    hours = g("cooling_schedule.cooling_hours")
    m["ac_daily_energy_wh"] = m["ac_avg_power_w"] * hours

    m["non_ac_daily_energy_wh"] = sum(i["watts"] * i["hours_per_day"] for i in scenario["non_ac_loads"]["items"])
    m["inverter_idle_energy_wh"] = inv.get("idle_w", 0) * (hours + 2) if inv else 0
    inv_eff = inv.get("efficiency", 0.90) if inv else None
    m["inverter_conv_loss_wh"] = m["ac_daily_energy_wh"] * (1 / inv_eff - 1) if inv else 0
    m["converter_loss_wh"] = m["ac_daily_energy_wh"] * (1 / conv["efficiency"] - 1) if conv else 0
    m["design_daily_energy_wh"] = (m["ac_daily_energy_wh"] + m["non_ac_daily_energy_wh"]
                                   + m["inverter_idle_energy_wh"] + m["inverter_conv_loss_wh"]
                                   + m["converter_loss_wh"]) * K["energy_margin"]

    # part-specific panel temperature derate + composite PV-system derate
    noct = pan.get("noct", 45)
    tc = pan.get("temp_coeff_pmax", -0.38)
    m["cell_temp_c"] = g("site.outside_temp_day") + (noct - 20) / 800 * K["irradiance_design"]
    m["panel_temp_derate"] = 1 + tc / 100 * (m["cell_temp_c"] - 25)
    mppt_eff = cc.get("efficiency", 0.97) if cc else (inv.get("mppt_efficiency", 0.97) if inv else 0.97)
    m["pv_system_derate"] = m["panel_temp_derate"] * K["soiling_derate"] * K["wiring_derate"] * mppt_eff
    m["array_w_required"] = m["design_daily_energy_wh"] / (g("site.peak_sun_hours") * m["pv_system_derate"] * K["battery_roundtrip"])
    m["panels_needed"] = math.ceil(m["array_w_required"] / pan["watt"])
    m["array_w_provided"] = m["panels_needed"] * pan["watt"]
    m["mppt_current_required"] = m["array_w_provided"] / bus * K["mppt_headroom"]
    m["panel_voc_cold"] = pan["voc"] * K["cold_voc_factor"]

    dod = g("resilience.usable_depth_of_discharge")
    derate = g("resilience.cloudy_derate")
    usable_need = (m["ac_avg_power_w"] * g("resilience.battery_buffer_runtime")
                   + m["design_daily_energy_wh"] * g("resilience.cloudy_day_bridge") * (1 - derate))
    m["battery_usable_needed_wh"] = usable_need
    m["battery_nominal_needed_wh"] = usable_need / dod
    need_kwh = m["battery_nominal_needed_wh"] / 1000
    if bat.get("form") == "cell":
        S = SERIES_FOR_BUS[bus]
        string_kwh = S * bat["capacity_kwh"]
        strings = max(1, math.ceil(need_kwh / string_kwh))
        m["series_count"] = S
        m["battery_strings"] = strings
        m["battery_blocks_needed"] = S * strings
        m["battery_kwh_provided"] = strings * string_kwh
    else:
        count = max(1, math.ceil(need_kwh / bat["capacity_kwh"]))
        m["series_count"] = 1
        m["battery_strings"] = count
        m["battery_blocks_needed"] = count
        m["battery_kwh_provided"] = count * bat["capacity_kwh"]
    m["autonomy_hours"] = (m["battery_kwh_provided"] * 1000 * dod / m["ac_avg_power_w"]) if m["ac_avg_power_w"] else float("inf")

    # --- objective metrics: panel area, system mass, total construction cost ---
    qty = {"ac_unit": 1, "inverter": 1, "charge_controller": 1, "dc_dc_converter": 1,
           "bms": m["battery_strings"], "battery": m["battery_blocks_needed"],
           "solar_panel": m["panels_needed"]}
    m["array_area_m2"] = m["panels_needed"] * pan.get("area_m2", 0)
    m["system_mass_kg"] = sum(p.get("mass_kg", 0) * qty.get(c, 1)
                              for c, p in combo.items() if p is not None)
    parts_cost = 0.0
    missing = None
    for c, p in combo.items():
        if p is None:
            continue
        pr = p.get("price_usd")
        if pr is None:
            missing = f"{c}:{p['id']}"
            break
        parts_cost += pr * qty.get(c, 1)
    m["cost_missing"] = missing
    if costs is not None and missing is None:
        adders = sum(v["value"] for v in costs["adders"].values())
        copper = costs["rules"]["wiring_copper_cost_per_a_m"]["value"]
        m["wiring_cost_usd"] = copper * (g("install.battery_run_m") * m["ac_avg_power_w"] / bus
                                         + g("install.panel_run_m") * m["array_w_provided"] / bus)
        m["total_construction_cost"] = (parts_cost + adders + m["wiring_cost_usd"]) * costs["rules"]["contingency_factor"]["value"]
    else:
        m["wiring_cost_usd"] = None
        m["total_construction_cost"] = None

    checks = [("ac_can_hold_setpoint", "FAIL", m["thermal_load_w"] <= m["ac_cooling_w"])]
    pv_limit = (cc or {}).get("max_pv_voc") if cc else (inv or {}).get("pv_max_voltage")
    if pv_limit is not None:
        checks.append(("controller_voltage_ok (1 panel)", "FAIL", m["panel_voc_cold"] <= pv_limit))
    if cc:
        checks.append(("controller_current_ok", "WARN", cc["rated_a"] >= m["array_w_provided"] / bus))
        checks.append(("controller_bus_ok", "FAIL", bus in cc["max_battery_v"]))
    if inv:
        checks.append(("inverter_power_ok", "FAIL", inv["continuous_w"] >= ac["running_w"] * K["inverter_headroom"]))
    m["nonworking_count"] = sum(1 for p in combo.values() if p is not None and p.get("condition") == "needs-repair")
    if conv and ac.get("running_a"):
        checks.append(("converter_current_ok", "FAIL", conv["continuous_a"] >= ac["running_a"]))
    if m["nonworking_count"]:
        checks.append(("all_parts_working", "WARN", False))
    if bms:
        checks.append(("bms_current_ok", "WARN", bms["continuous_a"] >= m["ac_avg_power_w"] / bus))
    checks.append(("buffer_meets_need", "WARN", m["battery_kwh_provided"] * dod * 1000 >= usable_need - 1))
    return m, checks


def verdict(checks):
    if any(sev == "FAIL" and not ok for _, sev, ok in checks):
        return "FAIL"
    if any(not ok for _, _, ok in checks):
        return "WARN"
    return "PASS"


# ---------- cost breakdown ----------

def part_quantities(m):
    """Quantity of each part category in a built system (from solved metrics)."""
    return {"ac_unit": 1, "inverter": 1, "charge_controller": 1, "dc_dc_converter": 1,
            "bms": m.get("battery_strings", 1), "battery": m.get("battery_blocks_needed", 1),
            "solar_panel": m.get("panels_needed", 1)}


def cost_breakdown(combo, m, costs):
    """Itemized cost breakdown for a solved combination: per-part line items,
    adders, wiring, contingency, total."""
    qty = part_quantities(m)
    lines, parts_total = [], 0.0
    for cat in load_configs()["part_categories"]:
        p = combo.get(cat)
        if p is None:
            continue
        q = qty.get(cat, 1)
        unit = p.get("price_usd")
        line = unit * q if unit is not None else None
        lines.append({"cat": cat, "id": p["id"], "name": p.get("name", p["id"]),
                      "qty": q, "unit": unit, "line": line})
        if line is not None:
            parts_total += line
    adders = {k: v["value"] for k, v in costs["adders"].items()}
    wiring = m.get("wiring_cost_usd") or 0.0
    contingency = costs["rules"]["contingency_factor"]["value"]
    subtotal = parts_total + sum(adders.values()) + wiring
    return {"lines": lines, "parts_total": parts_total, "adders": adders,
            "wiring": wiring, "subtotal": subtotal, "contingency": contingency,
            "total": subtotal * contingency}


# ---------- balance score ----------

def score(m, costs):
    """Weighted balance of the three objectives (lower = better). None if cost unknown.
    score = cost + mass_penalty_per_kg*mass + area_penalty_per_m2*area (all cost-equivalent)."""
    c = m.get("total_construction_cost")
    if c is None:
        return None
    w = costs["balance"]["weights"]
    return (w["cost_per_usd"]["value"] * c
            + w["mass_penalty_per_kg"]["value"] * m["system_mass_kg"]
            + w["area_penalty_per_m2"]["value"] * m["array_area_m2"]
            + w.get("condition_penalty_per_part", {}).get("value", 0) * m.get("nonworking_count", 0))


# ---------- rendering / CLI ----------

def summarize_constraint(cell):
    if cell is None:
        return "none"
    if cell == {}:
        return "any"
    bits = []
    for field, req in cell.items():
        if isinstance(req, dict):
            inner = ",".join(f"{op}{v}" for op, v in req.items())
            bits.append(f"{field}[{inner}]")
        else:
            bits.append(f"{field}={req}")
    return "; ".join(bits)


def run(configs, cats, only=None, enumerate_n=0):
    categories = configs["part_categories"]
    for cfg in configs["configs"]:
        if only and cfg["id"] != only:
            continue
        print(f"\n=== {cfg['id']}: {cfg['label']}  ({cfg['group']}) ===")
        opts = slot_options(cfg, cats)
        combo_count = 1
        for cat in categories:
            hits = opts[cat]
            if hits is None:
                print(f"  {cat:<18}: none")
                continue
            if hits:
                print(f"  {cat:<18}: {len(hits):>2} match  [{', '.join(p['id'] for p in hits)}]")
                combo_count *= len(hits)
            else:
                print(f"  {cat:<18}:  0 match  ! NO QUALIFYING PART")
                combo_count = 0
        print(f"  -> valid combinations: {combo_count}")
        if enumerate_n and combo_count:
            for i, combo in enumerate(iter_combos(cfg, cats)):
                if i >= enumerate_n:
                    print(f"     ... ({combo_count - enumerate_n} more)")
                    break
                used = [(c, p) for c, p in combo.items() if p is not None]
                print(f"     [{i + 1}] " + ", ".join(f"{c}={p['id']}" for c, p in used))


def metrics_summary(configs, cats, only=None):
    scenario, K, costs = load_scenario(), load_metric_constants(), load_costs()
    for cfg in configs["configs"]:
        if only and cfg["id"] != only:
            continue
        combo = pick_combo(cfg, cats)
        if any(combo[c] is None for c in ("ac_unit", "solar_panel", "battery")):
            print(f"{cfg['id']:<3} incomplete combo — skipping")
            continue
        m, checks = compute_metrics(cfg, combo, scenario, K, costs)
        if m.get("incomplete"):
            print(f"{cfg['id']:<3} {cfg['architecture']:<12} {cfg['bus_voltage']:>2}V  -> DATA INCOMPLETE: {m['incomplete']}")
            continue
        cost = m["total_construction_cost"]
        cost_s = f"${cost:,.0f}" if cost is not None else "$ n/a"
        sc = score(m, costs)
        sc_s = f"{sc:,.0f}" if sc is not None else "n/a"
        print(f"{cfg['id']:<3} {cfg['architecture']:<12} {cfg['bus_voltage']:>2}V  "
              f"duty={m['ac_duty_cycle']:.2f} daily={m['design_daily_energy_wh']/1000:.1f}kWh "
              f"array={m['array_w_provided']:.0f}W/{m['array_area_m2']:.1f}m2 batt={m['battery_kwh_provided']:.1f}kWh "
              f"mass={m['system_mass_kg']:.0f}kg {cost_s:>7} score={sc_s:>6}  -> {verdict(checks)}")


def render_table(configs):
    categories = configs["part_categories"]
    rows = [["Config"] + categories]
    for cfg in configs["configs"]:
        rows.append([cfg["id"]] + [summarize_constraint(cfg["constraints"].get(c)) for c in categories])
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    for ri, row in enumerate(rows):
        print(" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))
        if ri == 0:
            print("-+-".join("-" * widths[i] for i in range(len(row))))


def catalog_feedback(configs, cats, thin=2):
    """Highlight research gaps: config slots with few qualifying parts, and
    price outliers within each category."""
    print(f"=== Coverage — qualifying parts per config slot (! = <= {thin}, research gap) ===")
    gaps = []
    for cfg in configs["configs"]:
        opts = slot_options(cfg, cats)
        cells = []
        for cat in configs["part_categories"]:
            ps = opts[cat]
            if ps is None:
                continue
            n = len(ps)
            cells.append(f"{cat}={n}{'!' if n <= thin else ''}")
            if n <= thin:
                gaps.append((cfg["id"], cat, n, [p["id"] for p in ps]))
        print(f"  {cfg['id']:<3} {cfg['bus_voltage']:>2}V  " + "  ".join(cells))
    if gaps:
        print("\n  Thin slots (more part research would help):")
        for cid, cat, n, ids in gaps:
            print(f"    {cid} {cat:<16} {n} option(s): {', '.join(ids)}")

    print("\n=== Price outliers per category (Tukey 1.5*IQR; flags catalog gaps) ===")
    for cat in sorted(cats):
        priced = [(p["id"], p["price_usd"]) for p in cats[cat]["parts"] if p.get("price_usd") is not None]
        n_total = len(cats[cat]["parts"])
        vals = sorted(v for _, v in priced)
        if len(vals) < 4:
            print(f"  {cat:<18} {len(priced)}/{n_total} priced — too few to judge outliers")
            continue
        q1, _, q3 = statistics.quantiles(vals, n=4)
        iqr = q3 - q1
        lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outliers = sorted(((i, v) for i, v in priced if v < lo or v > hi), key=lambda x: x[1])
        spread = f"${vals[0]:,.0f}/{statistics.median(vals):,.0f}/{vals[-1]:,.0f} (min/med/max)"
        unpriced = [p["id"] for p in cats[cat]["parts"] if p.get("price_usd") is None]
        tail = ""
        if outliers:
            tail = "  outliers: " + ", ".join(f"{i} ${v:,.0f}{'↓' if v < lo else '↑'}" for i, v in outliers)
        if unpriced:
            tail += f"  | unpriced: {', '.join(unpriced)}"
        print(f"  {cat:<18} {len(priced)}/{n_total} priced  {spread}{tail}")


def check(configs, cats):
    ok = True
    categories = set(configs["part_categories"])
    for cfg in configs["configs"]:
        for cat, cell in cfg["constraints"].items():
            if cat not in categories:
                print(f"  {cfg['id']}: '{cat}' not in part_categories"); ok = False
            if cell in (None, {}):
                continue
            specs = cats.get(cat, {}).get("specs", {})
            for field in cell:
                if field not in specs:
                    print(f"  {cfg['id']}.{cat}: constraint field '{field}' not in {cat} specs"); ok = False
    print("check: OK" if ok else "check: problems found")
    return ok


def main():
    ap = argparse.ArgumentParser(description="Filter parts against configs and compute metrics/cost.")
    ap.add_argument("--config", help="only this config id (e.g. C6)")
    ap.add_argument("--table", action="store_true", help="print the config x category constraint table")
    ap.add_argument("--metrics", action="store_true", help="metrics + cost for each config's representative combo")
    ap.add_argument("--catalog", action="store_true", help="catalog feedback: thin config slots + price outliers per category")
    ap.add_argument("--enumerate", type=int, default=0, metavar="N", help="list up to N full part combinations per config")
    ap.add_argument("--check", action="store_true", help="validate constraint fields against spec definitions")
    args = ap.parse_args()

    cats = load_categories()
    configs = load_configs()
    if args.check:
        check(configs, cats)
    elif args.table:
        render_table(configs)
    elif args.catalog:
        catalog_feedback(configs, cats)
    elif args.metrics:
        metrics_summary(configs, cats, only=args.config)
    else:
        run(configs, cats, only=args.config, enumerate_n=args.enumerate)


if __name__ == "__main__":
    main()
