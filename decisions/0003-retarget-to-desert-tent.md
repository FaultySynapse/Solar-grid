# 0003 — Retarget: desert tent, daytime solar-direct cooling

**Status:** Accepted · 2026-07-08 · supersedes the residential baseline in `0001`-era configs

## Context
Initial scaffolding assumed a residential room/dwelling (12k mini-split, 48 V,
overnight autonomy — configs A/B/C). The real use case is very different:

- **Space:** a shaded tent, ~60–70 sq ft (two-queen footprint), fabric envelope.
- **Location:** Nevada desert, August — ~100–110 °F days, ~7 PSH, **very dry**, big day/night swing.
- **When:** cooling **during the day, while sleeping** (~8 h).
- **Type:** refrigerant AC (not evaporative).
- **Build:** DIY battery + solar + MPPT.
- **Duration:** one-off ~1-week trip → portable, dust-hardened.

## Decision
Retarget the whole project to this use case:

1. **Daytime cooling ⇒ solar-direct architecture.** The sleep/cool window overlaps
   peak sun, so the **array runs the AC live** and the **battery is a small buffer**
   (surge + clouds + shoulders), *not* an overnight bank. This is the cheapest
   possible design and the single biggest simplification.
2. **DC unit, no inverter** (from `0002`, Option C).
3. **Right-size down.** A shaded tent needs far less than 11k BTU; the linked unit
   is oversized but cheap and fine. Real driver of array size is the unit's
   measured running watts + duty cycle.
4. **Refrigerant over evaporative** — see "Evaporative considered" below.
5. **Portability & dust survival are first-class requirements**, not afterthoughts.

New primary build: `../configurations/config-d-tent-solar-direct.md`.
Configs A/B/C are retained as **reference for a room/dwelling** but flagged
oversized for this target.

## Evaporative (swamp) cooling — considered, not chosen
Nevada August air is very dry, so an evaporative cooler would cool at **~50–150 W
vs ~500 W** for refrigerant — cutting solar/battery needs ~5–10×. It was declined
in favor of **reliable cold** (refrigerant AC), because a swamp cooler adds
humidity, needs a water supply/refill, and loses effectiveness during any humid
spell or dust storm. *Kept on record:* if power/weight becomes the binding
constraint, revisit — a DC swamp cooler + a couple hundred watts of panel is a
radically lighter kit.

## Consequences
- Small battery (~2.5 kWh) instead of a 7–20 kWh bank → big cost/weight savings.
- Array (~1 kW) is sized to **run the load at midday**, not to refill a big bank.
- No inverter to buy, wire, or protect.
- Must engineer for **playa dust and heat**: sealed enclosure for battery+MPPT,
  cable glands, cleanable filters, wind-secured low-tilt panels, shaded electronics.
- Highest-ROI "component" is **more shade** over the tent (reflective tarp + air gap).

## Affected
- `../docs/requirements.md` (fully retargeted)
- `../configurations/config-d-tent-solar-direct.md` (new primary)
- `../configurations/README.md` (A/B/C demoted to reference)
- `../data/parts/ac-units.json` (DC vehicle-unit section is the active class)
