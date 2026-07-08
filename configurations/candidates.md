# Tent Configuration Candidates

Complete candidate builds assembled from the researched catalog, spanning the two
architectures (**DC-direct** vs **AC-inverter mini-split**) across **12 / 24 / 48 V**
buses. These are options to compare and pivot between — **no pick yet**.

All share the tent target and the **solar-direct daytime** approach, sizing, Step-0
shade, and playa/dust notes in [`config-d-tent-solar-direct.md`](config-d-tent-solar-direct.md)
(the fundamentals doc). Part specs/links live in [`../catalog/`](../catalog/).

## Shared kit (in every config unless noted)
- **Array ~1 kW** — used residential panels (~$150, Craigslist ~$0.15/W) *or* foldable (~+$240 for portability). [solar-panels](../catalog/solar-panels.md)
- **BoS + dust box + mounts** (~$300) — fuses, DC breaker/disconnect, busbar, cables, MC4, sealed enclosure, panel stakes/ballast. [balance-of-system](../catalog/balance-of-system.md)
- **Battery ~2.5 kWh+** LiFePO4 (per config; DIY no-weld EVE cells or turnkey). [batteries](../catalog/batteries.md)
- **Step-0 shade** (free) — reflective tarp over the tent. Efficiency add-ons parked in [`../docs/efficiency-backlog.md`](../docs/efficiency-backlog.md).

> **MPPT note:** DC-direct and standalone-inverter configs need a separate **60 A
> MPPT** (~$250). **All-in-one** inverter configs include the MPPT. High-Voc 72-cell
> surplus panels string best on 48 V / high-voltage-PV controllers — see stringing
> notes in [solar-panels](../catalog/solar-panels.md).

## Comparison matrix

