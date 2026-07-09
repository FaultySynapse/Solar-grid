# Data-driven configurations

The configuration space is data, not prose. Parts live as structured JSON; each
configuration is a row of **constraints** per part category; a script filters the
parts against the constraints to tell you which parts qualify and how many valid
combinations each config has.

All quantities are **metric** (W, degC, m2, Wh, kWh); AC nameplate BTU/h is
converted to thermal watts inside the engine.

```
data/
  scenario.json           # CONDITIONS only — inputs. No derived values.
  metrics.json            # derived-parameter DEFINITIONS (formulas, inputs, feasibility) + constants
  costs.json              # cost adders (feed the cost metric) + BALANCE weights (trade cost vs mass vs area)
  parts/<category>.json   # per-category: spec definitions + the parts list (incl. mass_kg; panels have area_m2; bms is its own category)
  configs.json            # the config table (rows=configs, cols=part categories; each row tags bus_voltage + architecture)
scripts/
  run_combinations.py     # ENGINE: filters parts against constraints AND computes metrics (incl. cost/mass/area)
  solve.py                # detailed metrics + feasibility + objectives for one combination
  rank.py                 # top-N combinations by balanced score, per config and overall
```

Part categories: `ac_unit`, `inverter`, `charge_controller`, `dc_dc_converter`,
`battery`, **`bms`** (its own part), `solar_panel`, plus `balance_of_system` (reference).
The tent configs require **bare batteries** (`bms_included: false`) so a BMS part is
always selected; turnkey packs with an integrated BMS aren't in the candidate set.

## Conditions vs. derived (important split)
- **`scenario.json` holds only conditions/inputs** — site, space, thermal
  envelope, cooling schedule, non-AC loads, resilience targets, system
  constraints. It contains **no derived values**. In particular, **AC running
  power and duty cycle are NOT stored here** — they are computed from the chosen
  AC part (`running_w`, `cooling_btu`) and the thermal load.
- **`metrics.json` defines the derived parameters** — each with a formula, the
  inputs it consumes, and (where relevant) a feasibility condition. Plus shared
  constants (system efficiency, margins, cold-Voc factor, headrooms).
- **`solve.py` solves those metrics for a part combination.** Because the derived
  values depend on which parts are picked, they are computed per combination, not
  stored.

```bash
python3 scripts/run_combinations.py --metrics       # metrics + cost, representative combo per config
python3 scripts/solve.py --config C6                 # full metrics + feasibility + cost for one combo
python3 scripts/solve.py --config C2 --set battery=eve-lf280k --set solar_panel=canadian-400w
python3 scripts/solve.py --list-metrics              # the derived-parameter definitions + constants
```
Verdict per combination is PASS / WARN / FAIL from the feasibility checks (e.g. AC
can hold setpoint, controller PV-voltage/current fits, inverter power headroom).

## Objectives, balancing & ranking — `data/costs.json` + `scripts/rank.py`
Three **objective metrics** are computed per combination:
- **`total_construction_cost`** = sum(part `price_usd` × quantity) + adders (BoS,
  wiring, mounting, dust box) × contingency. Quantities come from the solved
  metrics (`panels_needed`, `battery_blocks_needed`, and BMS × `battery_strings`).
  A part with no `price_usd` makes the cost unknown → excluded from ranking.
- **`array_area_m2`** = `panels_needed` × panel `area_m2` (transport/mount bulk).
- **`system_mass_kg`** = Σ(part `mass_kg` × quantity) (portability).

`costs.json` `balance.weights` combine them into one **score** (lower = better):
```
score = total_construction_cost
      + mass_penalty_per_kg  × system_mass_kg     (default $5/kg)
      + area_penalty_per_m2  × array_area_m2       (default $20/m²)
```
Penalties are cost-equivalent, so the score is in dollars; set a penalty to 0 to
ignore that objective. `rank.py` enumerates every qualifying combination, solves
it, drops FAILs, and reports the best N by score, per config and overall:
```bash
python3 scripts/rank.py                 # top 3 per config + top 10 overall (by balanced score)
python3 scripts/rank.py --n 5 --overall 20
python3 scripts/rank.py --no-warn       # PASS-only (exclude WARN)
python3 scripts/rank.py --by cost       # rank by raw cost instead of balanced score
```

## Scenario — `data/scenario.json`
The machine-readable **conditions** that drive a power solution (the companion to
`docs/requirements.md`): site (location, peak sun hours, outside temps, humidity,
dust), space (tent area, envelope, shading, occupancy), thermal load (AC size,
running watts, duty cycle), cooling schedule, non-AC loads, resilience
(**cloudy-day bridge**, buffer runtime, DoD), system constraints (bus voltage,
chemistry, no-weld, budget), and **derived_targets** computed from those via
`docs/sizing-methodology.md`. Every field carries `value`, `unit`, `definition`,
and a `status` of `known` / `assumption` / `open` / `derived`.

## Part files — `data/parts/<category>.json`
Each file has two blocks:
- **`specs`** — the spec configuration: every spec key with its `definition`,
  `unit`, and `type`. This is the data dictionary for that category.
- **`parts`** — the actual parts, each an object of `spec_key: value`.

A value may be a scalar or a **list** (e.g. a multi-voltage unit's
`supply_voltage: [24, 48]`, or a controller's `max_battery_v: [12, 24, 48]`).

Categories: `ac_unit`, `inverter`, `charge_controller`, `battery`,
`dc_dc_converter`, `solar_panel`.

## Config table — `data/configs.json`
`part_categories` are the columns. Each config has a `constraints` object mapping
category → **cell**, where a cell is:
- **`null`** — the part is **not used** in this config ("none").
- **`{}`** — any part in the category qualifies.
- **a constraint object** — `spec_key: requirement` pairs. A part qualifies only if
  it satisfies **every** requirement; a missing field or any violation disqualifies it.

### Requirement forms
| Form | Meaning |
|------|---------|
| `"DC"` / `24` | equality; if the part field is a list, **membership** (`24` matches `[24,48]`) |
| `{ "min": 60 }` | numeric `>= 60` |
| `{ "max": 100 }` | numeric `<= 100` |
| `{ "in": [12,24] }` | value is one of |
| `{ "ne": "weld-only" }` | not equal to |
| `{ "contains": 48 }` | the part's **list** field includes `48` (e.g. `bus_voltage`) |

Example cell — *"a LiFePO4 pack that can build a 48 V bus and isn't weld-only"*:
```json
"battery": { "chemistry": "LFP", "bus_voltage": { "contains": 48 }, "terminal_type": { "ne": "weld-only" } }
```

## Running it
```bash
python3 scripts/run_combinations.py            # qualifying parts + combo count per config
python3 scripts/run_combinations.py --table    # the config x category constraint table
python3 scripts/run_combinations.py --config C6 --enumerate 5   # list some full combinations
python3 scripts/run_combinations.py --check    # validate every constraint field is a defined spec
```
Standard library only (Python 3.8+).

## How this maps to the axes
- **Architecture** shows up as which slots are `null`: DC-direct has `inverter: null`;
  the converter path fills `dc_dc_converter`; the AC path fills `inverter` and (for
  standalone) `charge_controller`.
- **Combined vs standalone** is the inverter cell's `class` (`all-in-one` vs
  `standalone`) — and standalone configs additionally require a `charge_controller`.
- **Bus voltage** threads through `supply_voltage` / `input_voltage` /
  `max_battery_v` / `bus_voltage`.

To add a part, drop it into the category's `parts` list. To add a configuration,
add a row to `configs.json`. Re-run the script — no code changes needed.
