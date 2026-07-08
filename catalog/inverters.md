# Catalog — Inverters

Must be **pure sine wave** (AC compressors and electronics require it). Two paths:

- **All-in-one / hybrid** — inverter + MPPT charge controller + battery charger in
  one box. Fewer parts, integrated, usually best value. **Preferred for this build.**
- **Standalone inverter/charger** (e.g. Victron) + separate MPPT — more modular,
  higher quality, higher cost/complexity.

Low-frequency (transformer) inverters tolerate motor surge better; high-frequency
all-in-ones are fine for *inverter* mini-splits (mild surge).

> Verify continuous/surge ratings and PV input limits against datasheet.
> Last touched: baseline seed.

## All-in-one / hybrid (48 V)

| Model | Cont. output | Surge | Batt V | Waveform | MPPT built-in | Max PV | ~Price | Fit | Notes |
|-------|-------------|-------|--------|----------|---------------|--------|--------|-----|-------|
| EG4 6000XP | 6,000 W | ~12 kW | 48 V | Pure sine | Yes, 2×MPPT ~80 A | ~500 VDC, ~8 kW PV | ~$1,500 | ✅ | **Baseline pick.** Huge PV headroom, split-phase capable, comms with EG4 batteries. |
| EG4 3000EHV-48 | 3,000 W | ~9 kW | 48 V | Pure sine | Yes, ~80 A | ~145 VDC, ~4 kW PV | ~$650 | ✅ | Cheaper single 12k-AC build; lower PV voltage window. |
| Growatt SPF 3000TL LVM | 3,000 W | ~6 kW | 48 V | Pure sine | Yes, ~80 A | ~145 VDC | ~$550 | ⚖️ | Very common budget all-in-one; parallelable. |
| Growatt SPF 5000 ES | 5,000 W | ~10 kW | 48 V | Pure sine | Yes, ~80 A | ~450 VDC | ~$900 | ⚖️ | More PV voltage room than the 3000TL. |
| Sol-Ark 12K | 9,000 W | high | 48 V | Pure sine | Yes | ~500 VDC | ~$5,000+ | ⚖️ | Premium, grid-hybrid, overkill for one 12k AC. |

## Standalone inverter/charger (48 V) — pair with separate MPPT

| Model | Cont. output | Surge | Batt V | Waveform | MPPT | ~Price | Fit | Notes |
|-------|-------------|-------|--------|----------|------|--------|-----|-------|
| Victron MultiPlus-II 48/3000 | 2,400 W (3 kVA) | ~6 kW | 48 V | Pure sine | No (add SmartSolar) | ~$1,000 | ⚖️ | Excellent quality/monitoring; low-frequency, superb surge; needs separate MPPT. |
| Victron Quattro 48/5000 | 4,000 W | ~10 kW | 48 V | Pure sine | No | ~$1,700 | ⚖️ | Dual AC input; robust; premium ecosystem. |
| Giandel 48 V 3000 W | 3,000 W | ~6 kW | 48 V | Pure sine | No (inverter only) | ~$350 | 🚫 | Cheap pure-sine but no charger/MPPT and limited support; not ideal as system core. |

## Selecting for this project

- **Baseline:** **EG4 6000XP** — one box does inverter + dual MPPT + charger, with
  plenty of PV and surge headroom, and closed-loop comms with the baseline EG4
  battery. Leaves room to add a second AC or more panels later.
- **Budget:** Growatt SPF 3000TL or EG4 3000EHV — fine for a single 12k inverter
  mini-split; watch the lower PV voltage window when stringing panels.
- **Modular/premium:** Victron MultiPlus-II 48/3000 + SmartSolar MPPT — best
  monitoring and surge behavior, more money and parts.
- Sizing check: single 12k inverter mini-split (~1 kW running, mild surge) is
  easily inside a 3 kW inverter; 6 kW gives future headroom.
