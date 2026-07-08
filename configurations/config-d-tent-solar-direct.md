# Config D — Desert Tent, Solar-Direct Daytime ⭐ (active build)

**One-line:** Cool a shaded ~60–70 sq ft tent while you sleep during the day, in
the Nevada desert in August, by running a small DC AC **directly off a portable
solar array** with a small LiFePO4 buffer battery — no inverter.

Serves the retargeted [`../docs/requirements.md`](../docs/requirements.md).
Pivot rationale in [`../decisions/0003-retarget-to-desert-tent.md`](../decisions/0003-retarget-to-desert-tent.md).

## The key idea
You cool **during the day, when the sun is strongest.** So the panels run the AC
**live**, and the battery only has to cover the compressor's inrush, passing
clouds, and the hour or two on either side of solar noon. That means a **~1 kW
array + a tiny ~2.5 kWh battery** — not a big overnight bank.

## Step 0 — free cooling first (do this regardless)
- Keep the tent **fully shaded** (you already are ✅). Add a **reflective tarp /
  space blanket over the tent with a 2–6" air gap** — cuts radiant load a lot.
- Seal the tent as much as possible where the AC blows; every open flap is load.
- These do more per dollar than any component below.

## Target
| Parameter | Value |
|-----------|-------|
| Space | shaded tent, ~60–70 sq ft |
| Location | Nevada desert, August (~7 PSH, very dry, ~100–110 °F) |
| Cooling window | daytime, sleeping, ~8 h |
| AC | DC split AC (vehicle class), ~9–11k BTU, ~500 W |
| Autonomy | buffer only (~4–5 h AC-only), no overnight bank |

## Sizing
| Step | Calc | Result |
|------|------|--------|
| AC running power | ~500 W (measure to confirm) | ~500 W |
| Live-solar array | run ~500–600 W through morning/afternoon shoulders + desert heat/dust derate | **~1,000 W** |
| Buffer battery | ~1.5 kWh working + margin, 80% DoD | **~2.5 kWh** |
| Charge controller | array_W ÷ V × 1.25 | 60 A MPPT |
| Inverter | none (DC unit) | — |

> If your sleep window hugs solar noon, you can run leaner (~800 W array). If the
> tent runs hot/leaky and the AC never cycles off, go to ~1.2–1.5 kW.

---

## Recommended build — 24 V (cleaner wiring)
At 24 V the AC draws ~half the amps of the 12 V unit (~25–30 A vs ~60–80 A), so
wiring, fusing, and the MPPT are all easier and cheaper. Worth sourcing the **24 V
variant** of the DC AC.

| Qty | Part | From catalog | ~Unit | ~Subtotal |
|-----|------|--------------|-------|-----------|
| 1 | 24 V DC split AC, ~9–12k BTU | [ac-units](../catalog/ac-units.md) | $600 | $600 |
| 1 | 24 V 100 Ah LiFePO4 (2.56 kWh) *(or 2× 12 V 100 Ah in series)* | [batteries](../catalog/batteries.md) | $520 | $520 |
| 5 | 200 W rigid panel (~1,000 W) *(or 2× 400 W)* | [solar-panels](../catalog/solar-panels.md) | $110 | $550 |
| 1 | 60 A MPPT (Victron 100/50 or EPEver 6415AN) | [charge-controllers](../catalog/charge-controllers.md) | $280 | $280 |
| — | BoS: ANL/Class-T fuse, DC breaker, PV fuses, cables, MC4, busbar | [balance-of-system](../catalog/balance-of-system.md) | — | ~$180 |
| — | Dust box (sealed tote/case + cable glands), panel stakes/ballast | [balance-of-system](../catalog/balance-of-system.md) | — | ~$120 |
| **Total (parts)** | | | | **~$2,250** |

## As-linked build — 12 V (uses the exact eBay unit)
Cheapest unit, but 12 V means **high current everywhere**: ~60–80 A on the AC feed
(fat, short cables) and, for a full 1 kW array, an ~80–100 A MPPT. Keeping the
array at ~600–750 W lets you use a 60 A MPPT.

| Qty | Part | From catalog | ~Unit | ~Subtotal |
|-----|------|--------------|-------|-----------|
| 1 | 12 V 11k BTU DC split AC ([eBay 366514149055](https://www.ebay.com/itm/366514149055)) | [ac-units](../catalog/ac-units.md) | $335 | $335 |
| 1 | 12 V 200 Ah LiFePO4 (2.56 kWh) *(or 2× 100 Ah parallel)* | [batteries](../catalog/batteries.md) | $520 | $520 |
| 3–4 | 200 W rigid panel (~600–750 W) | [solar-panels](../catalog/solar-panels.md) | $110 | $330–440 |
| 1 | 60 A MPPT *(100 A if you push to ~1 kW array)* | [charge-controllers](../catalog/charge-controllers.md) | $250 | $250 |
| — | BoS: **Class-T fuse (high current!)**, heavy 2–4 AWG AC-feed cable, DC breaker, PV fuses | [balance-of-system](../catalog/balance-of-system.md) | — | ~$200 |
| — | Dust box + panel stakes/ballast | [balance-of-system](../catalog/balance-of-system.md) | — | ~$120 |
| **Total (parts)** | | | | **~$1,750** |

## Wiring & protection highlights
- **Fuse the battery** with an ANL (24 V) or **Class-T (12 V, high fault current)**
  main, sized just above the AC's running amps; DC breaker/disconnect on the feed.
- **AC-feed cable** sized to the unit's amps and kept **short**: 12 V @ 60–80 A →
  2–4 AWG; 24 V @ ~30 A → 8–10 AWG.
- **PV**: 10 AWG PV wire, MC4, per-string fuse if ≥3 parallel; keep string Voc
  under the MPPT's max.
- **MPPT sized to full array** (it must survive the AC switching off): 24 V ~1 kW → 42 A → 60 A; 12 V ~1 kW → 83 A → 100 A (why 12 V wants a smaller array).

## Playa / dust & heat survival (one-week desert trip)
- Battery + MPPT in a **sealed tote/Pelican-style case** with cable glands; keep it **shaded** (heat derates both, and LiFePO4 shouldn't charge hot).
- Panels **low and staked/ballasted** against wind; expect to **wipe dust** daily (dust = lost watts).
- Clean the AC's **intake/condenser filter** regularly; make sure hot condenser air exhausts **outside** the tent.
- Bring spare fuses, MC4s, and a multimeter/clamp meter.

## Behavior
- Midday: array runs the AC live with surplus topping the buffer.
- Cloud passes / dawn & dusk shoulders: buffer carries the AC ~4–5 h.
- Overnight: not cooled (by design) — desert nights are cool.

## Tradeoffs / when to switch
- **Want it lighter/cheaper?** Right-size to a **5–6k BTU** DC unit (~300–400 W) →
  drop array to ~600 W and battery to ~1.5 kWh.
- **Want plug-and-play over DIY?** A portable power station + folding panels +
  small AC is easier but pricier and adds inverter loss (noted in `../decisions/0002`, Option path).
- **Power/weight becomes critical?** Reconsider an **evaporative cooler** — dry
  desert makes it ~5–10× lower power (see `../decisions/0003`).
- Cooling a real room/dwelling instead → the reference builds
  [A](config-a-daytime-budget.md)/[B](config-b-balanced-evening.md)/[C](config-c-24-7-reliable.md).
