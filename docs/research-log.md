# Research Log

We're in **options-gathering mode** — capturing candidates and tradeoffs, not
locking conclusions yet. This tracks what's been researched, what's open, and where
the findings live. Detailed specs go in `catalog/`; forks go in `decisions/`.

## Open decisions (not yet made)
- **Bus voltage: 12 V vs 24 V vs 48 V** — the pivotal open choice; it ties together
  the AC unit, battery cells, panels, and charge controller. See `decisions/0002`.
- **AC unit** — 24 V real mini-split vs 12 V budget cooler vs 48 V unit.
- **Battery** — DIY no-weld cells (which chemistry/size) vs turnkey module.
- **Panels** — cheap used residential (bulk watts, bulky) vs foldable (portable).

## Research threads
| Date | Thread | Status | Findings → where |
|------|--------|--------|------------------|
| 2026-07-08 | DC split/mini-split AC units (12/24/48 V) | ✅ done | `catalog/ac-units.md` — Full Battery 24V 9k (~$2,030, ~500 W/19 A, no converter) is the standout affordable 24 V; 12 V coolers $335–895; HotSpot/Full Battery 48 V. |
| 2026-07-08 | No-weld LFP battery cells (Battery Hookup) | ✅ done | `catalog/batteries.md` — EVE LF206/LF280K bolt-terminal cells (~$70–77/kWh) scale to 4S/8S/16S; 48 V turnkey rack module ~$384. Flat-terminal weld-only cells excluded. |
| 2026-07-08 | Surplus panels, SF Bay Area | ✅ done (FB login-walled) | `catalog/solar-panels.md` — Craigslist used 300–315 W at ~$0.15/W; Renogy 400 W foldable ~$195. FB Marketplace not accessible — self-search tips captured. |

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

## Candidate threads not yet researched
- [ ] Charge controllers matched to the final bus voltage + surplus-panel Voc.
- [ ] Portable/dust-proof mounting & enclosure specifics for playa.
- [ ] BMS choice + top-balancing gear for the DIY pack.
- [ ] Real running-watt/duty measurement of the chosen AC unit (clamp meter).
