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

---

# For the tent build — run a small AC mini-split off the battery

Only needed on the **AC-inverter mini-split path** (skip entirely if you use a
native DC AC unit). One 9k inverter mini-split (or Midea U window) draws **~300–800 W
with soft-start**, so any 1,500–3,000 W pure-sine unit has ample margin. The real
differentiators: **input voltage** (drives DC current/cabling) and **idle draw**
(the inverter is on for hours of daytime cooling — every 10 W idle ≈ 80 Wh/day).
*(Researched July 2026 — idle figures marked ~ are estimates; confirm on datasheet.
Options, not a pick.)*

**Bus-voltage coupling:** a 2 kW load pulls ~170 A at 12 V, ~85 A at 24 V, ~42 A at
48 V. So 12 V inverters are cheap but cap ~2–3 kW and run hot/hungry; the best
2–3 kW and all-in-one units are **24 V or 48 V**. Decide the inverter and bus together.

### 12 V input (budget / small; heavy DC current at 2 kW+)
| Model | Cont./Surge W | Idle | Eff. | MPPT? | ~Price | Notes |
|-------|---------------|------|------|-------|--------|-------|
| Victron Phoenix 12/1200 | 1000 / 2400 | **~8–10 W** (search <2 W) | ~92% | No | ~$350–450 | Best idle; only ~1 kW at 12 V. |
| Renogy 2000/3000 W 12 V (Pro EcoSleep) | 2000–3000 / 4–6k | <10 W (Pro) | >90% | No | ~$249–415 | 3 kW @12 V ≈ 250 A — very heavy cable. |
| Giandel 2000 W / Ampeak 2000 W | 2000 / 4–6k | ~15–20 W~ | ~90–93% | No | ~$180–270 | Budget; idle unpublished. |

### 24 V input (sweet spot for 2–3 kW; half the current of 12 V)
| Model | Cont./Surge W | Idle | Eff. | MPPT? | ~Price | Notes |
|-------|---------------|------|------|-------|--------|-------|
| Victron Phoenix Smart 24/2000 (120 V) | ~1600 / 4000 | **~8–15 W** | ~92–94% | No | ~$700–900 | Frugal standalone; add separate MPPT. |
| Victron MultiPlus-II 24/3000 120 V | ~2400 / 6000 | ~13 W | 94% | Charger, no PV MPPT | ~$900–1,100 | Inverter/charger; needs external MPPT. |
| **LVYUAN SHP3024 all-in-one** | 3000 / 6000 | ~20–40 W~ | ~90% | **Yes, 60 A MPPT (~1.4 kW PV) + charger** | ~$400–550 | One box; modest PV window; budget brand. |
| **Sungold 3000 W 24 V all-in-one** | 3000 / 6000 | ~25–40 W~ | ~90% | **Yes, 60 A MPPT + charger** | ~$400–500 | One box; UL1741; low-V PV window. |
| Renogy 2000 W 24 V | 2000 / 4000 | ~15–20 W~ | >90% | No | ~$250–300 | Budget standalone. |

### 48 V input (lowest current & idle %; best for hybrids + high-Voc panels)
| Model | Cont./Surge W | Idle | Eff. | MPPT? | ~Price | Notes |
|-------|---------------|------|------|-------|--------|-------|
| **EG4 3000EHV-48 all-in-one** | 3000 / 6000 | <70 W op / <15 W standby | 97% PV→AC | **Yes, 500 V / 5 kW PV MPPT + charger** | ~$650–800 | High-V PV = long panel strings (pairs w/ surplus 72-cell). Mature/supported. |
| **Growatt SPF 3000TL LVM-48 all-in-one** | 3000 / 6000 | ~25–50 W~ | ~93% | **Yes, 80 A MPPT + charger** | ~$580–720 | Stackable; two PV-voltage variants. |
| Victron Phoenix Smart 48/3000 120 V | ~2400 / 6000 | **~8–15 W** | ~92–94% | No | ~$800–1,100 | Superb idle; standalone + separate MPPT. |
| Victron MultiPlus-II 48/3000 120 V | ~2400 / 6000 | ~13 W | 94% | Charger, no PV MPPT | ~$900–1,100 | Inverter/charger; external MPPT. |

**Standalone vs all-in-one (tradeoff, not a verdict):** a bare Victron Phoenix
idles ~8–13 W but needs a separate MPPT (more boxes, more cost summed). An all-in-one
(EG4/Growatt/LVYUAN/Sungold) bundles inverter+MPPT+charger for ~$580–800 but idles
higher (~40–70 W all day) — a real penalty on a solar-direct daytime build, partly
offset by a load-sensing eco/search mode when the compressor cycles off.

**Idle-draw ranking:** frugal = Victron Phoenix / MultiPlus (~8–13 W), Renogy Pro
EcoSleep (<10 W); middle = budget standalones (~15–30 W, mostly unpublished);
hungry = all-in-ones + AIMS (~25–70 W).

> **Reminder:** this whole inverter cost + idle loss only applies to the AC-mini-
> split path. A **native DC AC unit** ([`ac-units.md`](ac-units.md)) skips the
> inverter entirely — that's the core tradeoff between the two architectures.

---

# Dwelling-scale reference (from the original room/house baseline)

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
