# Catalog Pruning — strictly-worse parts

Some parts in the catalog can never be the right choice: another part matches
them on every capability that gates a slot **and** is at least as good on every
cost/mass/size dimension the solver scores, while being strictly better on at
least one. Such a part is *Pareto-dominated* — removing it changes no optimal
solution, only shrinks the search.

`scripts/prune.py` finds these automatically and documents why. It never
touches data unless you pass `--apply`.

```bash
python3 scripts/prune.py            # report: criteria + dominated parts per category
python3 scripts/prune.py --apply    # ALSO delete dominated parts from data/parts/*.json
```

## Domination rule

A part **A dominates B** when, for A to be a drop-in replacement anywhere B
could go and never be worse:

1. **Gating fields must match or cover.** A must satisfy every categorical /
   capability field the solver keys on — otherwise A can't physically stand in
   for B in some slot B qualifies for.
   - `=` equal (e.g. `supply_type`, inverter `class`/`waveform`, converter
     `output_voltage`).
   - `⊇` superset — A supports every bus/input voltage B does, and maybe more
     (e.g. `input_voltage`, `bus_voltage`, `max_battery_v`).
   - `≥` A's boolean capability is not lower (e.g. `inverter_compressor`).
   - `≈` within tolerance — same size class, so per-unit coupling is identical
     (battery `capacity_kwh` within 2%; see below).
   - `condition≥` A is in equal-or-better working order (new > used >
     needs-repair). A part in worse condition never dominates.
2. **Scored dimensions: A ≤ B on every "lower is better", ≥ on every "higher is
   better", strictly so on at least one.** `≤` price, mass, idle/running draw;
   `≥` capacity, efficiency, rated current/power/voltage headroom.

## Per-category criteria

| category | gating (must match/cover) | scored (A must win) | class |
|---|---|---|---|
| `ac_unit` | supply_type=, supply_voltage⊇, inverter_compressor≥, condition≥ | price≤, mass≤, running_w≤, cooling_btu≥ | SAFE |
| `inverter` | class=, waveform=, input_voltage⊇ | price≤, mass≤, idle_w≤, continuous_w≥, efficiency≥, mppt_efficiency≥, pv_max_voltage≥ | SAFE |
| `charge_controller` | type=, max_battery_v⊇ | price≤, mass≤, rated_a≥, max_pv_voc≥, efficiency≥ | SAFE |
| `bms` | bus_voltage⊇ | price≤, mass≤, continuous_a≥ | SAFE |
| `dc_dc_converter` | output_voltage=, input_voltage⊇ | price≤, mass≤, continuous_a≥, efficiency≥ | SAFE |
| `battery` | capacity_kwh≈, bus_voltage⊇, condition≥ | price≤, mass≤ | SAFE |
| `solar_panel` | (per effective watt) | price/effW≤, mass/effW≤, area/effW≤, voc≤ | ADVISORY |

**SAFE** = raw-spec domination. Removing these parts is guaranteed not to drop
any optimal build.

**ADVISORY** = a per-unit normalization is applied, so domination is a strong
hint but not a proof. Review before applying.

### Why battery uses `capacity_kwh≈` and not `$/kWh`

Batteries look like a per-kWh commodity, but the solver couples cell size
non-linearly: cells go in fixed **series strings** (S = 4/8/16 for 12/24/48 V)
with **one BMS per string**, and packs round **up** to whole cells. A cheaper
`$/kWh` cell can still lose once you count more strings (more BMS cost) or more
overshoot past the energy target. That is a genuine two-sided tradeoff across
sizes, so we do **not** prune on `$/kWh`.

Instead we only compare cells of the **same capacity** (within 2%). Equal kWh →
identical string count, BMS count, and packing granularity, so the cheaper +
lighter cell wins outright. This keeps every energy-vs-count tradeoff in the
catalog and prunes only true same-class duplicates — hence SAFE.

### Terminal type — unusable, not dominated

Weld-only cells (`terminal_type: weld-only`) are excluded from the battery
domination pool entirely. The configs require bolt/stud/lug terminals (a DIY
build can't spot-weld a busbar), so a weld-only cell can never substitute for
another cell — it is neither dominator nor dominated. `prune.py` lists these
separately as **unusable** rather than letting a cheap weld-only cell falsely
"dominate" cells you can actually build with.

### Why solar panels use effective watts

A panel's real contribution is its rating **after** the cell-temperature derate
at the design ambient (desert August), so we compare `$`, `mass`, and `area`
**per effective watt**, and prefer lower `Voc` (more controller-compatible).
This crosses different panel sizes, so it's ADVISORY — a dominated panel is
very likely redundant, but confirm it isn't the only one that fits a specific
string-voltage window before deleting.

## Workflow

Run the report, sanity-check the ADVISORY (solar_panel) findings, then
`--apply` and re-run the solver self-check:

```bash
python3 scripts/prune.py
python3 scripts/prune.py --apply
python3 scripts/run_combinations.py --check
```
