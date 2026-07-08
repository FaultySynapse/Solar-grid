# Config C — 24/7 Reliable

**One-line:** Continuous cooling with a genuine cloudy-day reserve. Oversized array
and a ~2-day battery bank so the AC keeps running through weather and overnight.

Serves a **reliability-first** variant of [`../docs/requirements.md`](../docs/requirements.md).

## Target

| Parameter | Value |
|-----------|-------|
| AC | 12,000 BTU inverter mini-split (run near-continuous in heat) |
| Design daily energy | ~8–10 kWh (higher duty cycle, longer hours) |
| Location | ~5.0 peak sun hours (hot climate → high duty cycle) |
| Runtime | Effectively 24/7 in cooling season |
| Autonomy | ~2 days |

## Sizing

| Step | Calc | Result |
|------|------|--------|
| Daily energy | ~600–800 W avg × ~14–18 h, hot-climate duty | ~9–10 kWh/day |
| Battery (80% DoD, 2 days) | 10 × 2 / 0.8 = 25 kWh → practical | **20.48 kWh** (4 packs) |
| Array (5 PSH, 0.72 eff) | 10,000 / (5 × 0.72) ≈ 2,780 W | **3,200 W** (8 × 400 W) |
| Inverter | single 12k + big PV + charge current | **6,000 W** all-in-one |

> Note: at true 24/7 in a hot climate, the honest daily energy can approach or
> exceed the AC's full-load draw. Measure and adjust — this config errs generous.

## Bill of materials

| Qty | Part | From catalog | ~Unit | ~Subtotal |
|-----|------|--------------|-------|-----------|
| 1 | 12k BTU inverter mini-split | [ac-units](../catalog/ac-units.md) | $900 | $900 |
| 8 | Canadian Solar 400 W panel | [solar-panels](../catalog/solar-panels.md) | $120 | $960 |
| 4 | EG4 LifePower4 48 V 100 Ah (20.48 kWh) | [batteries](../catalog/batteries.md) | $1,300 | $5,200 |
| 1 | EG4 6000XP all-in-one | [inverters](../catalog/inverters.md) | $1,500 | $1,500 |
| — | BoS: Class-T, busbars, per-string fuses, PV combiner, cables | [balance-of-system](../catalog/balance-of-system.md) | — | ~$700 |
| — | Racking (ground/tilt) + grounding | [balance-of-system](../catalog/balance-of-system.md) | — | ~$600 |
| **Total (parts, no labor)** | | | | **~$9,000+** |

## Wiring & protection highlights

- 4 parallel 48 V batteries → **each needs its own 100 A fuse**, common busbars,
  and a Class-T main; equal-length interconnects for current balance.
- 8 × 400 W = 3.2 kW PV → likely 2 strings of 4; PV combiner with per-string
  fuses; verify cold-Voc against the 6000XP's ~500 VDC max.
- Larger battery cables and busbars for sustained high charge/discharge current.
- Consider closed-loop BMS comms (EG4 battery ↔ 6000XP) for coordinated charging.

## Behavior

- Runs the AC live all day and banks ~2 days of reserve for clouds/heat waves.
- Comfortable overnight cooling without deep-cycling the bank.

## Tradeoffs / when to switch

- **Biggest cost driver is the battery** (4 packs). If 24/7 isn't essential →
  [Config B](config-b-balanced-evening.md) halves the battery for ~$3.5k less.
- If the space heat-loads hard, consider a **2nd smaller mini-split zone** on the
  same 6 kW inverter rather than one oversized head.
- A **native 48 VDC AC unit** (see
  [`../decisions/0002-native-dc-ac-vs-inverter-path.md`](../decisions/0002-native-dc-ac-vs-inverter-path.md))
  shaves inverter conversion loss — meaningful when running continuously.
