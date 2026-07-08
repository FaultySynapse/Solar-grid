# Catalog — Solar Panels

Monocrystalline is the default (best efficiency/area). Choose panel voltage class
to string cleanly under your charge controller's max PV voltage. For a ~2,000 W
48 V system, larger (60/72-cell or "residential") panels give the best $/W; small
12 V-nominal panels are convenient for tiny/RV builds but cost more per watt.

> Representative specs at STC — verify against datasheet. Last touched: baseline seed.

| Model | W (STC) | Voc | Vmp | Imp | Isc | Cells | Dimensions (approx) | ~$/W | ~Price | Fit | Notes |
|-------|---------|-----|-----|-----|-----|-------|--------------------|------|--------|-----|-------|
| Renogy 100 W 12 V mono | 100 | ~24.3 | ~20.4 | ~4.9 | ~5.2 | 36 | 42×20×1.4 in | ~$1.00 | ~$100 | ⚖️ | Convenient/rigid, but pricey per watt; good for small/RV. |
| Renogy 200 W 12 V mono | 200 | ~27.5 | ~22.3 | ~9.0 | ~9.5 | — | 59×27×1.4 in | ~$0.65 | ~$130 | ⚖️ | Better $/W than 100 W. |
| Newpowa 240 W 24 V mono | 240 | ~37 | ~30 | ~8.0 | ~8.6 | 60 | 65×26×1.4 in | ~$0.50 | ~$120 | ✅ | Good value mid-size. |
| Canadian Solar 400 W mono | 400 | ~45 | ~37 | ~10.8 | ~11.4 | 108 half-cell | 68×45×1.4 in | ~$0.30 | ~$120 | ✅ | **Baseline pick.** 5×400 W = 2 kW at great $/W. |
| Trina/Jinko 550 W bifacial | 550 | ~50 | ~42 | ~13.1 | ~13.9 | 144 half-cell | 90×45×1.4 in | ~$0.25 | ~$140 | ✅ | Cheapest $/W; large/heavy, needs bigger racking. |
| "Used/blemished" 370 W (SanTan-style) | 370 | ~47 | ~39 | ~9.5 | ~10 | 72 | 77×39×1.4 in | ~$0.15 | ~$55 | ⚖️ | Cheapest of all if available; verify condition/warranty. |

## Portable / folding panels (for the tent trip)

For a one-week trip you can use rigid panels (cheapest $/W, bulky) or folding
"briefcase" / blanket panels (pack small, set up fast, cost more per watt). On
playa, whatever you pick must be **staked/ballasted against wind** and **wiped of
dust daily**.

| Model | W | Type | Voc | ~$/W | ~Price | Fit | Notes |
|-------|---|------|-----|------|--------|-----|-------|
| Rigid 200 W mono (generic) | 200 | Rigid | ~24 | ~0.55 | ~$110 | ✅ | Best $/W for ~1 kW array; bulky to haul. |
| Renogy 200 W folding suitcase | 200 | Folding + legs | ~24 | ~1.5 | ~$300 | ⚖️ | Fast setup, built-in tilt legs; pricey per watt. |
| EF/generic 220 W folding blanket | 220 | Fold-out blanket | ~26 | ~1.4 | ~$300 | ⚖️ | Packs flat; secure against wind. |

> For Config D's ~1 kW: **5× rigid 200 W** (~$550, bulkier) or **2–3× folding
> 200–220 W** (~$600–900, easiest transport/setup). Match the array voltage to
> your MPPT and system (12 V vs 24 V).

## Surplus / used panels — SF Bay Area (cheap-array options being researched)

