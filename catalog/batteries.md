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

## DIY no-weld LFP cells / modules (Battery Hookup) — options being researched

For a DIY bolt-together pack (**no laser/spot welding** — hand tools only), the
gating spec is **bolt-on / threaded-stud terminals**. Bus voltage is still open, so
these scale to 12 V (4S) / 24 V (8S) / 48 V (16S). *(Researched July 2026 — Battery
Hookup sells out fast; re-verify price & stock at checkout. Options, not a pick.)*

| Product | Chem | Per cell/module | Terminal (no-weld?) | Condition | ~Price | ~$/kWh | Bus fit |
|---------|------|-----------------|---------------------|-----------|--------|--------|---------|
| [4× EVE LF280K 280 Ah](https://batteryhookup.com/products/new-4x-eve-lf280k-3-2v-280ah-lifepo4-cells-with-thick-busbars-m6-bolts) | LFP | 3.2 V · 280 Ah · 0.896 kWh (set = 3.58 kWh) | ✅ welded terminal blocks, **M6 threaded**, bolts incl. | New, Grade A | $250 / 4 | **~$70** | 4/8/16 cells |
| [4× EVE LF206 206 Ah](https://batteryhookup.com/products/new-4x-eve-lf206-3-22v-206ah-lifepo4-cells-with-thick-welded-terminal-blocks-m6-bolts) | LFP | 3.22 V · 206 Ah · 0.663 kWh (set = 2.65 kWh) | ✅ **M6 threaded** blocks, bolts incl. | New overstock | $205 / 4 | ~$77 | 4/8/16 cells |
| 51.2 V 100 Ah rack module (needs BMS) | LFP | 51.2 V · 100 Ah · **5.12 kWh** | ✅ external bolt lugs (pre-built 16S) | Used, working | ~$384 | ~$75 | 48 V turnkey |
| 51.2 V 100 Ah rack "2 bad group" | LFP | 5.12 kWh nom (~4.5 usable after repair) | ✅ bolt lugs | Used, needs repair | ~$225 | ~$44* | 48 V (tinkerer) |
| 48 V 200 Ah w/ BMS | LFP | 51.2 V · 200 Ah · **9.6 kWh** | ✅ bolt lugs, BMS incl. | Used | ~$750 | ~$78 | 48 V turnkey (large) |
| 12.8 V 34 Ah module w/ BMS | LFP | 12.8 V · 34 Ah · 0.435 kWh | ✅ bolt/terminal, BMS incl. | Used/overstock | ~$30 | ~$69 | 12 V turnkey (small) |
| [PC40138-LFP 17 Ah](https://batteryhookup.com/products/lifepo4-power-cells-pc40138-lfp-3-2v-17ah) | LFP | 3.2 V · 17 Ah · 0.054 kWh | ✅ threaded stud, nuts incl. | Used | $10 | ~$184 | any (small) |

\* if successfully repaired. **Excluded (require laser welding — flat terminals):**
Sunwoda LF314 314 Ah (~$40/kWh, cheapest but weld-only), Envision AESC 305 Ah,
3.2 V 300 Ah overstock, bare 18650/21700, pouch cells. Considered and rejected per
the no-weld constraint.

### Sample no-weld packs (from EVE cells)
- **12 V (4S):** 4× EVE LF206 → 12.8 V 206 Ah = **2.65 kWh** (~$205); or 4× LF280K = **3.58 kWh** (~$250). + 4S 100 A BMS (~$25).
- **24 V (8S):** 8× EVE LF206 → 25.6 V 206 Ah = **5.3 kWh** (~$410). + 8S BMS (~$25).
- **48 V (16S):** cleanest = 1× 51.2 V 100 Ah rack module **5.12 kWh** (~$384) + 16S BMS; all-cell alt = 16× LF206 = **10.6 kWh** (~$820, overshoots target).

### Ancillaries for a bolt-together pack
- **BMS** sized to S-count & current: 4S/8S/16S 100 A from ~$25; 4S 300 A ~$60; LCD/RS485 units ~$12–90.
- **Bus bars + M6 hardware** (~$5–20; EVE sets include bolts). **Compression fixture** (end plates + threaded rod, generic ~$30–60 — Battery Hookup doesn't stock one).
- **Top-balance** all cells in parallel to ~3.6 V before series assembly.

> Note vs. the tent buffer: the active build wants only **~2.5 kWh**. These cells
> can hit that (12 V 4S LF206) or scale up cheaply if the design grows — kept here
> as options while bus voltage and unit choice are still open.

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
