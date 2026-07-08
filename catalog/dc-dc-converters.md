# Catalog — DC-DC Converters (24→12 V, 48→12 V)

Only needed **if** you run a **12 V DC AC unit off a 24 V or 48 V battery bank**.
A cheap 12 V "parking cooler" pulls **~40–80 A at 12 V** (≈500–960 W), so the
converter must be rated for that **continuous** current (aim 60 A, ideally ~100 A
for margin). *(Researched July 2026 — options, not a pick. Verify prices/specs;
several below are flagged estimates. Re-check continuous vs peak ratings.)*

> **The bigger point:** many native 12/24/48 V AC units cost the *same* regardless
> of voltage, so **choosing the bus voltage to match the AC unit can delete the
> converter entirely** — saving its cost, its ~5–15% loss, and a failure point.
> A converter is the right answer mainly when the AC you want is **12 V-only**
> (the cheapest coolers) or you already own one.

## 24 → 12 V (easy, cheap)

| Brand / Model | Input | Out A / W | Eff. | Iso? | Cooling | ~Price | Notes |
|---------------|-------|-----------|------|------|---------|--------|-------|
| Daygreen A2D12C60 | 18–35 V | 60 A / 720 W | 95% | No | Fanless IP68 | ~$70 | Best budget 60 A; generic brand. |
| Victron Orion 24/12-70A | 18–35 V | 70 A / ~840 W | 92% | No | Fanless | ~$200–260* | Reputable; remote on/off, parallelable. Not a charger. |
| Meanwell SD-1000L-12 | **19–72 V** (24 & 48) | 60 A / 720 W | ~87% | **Isolated** | Fan | ~$290 | Industrial, 3-yr warranty; one box works on 24 **or** 48 V. |
| Victron Orion-Tr 24/12 iso | 24 V | ~15–30 A | ~87% | **Isolated** | Fanless | ~$120–250 | Isolated but low current — need 3–5 in parallel for 60–80 A. |
| Renogy 12 V 60 A DC-DC | 12/24 V | 60 A / ~750 W | — | No | Fan | ~$225 | Sold as a multi-stage **charger** — confirm it works as a steady supply for an AC load. |

## 48 → 12 V (thinner, pricier market)

| Brand / Model | Input | Out A / W | Eff. | Iso? | Cooling | ~Price | Notes |
|---------------|-------|-----------|------|------|---------|--------|-------|
| Signature Solar 60A (OEM) | 20–60 V | 60 A / 828 W | up to 96% | No | Fanless IP68 | ~$62 | Standout value for 48→12 60 A; generic OEM. |
| Daygreen A4D12C100 | 30–60 V | **100 A / 1200 W** | 95% | No | Fanless | ~$180 | Single box for an 80 A AC with margin. |
| FORYON 80/100A | 30–60 V | 80–100 A | ~95% claim | No | Fan/heatsink | ~$90–150* | Budget Amazon; verify continuous rating. |
| Meanwell SD-1000L-12 | 19–72 V | 60 A / 720 W | ~87% | **Isolated** | Fan | ~$290 | The reputable isolated 48→12 60 A option. |
| Meanwell RSD-500C-12 | 33.6–67.2 V | 35 A / 420 W | ~88% | **Isolated** | Fanless | ~$300+* | Rugged/isolated but only 35 A → need 2 in parallel (~$600+) for 60–80 A. |

\* estimate — not confirmed on a live price page. **Note:** Victron makes **no**
high-current 48→12 unit (its isolated 48/12 tops ~15–20 A), so a Victron-only
48→12 80 A build means impractical paralleling.

## Cost / energy / reliability of the converter path (quantified, not concluded)

- **Extra cost:** +$60–290 for a single 60–100 A step-down; +$300–600 if paralleling reputable isolated units for 80 A.
- **Loss/heat:** ~5–15% of AC energy → **~40–110 W continuous heat** at 720–960 W load; roughly **0.5–0.9 kWh lost per 8 h** — dumped into the space you're cooling or the battery box.
- **Reliability:** an added **series failure point** carrying full AC current; thermal derating on a hot day can shut the AC off.
- **When it's still worth it:** the AC you want is **12 V-only**, you already own a 12 V unit, or you want a 12 V house bus for other loads.

**Cross-reference:** native 24 V / 48 V AC units (no converter) are in
[`ac-units.md`](ac-units.md). On a 48 V bus a native unit also cuts wiring current
~4× vs running the load at 12 V.
