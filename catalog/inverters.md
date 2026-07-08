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

There are **two classes** — pick the class first, then the model:

## Class 1 — All-in-one (inverter + MPPT + charger in one box)
One purchase covers DC→AC **and** solar charging **and** grid/gen charging. Simplest
wiring, lowest summed cost. Trade: **higher idle** (the controller/display run all
day) and a **fixed PV window** you can't upgrade. Almost all are 24 V or 48 V.

| Model | Bus | Cont./Surge W | Idle | Built-in PV MPPT | **~System $** (inverter+MPPT+charger) |
|-------|-----|---------------|------|------------------|----------------------------------------|
| LVYUAN SHP3024 | 24 V | 3000 / 6000 | ~20–40 W~ | 60 A, ~1.4 kW PV (30–90 V) | **~$400–550** |
| Sungold 3000 W 24 V | 24 V | 3000 / 6000 | ~25–40 W~ | 60 A, low-V PV window | **~$400–500** |
| Growatt SPF 3000TL LVM-48 | 48 V | 3000 / 6000 | ~25–50 W~ | 80 A; 60–250 V PV (variant) | **~$580–720** |
| **EG4 3000EHV-48** | 48 V | 3000 / 6000 | <70 W op / <15 W standby | **500 V / 5 kW PV** | **~$650–800** |

## Class 2 — Standalone inverter (+ add a separate MPPT ~$250–280)
Just DC→AC; you buy a solar charge controller separately. Trade: **more boxes and a
higher summed cost**, but you get the **lowest idle** and **free choice of MPPT**
(e.g. a 500 V Victron for long surplus-panel strings). Modular — replace one piece
at a time. *(Victron MultiPlus adds a grid/gen charger but still no PV MPPT.)*

| Model | Bus | Cont./Surge W | Idle | Inverter $ | **~System $** (+ MPPT) |
|-------|-----|---------------|------|-----------|------------------------|
| Giandel / Ampeak 2000 W | 12 V | 2000 / 4–6k | ~15–20 W~ | ~$180–270 | **~$410–520** |
| Renogy 2000 W 24 V | 24 V | 2000 / 4000 | ~15–20 W~ | ~$250–300 | **~$480–580** |
| WZRELB RBP-3000 | 24/48 V | 3000 / 6000 | <30 W | ~$349–449 | **~$600–730** |
| **Victron Phoenix Smart 24/2000** | 24 V | ~1600 / 4000 | **~8–15 W** | ~$700–900 | **~$980–1,180** |
| **Victron Phoenix Smart 48/3000** | 48 V | ~2400 / 6000 | **~8–15 W** | ~$800–1,100 | **~$1,080–1,380** |
| Victron MultiPlus-II 24 or 48/3000 | 24/48 V | ~2400 / 6000 | ~13 W | ~$900–1,100 | **~$1,180–1,380** |

## Which class?
- **All-in-one** if you want the **cheapest, simplest** build (one box ~$400–800) and
  can accept ~25–70 W idle. The **EG4 3000EHV** is the exception on PV — its 500 V
  input strings cheap 72-cell surplus panels the way a good standalone MPPT would.
- **Standalone + MPPT** if you want **frugal idle** (Victron ~8–15 W → saves ~0.3–0.5
  kWh/day vs a hungry all-in-one) and **full control of the charge controller**, and
  don't mind more wiring and ~$500–1,400 summed. Budget standalones (~$480–730 system)
  sit between the two on both cost and idle.

**Idle-draw ranking** (matters — it runs all day): frugal = Victron Phoenix/MultiPlus
(~8–15 W); middle = budget standalones (~15–30 W, mostly unpublished); hungry =
all-in-ones + AIMS (~25–70 W). Every 10 W idle ≈ 80 Wh/day.

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
