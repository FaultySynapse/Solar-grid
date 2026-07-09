#!/usr/bin/env python3
"""
Full solution sheet for one system: parts, itemized cost breakdown, sizing,
objectives, and feasibility. Use it to inspect a candidate before iterating.

By default it picks the best (lowest-score) feasible, fully-priced combination —
for a given config, or across all configs. Pin specific parts with --set.

Usage:
  python3 scripts/detail.py                       # best solution overall
  python3 scripts/detail.py --config C6           # best solution for C6
  python3 scripts/detail.py --by cost             # best by raw cost instead of balanced score
  python3 scripts/detail.py --config C2 --set battery=eve-lf280k --set solar_panel=canadian-400w
"""
import argparse
import run_combinations as rc


def evaluate(cfg, combo, scenario, K, costs):
    m, checks = rc.compute_metrics(cfg, combo, scenario, K, costs)
    return m, checks


def best_for_config(cfg, cats, scenario, K, costs, by):
    res = rc.optimize_config(cfg, cats, scenario, K, costs, by=by)
    if not res:
        return None
    r = res[0]
    return (r["score"], r["combo"], r["m"], r["checks"])


def money(x):
    return f"${x:,.0f}" if x is not None else "n/a"


def report(cfg, combo, m, checks, costs):
    v = rc.verdict(checks)
    sc = rc.score(m, costs)
    print(f"\n{'='*68}")
    print(f" SOLUTION  {cfg['id']}: {cfg['label']}")
    print(f" architecture: {cfg['architecture']} | bus: {cfg['bus_voltage']} V | VERDICT: {v} | score: {sc:,.0f}")
    print(f"{'='*68}")

    bd = rc.cost_breakdown(combo, m, costs)
    print("\nBILL OF MATERIALS")
    print(f"  {'category':<16}{'qty':>4}  {'part':<26}{'unit':>8}{'line':>9}")
    for ln in bd["lines"]:
        print(f"  {ln['cat']:<16}{ln['qty']:>4}  {ln['id']:<26}{money(ln['unit']):>8}{money(ln['line']):>9}")

    print("\nCOST BREAKDOWN")
    print(f"  {'parts subtotal':<40}{money(bd['parts_total']):>10}")
    for k, val in bd["adders"].items():
        print(f"  + {k:<38}{money(val):>10}")
    br = m['ac_avg_power_w'] / cfg['bus_voltage']
    pr = m['array_w_provided'] / cfg['bus_voltage']
    print(f"  + {'wiring (2m batt @'+f'{br:.0f}A + 4m pv @{pr:.0f}A)':<38}{money(bd['wiring']):>10}")
    print(f"  {'subtotal':<40}{money(bd['subtotal']):>10}")
    print(f"  x contingency {bd['contingency']:<26}{'':>10}")
    print(f"  {'TOTAL':<40}{money(bd['total']):>10}")

    print("\nOBJECTIVES")
    print(f"  cost {money(m['total_construction_cost'])}  |  mass {m['system_mass_kg']:.0f} kg  |  "
          f"panel area {m['array_area_m2']:.1f} m2  |  balance score {sc:,.0f}")

    print("\nSIZING")
    print(f"  thermal load {m['thermal_load_w']:.0f} W  (AC cap {m['ac_cooling_w']:.0f} W, duty {m['ac_duty_cycle']:.2f}, avg draw {m['ac_avg_power_w']:.0f} W)")
    print(f"  daily energy {m['design_daily_energy_wh']/1000:.2f} kWh  (AC {m['ac_daily_energy_wh']/1000:.2f} + other {m['non_ac_daily_energy_wh']/1000:.2f}"
          f"{' + inv_idle '+format(m['inverter_idle_energy_wh']/1000,'.2f') if m['inverter_idle_energy_wh'] else ''}"
          f"{' + inv_conv '+format(m['inverter_conv_loss_wh']/1000,'.2f') if m['inverter_conv_loss_wh'] else ''}"
          f"{' + conv_loss '+format(m['converter_loss_wh']/1000,'.2f') if m['converter_loss_wh'] else ''}, x margin)")
    print(f"  PV derate {m['pv_system_derate']:.2f}  (cell {m['cell_temp_c']:.0f}C, temp factor {m['panel_temp_derate']:.2f})")
    print(f"  array need {m['array_w_required']:.0f} W -> {m['panels_needed']} x {combo['solar_panel']['id']} = {m['array_w_provided']:.0f} W ({m['array_area_m2']:.1f} m2)")
    print(f"  battery need {m['battery_nominal_needed_wh']/1000:.1f} kWh nominal -> "
          f"{m['series_count']}S x {m['battery_strings']}P = {m['battery_blocks_needed']} x {combo['battery']['id']} "
          f"= {m['battery_kwh_provided']:.1f} kWh  (autonomy {m['autonomy_cycles']:.1f} usage cycles / {m['autonomy_cloudy_cycles']:.1f} cloudy))")
    print(f"  MPPT current required {m['mppt_current_required']:.0f} A  |  panel Voc(cold) {m['panel_voc_cold']:.0f} V")

    print("\nFEASIBILITY")
    for name, sev, ok in checks:
        print(f"  [{'ok ' if ok else sev}] {name}")


def main():
    ap = argparse.ArgumentParser(description="Full solution sheet + cost breakdown for one system.")
    ap.add_argument("--config", help="config id (e.g. C6); default = best across all configs")
    ap.add_argument("--set", action="append", default=[], metavar="CAT=ID", help="pin a slot's part (requires --config)")
    ap.add_argument("--by", choices=["score", "cost"], default="score", help="how to pick 'best' (default balanced score)")
    args = ap.parse_args()

    scenario, K, costs = rc.load_scenario(), rc.load_metric_constants(), rc.load_costs()
    cats, configs = rc.load_categories(), rc.load_configs()

    if args.set and not args.config:
        ap.error("--set requires --config")

    if args.config:
        cfg = next((c for c in configs["configs"] if c["id"] == args.config), None)
        if cfg is None:
            ap.error(f"unknown config {args.config}")
        if args.set:
            overrides = dict(s.split("=", 1) for s in args.set)
            combo = rc.pick_combo(cfg, cats, overrides)
            if any(combo[c] is None for c in ("ac_unit", "solar_panel", "battery", "bms")):
                print("Pinned combo is incomplete (a slot has no matching part)."); return
            m, checks = evaluate(cfg, combo, scenario, K, costs)
            if m.get("incomplete"):
                print(f"DATA INCOMPLETE: {m['incomplete']}"); return
            report(cfg, combo, m, checks, costs)
        else:
            b = best_for_config(cfg, cats, scenario, K, costs, args.by)
            if not b:
                print(f"No feasible priced solution for {args.config}."); return
            report(cfg, b[1], b[2], b[3], costs)
    else:
        best = None
        for cfg in configs["configs"]:
            b = best_for_config(cfg, cats, scenario, K, costs, args.by)
            if b and (best is None or b[0] < best[0]):
                best = (b[0], cfg, b[1], b[2], b[3])
        if not best:
            print("No feasible priced solution found."); return
        _, cfg, combo, m, checks = best
        report(cfg, combo, m, checks, costs)


if __name__ == "__main__":
    main()
