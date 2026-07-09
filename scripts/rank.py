#!/usr/bin/env python3
"""
Rank part combinations by the balanced score — top N per config and overall.

The score balances the three objective metrics (total construction cost, panel
area, system mass) using the weights in data/costs.json:

    score = total_construction_cost
          + mass_penalty_per_kg * system_mass_kg
          + area_penalty_per_m2 * array_area_m2      (lower = better)

FAIL combinations are excluded; WARN combinations are included unless --no-warn.
Combinations with an unknown price (a selected part has no price_usd) are skipped.

Usage:
  python3 scripts/rank.py               # top 3 per config + top 10 overall
  python3 scripts/rank.py --n 5 --overall 20
  python3 scripts/rank.py --no-warn     # only fully-PASS combinations
  python3 scripts/rank.py --by cost     # rank by raw cost instead of balanced score
"""
import argparse
import run_combinations as rc


def rank_all(no_warn=False, by="score"):
    scenario = rc.load_scenario()
    K = rc.load_metric_constants()
    costs = rc.load_costs()
    cats = rc.load_categories()
    configs = rc.load_configs()

    per_config, stats = {}, {}
    for cfg in configs["configs"]:
        results, evaluated, priced = [], 0, 0
        for combo in rc.iter_combos(cfg, cats):
            if any(combo[c] is None for c in ("ac_unit", "solar_panel", "battery", "bms")):
                continue
            evaluated += 1
            m, checks = rc.compute_metrics(cfg, combo, scenario, K, costs)
            if m.get("incomplete"):
                continue
            v = rc.verdict(checks)
            if v == "FAIL" or (no_warn and v == "WARN"):
                continue
            if m["total_construction_cost"] is None:
                continue
            priced += 1
            sc = rc.score(m, costs)
            results.append({
                "config": cfg["id"], "arch": cfg["architecture"], "bus": cfg["bus_voltage"],
                "score": sc, "cost": m["total_construction_cost"], "verdict": v,
                "mass": m["system_mass_kg"], "area": m["array_area_m2"],
                "daily_kwh": m["design_daily_energy_wh"] / 1000, "array_w": m["array_w_provided"],
                "batt_kwh": m["battery_kwh_provided"], "autonomy_h": m["autonomy_hours"],
                "combo": {c: (p["id"] if p else None) for c, p in combo.items()},
            })
        key = (lambda r: r["cost"]) if by == "cost" else (lambda r: r["score"])
        results.sort(key=key)
        per_config[cfg["id"]] = results
        stats[cfg["id"]] = (evaluated, priced, len(results))
    return configs, per_config, stats, by


def line(r):
    c = r["combo"]
    picks = " ".join(f"{k}={c[k]}" for k in ("ac_unit", "inverter", "dc_dc_converter",
                     "charge_controller", "battery", "bms", "solar_panel") if c.get(k))
    return (f"score {r['score']:>6,.0f} | ${r['cost']:>6,.0f} {r['mass']:>3.0f}kg "
            f"{r['area']:.1f}m2 [{r['verdict']:<4}] {r['daily_kwh']:.1f}kWh/d "
            f"auton {r['autonomy_h']:.0f}h  {picks}")


def main():
    ap = argparse.ArgumentParser(description="Top-N combinations per config and overall.")
    ap.add_argument("--n", type=int, default=3, help="top N per config (default 3)")
    ap.add_argument("--overall", type=int, default=10, help="top N overall (default 10)")
    ap.add_argument("--no-warn", action="store_true", help="exclude WARN combinations")
    ap.add_argument("--by", choices=["score", "cost"], default="score", help="ranking key (default balanced score)")
    args = ap.parse_args()

    configs, per_config, stats, by = rank_all(no_warn=args.no_warn, by=args.by)
    print(f"Ranking by: {by}  (score = cost + mass/area penalties from data/costs.json)")

    cats = rc.load_categories()
    all_results = []
    print("\n=== Top per config ===")
    for cfg in configs["configs"]:
        res = per_config[cfg["id"]]
        all_results.extend(res)
        ev, pr, fe = stats[cfg["id"]]
        opts = rc.slot_options(cfg, cats)
        thin = [f"{c}={len(ps)}" for c, ps in opts.items() if ps is not None and len(ps) <= 2]
        thin_s = f"  ⚠ thin: {', '.join(thin)}" if thin else ""
        print(f"\n{cfg['id']} {cfg['label']}  [{cfg['architecture']}, {cfg['bus_voltage']}V]  "
              f"({fe} feasible / {pr} priced / {ev} combos){thin_s}")
        if not res:
            print("   (no feasible+priced combinations)")
        for r in res[:args.n]:
            print("   " + line(r))

    key = (lambda r: r["cost"]) if by == "cost" else (lambda r: r["score"])
    all_results.sort(key=key)
    print(f"\n=== Top {args.overall} overall ===")
    for r in all_results[:args.overall]:
        print(f"  {r['config']:<3} " + line(r))
    if not all_results:
        print("  (none)")


if __name__ == "__main__":
    main()
