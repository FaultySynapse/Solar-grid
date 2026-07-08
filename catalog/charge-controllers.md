# Catalog — Charge Controllers (MPPT)

Only needed as a **standalone** part if your inverter is inverter-only (e.g. a
Victron MultiPlus). Most 48 V **all-in-one** inverters in `inverters.md` already
include MPPT controller(s), so a separate one is redundant for those builds.

Use **MPPT** (not PWM) at this scale — 15–30% more harvest and lets panel string
voltage exceed battery voltage. Size for `array_W / battery_V × 1.25`.

> Verify max PV voltage/current against datasheet. Last touched: baseline seed.

| Model | Type | Rated A | Max battery V | Max PV Voc | Max PV W (48 V) | ~Price | Fit | Notes |
|-------|------|---------|---------------|-----------|-----------------|--------|-----|-------|
| Victron SmartSolar MPPT 150/60 | MPPT | 60 A | 12–48 V | 150 V | ~3,400 W | ~$430 | ✅ | **Baseline standalone pick.** Bluetooth, great data; pairs with Victron inverters. |
| Victron SmartSolar MPPT 250/100 | MPPT | 100 A | 12–48 V | 250 V | ~5,800 W | ~$720 | ⚖️ | Headroom for bigger arrays / higher string V. |
| EPEver Tracer 6415AN | MPPT | 60 A | 12–48 V | 150 V | ~3,200 W | ~$230 | ⚖️ | Budget standalone MPPT; decent, less polished monitoring. |
| Renogy Rover 60 A | MPPT | 60 A | 12–48 V | 100 V | ~3,200 W | ~$260 | ⚖️ | Common budget unit; note lower 100 V PV limit. |
| Victron SmartSolar MPPT 100/50 | MPPT | 50 A | 12–48 V | 100 V | ~2,900 W | ~$330 | ⚖️ | Fine for ~2 kW array if string Voc stays < 100 V. |

## Sizing to the baseline

- Baseline array 2,000 W at 48 V → 2,000 / 48 ≈ 42 A → **60 A** controller for margin.
- Ensure **max PV Voc ≥ cold-adjusted string Voc**. A 100 V-limit controller
  constrains you to short series strings; a 150 V/250 V unit gives stringing freedom.

## Selecting for this project

- **If using an all-in-one inverter (baseline EG4 6000XP): none needed** — MPPT is
  built in. This catalog matters only for the Victron/modular path.
- **Modular path baseline:** Victron SmartSolar **150/60** — 60 A handles the 2 kW
  array, 150 V PV input allows sensible series stringing, and it integrates with
  Victron monitoring (VE.Direct / Cerbo GX).
