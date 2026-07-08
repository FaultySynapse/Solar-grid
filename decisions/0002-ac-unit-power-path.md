# 0002 — AC unit power path: AC-inverter vs 48 V DC vs 12/24 V DC

**Status:** **Resolved → Option C (12/24 V DC vehicle unit)** · 2026-07-08

> **Resolution:** The space is a shaded ~60–70 sq ft tent → **Option C** (DC unit,
> no inverter). Full build in `../configurations/config-d-tent-solar-direct.md`;
> broader tent retarget in `0003`.
>
> **12 V vs 24 V sub-decision (still open — researching, 2026-07-08):**
> New input from DC-unit research: a real, affordable **24 V mini-split exists** —
> the **Full Battery 24V Mini Split, 9k BTU, ~$2,030** (variable-speed Panasonic
> compressor, ~500 W / 19 A, no inverter **and no DC-DC converter**). This changes
> the tradeoff — 24 V no longer means an exotic/expensive unit — but **no decision
> yet.** The live tradeoffs to weigh:
> - **24 V:** better comfort + dehumidification (variable-speed), ~19 A (easy
>   wiring), no converter — but ~$2,030 unit and a more involved split install.
> - **12 V:** ~$335–895 cooler, cheapest hardware — but crude, 60–80 A, and needs a
>   converter if the bank is 24 V.
> - **48 V:** cleanest current; pairs well with high-Voc surplus panels; HotSpot /
>   Full Battery 48 V units (~$2,030–2,195).
> Decide alongside bus voltage, battery cells, and panel choice.

## Context
The AC unit's power type dictates the whole system architecture: system voltage,
whether an inverter sits in the AC path at all, wire sizing, and cost. The user is
**open to both DC and AC mini-splits**, and pointed at a specific cheap 12 V DC
vehicle split AC ([eBay 366514149055](https://www.ebay.com/itm/366514149055),
11k BTU, ~$335) as an example of interest.

The deciding factor is **how big a space we're cooling** — which isn't pinned down
yet (see open question in `../docs/requirements.md`).

## Options

### A. Residential AC-inverter mini-split → through a 48 V pure-sine inverter
- 12k BTU inverter mini-split (Pioneer/MRCOOL class), ~SEER2 19–20, ~600 W avg.
- System: 48 V battery + all-in-one inverter (baseline configs A/B/C).
- **Pros:** best cooling per watt, cools a real room/dwelling well, huge model
  choice, quiet, soft-start. 48 V = low current, thin cable, cheap to expand.
- **Cons:** inverter conversion loss (~5–10%) sits in the AC path; higher unit +
  inverter cost than a bare DC unit.

### B. Native 48 V DC residential mini-split (e.g. HotSpot ACDC12)
- Runs the compressor straight off the 48 V bus; hybrid models also take grid AC.
- **Pros:** no inverter loss in the AC path, clean solar architecture, still
  residential-grade cooling, 48 V low current.
- **Cons:** few models, higher unit price (~$900–1,600), verify battery-voltage
  window compatibility.

### C. 12 V / 24 V DC vehicle/RV split AC (the linked eBay unit)
- 11k BTU truck/van split AC, ~400–600 W, **no inverter**, ~$335.
- **Pros:** cheapest by far, dead-simple (battery → unit), inverter-free.
- **Cons:** built for a **small space** (cab/van/single small room), typically
  lower efficiency and may run near-continuous in heat (higher daily kWh than the
  spec implies). **At 12 V the current is very high (60–80 A)** → short thick
  cables, real resistive loss, and 12 V batteries are a worse fit for a 2 kW+
  solar array than 48 V. A **24 V** version halves the current and is preferable.

## Tradeoff summary

| | A: AC-inverter | B: 48 V DC | C: 12/24 V DC vehicle |
|---|---|---|---|
| Unit cost | ~$700–1,100 | ~$900–1,600 | **~$335** |
| Inverter in AC path | Yes | No | No |
| Best for space size | Room → dwelling | Room → dwelling | **Small room / van / cab** |
| System voltage fit | 48 V ✅ | 48 V ✅ | 12 V ⚠️ / 24 V ⚖️ |
| Efficiency (cooling/watt) | High | High | Lower |
| Model choice | Huge | Few | Many (RV market) |
| Wiring current | Low | Low | **High (esp. 12 V)** |

## Recommendation (pending the space-size answer)
- **Cooling a real room or dwelling → Option A** (current baseline configs), or
  **B** if you want to shave inverter loss and accept fewer models.
- **Cooling a small/van/single-room space, cost-first → Option C**, ideally the
  **24 V** variant, which flips the system toward a small 24 V (or 12 V) battery +
  MPPT with **no inverter** — a materially cheaper, simpler build than configs A–C.

## Decision
**Not yet made.** Blocked on:
1. What space is being cooled (approx. area / van / room / whole dwelling)?
2. Is inverter-free simplicity + low cost worth lower efficiency and small
   capacity? Or is residential-grade cooling the priority?

Once answered, record the choice here and (for Option C) add a `config-d-dc-direct`
build with a 12/24 V battery and no inverter.

## Affected
- `../data/parts/ac-units.json` (all three unit classes listed)
- `../configurations/` (A/B/C assume Option A today; Option C would add a new config)
- `../docs/requirements.md` (system voltage + "space to cool" open question)
