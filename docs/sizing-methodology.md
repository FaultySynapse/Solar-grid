# Sizing Methodology

How we go from "run a 12k BTU mini-split" to actual component numbers. Every
configuration in `configurations/` uses these formulas so the builds are
comparable. Values in ⟨brackets⟩ come from [`requirements.md`](requirements.md).

> Rule of thumb up front: **size the battery for the load, and size the array
> to refill the battery in one solar day plus run the daytime load.** For AC,
> also make sure the inverter can carry the compressor's real running + startup
> draw.

> **Special case — solar-direct daytime cooling (the current tent build):** if
> you only cool *while the sun is up*, the array runs the AC **live** and the
> battery is just a **buffer** (surge + clouds + shoulders), not an overnight
> bank. Then flip the logic in Steps 2–3: size the **array to carry the running
> load at midday** (Step 3, treating `design_daily_Wh ≈ running_W × sun-window
> hours`), and size the **battery small** (a few hours of run-time at 80% DoD),
> because you are not storing a full day. See `../configurations/config-d-tent-solar-direct.md`.

---

## Step 1 — Daily energy (the anchor number)

Two ways to estimate the AC's daily energy; use whichever you have data for, then
cross-check.

**A. From efficiency (SEER2/EER):**
```
Wh_per_hour_full = BTU_per_hour / EER          (EER in BTU per Wh)
daily_Wh = Wh_per_hour_full × runtime_hours × duty_cycle
```
Example: 12,000 BTU/h ÷ EER 12 = 1,000 Wh per full-load hour. Over 10 h at a
0.5 duty cycle → **5,000 Wh/day**.

**B. From measured/average power:**
```
daily_Wh = avg_running_watts × runtime_hours
```
Example: 600 W average × ~8–9 h → ~5,000 Wh/day.

Add other loads and a margin:
```
design_daily_Wh = (AC_daily_Wh + other_loads_Wh) × 1.1     # 10% margin
                = (5,000 + 500) × 1.1 ≈ 6,050 Wh/day
```
Baseline design target: **~5.5–6.0 kWh/day.**

> ⚠️ Duty cycle is the biggest unknown. In a hot climate or a poorly-insulated
> space the compressor runs closer to 100% and energy can double. Measure with a
> plug meter (Kill A Watt / clamp meter) for one real day if you can.

---

## Step 2 — Battery bank

```
usable_Wh_needed = design_daily_Wh × autonomy_days
nominal_Wh       = usable_Wh_needed / usable_DoD
```
- LiFePO4 usable depth of discharge (DoD): use **0.8** for daily cycling
  (protects cycle life; you *can* go 0.9–1.0 occasionally).
- Round-trip inverter/battery losses (~10–15%) are covered by the margin above.

Baseline: 6,000 Wh × 1 day ÷ 0.8 = **7,500 Wh nominal → ~7.5 kWh**.
At 48 V: 7,500 / 48 ≈ **156 Ah**. Round to a real product size, e.g. one
48 V 100 Ah (5.12 kWh) is a bit tight for a full hot day; **two in parallel
(10.24 kWh)** gives comfortable margin and ~1.5–2 days light autonomy.

Battery amp-hours ↔ energy:
```
Wh = Ah × V_nominal          # 100 Ah × 51.2 V ≈ 5,120 Wh
```

---

## Step 3 — Solar array

Array must replace a day's energy during the usable sun window **and** ideally
run the AC directly at midday (so battery cycles less).

```
array_W = design_daily_Wh / (PSH × system_efficiency)
```
- `system_efficiency` ≈ **0.7–0.75** (MPPT loss, wiring, heat derate, dust,
  charge inefficiency).
- PSH from requirements (baseline 5.0).

Baseline: 6,000 Wh ÷ (5.0 × 0.72) ≈ **1,670 W** to net-zero the day. Round up to
**~2,000 W** so you also power the AC live at midday and recover from a cloudy
day. In a hot/high-duty climate, target **2,400–3,000 W**.

Panels in series/parallel: keep string **Voc (cold-adjusted)** under the charge
controller / inverter PV max, and total power under the controller's rating.
```
Voc_cold = Voc_STC × [1 + (T_min_C − 25) × (β/100)]     # β ≈ −0.3%/°C typical
```

---

## Step 4 — Inverter

The inverter must handle **continuous** AC running load plus everything else on
at once, and the AC's **startup surge**.

```
inverter_cont_W ≥ (peak_simultaneous_running_W) × 1.25
inverter_surge_W ≥ AC_startup_surge_W
```
- Inverter mini-splits: soft-start, surge is mild → a 3,000 W 48 V pure-sine
  inverter is comfortable for a single 12k unit.
- Non-inverter (window/portable) units: startup LRA can be 3–5× running →
  size for surge or add a soft-start / hard-start kit.
- Prefer **low-frequency (transformer)** inverters for heavy motor surge;
  high-frequency all-in-ones are fine for inverter mini-splits.

Baseline: single 12k inverter mini-split → **3,000 W 48 V pure-sine** (or a 6 kW
all-in-one for headroom + future expansion).

---

## Step 5 — Charge controller (if not built into an all-in-one)

```
controller_A ≥ array_W / V_battery × 1.25
```
Baseline: 2,000 W ÷ 48 V = 42 A → **60 A MPPT** for margin.
(Most 48 V all-in-one inverters include an MPPT controller, making a standalone
one unnecessary — see configs.)

---

## Step 6 — Wiring, protection, balance of system

- **Wire gauge** by current & length to keep voltage drop < 2–3%. Battery-to-
  inverter cables at 48 V/3 kW carry ~65 A → typically **2–4 AWG**; verify with
  an ampacity/voltage-drop calc for your run length.
- **Overcurrent protection** on every source: PV fuses/breakers, a **Class-T
  fuse** on the battery main (lithium can deliver huge fault current), inline
  fuses on parallel battery strings.
- **Disconnects**: DC disconnect between array and controller, and between
  battery and inverter.
- **Grounding & bonding** per NEC Article 690/710.

See [`catalog/balance-of-system.md`](../catalog/balance-of-system.md).

---

## Worked baseline summary

| Item | Result |
|------|--------|
| Design daily energy | ~6.0 kWh/day |
| Battery (48 V, LiFePO4, 1-day autonomy) | ~7.5 kWh min → **10.24 kWh** (2 × 48 V 100 Ah) |
| Solar array (5 PSH) | ~1,670 W min → **~2,000 W** |
| Inverter | **3,000 W** 48 V pure-sine (or 6 kW all-in-one) |
| Charge controller | **60 A** MPPT (or integrated in all-in-one) |

These feed directly into the three starter builds in `configurations/`.