| # | Config | Arch | Bus | AC unit | Inverter/converter | Battery | ~Total | Pick when |
|---|--------|------|-----|---------|--------------------|---------|--------|-----------|
| [C1](#c1) | DC-12V cooler | DC-direct | 12 V | 12 V cooler ($335) | none | ~2.65 kWh | **~$1,250** | Absolute lowest cost |
| [C2](#c2) | DC-24V mini-split | DC-direct | 24 V | Full Battery 24V 9k | none | ~5.3 kWh | ~$3,200 | Best comfort, no converter/inverter |
| [C3](#c3) | DC-48V mini-split | DC-direct | 48 V | HotSpot/FB 48V | none | ~5.1 kWh | ~$3,200 | Lowest current, big surplus-panel arrays |
| [C4](#c4) | 48V + 12V cooler | DC + converter | 48 V | 12 V cooler ($335) | 48→12 V DC-DC | ~5.1 kWh | ~$1,650 | Cheap unit but a clean 48 V bus |
| [C5](#c5) | AC-24V all-in-one | AC mini-split | 24 V | Midea U 8k / C&H 6k | 24 V all-in-one | ~5.3 kWh | ~$1,700 | Cheap + efficient AC unit, one box |
| [C6](#c6) | AC-48V EG4 | AC mini-split | 48 V | 9k 115 V mini-split | EG4 3000EHV all-in-one | ~5.1 kWh | ~$2,500 | Most efficient + expandable |
| [C7](#c7) | AC-12V standalone | AC mini-split | 12 V | Midea U 8k window | 12 V inverter + MPPT | ~2.65 kWh | ~$1,500 | Simplest cheap AC path |

Totals are rough part sums (no labor). See [`../docs/research-log.md`](../docs/research-log.md)
for the open decisions these span.

---

## C1 — DC-direct, 12 V, budget cooler {#c1}
**Cheapest possible.** 12 V bank runs a 12 V "parking cooler" straight — no inverter,
no converter.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | 12 V cooler (eBay $335, or OutEquipPro $895 for a real split) | 335 |
| Battery | DIY 4× EVE LF206 (4S, 2.65 kWh) + 4S BMS | 230 |
| MPPT | 60 A (limit array ~600 W to keep charge current in range) | 230 |
| Shared kit | panels + BoS/dust/mounts | 450 |
| **Total** | | **~$1,245** |

- **Watch-outs:** 12 V = **high current everywhere** (AC feed 60–80 A → thick short
  cables; ~600 W array cap so MPPT stays ≤60 A). Crude cooling, weakest humidity control.

## C2 — DC-direct, 24 V, real mini-split {#c2}
**Best DC comfort.** 24 V bank runs the Full Battery 24V 9k variable-speed mini-split
directly — no inverter, **no DC-DC converter**, ~19 A draw.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | Full Battery 24V Mini Split 9k (~500 W/19 A) | 2,030 |
| Battery | DIY 8× EVE LF206 (8S, 5.3 kWh) + 8S BMS | 435 |
| MPPT | 60 A | 280 |
| Shared kit | panels + BoS/dust/mounts | 450 |
| **Total** | | **~$3,195** |

- **Watch-outs:** priciest AC unit; real split = indoor head + condenser + lineset to
  rig in a tent. Verify live stock. Best match to the comfort/low-humidity priority.

## C3 — DC-direct, 48 V, mini-split {#c3}
**Lowest current, best panel pairing.** 48 V bank + native 48 V DC unit; high-Voc
surplus panels string cleanly.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | HotSpot DC4812VRF (~$2,195) or Full Battery 48V (~$2,030) | 2,100 |
| Battery | 48 V turnkey rack module (5.12 kWh) + BMS | 409 |
| MPPT | 30–60 A (1 kW at 48 V ≈ 21 A) | 250 |
| Shared kit | panels + BoS/dust/mounts | 450 |
| **Total** | | **~$3,209** |

- **Watch-outs:** verify HotSpot stock (some resellers list discontinued). 48 V AC-unit
  choice is thin. Best if you want to grow the array with cheap 72-cell panels.

## C4 — 48 V bank + 12 V cooler via DC-DC converter {#c4}
**Cheap unit on a good bus.** 48 V battery/array (clean wiring, great panels) feeding a
$335 12 V cooler through a step-down.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | 12 V cooler (eBay) | 335 |
| Converter | 48→12 V 100 A (Daygreen A4D12C100) | 180 |
| Battery | 48 V turnkey rack module (5.12 kWh) + BMS | 409 |
| MPPT | 30–60 A | 250 |
| Shared kit | panels + BoS/dust/mounts | 450 |
| **Total** | | **~$1,624** |

- **Watch-outs:** converter adds ~5–15% loss (~40–110 W heat) + a series failure point
  carrying full AC current. Only worth it to keep the cheap 12 V unit on a 48 V system.

## C5 — AC mini-split, 24 V, all-in-one {#c5}
**Cheap + efficient AC unit, one box.** 24 V all-in-one (inverter+MPPT+charger) runs a
115 V Midea U window or C&H 6k split.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | Midea U 8k window ($350) or C&H 6k split ($760) | 350 |
| Inverter | LVYUAN/Sungold 3000 W 24 V all-in-one (incl. 60 A MPPT) | 450 |
| Battery | DIY 8× EVE LF206 (8S, 5.3 kWh) + 8S BMS | 435 |
| Shared kit | panels + BoS/dust/mounts (MPPT in the all-in-one) | 450 |
| **Total** | | **~$1,685** |

- **Watch-outs:** all-in-one idles ~20–40 W all day (solar-direct penalty). Midea U
  needs a rigid sealable port in the tent wall. All-in-one PV window is modest (~1.4 kW).

## C6 — AC mini-split, 48 V, EG4 all-in-one {#c6}
**Most efficient + expandable.** EG4 3000EHV (500 V/5 kW PV MPPT) + a high-EER 115 V
mini-split; cheap 72-cell panels in long series strings.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | Pioneer Quantum Ultra 9k (13 EER2, ~$900) or Midea U 8k ($350) | 900 |
| Inverter | EG4 3000EHV-48 all-in-one (incl. 500 V MPPT + charger) | 700 |
| Battery | 48 V turnkey rack (5.12 kWh) + BMS (or DIY 16S 10.6 kWh ~$845) | 409 |
| Shared kit | panels + BoS/dust/mounts (MPPT in the all-in-one) | 450 |
| **Total** | | **~$2,459** (**~$1,950** with Midea U) |

- **Watch-outs:** EG4 idles <70 W operating. Most room to grow (array + a 2nd zone).
  Best efficiency of the AC-path configs; verify refrigerant is R454B/R32.

## C7 — AC mini-split, 12 V, budget standalone {#c7}
**Simplest cheap AC path.** 12 V budget pure-sine inverter + separate MPPT, running a
Midea U 8k window unit.

| Part | Pick | ~$ |
|------|------|----|
| AC unit | Midea U 8k window inverter | 350 |
| Inverter | Giandel/Ampeak 2000 W 12 V pure sine | 220 |
| MPPT | 60 A (cap array ~600 W) | 230 |
| Battery | DIY 4× EVE LF206 (4S, 2.65 kWh) + 4S BMS | 230 |
| Shared kit | panels + BoS/dust/mounts | 450 |
| **Total** | | **~$1,480** |

- **Watch-outs:** 12 V limits inverter/array size; budget inverter idle ~15–20 W
  (unpublished). Fine for one small window unit; little headroom to grow.
