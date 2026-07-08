# Catalog — AC Units

The load the whole system exists to run. **Inverter (variable-speed) mini-splits
are strongly preferred** for off-grid: they soft-start and modulate, so they draw
far less surge and average power than fixed-speed window/portable units.

> Representative specs — verify against the current datasheet. Running watts are
> *typical while cooling*; nameplate max is higher. Last touched: baseline seed.

## Standard-AC (run through a pure-sine inverter)

| Model | Type | BTU/h | SEER2 / EER | Running W (typ) | Startup surge | Supply V | ~Price | Fit | Notes |
|-------|------|-------|-------------|-----------------|---------------|----------|--------|-----|-------|
| MRCOOL DIY 4th Gen 12k | Inverter mini-split | 12,000 | SEER2 ~20 / EER ~10 | ~500–900 | Low (soft start) | 115 VAC | ~$1,100 | ✅ | DIY pre-charged lineset; very off-grid friendly. |
| Pioneer WYS012 12k | Inverter mini-split | 12,000 | SEER2 ~19 | ~450–850 | Low | 115 VAC | ~$700 | ✅ | Popular budget inverter mini-split; needs vacuum/charge. |
| Senville LETO 12k | Inverter mini-split | 12,000 | SEER2 ~19 | ~500–900 | Low | 115 VAC | ~$800 | ✅ | Similar class to Pioneer. |
| Midea U-Shaped 12k | Inverter window | 12,000 | SEER2 ~15 / CEER 15 | ~700–1,000 | Low–moderate | 115 VAC | ~$450 | ⚖️ | Window unit but *inverter* — quiet, no lineset, easy install. |
| Generic non-inverter window 12k | Fixed-speed window | 12,000 | EER ~11 | ~1,050 | **High (LRA 3–5×)** | 115 VAC | ~$300 | 🚫 | Cheap but hard surge; needs soft-start kit + big inverter. Avoid if possible. |
| Pioneer 24k mini-split | Inverter mini-split | 24,000 | SEER2 ~19 | ~1,100–1,900 | Low | 230 VAC | ~$1,300 | ⚖️ | If you retarget to 2 tons — roughly doubles array/battery. |

## 24 V DC split / mini-split — no inverter, no DC-DC converter ✅ (active class)

The sweet spot for this project: runs straight off a **24 V** LiFePO4 bus (no
inverter, and — unlike a 12 V unit on a 24 V bank — **no DC-DC converter**), at
about **half the current** of a 12 V unit. The market is thin but a genuine
affordable option now exists. *(Researched July 2026 — re-verify stock/price.)*

