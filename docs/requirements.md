# Requirements & Design Target

This is the **single source of truth** for what the system must do. Every
configuration and every sizing calculation references the numbers here. Edit
this file to retarget the whole project.

> Status: **Baseline / placeholder values.** Replace the ⟨bracketed⟩ items and
> the "Baseline value" column with your real numbers.

## 1. Primary load — the AC unit

| Parameter | Baseline value | Notes / how to fill in |
|-----------|---------------|------------------------|
| AC type | Inverter mini-split (ductless) | Inverter compressors soft-start and modulate → far kinder to off-grid than non-inverter window units. |
| Cooling capacity | 12,000 BTU/h (1 ton) | From the unit's nameplate. |
| Efficiency (SEER2 / EER) | ~SEER2 20, EER ~12 | Higher = less energy per BTU. Modern mini-splits: SEER2 18–24. |
| Rated running power | ~700 W nominal (range ~300–1,100 W) | Inverter units modulate; nameplate max is higher than typical draw. |
| Startup surge | Low (soft start) | Inverter units avoid the hard LRA surge of non-inverter compressors. |
| Supply voltage | 115 VAC (or 230 VAC) | Determines inverter output. Some off-grid units are native 48 VDC (see catalog). |

## 2. Site / environment

| Parameter | Baseline value | Notes |
|-----------|---------------|-------|
| Location | ⟨your location⟩ | Drives peak sun hours and cooling demand. |
| Space to cool | ⟨area / room / van / dwelling⟩ | **Deciding factor for the AC power path** (see `decisions/0002`). Small van/room favors a cheap 12/24 V DC unit; a real room/dwelling favors a residential mini-split. |
| Peak sun hours (PSH) | **5.0 PSH/day** (placeholder) | Look up your location's PSH; design around the **worst-usable month**, not the annual average. |
| Design ambient temp | ⟨°F/°C⟩ | Hotter = higher AC duty cycle = more kWh/day. |
| Mounting | ⟨roof / ground / pole⟩ | Affects panel count, tilt, wiring runs. |

## 3. Load profile & autonomy

| Parameter | Baseline value | Notes |
|-----------|---------------|-------|
| Cooling runtime | ~8–10 h/day | When the AC actually runs. |
| Average AC power while running | ~600 W (duty-cycled) | Real average is below nameplate because the compressor modulates. |
| **AC energy/day** | **~5.0 kWh/day** | See sizing methodology for how this is derived. |
| Other loads | ~0.5 kWh/day (controls, fans, phantom) | Keep the AC the dominant load; budget small extras here. |
| **Total energy/day (design)** | **~5.5 kWh/day** | The number configs are sized to. |
| Autonomy | **1 day** | Days the battery alone can carry the load with no sun. |
| System voltage | **48 V** nominal | 48 V is the sweet spot at this power (lower current, thinner wire, more inverter choice). |

## 4. Priorities (ranked)

1. **Balanced cost/performance** — reasonable off-the-shelf parts, good value.
2. Reliability adequate for daily use (LiFePO4 battery, pure-sine inverter).
3. Expandability — leave room to add panels/battery later.

> To change priority (e.g. "lowest upfront cost" or "max reliability"), note it
> here and add/adjust a configuration in `configurations/`.

## 5. Constraints & preferences

- Budget target: ⟨$ ceiling⟩ — *set this; it decides many part choices.*
- Battery chemistry: **LiFePO4** (safety, cycle life, depth of discharge).
- Inverter waveform: **pure sine** (required — AC compressors dislike modified sine).
- Code/permitting: ⟨grid-tied backfeed? permit required? RV/marine?⟩
- Physical space for array: ⟨m²/ft² available⟩.

## 6. Open questions to resolve

- [ ] Confirm the exact AC model and pull its real datasheet power/energy figures.
- [ ] Confirm location → real peak sun hours (worst-usable month).
- [ ] Confirm runtime pattern (daytime-only vs into the evening vs 24/7).
- [ ] Set a budget ceiling.
- [ ] AC power path: AC-inverter mini-split vs native 48 V DC vs 12/24 V DC vehicle unit? (big architecture fork — see `decisions/0002-ac-unit-power-path.md`). Depends on the "space to cool" answer above.
