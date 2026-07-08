# Efficiency Add-Ons — Backlog (parked)

These reduce the cooling *load* or the *power* needed, so they'd shrink the solar/
battery bill. They are **deliberately parked**: the active build does **not** rely
on any of them to hit comfort. The refrigerant AC must reliably reach a
comfortable temperature (and dehumidify) **on its own** — see
[`../decisions/0004-active-ac-is-the-required-baseline.md`](../decisions/0004-active-ac-is-the-required-baseline.md).

Revisit these only after the active AC build works, as optional upgrades.

## Load-reduction (shade / insulation / sealing)
| Idea | Effect | Cost/effort | Notes |
|------|--------|-------------|-------|
| Reflective tarp/space-blanket over the tent, air gap | Cuts radiant heat gain | Low | Biggest bang for the buck; the tent is already out of direct sun. |
| Reflective bubble insulation on tent interior walls/floor | Lowers conductive/radiant gain | Low–med | Adds weight/bulk to pack. |
| Aggressive air sealing around the AC outlet / doorways | Less warm-air infiltration | Low | Every open flap is load on a fabric tent. |
| Shade structure / second canopy with airflow gap | Keeps the whole envelope cooler | Med | Also shades the battery/electronics — helps them too. |

**If added:** the AC's duty cycle drops → you could trim the array (~1 kW → ~0.6–0.8 kW)
and/or battery. Re-measure running watts before resizing.

## Alternative / supplemental cooling
| Idea | Effect | Why parked |
|------|--------|-----------|
| Evaporative (swamp) cooler as a supplement | ~50–150 W vs ~500 W; great in dry desert | **Adds humidity** and loses effect in humid spells/dust storms; the whole point of choosing refrigerant AC is reliable cold + low humidity. Could pre-cool intake air or run in mild hours to spare the battery. |
| Small DC fans for air mixing | Improves perceived comfort, spreads cold | Cheap; can add anytime, not load-bearing for the design. |

## How to promote something off this backlog
1. Add/measure its real effect (temp drop, watts saved).
2. Record a decision (`decisions/NNNN`) if it changes the active sizing.
3. Update `configurations/config-d-tent-solar-direct.md` and re-run the numbers.
