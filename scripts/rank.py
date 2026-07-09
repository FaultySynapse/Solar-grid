#!/usr/bin/env python3
"""
Rank part combinations by the balanced score — top N per config and overall.

Uses the fast decomposed optimizer (run_combinations.optimize_config): it returns
the best solution per load block (ac_unit x inverter x converter), which is both
fast and diverse (each entry is a genuinely different system, not a near-duplicate).

Score = total_construction_cost + mass/area penalties + condition penalty (costs.json).
FAIL combos are excluded; WARN included unless --no-warn.

Usage:
  python3 scripts/rank.py               # top 3 per config + top 10 overall
  python3 scripts/rank.py --n 5 --overall 20
  python3 scripts/rank.py --no-warn     # only fully-PASS combinations
  python3 scripts/rank.py --by cost     # rank by raw cost instead of balanced score
"""
import argparse
import run_combinations as rc


def line(r):
    c = {k: (p["id"] if p else None) for k, p in r["combo"].items()}
    picks = " ".join(f"{k}={c[k]}" for k in ("ac_unit", "inverter", "dc_dc_converter",
                     "charge_controller", "battery", "bms", "solar_panel") if c.get(k))
    m = r["m"]
    return (f"score {r['score']:>6,.0f} | ${r['cost']:>6,.0f} {m['system_mass_kg']:>3.0f}kg "
            f"{m['array_area_m2']:.1f}m2 [{r['verdict']:<4}] {m['design_daily_energy_wh']/1000:.1f}kWh/d "
            f"auton {m['autonomy_cycles']:.1f}cyc  {picks}")


def main():
    ap = argparse.ArgumentParser(description="Top-N combinations per config and overall.")
    ap.add_argument("--n", type=int, default=3, help="top N per config (default 3)")
    ap.add_argument("--overall", type=int, default=10, help="top N overall (default 10)")
    ap.add_argument("--no-warn", action="store_true", help="exclude WARN combinations")
    ap.add_argument("--by", choices=["score", "cost"], default="score", help="ranking key")
    args = ap.parse_args()

    scenario, K, costs = rc.load_scenario(), rc.load_metric_constants(), rc.load_costs()
    cats, configs = rc.load_categories(), rc.load_configs()
    cat_opts_of = lambda cfg: rc.slot_options(cfg, cats)

    print(f"Ranking by: {args.by}  (score = cost + mass/area/condition penalties, data/costs.json)")
    all_results = []
    print("\n=== Top per config (best per load block) ===")
    for cfg in configs["configs"]:
        res = rc.optimize_config(cfg, cats, scenario, K, costs, by=args.by, no_warn=args.no_warn)
        for r in res:
            r["config"] = cfg["id"]
        all_results.extend(res)
        opts = cat_opts_of(cfg)
        thin = [f"{c}={len(ps)}" for c, ps in opts.items() if ps is not None and len(ps) <= 2]
        thin_s = f"  ⚠ thin: {', '.join(thin)}" if thin else ""
        print(f"\n{cfg['id']} {cfg['label']}  [{cfg['architecture']}, {cfg['bus_voltage']}V]  "
              f"({len(res)} feasible load blocks){thin_s}")
        if not res:
            print("   (no feasible priced solution)")
        for r in res[:args.n]:
            print("   " + line(r))

    all_results.sort(key=(lambda r: r["cost"]) if args.by == "cost" else (lambda r: r["score"]))
    print(f"\n=== Top {args.overall} overall ===")
    for r in all_results[:args.overall]:
        print(f"  {r['config']:<3} " + line(r))
    if not all_results:
        print("  (none)")


if __name__ == "__main__":
    main()
