# 0001 — Track product selection in a repo with an ADR log

**Status:** Accepted · 2026-07-08

## Context
We're selecting parts for an off-grid solar system to run an AC, and we expect to
**pivot** between ideas and configurations repeatedly. We need catalogs of part
specs and a set of comparable full-system configurations, without losing the
reasoning behind changes.

## Decision
Keep everything version-controlled:
- `docs/` — the requirements target + sizing methodology (the shared math).
- `data/parts/` — datasheet-level part specs per category (JSON + spec definitions).
- `data/configs.json` + `scripts/run_combinations.py` — the config constraint table and solver.
- `configurations/` — human-readable build write-ups referencing the part data.
- `decisions/` — this ADR log for choices/pivots.
- `templates/` — to add parts and configs consistently.

> Update: parts began as Markdown catalog tables and were later migrated to JSON
> in `data/parts/` (the markdown catalog was removed) so a script can solve the
> combinations. See `docs/research-log.md`.

## Consequences
- Cheap to compare alternatives (config files) and to swap parts (edit a JSON part).
- The "why" behind a pivot is preserved as an ADR, not lost in chat.
- Requires discipline: verify specs/prices against live datasheets before buying,
  and record real pivots here.
