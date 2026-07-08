# Research Log

We're in **options-gathering mode** — capturing candidates and tradeoffs, not
locking conclusions yet. This tracks what's been researched, what's open, and where
the findings live. Detailed specs go in `catalog/`; forks go in `decisions/`.

## The two competing architectures (top-level fork)
1. **DC-direct** — a native 12/24/48 V DC AC unit runs straight off the battery,
   **no inverter**. Simpler, no idle loss, but unit choice is narrower.
2. **AC-inverter mini-split** — a cheap, efficient 115 VAC inverter mini-split (or
   Midea U window) runs through a **pure-sine inverter**. Huge unit selection +
   efficiency, but adds an inverter (cost + all-day idle draw) and a split install.

Both are now researched (units, inverters, converters). Bus voltage still ties
everything together.

## Open decisions (not yet made)
- **Architecture:** DC-direct vs AC-inverter-mini-split (the fork above).
- **Bus voltage: 12 V vs 24 V vs 48 V** — pivotal; ties AC unit, cells, panels,
  inverter/controller together. See `decisions/0002`.
- **AC unit** — 24 V real mini-split / 12 V cooler / 48 V unit / 115 V AC mini-split.
- **Battery** — DIY no-weld cells (chemistry/size) vs turnkey module.
- **Panels** — cheap used residential (bulk watts, bulky) vs foldable (portable).
- **Inverter** (only if AC path) — standalone (frugal idle) vs all-in-one (one box).

## Research threads
| Date | Thread | Status | Findings → where |
|------|--------|--------|------------------|
| 2026-07-08 | DC split/mini-split AC units (12/24/48 V) | ✅ done | `catalog/ac-units.md` — Full Battery 24V 9k (~$2,030, ~500 W/19 A, no converter) is the standout affordable 24 V; 12 V coolers $335–895; HotSpot/Full Battery 48 V. |
| 2026-07-08 | No-weld LFP battery cells (Battery Hookup) | ✅ done | `catalog/batteries.md` — EVE LF206/LF280K bolt-terminal cells (~$70–77/kWh) scale to 4S/8S/16S; 48 V turnkey rack module ~$384. Flat-terminal weld-only cells excluded. |
| 2026-07-08 | Surplus panels, SF Bay Area | ✅ done (FB login-walled) | `catalog/solar-panels.md` — Craigslist used 300–315 W at ~$0.15/W; Renogy 400 W foldable ~$195. FB Marketplace not accessible — self-search tips captured. |
| 2026-07-08 | AC-inverter mini-splits (115/230 V) | ✅ done | `catalog/ac-units.md` — 115 V preferred; pick on **EER not SEER2**; Midea U 8k window $350 (no lineset), C&H 6k smallest split, MRCOOL DIY (no vacuum), Pioneer Quantum Ultra (13 EER2). |
| 2026-07-08 | DC-DC converters 24→12 / 48→12 | ✅ done | `catalog/dc-dc-converters.md` — 24→12 @60–80 A easy/cheap ($70–290); 48→12 thinner/pricier; ~5–15% loss + a failure point. Native-voltage AC unit often deletes the converter at $0 extra. |
| 2026-07-08 | Inverters for AC mini-split (12/24/48 V) | ✅ done | `catalog/inverters.md` — best 2–3 kW units are 24/48 V; idle draw matters (Victron ~8–13 W frugal, all-in-ones ~40–70 W); standalone vs all-in-one tradeoff. |

## Cross-cutting notes surfaced by research
- **Charge-controller max PV voltage is the stringing ceiling**, not the battery
  bus. 72-cell surplus panels are ~40 V Voc each and Voc rises in cold — pick panels
  and controller together.
- **12 V is high-current everywhere** (AC feed 60–80 A, ~1 kW array ~83 A). 24 V
  halves it; 48 V quarters it and pairs best with high-Voc surplus panels.
- A **24 V bank + 24 V AC unit** avoids a DC-DC converter entirely (the reason to
  hunt for a 24 V unit in the first place).
- No-weld packs are cleanest at **12 V/24 V from EVE cells** or **48 V from a
  pre-built rack module**.

## Data-driven config solver (2026-07-08)
Parts are now structured JSON in [`../data/parts/`](../data/parts/) (each with a
spec-definition block), configs are a constraint table in
[`../data/configs.json`](../data/configs.json), and
[`../scripts/run_combinations.py`](../scripts/run_combinations.py) filters parts
against each config to list qualifying parts + count valid combinations
(`--table`, `--config`, `--enumerate`, `--check`). See [`../data/README.md`](../data/README.md).
The markdown catalog/configs remain the human-readable view; keep the two in sync
when adding parts.

## Candidate threads not yet researched
- [ ] Charge controllers matched to the final bus voltage + surplus-panel Voc.
- [ ] Portable/dust-proof mounting & enclosure specifics for playa.
- [ ] BMS choice + top-balancing gear for the DIY pack.
- [ ] Real running-watt/duty measurement of the chosen AC unit (clamp meter).
