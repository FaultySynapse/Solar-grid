#!/usr/bin/env python3
"""
Detailed solve of the derived parameters for ONE part combination.

Uses the engine in run_combinations.py (compute_metrics / compute_cost / verdict).
Prints every metric + the feasibility checks + total cost for a config's
representative combo (or an overridden one).

Usage:
  python3 scripts/solve.py                      # representative combo for every config (one line each)
  python3 scripts/solve.py --config C6          # full metrics + feasibility + cost for C6
  python3 scripts/solve.py --config C2 --set battery=eve-lf280k --set solar_panel=canadian-400w
  python3 scripts/solve.py --list-metrics       # the derived-parameter definitions
"""
import argparse
import run_combinations as rc


def report_one(cfg, combo, m, checks, cost, breakdown):
    print(f"\n=== {cfg['id']}: {cfg['label']}  [{cfg['architecture']}, {cfg['bus_voltage']}V] ===")
    print("  parts:")
    for cat, part in combo.items():
        print(f"    {cat:<18}: {part['id'] if part else 'none'}")
    print("  derived metrics:")
    order = ["thermal_load_w", "ac_cooling_w", "ac_duty_cycle", "ac_avg_power_w",
             "ac_daily_energy_wh", "non_ac_daily_energy_wh", "inverter_idle_energy_wh",
             "converter_loss_wh", "design_daily_energy_wh", "array_w_required",
             "panels_needed", "array_w_provided", "mppt_current_required", "panel_voc_cold",
             "battery_usable_needed_wh", "battery_nominal_needed_wh", "series_count",
             "battery_strings", "battery_blocks_needed", "battery_kwh_provided", "autonomy_hours"]
    for k in order:
        if k in m:
            v = m[k]
            print(f"    {k:<26}= {v:.2f}" if isinstance(v, float) else f"    {k:<26}= {v}")
    print("  feasibility:")
    for name, sev, ok in checks:
        print(f"    [{'ok ' if ok else sev}] {name}")
    if cost is not None:
        print(f"  cost: ${cost:,.0f}  (parts ${breakdown['_parts']:,.0f} + adders ${breakdown['_adders']:,.0f} + bms ${breakdown['bms']:,.0f}, x contingency)")
    else:
        print(f"  cost: n/a ({breakdown})")
    print(f"  VERDICT: {rc.verdict(checks)}")


def main():
    ap = argparse.ArgumentParser(description="Solve derived parameters for a part combination.")
    ap.add_argument("--config", help="config id (e.g. C6); default = all configs, one line each")
    ap.add_argument("--set", action="append", default=[], metavar="CAT=ID", help="override a slot's part (repeatable)")
    ap.add_argument("--list-metrics", action="store_true", help="print the derived-parameter definitions")
    args = ap.parse_args()

    if args.list_metrics:
        md = rc.load_json("metrics.json")
        print("Constants:")
        for k, v in md["constants"].items():
            print(f"  {k} = {v['value']}  ({v['definition']})")
        print("\nDerived metrics:")
        for x in md["metrics"]:
            print(f"  {x['id']} [{x.get('unit','')}] = {x['formula']}")
        return

    scenario = rc.load_scenario()
    K = rc.load_metric_constants()
    costs = rc.load_costs()
    cats = rc.load_categories()
    configs = rc.load_configs()
    overrides = dict(s.split("=", 1) for s in args.set)

    for cfg in configs["configs"]:
        if args.config and cfg["id"] != args.config:
            continue
        combo = rc.pick_combo(cfg, cats, overrides)
        if any(combo[c] is None for c in ("ac_unit", "solar_panel", "battery")):
            print(f"{cfg['id']:<3} incomplete combo (missing a required part) — skipping")
            continue
        m, checks = rc.compute_metrics(cfg, combo, scenario, K)
        if m.get("incomplete"):
            print(f"{cfg['id']:<3} -> DATA INCOMPLETE: {m['incomplete']}")
            continue
        cost, breakdown = rc.compute_cost(combo, m, costs)
        if args.config:
            report_one(cfg, combo, m, checks, cost, breakdown)
        else:
            cost_s = f"${cost:,.0f}" if cost is not None else "$ n/a"
            print(f"{cfg['id']:<3} {cfg['architecture']:<12} {cfg['bus_voltage']:>2}V  "
                  f"duty={m['ac_duty_cycle']:.2f} ac_avg={m['ac_avg_power_w']:.0f}W "
                  f"daily={m['design_daily_energy_wh']/1000:.1f}kWh array={m['array_w_provided']:.0f}W "
                  f"batt={m['battery_kwh_provided']:.1f}kWh {cost_s:>8} -> {rc.verdict(checks)}")


if __name__ == "__main__":
    main()
