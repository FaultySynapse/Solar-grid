# Catalog — AC Units

The load the whole system exists to run. **Inverter (variable-speed) mini-splits
are strongly preferred** for off-grid: they soft-start and modulate, so they draw
far less surge and average power than fixed-speed window/portable units.

> Representative specs — verify against the current datasheet. Running watts are
> *typical while cooling*; nameplate max is higher. Last touched: baseline seed.

## AC-inverter mini-splits & window units (run through a pure-sine inverter)

Cheap, efficient, everywhere, and (some) DIY-installable — but they need a **pure-
sine inverter** in the loop (see `inverters.md`) and a place to mount. **Prefer
115 V** (drives off a common 120 V inverter; 230 V needs a split-phase/230 V
inverter for no benefit at this size). **Pick on EER, not SEER2** — at desert
daytime temps the compressor runs hard, so steady-state EER predicts battery draw
better than the seasonal SEER2 headline. All inverter units **soft-start** (no big
surge). *(Researched July 2026 — running-W figures marked ~ are estimates; verify.
New stock is R454B/R32; R410A is being phased out.)*

| Model | Type | BTU/h | SEER2 / EER | Running W (typ) | Supply V | DIY install? | ~Price | Fit | Notes / source |
|-------|------|-------|-------------|-----------------|----------|--------------|--------|-----|----------------|
| **Midea U** MAW08V1QWT | Inverter **window** | 8,000 | — / EER ~11 | ~350–600 | 115 VAC | ✅ one box, **no lineset/vacuum** | **~$350** | ✅ | Lowest-friction mount (no condenser to hang). Needs a rigid sealable opening (~44 lb). [HomeDepot](https://www.homedepot.com/p/336424813) |
| **Cooper & Hunter MIA 6k** | Inverter mini-split | **6,000** | 21.5 / ~11–12 | ~300–500 | 115 VAC | Pre-flared kit; needs vacuum | ~$700–820 | ✅ | Smallest true split — best-matched to a tiny tent. |
| **MRCOOL DIY 5th Gen 9k** | Inverter mini-split | 9,000 | 23.6 / **~14 EER** | ~400–700 (max ~900) | 115 VAC | ✅ **TRUE DIY** QuickConnect, no vacuum/EPA | ~$1,300–1,900 | ✅ | Only real no-vacuum split; best EER; priciest. [HomeDepot](https://www.homedepot.com/p/335524169) |
| **Pioneer Quantum Ultra 9k** | Inverter mini-split | 9,000 | 23 / **13 EER2** | ~350–650 | 115 VAC | Needs vacuum/KWIK-E-VAC | ~$800–1,000 | ✅ | Best-in-class efficiency among cheaper splits. |
| **Della Vita 9k** | Inverter mini-split | 9,000 | 20 / ~12 EER | ~450–700 (6.7 A) | 115 VAC | Pre-charged condenser; usually still vacuum | ~$500–650 | ✅ | Cheapest 9k split with a confirmed ~770 W nameplate. |
| Senville LETO / Klimaire KSIV 9k | Inverter mini-split | 9,000 | 21.5 / ~12–12.5 | ~450–700 | 115 VAC | Pre-flared; needs vacuum | ~$650–750 | ⚖️ | Solid mid-budget 9k options. |
| Pioneer WYT/Diamante 9k | Inverter mini-split | 9,000 | 19 / **10 EER2** | ~500–750 | 115 VAC | Needs vacuum | ~$590–900 | ⚖️ | Cheap but **worst off-grid draw** (low EER). |
| Gree Sapphire 9k | Inverter mini-split | 9,000 | 30 / ~13–14 | lowest of group | **230 VAC** | Needs vacuum | ~$1,600–1,900 | ⚖️ | Most efficient, but 230 V (needs split-phase inverter) + premium price. |
| Generic non-inverter window 12k | Fixed-speed window | 12,000 | ~11 EER | ~1,050 | 115 VAC | window | ~$300 | 🚫 | Hard LRA surge (3–5×) → needs soft-start kit + big inverter. Avoid. |

**Notes for this project:**
- For a tiny shaded tent, a **9k (or 6k) unit is heavily oversized** → it'll idle at
  minimum modulation and draw at the low end (~2–4 kWh over an 8 h day), *if* the
  tent isn't too leaky. The **Midea U 8k window ($350)** is the simplest to mount;
  a **6k C&H split** is the smallest true split.
- Split install on fabric is the real friction (indoor head + outdoor condenser +
  lineset, usually a vacuum pump). **MRCOOL DIY** avoids the vacuum step; a **window
  unit** avoids the split entirely but needs a rigid framed port.
- This whole path costs the AC **+ a pure-sine inverter + its idle draw** — compare
  against the DC-direct path (below) which skips the inverter.

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
