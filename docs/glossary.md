# Glossary & Units

Quick reference for the terms and units used across the catalog and configs.

## Energy & power
- **W (watt)** — instantaneous power. **kW** = 1,000 W.
- **Wh / kWh** — energy = power × time. A 500 W load for 2 h = 1,000 Wh = 1 kWh.
- **PSH (Peak Sun Hours)** — equivalent hours/day of full 1,000 W/m² sun. A
  location with 5 PSH gives a 100 W panel about 500 Wh on an average day.
- **Duty cycle** — fraction of time a compressor actually runs (0–1). Drives AC energy.

## AC / cooling
- **BTU/h** — cooling capacity. 12,000 BTU/h = 1 "ton" of cooling.
- **EER** — Energy Efficiency Ratio = BTU/h per watt, at a fixed test point.
  Higher is better. EER 12 → 1,000 W to make 12,000 BTU/h.
- **SEER2** — Seasonal EER (updated 2023 "M1" test). Seasonal average; marketing
  headline number. Real off-grid draw tracks EER at your ambient better than SEER2.
- **Inverter (mini-split)** — variable-speed compressor that modulates output and
  soft-starts. Much friendlier to batteries than fixed-speed units.
- **LRA (Locked Rotor Amps)** — startup surge current of a fixed-speed compressor.
- **Soft start / hard start kit** — device to reduce compressor startup surge.

## Battery
- **LiFePO4 (LFP)** — lithium iron phosphate; safe, long cycle life, deep DoD. Preferred.
- **DoD (Depth of Discharge)** — % of capacity used per cycle. LFP daily target ~80%.
- **Ah (amp-hour)** — charge capacity. Wh = Ah × nominal V.
- **C-rate** — charge/discharge current relative to capacity. 100 Ah at 0.5C = 50 A.
- **BMS** — Battery Management System; protects cells (over/under V, temp, current).

## Solar / electrical
- **STC** — Standard Test Conditions (25 °C, 1,000 W/m²) — the nameplate rating.
- **Voc** — open-circuit voltage (highest, at cold/no load). Sizing limit for controllers.
- **Vmp / Imp** — voltage/current at max power point.
- **Isc** — short-circuit current.
- **MPPT** — Maximum Power Point Tracking charge controller (most efficient type).
- **PWM** — simpler, cheaper charge controller; lower efficiency, panel V must match battery.
- **All-in-one / hybrid inverter** — combines inverter + MPPT + battery charger in one box.
- **Pure sine wave** — clean AC output required by AC compressors and electronics.
- **Class-T fuse** — fast fuse rated for lithium's high fault current; used on battery main.
- **Voltage drop** — loss in wiring; keep under ~2–3% by choosing adequate wire gauge.
- **48 V / 24 V / 12 V** — system nominal voltage. Higher V = lower current = thinner wire; 48 V preferred at this power.
