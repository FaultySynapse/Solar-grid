# Tent Build — Fundamentals (shared by all candidates)

The qualitative fundamentals every candidate build relies on: the solar-direct
concept, the shade requirement, and the wiring / playa-survival notes. **Specific
part picks and all sizing/cost numbers are computed** from `../data/` by the
scripts — this file is narrative only.

- Candidate configurations (C1–C9): [`candidates.md`](candidates.md) / [`../data/configs.json`](../data/configs.json)
- Conditions: [`../data/scenario.json`](../data/scenario.json) · Sizing/feasibility: `python3 scripts/solve.py --config Cx` · Cheapest builds: `python3 scripts/rank.py`
- Target & pivot rationale: [`../docs/requirements.md`](../docs/requirements.md), [`../decisions/0003`](../decisions/0003-retarget-to-desert-tent.md)

## The key idea — solar-direct daytime cooling
You cool **during the day, when the sun is strongest.** So the panels run the AC
**live**, and the battery only has to cover the compressor's inrush, passing
clouds, and the hour or two on either side of solar noon — a small **buffer**, not
an overnight bank. This is the cheapest architecture and the main simplification.

The **refrigerant AC is the required core**: it must reach a comfortable
temperature — and keep humidity down — **on its own**, with no reliance on
shade/insulation upgrades ([`../decisions/0004`](../decisions/0004-active-ac-is-the-required-baseline.md)).
The load is sized **conservatively** (see `scenario.json` `envelope_ua`) so the
solution is over-sized; small units correctly show up as unable to hold setpoint.

> Efficiency add-ons (reflective tarp, insulation, evaporative pre-cooling) are
> parked in [`../docs/efficiency-backlog.md`](../docs/efficiency-backlog.md) — they'd
> cut power use later, but the build does **not** rely on them for comfort.

## Wiring & protection
- **Fuse the battery** with an ANL (24/48 V) or **Class-T (12 V, high fault current)**
  main, sized just above the AC's running amps; DC breaker/disconnect on the feed.
- **AC-feed cable** sized to current and kept **short**: 12 V @ 60–80 A → 2–4 AWG;
  24 V @ ~30 A → 8–10 AWG (why lower voltage means heavier copper).
- **PV**: 10 AWG PV wire, MC4, per-string fuse if ≥3 parallel; keep cold-adjusted
  string Voc under the controller's max PV voltage (the stringing ceiling).
- **MPPT sized to the full array** (it must survive the AC switching off).

## Playa / dust & heat survival (one-week desert trip)
- Battery + electronics in a **sealed tote/Pelican-style case** with cable glands;
  keep it **shaded** (heat derates both; LiFePO4 shouldn't charge hot).
- Panels **low and staked/ballasted** against wind; **wipe dust** daily (dust = lost watts).
- Clean the AC's **intake/condenser filter**; exhaust hot condenser air **outside** the tent.
- Bring spare fuses, MC4s, and a multimeter/clamp meter.

## Behavior
- Midday: array runs the AC live with surplus topping the buffer.
- Cloud passes / dawn & dusk shoulders: buffer carries the AC a few hours.
- Overnight: not cooled (by design) — desert nights are cool.

## Tradeoffs / when to switch
- **Cheapest vs. best comfort / lowest current:** compare the 9 candidates with
  `python3 scripts/rank.py` (cost) and `solve.py --config Cx` (feasibility).
- **Plug-and-play over DIY?** A portable power station + folding panels + small AC
  is easier but pricier and adds inverter loss (see [`../decisions/0002`](../decisions/0002-ac-unit-power-path.md)).
- **Lower power later?** Add efficiency measures from
  [`../docs/efficiency-backlog.md`](../docs/efficiency-backlog.md) *after* the active build works.
