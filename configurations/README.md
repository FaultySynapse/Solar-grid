# Configurations

Complete, costed system builds. Each file is a self-contained design that picks
parts from [`../catalog/`](../catalog/) and runs the numbers from
[`../docs/sizing-methodology.md`](../docs/sizing-methodology.md) against the target
in [`../docs/requirements.md`](../docs/requirements.md).

Copy [`../templates/configuration-template.md`](../templates/configuration-template.md)
to add a new one. When you pivot between these, record why in [`../decisions/`](../decisions/).

## Comparison (baseline: 12k BTU inverter mini-split, ~5 PSH, ~6 kWh/day design)

| # | Config | Array | Battery | Inverter | Autonomy | Runtime target | ~Total cost | Best when |
|---|--------|-------|---------|----------|----------|----------------|-------------|-----------|
| A | [Daytime Budget](config-a-daytime-budget.md) | 1,200 W | 5.12 kWh | 3,000 W all-in-one | <1 day | AC mostly while sun is up | **~$3,000** | Cheapest; cooling is a daytime luxury |
| B | [Balanced Evening](config-b-balanced-evening.md) ⭐ | 2,000 W | 10.24 kWh | 6,000 W all-in-one | ~1–1.5 days | ~8–10 h incl. evening | **~$5,500** | Recommended default; good value + margin |
| C | [24/7 Reliable](config-c-24-7-reliable.md) | 3,200 W | 20.48 kWh | 6,000 W all-in-one | ~2 days | Continuous, cloudy-day reserve | **~$9,000** | Full-time comfort, weather resilience |

⭐ = current recommended baseline.

> Costs are rough part-sum ballparks (no install/labor/permits/tax). Verify
> against live pricing. See each file for the bill of materials.

## How to read a config

Each config documents: the target it serves, the sizing math, a **bill of
materials** with catalog links, wiring/protection notes, expansion path, and the
tradeoffs that would make you pick a different one.
