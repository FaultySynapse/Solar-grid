#!/usr/bin/env python3
"""
Solve the derived parameters for a part combination.

Reads the CONDITIONS from data/scenario.json (no derived values live there),
the derived-parameter definitions/constants from data/metrics.json, and the
parts + config table via run_combinations.py. For a given part combination it
computes every derived metric (AC power & duty from the AC part + thermal load,
daily energy, array/battery sizing, autonomy) and flags feasibility.

Usage:
  python3 scripts/solve.py                      # representative combo (first qualifying part) for every config
  python3 scripts/solve.py --config C6          # detailed solve for C6's representative combo
  python3 scripts/solve.py --config C2 --set battery=eve-lf280k --set solar_panel=canadian-400w
  python3 scripts/solve.py --list-metrics       # print the derived-parameter definitions

Standard library only.
"""
import argparse
import json
import math
from pathlib import Path

import run_combinations as rc  # same directory

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SERIES_FOR_BUS = {12: 4, 24: 8, 48: 16}


def load_json(name):
    return json.loads((DATA / name).read_text())


def sval(scenario, path):
    """Fetch scenario value at 'section.field' -> the field's 'value'."""
    section, field = path.split(".")
    return scenario[section][field]["value"]


def pick_combo(cfg, cats, overrides):
    """Choose one part per non-null slot: an override id, else the first qualifying part."""
    combo = {}
    for cat in load_json("configs.json")["part_categories"]:
        cell = cfg["constraints"].get(cat)
        if cell is None:
            combo[cat] = None
            continue
        parts = cats.get(cat, {}).get("parts", [])
        if cat in overrides:
            combo[cat] = next((p for p in parts if p["id"] == overrides[cat]), None)
        else:
            hits = rc.qualifying_parts(parts, cell)
            combo[cat] = hits[0] if hits else None
    return combo


def solve(cfg, combo, scenario, K):
    """Return (metrics dict, list of (check, severity, ok))."""
    g = lambda p: sval(scenario, p)
    m = {}

    # --- thermal load (conditions only) ---
    dT = g("site.outside_temp_day") - g("thermal_conditions.target_indoor_temp")
    m["thermal_load_w"] = (g("thermal_conditions.envelope_ua") * dT
                           + g("thermal_conditions.solar_gain")
                           + g("thermal_conditions.occupancy_gain") * g("space.occupancy_count"))
    m["cooling_need_btu"] = m["thermal_load_w"] * K["btu_per_wh"]

    ac = combo["ac_unit"]
    inv = combo["inverter"]
    conv = combo["dc_dc_converter"]
    cc = combo["charge_controller"]
    pan = combo["solar_panel"]
    bat = combo["battery"]
    bus = cfg["bus_voltage"]

    # incomplete part data -> can't size; flag it rather than assume zeros
    if not ac.get("cooling_btu") or ac.get("running_w") is None:
        return {"incomplete": f"ac_unit '{ac['id']}' is missing cooling_btu/running_w"}, \
               [("ac_data_complete", "FAIL", False)]

    # --- AC power & duty: from the PART + thermal load ---
    m["ac_duty_cycle"] = min(1.0, m["cooling_need_btu"] / ac["cooling_btu"])
    m["ac_avg_power_w"] = ac.get("running_w", 0) * m["ac_duty_cycle"]
    hours = g("cooling_schedule.cooling_hours")
    m["ac_daily_energy_wh"] = m["ac_avg_power_w"] * hours

    # --- other loads / path losses ---
    m["non_ac_daily_energy_wh"] = sum(i["watts"] * i["hours_per_day"] for i in scenario["non_ac_loads"]["items"])
    m["inverter_idle_energy_wh"] = inv["idle_w"] * (hours + 2) if inv else 0
    m["converter_loss_wh"] = m["ac_daily_energy_wh"] * (1 / conv["efficiency"] - 1) if conv else 0

    m["design_daily_energy_wh"] = (m["ac_daily_energy_wh"] + m["non_ac_daily_energy_wh"]
                                   + m["inverter_idle_energy_wh"] + m["converter_loss_wh"]) * K["energy_margin"]

    # --- array ---
    m["array_w_required"] = m["design_daily_energy_wh"] / (g("site.peak_sun_hours") * K["system_efficiency"])
    m["panels_needed"] = math.ceil(m["array_w_required"] / pan["watt"])
    m["array_w_provided"] = m["panels_needed"] * pan["watt"]
    m["mppt_current_required"] = m["array_w_provided"] / bus * K["mppt_headroom"]
    m["panel_voc_cold"] = pan["voc"] * K["cold_voc_factor"]

    # --- battery ---
    dod = g("resilience.usable_depth_of_discharge")
    usable_need = m["ac_avg_power_w"] * g("resilience.battery_buffer_runtime") + m["design_daily_energy_wh"] * g("resilience.cloudy_day_bridge")
    m["battery_usable_needed_wh"] = usable_need
    m["battery_nominal_needed_wh"] = usable_need / dod
    need_kwh = m["battery_nominal_needed_wh"] / 1000
    if bat.get("form") == "cell":
        S = SERIES_FOR_BUS[bus]
        string_kwh = S * bat["capacity_kwh"]
        strings = max(1, math.ceil(need_kwh / string_kwh))
        m["series_count"] = S
        m["battery_blocks_needed"] = S * strings
        m["battery_kwh_provided"] = strings * string_kwh
    else:
        count = max(1, math.ceil(need_kwh / bat["capacity_kwh"]))
        m["series_count"] = 1
        m["battery_blocks_needed"] = count
        m["battery_kwh_provided"] = count * bat["capacity_kwh"]
    m["autonomy_hours"] = (m["battery_kwh_provided"] * 1000 * dod / m["ac_avg_power_w"]) if m["ac_avg_power_w"] else float("inf")

    # --- feasibility ---
    checks = []
    checks.append(("ac_can_hold_setpoint", "FAIL", m["cooling_need_btu"] <= ac["cooling_btu"]))
    pv_limit = (cc or {}).get("max_pv_voc") if cc else (inv or {}).get("pv_max_voltage")
    if pv_limit is not None:
        checks.append(("controller_voltage_ok (1 panel)", "FAIL", m["panel_voc_cold"] <= pv_limit))
    if cc:
        checks.append(("controller_current_ok", "WARN", cc["rated_a"] >= m["array_w_provided"] / bus))
        checks.append(("controller_bus_ok", "FAIL", bus in cc["max_battery_v"]))
    if inv:
        checks.append(("inverter_power_ok", "FAIL", inv["continuous_w"] >= ac["running_w"] * K["inverter_headroom"]))
    if conv and ac.get("running_a"):
        checks.append(("converter_current_ok", "FAIL", conv["continuous_a"] >= ac["running_a"]))
    checks.append(("buffer_meets_need", "WARN", m["battery_kwh_provided"] * dod * 1000 >= usable_need - 1))
    return m, checks


