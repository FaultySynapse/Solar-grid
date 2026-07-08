# Configurations

Complete, costed system builds. Each file is a self-contained design that picks
parts from [`../catalog/`](../catalog/) and runs the numbers from
[`../docs/sizing-methodology.md`](../docs/sizing-methodology.md) against the target
in [`../docs/requirements.md`](../docs/requirements.md).

Copy [`../templates/configuration-template.md`](../templates/configuration-template.md)
to add a new one. When you pivot between these, record why in [`../decisions/`](../decisions/).

## Active build — shaded desert tent, daytime solar-direct cooling

Target: shaded ~60–70 sq ft tent, Nevada desert August, cool while sleeping by
day, DIY DC system, ~1-week trip. See [`../docs/requirements.md`](../docs/requirements.md)
and [`../decisions/0003`](../decisions/0003-retarget-to-desert-tent.md).

| # | Config | AC | Array | Battery | Inverter | ~Total cost | Best when |
|---|--------|----|-------|---------|----------|-------------|-----------|
| **D** | [Tent Solar-Direct](config-d-tent-solar-direct.md) ⭐ | DC split ~9–11k BTU | ~1,000 W | ~2.5 kWh | none | **~$1,750 (12 V) / ~$2,250 (24 V)** | The current use case |

⭐ = current recommended build. Config D has two variants inside it: **12 V**
(the exact linked eBay unit, cheapest) and **24 V** (recommended — half the
current, cleaner wiring).

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
