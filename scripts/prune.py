#!/usr/bin/env python3
"""
Find strictly-worse (Pareto-dominated) parts and document why.

A part B is *strictly worse* than A if A can substitute for B in every slot B
qualifies for (compatible on the categorical/capability fields the solver gates
on) AND A is at least as good on every scored dimension and strictly better on at
least one. Such a B is never optimal in any scenario, so it can be removed.

Two categories are normalized because the solver couples their cost non-linearly:
- battery: compared per kWh ($/kWh, kg/kWh) — ADVISORY (ignores pack granularity
  and per-string BMS count).
- solar_panel: compared per EFFECTIVE watt (watt x temperature derate at the
  design ambient) — ADVISORY.
All other categories use raw-spec domination (SAFE).

Usage:
  python3 scripts/prune.py            # report only (documents criteria + dominated parts)
  python3 scripts/prune.py --apply    # ALSO remove dominated parts from data/parts/*.json
"""
import argparse
import json
from pathlib import Path
import run_combinations as rc

DATA = Path(__file__).resolve().parent.parent / "data" / "parts"
COND_RANK = {"new": 2, "used": 1, "needs-repair": 0}

# Per-category domination rule. eq: must match. superset: A's set covers B's.
# ge: A >= B (bool/ordinal). cond: A condition not worse. max: higher better. min: lower better.
RULES = {
    "ac_unit":           {"eq": ["supply_type"], "superset": ["supply_voltage"], "ge": ["inverter_compressor"],
                          "cond": True, "max": ["cooling_btu"], "min": ["price_usd", "mass_kg", "running_w"], "safe": True},
    "inverter":          {"eq": ["class", "waveform"], "superset": ["input_voltage"],
                          "max": ["continuous_w", "efficiency", "mppt_efficiency", "pv_max_voltage"],
                          "min": ["price_usd", "mass_kg", "idle_w"], "safe": True},
    "charge_controller": {"eq": ["type"], "superset": ["max_battery_v"],
                          "max": ["rated_a", "max_pv_voc", "efficiency"], "min": ["price_usd", "mass_kg"], "safe": True},
    "bms":               {"superset": ["bus_voltage"], "max": ["continuous_a"], "min": ["price_usd", "mass_kg"], "safe": True},
    "dc_dc_converter":   {"eq": ["output_voltage"], "superset": ["input_voltage"],
                          "max": ["continuous_a", "efficiency"], "min": ["price_usd", "mass_kg"], "safe": True},
    "battery":           {"superset": ["bus_voltage"], "cond": True, "exclude_terminal": ["weld-only"],
                          "eq_approx": {"capacity_kwh": 0.02}, "min": ["price_usd", "mass_kg"], "safe": True,
                          "note": "same-capacity only (safe): equal kWh -> equal strings/BMS/granularity, then cheaper+lighter wins. Energy-value tradeoffs across sizes are kept, not pruned."},
    "solar_panel":       {"min_per_effw": ["price_usd", "mass_kg", "area_m2"], "min": ["voc"], "safe": False,
                          "note": "per effective watt (watt x temp derate at design ambient); voc lower = more controller-compatible"},
}


def to_set(v):
    return set(v) if isinstance(v, list) else {v}


def eff_watt(p, scenario, K):
    cell = rc.sval(scenario, "site.outside_temp_day") + (p.get("noct", 45) - 20) / 800 * K["irradiance_design"]
    return p["watt"] * (1 + p.get("temp_coeff_pmax", -0.38) / 100 * (cell - 25))


def dominates(a, b, rule, scenario, K):
    """True if a strictly dominates b. Returns (True, reasons) or (False, None)."""
    for f in rule.get("eq", []):
        if a.get(f) != b.get(f):
            return False, None
    for f, tol in rule.get("eq_approx", {}).items():
        av, bv = a.get(f), b.get(f)
        if av is None or bv is None or abs(av - bv) > tol * bv:
            return False, None
    for f in rule.get("superset", []):
        if not to_set(a.get(f, set())) >= to_set(b.get(f, set())):
            return False, None
    for f in rule.get("ge", []):
        if int(a.get(f, 0)) < int(b.get(f, 0)):
            return False, None
    if rule.get("cond") and COND_RANK.get(a.get("condition"), 1) < COND_RANK.get(b.get("condition"), 1):
        return False, None
    reasons, strict = [], False
    # normalization
    def norm(p, f):
        if rule.get("min_per_kwh") and f in rule["min_per_kwh"]:
            return p[f] / p["capacity_kwh"], "/kWh"
        if rule.get("min_per_effw") and f in rule["min_per_effw"]:
            return p[f] / eff_watt(p, scenario, K), "/effW"
        return p[f], ""
    minfields = rule.get("min", []) + rule.get("min_per_kwh", []) + rule.get("min_per_effw", [])
    for f in minfields:
        if a.get(f) is None or b.get(f) is None:
            continue
        av, sfx = norm(a, f)
        bv, _ = norm(b, f)
        if av > bv + 1e-9:
            return False, None
        if av < bv - 1e-9:
            strict = True
            reasons.append(f"{f}{sfx} {av:.3g}<={bv:.3g}")
    for f in rule.get("max", []):
        if a.get(f) is None or b.get(f) is None:
            continue
        if a[f] < b[f] - 1e-9:
            return False, None
        if a[f] > b[f] + 1e-9:
            strict = True
            reasons.append(f"{f} {a[f]:.3g}>={b[f]:.3g}")
    return (strict, reasons) if strict else (False, None)


