# Config B — Balanced Evening ⭐ (recommended baseline)

**One-line:** Run a 12k BTU inverter mini-split ~8–10 h/day including into the
evening, with ~1–1.5 days of battery autonomy, using solid off-the-shelf parts at
a sensible price.

Serves the baseline in [`../docs/requirements.md`](../docs/requirements.md).
This is the reference build; A and C are the budget and heavy-duty variants.

## Target

| Parameter | Value |
|-----------|-------|
| AC | 12,000 BTU inverter mini-split (~600 W avg while cooling) |
| Design daily energy | ~6.0 kWh/day |
| Location | ~5.0 peak sun hours |
| Runtime | ~8–10 h/day, incl. evening off battery |
| Autonomy | ~1–1.5 days |

## Sizing (from methodology)

| Step | Calc | Result |
|------|------|--------|
| Daily energy | 600 W × ~9 h + overhead, ×1.1 margin | ~6.0 kWh/day |
| Battery (80% DoD, 1 day) | 6.0 / 0.8 = 7.5 kWh min | **10.24 kWh** chosen (margin) |
| Array (5 PSH, 0.72 eff) | 6,000 / (5 × 0.72) ≈ 1,670 W | **2,000 W** chosen |
| Inverter | ~1 kW running, mild surge, + headroom | **6,000 W** all-in-one |
| Charge controller | Built into all-in-one | — |

## Bill of materials

| Qty | Part | From catalog | ~Unit | ~Subtotal |
|-----|------|--------------|-------|-----------|
| 1 | 12k BTU inverter mini-split (Pioneer/MRCOOL class) | [ac-units](../data/parts/ac-units.json) | $800 | $800 |
| 5 | Canadian Solar 400 W panel | [solar-panels](../data/parts/solar-panels.json) | $120 | $600 |
| 2 | EG4 LifePower4 48 V 100 Ah (10.24 kWh) | [batteries](../data/parts/batteries.json) | $1,300 | $2,600 |
| 1 | EG4 6000XP all-in-one (inverter + MPPT + charger) | [inverters](../data/parts/inverters.json) | $1,500 | $1,500 |
| — | BoS: Class-T fuse, DC breakers, busbars, cables, PV wire, disconnects | [balance-of-system](../data/parts/balance-of-system.json) | — | ~$500 |
| — | Racking + grounding | [balance-of-system](../data/parts/balance-of-system.json) | — | ~$300 |
| **Total (parts, no labor)** | | | | **~$5,500 (rounded ~$6,300 with mounting/BoS high side)** |

## Wiring & protection highlights

- 48 V bus; **Class-T ~150 A** battery main fuse; per-battery 100 A fuses; DC
  disconnect battery↔inverter.
- 5 × 400 W panels: string within the 6000XP's PV window (ample ~500 VDC max) —
  e.g. one series string keeps current low and wire thin; verify cold-Voc.
- 2–4 AWG battery cables (size for 6 kW inverter draw); 10 AWG PV wire with MC4.
- AC branch: 120 VAC 15–20 A breaker to the mini-split.

## Behavior

- Midday: array (2 kW) runs the AC live **and** charges the bank.
- Evening: AC runs off the 10.24 kWh bank; ~6 kWh load leaves comfortable reserve.
- Cloudy day: ~1–1.5 days autonomy before you must curb runtime.

## Expansion path

- Add 1–2 more panels (6000XP has PV headroom) to net-zero hotter days.
- Add a 3rd battery for closer to 2-day autonomy (moves toward Config C).
- 6 kW inverter can later carry a second 12k head or a 24k unit.

## Tradeoffs / when to switch

- **Too expensive?** → [Config A](config-a-daytime-budget.md): drop to 1 battery +
  1.2 kW array + 3 kW inverter, accept daytime-mostly cooling.
- **Need 24/7 + weather resilience?** → [Config C](config-c-24-7-reliable.md):
  double battery + bigger array.
- **Want to skip the inverter in the AC path?** → see
  [`../decisions/0002-native-dc-ac-vs-inverter-path.md`](../decisions/0002-native-dc-ac-vs-inverter-path.md).
