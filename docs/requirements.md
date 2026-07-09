# Requirements & Design Target

This is the **single source of truth** for what the system must do. Every
configuration and every sizing calculation references the numbers here. Edit
this file to retarget the whole project.

> **Machine-readable companion:** [`../data/scenario.json`](../data/scenario.json)
> holds these conditions as structured data (site, space, thermal load, non-AC
> loads, cloudy-day bridge, system constraints, and derived sizing targets), each
> field tagged `known` / `assumption` / `open` / `derived`. Keep the two in sync.

> Status: **Retargeted to the real use case — a shaded desert tent, daytime
> solar-direct cooling** (confirmed 2026-07-08). See `decisions/0003` for the
> pivot from the earlier residential-dwelling baseline. Earlier configs A/B/C are
> kept as *reference for a room/dwelling* but are oversized for this target.

## Use case in one line

Cool a **shaded ~60–70 sq ft tent** (two-queen footprint) in the **Nevada desert
in August**, **while sleeping during the day**, for a **~1-week trip**, using a
**DIY 12/24 V DC refrigerant AC + solar + battery** system. Because cooling
happens in the daytime, the array runs the AC **live off the sun** and the
battery is only a small buffer.

## 1. Primary load — the AC unit

| Parameter | Value | Notes |
|-----------|-------|-------|
| AC type | **DC refrigerant split AC** (vehicle/RV "parking cooler" class) | Runs straight off the battery bus — no inverter. Chosen over a mini-split because the space is tiny and DIY-DC is simplest. |
| Cooling capacity | ~9,000–11,000 BTU/h | *Oversized* for a shaded tent this size (5–6k would do), but cheap and gives margin against a leaky envelope + desert heat. |
| Running power | **~400–650 W** while cooling | The linked 12 V unit: ~400–600 W. A right-sized 5–6k unit would be ~300–400 W. |
| Supply voltage | **12 VDC (linked unit)** or **24 VDC (recommended variant)** | 24 V halves the current (~30 A vs ~60–80 A) → lighter wiring. See `decisions/0002`. |
| Startup surge | Moderate DC inrush | Battery buffer absorbs it so panels aren't slammed. |

## 2. Site / environment

| Parameter | Value | Notes |
|-----------|-------|-------|
| Location | **Nevada desert, August** (Black Rock–style playa) | Very hot, very bright, **very dry**, big day/night temperature swing. |
| Space to cool | **Tent, ~60–70 sq ft** (two queens), fabric envelope | Poor insulation & air-leaky → can't hold cold like a sealed room; **shade is the biggest lever**. |
| Shading | **Not in direct sun** ✅ | Already shaded — huge win. Add a reflective tarp/space-blanket over the tent with an air gap to cut radiant load further (free "component"). |
| Peak sun hours (PSH) | **~7.0 PSH/day** | Nevada August is near best-case solar; midday irradiance is intense. |
| Design ambient temp | ~100–110 °F day / ~60–70 °F night | Days are brutal; nights cool off (matters only if you ever cool at night). |
| Mounting | **Ground, portable, wind- & dust-secured** | One-week trip: stake/ballast the panels low, protect electronics from playa dust. |

## 3. Load profile & autonomy

| Parameter | Value | Notes |
|-----------|-------|-------|
| Cooling window | **Daytime, while sleeping (~8 h)** | Aligns with peak sun → run the AC **directly off the array**. |
| Average AC power while running | ~500 W | Assume near-continuous in a hot leaky tent. |
| **AC energy per sleep session** | **~4 kWh** | Most delivered **live from panels**; only a fraction comes from the battery. |
| Battery-backed portion | **~1.5 kWh** | Covers surge, passing clouds, and the shoulders before/after solar noon. |
| Autonomy | **2-day cloudy bridge** + ~4–5 h daily buffer | Battery carries 2 overcast days at `design_daily × (1 − cloudy_derate)` plus the daily solar-direct buffer. Set in `data/scenario.json` `resilience.cloudy_day_bridge`. |
| System voltage | **12 V (as-linked)** or **24 V (recommended)** | 24 V is meaningfully better for wiring/MPPT; 12 V is fine if you use the exact linked unit and keep runs short. |

## 4. Priorities (ranked)

1. **Reliable comfort from the active AC** — the refrigerant AC must reach a
   comfortable temperature **and keep humidity low on its own**, sized for a leaky
   fabric tent at 100–110 °F with **no reliance on shade/insulation or evaporative
   add-ons**. Keep the unit's capacity margin. See `decisions/0004`.
2. **Lowest cost + portability** — cheap parts, packs down, quick setup/teardown for a one-week trip.
3. **Dust & heat survivability** — playa dust and 110 °F sun are the real enemies of the gear.

> Efficiency add-ons (shade/insulation, evaporative cooling) are **parked** in
> `docs/efficiency-backlog.md` — desirable later, but explicitly *not* counted in
> sizing.

## 5. Constraints & preferences

- Budget target: ⟨set a $ ceiling⟩ — DIY tent build lands roughly **$1,500–2,400**.
- Battery chemistry: **LiFePO4** (safe, deep cycling, light) — small pack (~2.5 kWh).
- No inverter in the AC path (DC unit) → skip the pure-sine inverter entirely.
- Cooling type: **refrigerant AC** (chosen over evaporative — see `decisions/0003`).
- Dust protection: sealed tote/case for battery+MPPT, cable glands, filters cleanable.
- Physical space for array: portable ground array (~1 kW ≈ ~55 sq ft of panel).

## 6. Resolved / open questions

Resolved (2026-07-08):
- [x] Space = shaded tent (~60–70 sq ft) → small DC unit, not a mini-split.
- [x] Cooling window = daytime while sleeping → **solar-direct**, small battery.
- [x] Cooling type = refrigerant AC (not evaporative).
- [x] Build style = DIY battery + solar + MPPT.
- [x] Duration = one-off ~1-week trip → portable, dust-hardened.
- [x] Location = Nevada desert August → ~7 PSH.

Still open:
- [ ] **12 V (exact linked unit) vs 24 V (recommended)** — final call. See `decisions/0002`.
- [ ] Confirm the chosen unit's **real running watts + duty cycle** (measure with a clamp meter if possible) — drives array size.
- [ ] Set a budget ceiling.
- [ ] Confirm array is rigid panels vs folding "briefcase" kits (portability vs $/W).
