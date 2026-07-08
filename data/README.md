# Data-driven configurations

The configuration space is data, not prose. Parts live as structured JSON; each
configuration is a row of **constraints** per part category; a script filters the
parts against the constraints to tell you which parts qualify and how many valid
combinations each config has.

```
data/
  scenario.json           # the conditions that set up the power solution (inputs to size against)
  parts/<category>.json   # per-category: spec definitions + the parts list
  configs.json            # the config table (rows=configs, cols=part categories)
scripts/
  run_combinations.py     # loads it all and runs the combinations
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
