# Config A — Daytime Budget

**One-line:** Cheapest viable build. Cool mainly while the sun is up, with a small
battery for a few evening hours. Cooling is a daytime luxury, not a 24/7 guarantee.

Serves a **cost-first** variant of [`../docs/requirements.md`](../docs/requirements.md).

## Target

| Parameter | Value |
|-----------|-------|
| AC | 12,000 BTU inverter mini-split |
| Design daily energy | ~3–4 kWh (shorter runtime) |
| Location | ~5.0 peak sun hours |
| Runtime | Mostly 10:00–18:00 while producing; ~1–2 h into evening |
| Autonomy | <1 day |

## Sizing

| Step | Calc | Result |
|------|------|--------|
| Daily energy | run mostly on live solar; ~3.5 kWh battery-backed | ~3.5–4 kWh |
| Battery (80% DoD) | cover evening + buffer only | **5.12 kWh** (1 pack) |
| Array (5 PSH) | enough to run AC live at midday | **1,200 W** (3 × 400 W) |
| Inverter | single 12k, mild surge | **3,000 W** all-in-one |

## Bill of materials

| Qty | Part | From catalog | ~Unit | ~Subtotal |
|-----|------|--------------|-------|-----------|
| 1 | 12k BTU inverter mini-split | [ac-units](../catalog/ac-units.md) | $700 | $700 |
| 3 | Canadian Solar 400 W panel | [solar-panels](../catalog/solar-panels.md) | $120 | $360 |
| 1 | EG4 LifePower4 48 V 100 Ah (5.12 kWh) | [batteries](../catalog/batteries.md) | $1,300 | $1,300 |
| 1 | Growatt SPF 3000TL / EG4 3000EHV all-in-one | [inverters](../catalog/inverters.md) | $550 | $550 |
| — | BoS + racking | [balance-of-system](../catalog/balance-of-system.md) | — | ~$450 |
| **Total (parts, no labor)** | | | | **~$3,000** |

## Wiring & protection highlights

- Class-T ~100–125 A battery fuse; DC disconnect; single battery (no parallel
  string fusing needed yet).
- 3 × 400 W panels — mind the **lower PV voltage window** of budget 3 kW
  all-in-ones (~145 VDC): likely 3 in series is fine, verify cold-Voc < limit.
- 4 AWG battery cables; 10 AWG PV wire.

## Behavior

- Great midday: array runs the AC directly.
- Evenings/mornings: only ~1–2 h of AC before the small bank is low.
- Cloudy day: little reserve — expect to skip or minimize AC.

## Tradeoffs / when to switch

- This is a **compromise on comfort for cost**. If you want reliable evening
  cooling → [Config B](config-b-balanced-evening.md) (bigger battery + array +
  inverter headroom).
- Cheapest way to *start*: build A now, then add a 2nd battery and 2 more panels
  later — but note the 3 kW inverter's PV window may cap array growth; B's 6000XP
  avoids that ceiling.
