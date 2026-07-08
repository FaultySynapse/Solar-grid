#!/usr/bin/env python3
"""
Rank part combinations by total system cost — top N per config and overall.

For every config it enumerates all qualifying part combinations, solves the
derived metrics + cost + feasibility for each (via the engine in
run_combinations.py), then reports the cheapest N that pass. FAIL combinations
are excluded; WARN combinations are included unless --no-warn.

Usage:
  python3 scripts/rank.py               # top 3 per config + top 10 overall (cheapest feasible)
  python3 scripts/rank.py --n 5         # top 5 per config
  python3 scripts/rank.py --overall 20  # top 20 overall
  python3 scripts/rank.py --no-warn     # only fully-PASS combinations
"""
import argparse
import run_combinations as rc


def rank_all(no_warn=False):
    scenario = rc.load_scenario()
    K = rc.load_metric_constants()
    costs = rc.load_costs()
    cats = rc.load_categories()
    configs = rc.load_configs()

    per_config = {}   # cfg_id -> sorted list of result dicts
    stats = {}        # cfg_id -> (evaluated, priced, feasible)
    for cfg in configs["configs"]:
        results = []
        evaluated = priced = 0
        for combo in rc.iter_combos(cfg, cats):
            if any(combo[c] is None for c in ("ac_unit", "solar_panel", "battery")):
                continue
            evaluated += 1
            m, checks = rc.compute_metrics(cfg, combo, scenario, K)
            if m.get("incomplete"):
                continue
            v = rc.verdict(checks)
            if v == "FAIL" or (no_warn and v == "WARN"):
                continue
            cost, _ = rc.compute_cost(combo, m, costs)
            if cost is None:
                continue
            priced += 1
            results.append({
                "config": cfg["id"], "arch": cfg["architecture"], "bus": cfg["bus_voltage"],
                "cost": cost, "verdict": v, "combo": {c: (p["id"] if p else None) for c, p in combo.items()},
                "daily_kwh": m["design_daily_energy_wh"] / 1000, "array_w": m["array_w_provided"],
                "batt_kwh": m["battery_kwh_provided"], "autonomy_h": m["autonomy_hours"],
            })
        results.sort(key=lambda r: r["cost"])
        per_config[cfg["id"]] = results
        stats[cfg["id"]] = (evaluated, priced, len(results))
    return configs, per_config, stats


def line(r):
    c = r["combo"]
    picks = " ".join(f"{k}={c[k]}" for k in ("ac_unit", "inverter", "dc_dc_converter", "charge_controller", "battery", "solar_panel") if c.get(k))
    return (f"${r['cost']:>7,.0f} [{r['verdict']:<4}] {r['daily_kwh']:.1f}kWh/d "
            f"array {r['array_w']:.0f}W batt {r['batt_kwh']:.1f}kWh auton {r['autonomy_h']:.0f}h  {picks}")


def main():
    ap = argparse.ArgumentParser(description="Top-N cheapest feasible combinations per config and overall.")
    ap.add_argument("--n", type=int, default=3, help="top N per config (default 3)")
    ap.add_argument("--overall", type=int, default=10, help="top N overall (default 10)")
    ap.add_argument("--no-warn", action="store_true", help="exclude WARN combinations (PASS only)")
    args = ap.parse_args()

    configs, per_config, stats = rank_all(no_warn=args.no_warn)

    print("=== Top per config (cheapest feasible) ===")
    all_results = []
    for cfg in configs["configs"]:
        cid = cfg["id"]
        res = per_config[cid]
        all_results.extend(res)
        ev, pr, fe = stats[cid]
        print(f"\n{cid} {cfg['label']}  [{cfg['architecture']}, {cfg['bus_voltage']}V]  "
              f"({fe} feasible / {pr} priced / {ev} combos)")
        if not res:
            print("   (no feasible+priced combinations)")
        for r in res[:args.n]:
            print("   " + line(r))

    all_results.sort(key=lambda r: r["cost"])
    print(f"\n=== Top {args.overall} overall (cheapest feasible across all configs) ===")
    for r in all_results[:args.overall]:
        print(f"  {r['config']:<3} " + line(r))
    if not all_results:
        print("  (none)")


if __name__ == "__main__":
    main()
