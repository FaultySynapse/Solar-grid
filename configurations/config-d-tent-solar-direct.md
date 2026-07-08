# Tent Build — Fundamentals (shared by all candidates)

**One-line:** Cool a shaded ~60–70 sq ft tent while you sleep during the day, in
the Nevada desert in August, running a small AC **mostly off a portable solar
array** with a small LiFePO4 buffer battery.

This is the **shared fundamentals** doc — the solar-direct concept, sizing, Step-0
shade, and playa/dust notes that every candidate build relies on. **The full list
of complete candidate configurations is [`candidates.md`](candidates.md)** (C1–C7).
Serves the retargeted [`../docs/requirements.md`](../docs/requirements.md); pivot
rationale in [`../decisions/0003-retarget-to-desert-tent.md`](../decisions/0003-retarget-to-desert-tent.md).

> The two example builds below (Option A 24 V DC, Option B 12 V DC) are now
> generalized into the full candidate list in [`candidates.md`](candidates.md)
> (C2 and C1 respectively, plus five more). Kept here to illustrate the sizing.

## The key idea
You cool **during the day, when the sun is strongest.** So the panels run the AC
**live**, and the battery only has to cover the compressor's inrush, passing
clouds, and the hour or two on either side of solar noon. That means a **~1 kW
array + a tiny ~2.5 kWh battery** — not a big overnight bank.

The **refrigerant AC is the required core**: it's sized to reach a comfortable
temperature — and keep humidity down — **on its own**, without depending on any
shade/insulation upgrades ([`../decisions/0004`](../decisions/0004-active-ac-is-the-required-baseline.md)).
That's why we keep the ~9–11k BTU unit's capacity margin rather than downsizing.

> **Efficiency add-ons (reflective tarp, insulation, evaporative pre-cooling) are
> parked** in [`../docs/efficiency-backlog.md`](../docs/efficiency-backlog.md).
> They'd cut power use later, but the build does **not** rely on them for comfort.
> If you add and measure them, trim the array/battery via a new decision record.

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

> **Still researching — these are options, not a final pick.** Bus voltage (12/24/48 V),
> AC unit, panels, and cells are all open. Two candidate builds below; more may be
> added as research lands.

## Option A — 24 V build (real mini-split, no converter)
A genuine **24 V mini-split** exists at a fair price: the **Full Battery 24V Mini
Split, 9k BTU** (~$2,030, variable-speed Panasonic compressor, ~500 W / 19 A). It
runs straight off a 24 V bus — **no inverter and no DC-DC converter** — and its
variable-speed compressor dehumidifies and holds temperature far better than a 12 V
truck cooler (relevant to the "reliable comfort + low humidity" priority,
[`../decisions/0004`](../decisions/0004-active-ac-is-the-required-baseline.md)).
At 24 V the ~19 A draw also makes wiring/fusing easy. *Cost is the tradeoff vs 12 V.*

| Qty | Part | From catalog | ~Unit | ~Subtotal |
|-----|------|--------------|-------|-----------|
| 1 | **Full Battery 24V Mini Split, 9k BTU** (~500 W / 19 A) | [ac-units](../catalog/ac-units.md) | $2,030 | $2,030 |
| 1 | 24 V 100 Ah LiFePO4 (2.56 kWh) *(or 2× 12 V 100 Ah in series)* | [batteries](../catalog/batteries.md) | $520 | $520 |
| 5 | 200 W rigid panel (~1,000 W) *(or 2× 400 W)* | [solar-panels](../catalog/solar-panels.md) | $110 | $550 |
| 1 | 60 A MPPT (Victron 100/50 or EPEver 6415AN) | [charge-controllers](../catalog/charge-controllers.md) | $280 | $280 |
| — | BoS: ANL fuse, DC breaker, PV fuses, cables, MC4, busbar | [balance-of-system](../catalog/balance-of-system.md) | — | ~$180 |
| — | Dust box (sealed tote/case + cable glands), panel stakes/ballast | [balance-of-system](../catalog/balance-of-system.md) | — | ~$120 |
| **Total (parts)** | | | | **~$3,680** |

> Availability: cross-shop [fullbattery.com](https://fullbattery.com/products/24v-mini-split)
> vs the identical Amazon (ASIN B0CQTZFX9K) / eBay OEM listing; stock flickers.
> Setup note: it's a real split (indoor head + outdoor condenser + lineset) — more
> to rig in a tent than a self-contained cooler, but far better comfort.

## Option B — 12 V build (budget cooler, as-linked)
Cheapest unit (the linked $335 truck cooler, or OutEquipPro ~$895), but 12 V means
**high current everywhere**: ~60–80 A on the AC feed (fat, short cables) and, for a
full 1 kW array, an ~80–100 A MPPT. Keeping the array at ~600–750 W lets you use a
60 A MPPT. *Cheaper hardware; cruder cooling and heavier wiring than Option A.*

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
- **Want it lighter/cheaper?** You *could* right-size to a **5–6k BTU** DC unit
  (~300–400 W) → drop array to ~600 W and battery to ~1.5 kWh — but this trades
  away reliability margin, so [`../decisions/0004`](../decisions/0004-active-ac-is-the-required-baseline.md)
  keeps the larger unit. Only downsize if you've measured that a smaller unit holds
  comfort in your tent.
- **Want plug-and-play over DIY?** A portable power station + folding panels +
  small AC is easier but pricier and adds inverter loss (noted in `../decisions/0002`).
- **Want lower power later?** Add efficiency measures from
  [`../docs/efficiency-backlog.md`](../docs/efficiency-backlog.md) (shade, insulation,
  evaporative pre-cooling) *after* the active AC build works — parked for now on purpose.
- Cooling a real room/dwelling instead → the reference builds
  [A](config-a-daytime-budget.md)/[B](config-b-balanced-evening.md)/[C](config-c-24-7-reliable.md).