Used residential panels are the cheapest watts around. *(Researched July 2026 —
Craigslist listings are live but sell fast; **Facebook Marketplace is login-walled
and couldn't be browsed** — search it yourself, see tips below. Options, not a pick.)*

**Market snapshot:** SF Bay Craigslist has a steady supply of **used 300–315 W
60/72-cell residential panels at ~$0.14–0.18/W** (~$45–55 each), concentrated in
Union City, Santa Rosa, Napa/Petaluma, Oakland, San Jose — several are bulk lots.
That's the very good end of used pricing (secondary market spans ~$0.05–0.60/W).

| Example listing (sfbay.craigslist.org) | W | Price | $/W | Where | Note |
|-----------------------------------------|---|-------|-----|-------|------|
| "$25 Solar Panels 175W" | 175 | $25 | ~$0.14 | Union City | Cheapest $/W; low W = more panels for 1 kW |
| Trina 305 W | 305 | $49 | ~$0.16 | Oakland | Name brand |
| 20× 305 W blowout lot | 305 | $900/lot | ~$0.15 | San Jose | 6.1 kW lot — more than you need |
| 10× ~300 W lot ("3 kW") | ~300 | $450/lot | ~$0.15 | Union City | Lot of 10 |
| 315 W (several) | 315 | $55 | ~$0.17 | Union City / Napa | |
| JA Solar 455 W bifacial | 455 | $160 | ~$0.35 | Fremont | Big/heavy/modern |
| **Renogy 400 W suitcase (foldable)** | 400 | $195 | ~$0.49 | Santa Clara | Portable standout — packs down, self-standing |

**Mail-order surplus (ships):** SanTan Solar — used 250–320 W 72-cell ~$0.30–0.60/W
delivered, tested + 1-yr warranty, some 6-panel minimums (site blocks scraping —
verify live). Useful stringing spec: **Mission Solar 300 W 72-cell → Voc 40.18 V,
Vmp 32.80 V, Isc 9.61 A, ~40 lb, 66.5×39.3 in**.

**How to shop FB Marketplace yourself** (agent couldn't log in):
- Search: `solar panel(s)`, `used solar panels`, `solar panel pallet`, `300w solar`,
  `off grid solar`, `mono solar panel`; portable: `foldable solar`, `solar suitcase`.
  Sort by *Date listed*, tight radius, re-check every few days.
- **Good $/W:** ~$0.15/W is excellent; keep looking above ~$0.50/W for a plain used panel. Foldables run $1–2/W (the portability tax).
- **Inspect in person:** power-test under sun (Voc near rated, decent Isc); look for cracks/delamination/browning/burnt junction box; confirm **MC4 vs cut leads**; all panels in a lot **same model**.
- **Red flags:** won't power-test, cut/taped leads, hail cracks, grid-tie panel with attached microinverter (not off-grid friendly), mismatched "sets," pallet you can't haul.

**Tradeoffs for a portable ~1 kW tent array (not a recommendation):**
- *Used residential 300 W (~$0.15/W):* ~1 kW for ~$135–165, only 3–4 panels — but ~40 lb, ~66×39 in each, **big wind sails** in the desert (real ballast/staking needed).
- *Foldable suitcase (Renogy 400 W ~$195):* 2–3× the $/W, but light, packable, no glass, fast teardown.
- *Mix:* a couple cheap residential panels + one foldable for flexibility.

> ⚠️ **Stringing ceiling is the charge controller's max PV voltage, not the battery
> bus.** 72-cell panels are ~40 V Voc each and Voc *rises in cold* (×~1.15–1.25) —
> two in series can approach/exceed a 100 V MPPT limit on a cold desert morning.
> Decide panels and bus voltage together (see stringing notes below).

## Stringing notes

- **Baseline array:** 5 × 400 W = **2,000 W**. Two strings of... depends on
  controller. Keep **cold-adjusted Voc** under the controller/all-in-one PV max
  (e.g. 6000XP MPPT ~500 VDC max → several in series is fine; a 100 V controller
  needs mostly parallel).
- Cold-Voc rule: `Voc_cold = Voc_STC × (1 + (T_min − 25) × −0.003)`. In freezing
  climates a 45 V-Voc panel can hit ~52 V; multiply by string length.
- Higher string voltage (more panels in series) = lower current = thinner PV wire
  and less voltage drop over long roof-to-controller runs.
- Match physical space: 5×400 W ≈ 5 × (68×45 in) ≈ **~100 ft²** of array area.

## Selecting for this project

- **Baseline:** 5 × **Canadian Solar 400 W** (2 kW). Great $/W, manageable panel
  size, easy to string into a 48 V all-in-one.
- **Cheapest $/W:** 550 W bifacials or used 370 W panels — save money, but plan
  racking for larger/heavier modules.
- Add panels in the same model/string configuration when you expand; mixing
  mismatched panels on one string drags the string to the weakest panel.
