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

## Current baseline (edit in `docs/requirements.md`)

| Parameter | Baseline assumption |
|-----------|--------------------|
| AC load | 12,000 BTU (1-ton) **inverter** mini-split |
| Location / solar | ~5 peak sun hours/day (placeholder) |
| Runtime | ~8–10 h/day cooling, ~1 day battery autonomy |
| Priority | Balanced cost/performance |

> These are placeholders chosen to make the starter catalog and configs concrete.
> Change them in `docs/requirements.md` and the configs/sizing follow.

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