def criteria_text(cat, rule):
    parts = []
    for f in rule.get("eq", []):
        parts.append(f"{f}=")
    for f in rule.get("eq_approx", {}):
        parts.append(f"{f}≈")
    for f in rule.get("superset", []):
        parts.append(f"{f}⊇")
    for f in rule.get("ge", []):
        parts.append(f"{f}≥")
    if rule.get("cond"):
        parts.append("condition≥")
    for f in rule.get("min", []):
        parts.append(f"{f}≤")
    for f in rule.get("min_per_kwh", []):
        parts.append(f"{f}/kWh≤")
    for f in rule.get("min_per_effw", []):
        parts.append(f"{f}/effW≤")
    for f in rule.get("max", []):
        parts.append(f"{f}≥")
    tag = "SAFE (raw spec)" if rule.get("safe") else "ADVISORY (" + rule.get("note", "normalized") + ")"
    return "A dominates B if: " + ", ".join(parts) + f"  [{tag}]"


def split_excluded(parts, rule):
    """Partition parts into (eligible, excluded) by exclude_terminal (e.g. weld-only).
    Excluded parts can never substitute in a slot, so they are neither dominator nor
    dominated — report them as unusable, don't prune the catalog around them."""
    ex = rule.get("exclude_terminal", [])
    if not ex:
        return parts, []
    eligible = [p for p in parts if p.get("terminal_type") not in ex]
    excluded = [p for p in parts if p.get("terminal_type") in ex]
    return eligible, excluded


def find_dominated(cat, parts, rule, scenario, K):
    """Return {dominated_id: (dominator_id, reasons)}. A part dropped once dominated."""
    dominated = {}
    for b in parts:
        for a in parts:
            if a["id"] == b["id"] or a["id"] in dominated:
                continue
            ok, reasons = dominates(a, b, rule, scenario, K)
            if ok:
                dominated[b["id"]] = (a["id"], reasons)
                break
    return dominated


def main():
    ap = argparse.ArgumentParser(description="Find/remove strictly-worse (dominated) parts.")
    ap.add_argument("--apply", action="store_true", help="remove dominated parts from data/parts/*.json")
    args = ap.parse_args()

    scenario, K = rc.load_scenario(), rc.load_metric_constants()
    cats = rc.load_categories()
    total = 0
    to_remove = {}
    for cat, rule in RULES.items():
        all_parts = cats.get(cat, {}).get("parts", [])
        parts, excluded = split_excluded(all_parts, rule)
        dom = find_dominated(cat, parts, rule, scenario, K)
        print(f"\n=== {cat} ({len(all_parts)} parts, {len(dom)} strictly worse) ===")
        print("  " + criteria_text(cat, rule))
        if excluded:
            terms = "/".join(rule.get("exclude_terminal", []))
            print(f"  ({len(excluded)} unusable, excluded from domination pool: {terms} can't substitute in any slot)")
            for p in excluded:
                print(f"  ⊘ {p['id']:<26} unusable: terminal_type={p.get('terminal_type')}")
        if not dom:
            print("  (none dominated)")
        for bid, (aid, reasons) in dom.items():
            print(f"  ✗ {bid:<26} dominated by {aid:<26} ({'; '.join(reasons)})")
        if dom:
            to_remove[cat] = set(dom)
            total += len(dom)
    print(f"\nTotal strictly-worse parts: {total}")

    if args.apply and to_remove:
        for cat, ids in to_remove.items():
            f = DATA / (cat.replace("_", "-") + ".json")
            d = json.loads(f.read_text())
            before = len(d["parts"])
            d["parts"] = [p for p in d["parts"] if p["id"] not in ids]
            f.write_text(json.dumps(d, indent=2) + "\n")
            print(f"  removed {before - len(d['parts'])} from {f.name}")
        print("Applied. Re-run: python3 scripts/run_combinations.py --check")
    elif to_remove:
        print("Report only. Re-run with --apply to remove them.")


if __name__ == "__main__":
    main()