def verdict(checks):
    if any(sev == "FAIL" and not ok for _, sev, ok in checks):
        return "FAIL"
    if any(not ok for _, _, ok in checks):
        return "WARN"
    return "PASS"


def fmt(x):
    if isinstance(x, float):
        return f"{x:.0f}" if abs(x) >= 100 else f"{x:.2f}"
    return str(x)


def report_one(cfg, combo, m, checks):
    print(f"\n=== {cfg['id']}: {cfg['label']}  [{cfg['architecture']}, {cfg['bus_voltage']}V] ===")
    print("  parts:")
    for cat, part in combo.items():
        print(f"    {cat:<18}: {part['id'] if part else 'none'}")
    print("  derived metrics:")
    order = ["thermal_load_w", "cooling_need_btu", "ac_duty_cycle", "ac_avg_power_w",
             "ac_daily_energy_wh", "non_ac_daily_energy_wh", "inverter_idle_energy_wh",
             "converter_loss_wh", "design_daily_energy_wh", "array_w_required",
             "panels_needed", "array_w_provided", "mppt_current_required", "panel_voc_cold",
             "battery_usable_needed_wh", "battery_nominal_needed_wh", "series_count",
             "battery_blocks_needed", "battery_kwh_provided", "autonomy_hours"]
    for k in order:
        if k in m:
            print(f"    {k:<26}= {fmt(m[k])}")
    print("  feasibility:")
    for name, sev, ok in checks:
        print(f"    [{'ok ' if ok else sev}] {name}")
    print(f"  VERDICT: {verdict(checks)}")


def main():
    ap = argparse.ArgumentParser(description="Solve derived parameters for a part combination.")
    ap.add_argument("--config", help="config id (e.g. C6); default = all configs")
    ap.add_argument("--set", action="append", default=[], metavar="CAT=ID", help="override a slot's part (repeatable)")
    ap.add_argument("--list-metrics", action="store_true", help="print the derived-parameter definitions")
    args = ap.parse_args()

    metrics = load_json("metrics.json")
    if args.list_metrics:
        print("Constants:")
        for k, v in metrics["constants"].items():
            print(f"  {k} = {v['value']}  ({v['definition']})")
        print("\nDerived metrics:")
        for md in metrics["metrics"]:
            print(f"  {md['id']} [{md.get('unit','')}] = {md['formula']}")
        return

    K = {k: v["value"] for k, v in metrics["constants"].items()}
    scenario = load_json("scenario.json")
    cats = rc.load_categories()
    configs = load_json("configs.json")
    overrides = dict(s.split("=", 1) for s in args.set)

    detailed = args.config is not None
    for cfg in configs["configs"]:
        if args.config and cfg["id"] != args.config:
            continue
        combo = pick_combo(cfg, cats, overrides)
        if any(combo[c] is None for c in ("ac_unit", "solar_panel", "battery")):
            print(f"\n=== {cfg['id']} === incomplete combo (missing a required part) — skipping")
            continue
        m, checks = solve(cfg, combo, scenario, K)
        if m.get("incomplete"):
            print(f"{cfg['id']:<3} {cfg['architecture']:<12} {cfg['bus_voltage']:>2}V  "
                  f"-> DATA INCOMPLETE: {m['incomplete']}")
            continue
        if detailed:
            report_one(cfg, combo, m, checks)
        else:
            print(f"{cfg['id']:<3} {cfg['architecture']:<12} {cfg['bus_voltage']:>2}V  "
                  f"load={m['thermal_load_w']:.0f}W duty={m['ac_duty_cycle']:.2f} "
                  f"ac_avg={m['ac_avg_power_w']:.0f}W daily={m['design_daily_energy_wh']/1000:.1f}kWh "
                  f"array={m['array_w_provided']:.0f}W batt={m['battery_kwh_provided']:.1f}kWh "
                  f"auton={m['autonomy_hours']:.1f}h  -> {verdict(checks)}")
    if not detailed:
        print("\n(run with --config Cx for full metrics + feasibility of that config's representative combo)")


if __name__ == "__main__":
    main()
