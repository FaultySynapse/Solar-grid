# Configurations

Human-readable view of the candidate builds. The machine-readable source of truth
is [`../data/configs.json`](../data/configs.json) (the config constraint table);
sizing, feasibility, and cost are computed by the scripts in [`../scripts/`](../scripts/).

Target: shaded ~6 m² tent, Nevada desert August, cool while sleeping by day, DIY
system, ~1-week trip. See [`../docs/requirements.md`](../docs/requirements.md) and
[`../decisions/0003`](../decisions/0003-retarget-to-desert-tent.md).

**➡️ Full list by key parameter combination: [`candidates.md`](candidates.md)** — 9
builds spanning DC-direct vs AC-inverter (combined vs standalone) across 12/24/48 V.

| # | Architecture | Inverter class | Bus | AC unit |
|---|--------------|----------------|-----|---------|
| C1 | DC-direct | — | 12 V | 12 V cooler |
| C2 | DC-direct | — | 24 V | 24 V DC mini-split |
| C3 | DC-direct | — | 48 V | 48 V DC mini-split |
| C4 | DC + converter | — (48→12 V) | 48 V | 12 V cooler |
| C5 | AC-inverter | Combined (all-in-one) | 24 V | 115 V mini-split/window |
| C6 | AC-inverter | Combined (all-in-one) | 48 V | 115 V mini-split |
| C7 | AC-inverter | Standalone + MPPT | 12 V | 115 V window |
| C8 | AC-inverter | Standalone + MPPT | 24 V | 115 V mini-split/window |
| C9 | AC-inverter | Standalone + MPPT | 48 V | 115 V mini-split |

Shared fundamentals (solar-direct concept, shade, wiring, playa/dust) live in
[`config-d-tent-solar-direct.md`](config-d-tent-solar-direct.md).

## Working with configs
- **Compare / size:** `python3 scripts/run_combinations.py --metrics` (per-config
  representative combo) · `python3 scripts/solve.py --config Cx` (full detail).
- **Cheapest feasible builds:** `python3 scripts/rank.py`.
- **Add/edit a config:** edit the row in [`../data/configs.json`](../data/configs.json)
  (each cell is `null` or a constraint) and re-run. Record pivots in [`../decisions/`](../decisions/).
