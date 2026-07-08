# Solar-grid — Off-Grid Solar for AC

A working knowledge base for designing an **off-grid solar power system whose
primary job is running an air-conditioner (AC)**. It holds:

- **Component spec catalogs** — datasheet-level specs for panels, batteries,
  inverters, charge controllers, AC units, and balance-of-system parts.
- **Full system configurations** — complete, costed builds that combine parts
  into a working design, each documented so they can be compared.
- **A decision log** — a running record of ideas we explored and why we pivoted,
  so we never lose the reasoning behind a change.

The point is to make it cheap to **pivot**: swap a battery chemistry, retarget a
bigger AC unit, or trade cost for autonomy, without losing the trail.

## How this repo is organized

| Path | What lives there |
|------|------------------|
| [`docs/requirements.md`](docs/requirements.md) | The design target — the AC load, location, runtime, and priorities everything is sized against. **Start here / edit here to retarget.** |
| [`docs/sizing-methodology.md`](docs/sizing-methodology.md) | How we turn "run this AC" into panel watts, battery kWh, inverter size, and controller amps. Worked example included. |
| [`docs/glossary.md`](docs/glossary.md) | Terms and units (PSH, DoD, EER/SEER2, Voc, etc.). |
| [`catalog/`](catalog/) | Spec sheets per component category. One table per category, real representative parts. |
| [`configurations/`](configurations/) | Complete builds. [`configurations/README.md`](configurations/README.md) has the side-by-side comparison. |
| [`decisions/`](decisions/) | Lightweight decision records (ADR-style). One file per pivot. |
| [`templates/`](templates/) | Copy-paste templates for adding a new component or a new configuration. |

## Current target (edit in `docs/requirements.md`)

| Parameter | Value |
|-----------|-------|
| Space | Shaded **tent**, ~60–70 sq ft (two-queen footprint) |
| Location / solar | Nevada desert, August · ~7 peak sun hours · very dry · ~100–110 °F |
| AC load | Small **DC split AC** (vehicle class), ~9–11k BTU, ~500 W — no inverter |
| Cooling window | **Daytime, while sleeping** → run the AC **live off solar** |
| Battery | Small buffer (~2.5 kWh) — no overnight bank needed |
| Build / duration | DIY 12 V/24 V battery+solar+MPPT · one-off ~1-week trip · portable, dust-hardened |

**Candidate builds (research mode, no pick yet):**
[`configurations/candidates.md`](configurations/candidates.md) — 7 complete builds
(~$1,250–$3,200) spanning DC-direct vs AC-inverter-mini-split across 12/24/48 V.
Shared fundamentals in [`configurations/config-d-tent-solar-direct.md`](configurations/config-d-tent-solar-direct.md).
Configs A/B/C are kept as *reference for a room/dwelling* — oversized for a tent.
Open decisions and research threads are tracked in [`docs/research-log.md`](docs/research-log.md).

## Workflow: how to use this repo

1. **Set the target.** Edit `docs/requirements.md` with your real AC unit,
   location (peak sun hours), runtime, and autonomy needs.
2. **Add candidate parts.** Drop products into the relevant `catalog/*.md`
   table using [`templates/component-template.md`](templates/component-template.md).
   Keep specs at datasheet level so sizing math is trustworthy.
3. **Build a configuration.** Copy [`templates/configuration-template.md`](templates/configuration-template.md)
   into `configurations/`, pick parts from the catalog, and run the numbers using
   `docs/sizing-methodology.md`.
4. **Compare.** Update the table in `configurations/README.md`.
5. **When you pivot,** write a short note in `decisions/` so the "why" survives.

## Important caveats

- **Verify every spec and price against the current manufacturer datasheet
  and a live retailer.** Prices and even model specs drift; catalog values here
  are representative starting points, not quotes.
- Electrical work on battery/inverter systems is genuinely hazardous (DC arc
  flash, lithium fire risk, code compliance). This repo is a **planning aid**,
  not an installation authority. Follow NEC/local code and manufacturer manuals,
  and involve a licensed electrician where required.
