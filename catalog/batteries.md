# Catalog — Batteries

**LiFePO4 (LFP)** only for this project: safe chemistry, ~3,000–6,000 cycles,
deep daily DoD (~80%), and light weight vs lead-acid. At this power **48 V**
server-rack or wall-mount packs are the sweet spot; 12 V packs suit small/RV
builds but need 4 in series for 48 V.

> Usable kWh assumes ~80% daily DoD unless noted. Verify specs/BMS/warranty
> against datasheet. Last touched: baseline seed.

## 48 V packs (preferred at this power)

| Model | Nominal V | Ah | kWh (nom) | Usable @80% | BMS | Cont. discharge | Cycles | Form | ~Price | Fit | Notes |
|-------|-----------|-----|-----------|-------------|-----|-----------------|--------|------|--------|-----|-------|
| EG4 LifePower4 48 V 100 Ah | 51.2 | 100 | 5.12 | ~4.1 | 100 A, closed-loop comms | 100 A | ~3,500 | Server rack | ~$1,300 | ✅ | **Baseline pick.** Communicates with EG4/Growatt inverters. |
| EG4 LL-S 48 V 100 Ah | 51.2 | 100 | 5.12 | ~4.1 | 100 A, heated option | 100 A | ~8,000 | Server rack | ~$1,700 | ⚖️ | Premium cells, higher cycle life, cold-weather heat pad. |
| SOK 48 V 100 Ah | 51.2 | 100 | 5.12 | ~4.1 | 100 A | 100 A | ~4,000 | Rack/wall | ~$1,400 | ✅ | Well-regarded value rack battery. |
| Pytes / Ruixu 48 V 100 Ah | 51.2 | 100 | 5.12 | ~4.1 | 100 A comms | 100 A | ~6,000 | Rack | ~$1,500 | ⚖️ | Good comms support with common hybrids. |
| Generic 48 V 200 Ah wall (server) | 51.2 | 200 | 10.24 | ~8.2 | 200 A | 100–200 A | ~4,000 | Wall/rack | ~$2,200 | ⚖️ | One box = baseline autonomy; verify BMS quality. |

## 12 V packs (small/RV builds; 4S for 48 V)

| Model | Nominal V | Ah | kWh (nom) | BMS | Cont. discharge | ~Price | Fit | Notes |
|-------|-----------|-----|-----------|-----|-----------------|--------|-----|-------|
| Battle Born 12 V 100 Ah | 12.8 | 100 | 1.28 | 100 A | 100 A | ~$900 | ⚖️ | Premium, US support; expensive per kWh. |
| LiTime (Ampere Time) 12 V 100 Ah | 12.8 | 100 | 1.28 | 100 A | 100 A | ~$260 | ✅ | Best budget $/kWh; 4S for 48 V (check series rating). |
| SOK 12 V 206 Ah | 12.8 | 206 | 2.64 | 200 A | 100 A | ~$650 | ⚖️ | Large 12 V block. |

## Sizing to the baseline

- Design need (from methodology): **~7.5 kWh nominal** for 1-day autonomy at 80% DoD.
- **Baseline choice:** **2 × EG4 LifePower4 48 V 100 Ah = 10.24 kWh** nominal
  (~8.2 kWh usable). Comfortable margin for a hot high-duty day and ~1.5–2 days
  light autonomy.
- Budget alternative: **4 × LiTime 12 V 100 Ah in series (4S)** = 48 V 100 Ah =
  5.12 kWh — cheapest, but tighter autonomy and no inverter comms; ensure each
  12 V pack's BMS is rated for series use.

## Cautions

- **Closed-loop comms** (battery BMS ↔ inverter, CAN/RS485) improves charge
  control and protection — match battery + inverter brands where possible.
- Don't parallel batteries of different age/chemistry/SoC without care.
- Every parallel string needs its own fuse; the bank needs a **Class-T** main fuse.
- Lithium charge current below freezing damages cells — get heated packs or a
  low-temp charge cutoff for cold climates.
