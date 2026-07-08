# Configurations

Complete, costed system builds. Each file is a self-contained design that picks
parts from [`../catalog/`](../catalog/) and runs the numbers from
[`../docs/sizing-methodology.md`](../docs/sizing-methodology.md) against the target
in [`../docs/requirements.md`](../docs/requirements.md).

Copy [`../templates/configuration-template.md`](../templates/configuration-template.md)
to add a new one. When you pivot between these, record why in [`../decisions/`](../decisions/).

## Tent candidate configurations (the active list) ⭐

Target: shaded ~60–70 sq ft tent, Nevada desert August, cool while sleeping by
day, DIY DC system, ~1-week trip. See [`../docs/requirements.md`](../docs/requirements.md)
and [`../decisions/0003`](../decisions/0003-retarget-to-desert-tent.md).

**➡️ Full list by key parameter combination: [`candidates.md`](candidates.md)** — 9
builds spanning DC-direct vs AC-inverter (combined vs standalone) across 12/24/48 V.
Defined by parameters, not cost. Still options, no pick.

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

Shared fundamentals (solar-direct sizing, Step-0 shade, playa/dust notes) live in
[`config-d-tent-solar-direct.md`](config-d-tent-solar-direct.md).

## Reference builds — residential room/dwelling (oversized for the tent)

Kept from the original dwelling-scale baseline for comparison and reuse if the
target ever changes to a real room or house. **Not** sized for a tent.

| # | Config | Array | Battery | Inverter | Autonomy | ~Total cost | Best when |
|---|--------|-------|---------|----------|----------|-------------|-----------|
| A | [Daytime Budget](config-a-daytime-budget.md) | 1,200 W | 5.12 kWh | 3,000 W all-in-one | <1 day | ~$3,000 | Cheapest room/dwelling; daytime cooling |
| B | [Balanced Evening](config-b-balanced-evening.md) | 2,000 W | 10.24 kWh | 6,000 W all-in-one | ~1–1.5 days | ~$5,500 | Room/dwelling, evening cooling |
| C | [24/7 Reliable](config-c-24-7-reliable.md) | 3,200 W | 20.48 kWh | 6,000 W all-in-one | ~2 days | ~$9,000 | Room/dwelling, full-time comfort |

> Costs are rough part-sum ballparks (no labor/permits/tax). Verify against live
> pricing. See each file for the bill of materials.

## How to read a config

Each config documents: the target it serves, the sizing math, a **bill of
materials** with catalog links, wiring/protection notes, expansion path, and the
tradeoffs that would make you pick a different one.