| Model | BTU/h | Supply | Running W | Running A | Compressor | ~Price | Fit | Notes / source |
|-------|-------|--------|-----------|-----------|------------|--------|-----|----------------|
| **Full Battery 24V Mini Split (9k)** | 9,000 | 24 V (21–30 V) | ~500 W | ~19 A | Variable-speed Panasonic BLDC (soft-start) | **~$2,030** | ✅ **Recommended** | Real split (indoor head + outdoor condenser); no inverter/converter. Also on Amazon (ASIN B0CQTZFX9K) & eBay. Buy button flickered "sold out" — check live stock. [fullbattery.com](https://fullbattery.com/products/24v-mini-split) |
| Full Battery 24V Mini Split (6k / 12k) | 6,000 / 12,000 | 24 V | ~350 / ~750 W | ~14 / ~32 A | Same | ~$2,030 | ⚖️ | 6k for a well-shaded tent; 12k only if it runs hot (32 A → heavier wiring). |
| Inclusive Inc "48V/24V DC-Direct" mini-split | 12,000 | 48 **& 24** V | ~700 W (spec'd @48 V) | ~16 A @48 V → ~32 A @24 V | Variable-speed, 28–32+ SEER | ~$1,990–2,590/zone | ⚖️ | More efficient, solar-direct. **24 V watts/amps not separately published — confirm with vendor.** Pages are SPAs. [inclusiveinc.org](https://inclusiveinc.org/products/dc-direct-mini-split) |
| UndermountAC 24V | n/a (unpublished) | 24 V (12/48 too) | — | — | — | ~$3,799+ | 🚫 | No published BTU/W/A; vehicle under-mount; overpriced for a tent. |

## 12 V DC vehicle/RV split AC (budget "parking cooler" — no inverter)

Plentiful and cheap (truck/RV market), but **high current** (~40–80 A at 12 V →
thick short cables), crude fixed/variable coolers optimized for a truck cab. On a
**24 V bank they need a 24→12 V DC-DC converter (~60 A+)** — bulky, lossy, and it
erodes the price advantage. Best only if you commit to a **12 V bank**.

| Model | BTU/h | Supply | Running W | Current | ~Price | Fit | Notes / source |
|-------|-------|--------|-----------|---------|--------|-----|----------------|
| "Jay" 12 V truck split AC ([eBay 366514149055](https://www.ebay.com/itm/366514149055)) | 11,000 | 12 V | ~400–600 W | ~60–80 A | ~$335 | ⚖️ | The unit you linked. Cheapest; listing's "8500 W" is a spec error (~0.4–0.6 kW real). |
| OutEquipPro "Skyeline" 12V mini split | 12,500 | 12 V | ~215–745 W | ~18–62 A | ~$895 | ⚖️ | Cheapest *real* split; in stock US, 1-yr warranty. Up to 62 A. [outequippro.com](https://outequippro.com/products/12v-air-conditioner-unit-mini-split-12500-btu-dual-fan-quiet-ac) |
| KingClima 12V/24V parking AC (OEM) | ~E-clima | 12 or 24 V | — | — | quote only | ⚖️ | China OEM; **also does 24 V** — RFQ if chasing cheap 24 V; weeks lead time. |

## Native 48 V DC AC (no inverter — for a 48 V bank)

Cleanest at 48 V (lowest current), if you build a 48 V bank.

| Model | BTU/h | Supply | Running W | Running A | ~Price | Fit | Notes / source |
|-------|-------|--------|-----------|-----------|--------|-----|----------------|
| **HotSpot Energy DC4812VRF** | 12,000 | 48 V (46–58 V) | ~544 W avg | ~20 A max | ~$2,195 (unit) | ⚖️ | Established brand, variable-capacity, solar-direct. Some resellers list **discontinued** — verify stock. [hotspotenergy.com](https://www.hotspotenergy.com/DC-air-conditioner/) |
| Full Battery 48V Mini Split (9k) | 9,000 | 48 V | ~500 W | ~10 A | ~$2,030 | ⚖️ | Panasonic 48 V BLDC. (12k listing shows "30 A" — spec error, ~16 A real.) [fullbattery.com](https://fullbattery.com/products/48v-hvac) |

> ⚠️ **Not** low-voltage DC-bus units: **HotSpot ACDC12C** and the **EG4 hybrid**
> take high-voltage PV-direct (90–380 V) + AC grid — they **cannot** run off a
> 12/24/48 V battery bus. Excluded from the DC-bus builds.

## Options on the table (still researching — no pick yet)

- **24 V real mini-split — Full Battery 24V, 9k BTU (~$2,030).** The one mainstream
  affordable **real 24 V mini-split**: variable-speed compressor (efficient,
  dehumidifies, gentle startup), ~500 W / 19 A, no inverter, **no DC-DC converter**.
  Aligns with the "reliable comfort + low humidity" priority (`decisions/0004`).
  Tradeoff: higher unit cost + a more involved split install (head + condenser + lineset).
- **12 V truck cooler (~$335–895) on a 12 V bank.** Cheapest hardware; crude,
  high-current, weaker at holding temp/humidity.
- **48 V units — HotSpot DC4812VRF / Full Battery 48V** if a 48 V bank wins out.
- Cross-cutting: whichever unit, **confirm real running watts + duty cycle** (clamp
  meter) — it drives array size. Unit choice and bus voltage should be decided together.
