# Catalog — Balance of System (BoS)

The unglamorous parts that make the system safe and legal: overcurrent
protection, disconnects, wiring, busbars, and mounting. **Do not skip these** —
a 48 V lithium bank can push thousands of amps into a fault. Sizes below are
representative for the ~2 kW / 48 V / 3–6 kW-inverter baseline; verify ampacity
and voltage drop for your actual currents and run lengths, and follow NEC
Article 690 (PV) / 705 (interconnection) and local code.

> Last touched: baseline seed.

## Overcurrent protection & disconnects

| Item | Spec (baseline) | Purpose | ~Price | Notes |
|------|-----------------|---------|--------|-------|
| Battery main fuse | **Class-T, 125–200 A, 48 V DC** | Protects battery main; interrupts lithium's high fault current | ~$40–80 | Class-T has the high interrupt rating (AIC) lithium needs. Size just above max inverter DC current. |
| Battery-to-inverter breaker/disconnect | 48 V DC breaker, ~125–150 A | Service disconnect + protection | ~$50 | Or a fused DC disconnect. |
| Per-battery-string fuse | 100–125 A each | Protects each parallel battery | ~$20 ea | Every parallel string gets its own. |
| PV string fuse / combiner | 15–20 A per string, rated for PV DC | Protects PV strings on parallel arrays | ~$15–100 | Needed when ≥3 strings parallel; use PV-rated (not AC) fuses/breakers. |
| PV DC disconnect | Rated ≥ string Voc & Isc×1.25 | Isolate array from controller | ~$30–60 | Required for service/safety. |
| AC output breaker | Sized to load circuit (e.g. 15–20 A, 120 VAC) | Protects AC branch to the mini-split | ~$10 | In a small load center/subpanel. |

## Conductors & connection

| Item | Spec (baseline) | Purpose | Notes |
|------|-----------------|---------|-------|
| Battery cables | **2–4/0 AWG** to inverter (~65 A at 48 V/3 kW; bigger for 6 kW) | Low-loss battery ↔ inverter | Size by current + length for <2–3% drop; use fine-strand, lugged. |
| PV wire | 10 AWG PV wire (up to ~30 A), MC4 connectors | Array ↔ controller | UV-rated PV wire outdoors; keep string current in mind. |
| Busbars | Positive/negative 250 A busbars | Common tie point for battery/inverter/loads | Simplifies parallel connections. |
| Battery-interconnect | Match battery cont. current, short/equal lengths | Series/parallel between packs | Equal-length leads balance parallel current. |
| Grounding & bonding | Grounding electrode + equipment ground per NEC 690 | Safety | Bond frames, disconnects, and negative per your system's requirements. |

## Mounting & array

| Item | Spec (baseline) | Purpose | Notes |
|------|-----------------|---------|-------|
| Racking (roof/ground/pole) | Rated for panel size + wind/snow load | Hold the array at good tilt | Ground/tilt mounts ease cleaning & winter angle. |
| Tilt | ~= latitude (or steeper for winter) | Optimize seasonal yield | Cooling season favors a lower/summer tilt. |
| Grounding lugs / WEEBs | Per racking spec | Bond panel frames | Required for code-compliant grounding. |

## Monitoring (optional but recommended)

| Item | Purpose | Notes |
|------|---------|-------|
| Shunt-based battery monitor (Victron SmartShunt, or built-in BMS SoC) | True state-of-charge, energy in/out | Invaluable for tuning duty cycle vs battery. |
| Inverter/controller app (EG4 monitor, VictronConnect/Cerbo GX) | Live production/consumption | Confirms your sizing assumptions against reality. |

## Checklist per configuration

- [ ] Class-T battery main fuse sized to inverter DC current
- [ ] Per-string battery fuses (if parallel)
- [ ] DC disconnects: battery↔inverter and array↔controller
- [ ] PV overcurrent protection (if ≥3 parallel strings)
- [ ] Battery & PV conductors sized for ampacity **and** <2–3% voltage drop
- [ ] Grounding/bonding per NEC 690/705 and local code
- [ ] AC branch breaker for the mini-split circuit
