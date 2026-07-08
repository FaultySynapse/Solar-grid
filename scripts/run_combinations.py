#!/usr/bin/env python3
"""
Run the tent-cooling configuration combinations.

Loads the parts data (data/parts/*.json) and the config table (data/configs.json),
then for every configuration filters each part-category's parts against that
config's constraints. A part qualifies for a slot only if it satisfies EVERY
constraint; anything else is disqualified. `null` in a cell means the part is not
used in that config ("none").

Usage:
  python3 scripts/run_combinations.py                # summary per config
  python3 scripts/run_combinations.py --config C6    # one config, verbose
  python3 scripts/run_combinations.py --table        # render the config x category constraint table
  python3 scripts/run_combinations.py --enumerate 5  # list up to 5 full part combinations per config
  python3 scripts/run_combinations.py --check        # validate constraint fields against spec definitions

No third-party dependencies (Python 3.8+ standard library only).
"""
import argparse
import json
import itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PARTS_DIR = DATA / "parts"


# ---------- loading ----------

def load_categories():
    """Return {category: {"specs": {...}, "parts": [...]}} from data/parts/*.json."""
    cats = {}
    for f in sorted(PARTS_DIR.glob("*.json")):
        obj = json.loads(f.read_text())
        cats[obj["category"]] = {"specs": obj.get("specs", {}), "parts": obj.get("parts", [])}
    return cats


def load_configs():
    return json.loads((DATA / "configs.json").read_text())


# ---------- constraint matching ----------

def _as_number(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def match_field(part_value, requirement):
    """True if a single part field satisfies one constraint requirement."""
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
    # scalar requirement: equality, or membership if the part field is a list
    if isinstance(part_value, list):
        return requirement in part_value
    return _scalar_eq(part_value, requirement)


def _scalar_eq(a, b):
    na, nb = _as_number(a), _as_number(b)
    if na is not None and nb is not None:
        return na == nb
    return a == b


def matches(part, constraints):
    """True if a part satisfies all constraints in a cell (missing field => fail)."""
    for field, req in constraints.items():
        if field not in part:
            return False
        if not match_field(part[field], req):
            return False
    return True


def qualifying_parts(category_parts, constraints):
    return [p for p in category_parts if matches(p, constraints)]


# ---------- rendering ----------

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
        slot_options = {}
        combo_count = 1
        for cat in categories:
            cell = cfg["constraints"].get(cat)
            if cell is None:
                print(f"  {cat:<18}: none")
                continue
            parts = cats.get(cat, {}).get("parts", [])
            hits = qualifying_parts(parts, cell)
            slot_options[cat] = hits
            if hits:
                ids = ", ".join(p["id"] for p in hits)
                print(f"  {cat:<18}: {len(hits):>2} match  [{ids}]")
                combo_count *= len(hits)
            else:
                print(f"  {cat:<18}:  0 match  ⚠  NO QUALIFYING PART  ({summarize_constraint(cell)})")
                combo_count = 0
        print(f"  -> valid combinations: {combo_count}")
        if enumerate_n and combo_count:
            cats_used = [c for c in categories if cfg['constraints'].get(c) is not None]
            lists = [slot_options[c] for c in cats_used]
            for i, combo in enumerate(itertools.product(*lists)):
                if i >= enumerate_n:
                    print(f"     ... ({combo_count - enumerate_n} more)")
                    break
                parts_str = ", ".join(f"{c}={p['id']}" for c, p in zip(cats_used, combo))
                print(f"     [{i + 1}] {parts_str}")


def render_table(configs):
    categories = configs["part_categories"]
    header = ["Config"] + categories
    rows = [header]
    for cfg in configs["configs"]:
        row = [cfg["id"]]
        for cat in categories:
            row.append(summarize_constraint(cfg["constraints"].get(cat)))
        rows.append(row)
    widths = [max(len(r[i]) for r in rows) for i in range(len(header))]
    for ri, row in enumerate(rows):
        print(" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))
        if ri == 0:
            print("-+-".join("-" * widths[i] for i in range(len(header))))


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
                    print(f"  {cfg['id']}.{cat}: constraint field '{field}' not defined in {cat} specs"); ok = False
    print("check: OK" if ok else "check: problems found")
    return ok


def main():
    ap = argparse.ArgumentParser(description="Run tent-cooling config combinations.")
    ap.add_argument("--config", help="only show this config id (e.g. C6)")
    ap.add_argument("--table", action="store_true", help="print the config x category constraint table")
    ap.add_argument("--enumerate", type=int, default=0, metavar="N", help="list up to N full part combinations per config")
    ap.add_argument("--check", action="store_true", help="validate constraint fields against spec definitions")
    args = ap.parse_args()

    cats = load_categories()
    configs = load_configs()

    if args.check:
        check(configs, cats)
        return
    if args.table:
        render_table(configs)
        return
    run(configs, cats, only=args.config, enumerate_n=args.enumerate)


if __name__ == "__main__":
    main()
