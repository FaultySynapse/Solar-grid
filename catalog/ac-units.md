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

## 12 V / 24 V DC vehicle/RV split AC (small-space, no inverter)

"Parking cooler" style DC split ACs made for truck cabs, vans, and RVs. Run
straight off a 12 V or 24 V battery — **no inverter at all**. Cheap and simple,
but built to cool a *small* space (cab/van/single small room), generally lower
efficiency than residential inverter mini-splits, and at **12 V the current is
high** (thick, short cables essential). Prefer the **24 V** variant if offered —
half the current for the same power.

| Model | Type | BTU/h | Running W (typ) | Current | Supply | ~Price | Fit | Notes |
|-------|------|-------|-----------------|---------|--------|--------|-----|-------|
| "Jay" 12 V truck split AC ([eBay 366514149055](https://www.ebay.com/itm/366514149055)) | DC split (vehicle) | 11,000 | ~400–600 W | ~60–80 A @ 12 V | 12 VDC | ~$335 | ⚖️ | The unit you linked. Great $/BTU, no inverter; **12 V high-current**, small-space rated. Listing's "8500 W" is a spec error — real draw is ~0.4–0.6 kW. Verify duty/efficiency. |
| Generic 24 V DC RV split AC | DC split (vehicle) | 9,000–12,000 | ~400–700 W | ~20–35 A @ 24 V | 24 VDC | ~$400–700 | ⚖️ | Same class at 24 V — **half the current**, easier wiring. Preferred over 12 V if available. |

> ⚠️ These vehicle DC units are sized/optimized to cool a truck cab or small van,
> not a house. If your target space is a single small room / tiny cabin / van,
> they're an excellent cheap, inverter-free option. For a larger room or whole
> dwelling, a residential inverter mini-split (above) will cool better per watt.
> **Confirm the unit's real running power and duty cycle** — small DC units can run
> at near-continuous full draw in heat, which changes daily-energy math.

## Native 48 V DC "off-grid" AC (no inverter needed)

Running the compressor directly off the DC battery bus skips inverter conversion
losses and the surge-handling problem entirely. Fewer models, higher unit price,
but architecturally very clean for solar.

| Model | Type | BTU/h | Efficiency | Power draw | Supply | ~Price | Fit | Notes |
|-------|------|-------|-----------|-----------|--------|--------|-----|-------|
| HotSpot Energy ACDC12b/c | Hybrid AC/DC inverter mini-split | 12,000 | High | ~420–1,000 W (DC side) | 48 VDC solar + 115 VAC hybrid | ~$1,600 | ⚖️ | Can run straight off panels; hybrids AC grid + DC solar. Niche but purpose-built. |
| GREE/Generic 48 VDC mini-split 12k | DC inverter mini-split | 12,000 | High | ~500–900 W | 48 VDC | ~$900–1,400 | ⚖️ | "Solar DC" units; verify BMS/voltage-window compatibility with your bank. |

## Selecting for this project

- **Baseline pick:** a 12k **inverter mini-split** (MRCOOL DIY or Pioneer class) run
  through the system's pure-sine inverter. Best balance of cost, availability, and
  off-grid behavior.
- **Architecture fork:** a native **48 VDC** unit removes the inverter from the AC
  path (efficiency + simplicity) at higher unit cost and lower model choice — see
  `decisions/0002-native-dc-ac-vs-inverter-path.md`.
- Whatever you choose, **get the real datasheet power curve** and, ideally, measure
  a day with a clamp/plug meter. Duty cycle dominates daily energy.
