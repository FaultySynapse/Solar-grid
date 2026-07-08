# 0001 — Track product selection in a repo with an ADR log

**Status:** Accepted · 2026-07-08

## Context
We're selecting parts for an off-grid solar system to run an AC, and we expect to
**pivot** between ideas and configurations repeatedly. We need catalogs of part
specs and a set of comparable full-system configurations, without losing the
reasoning behind changes.

## Decision
Keep everything as version-controlled Markdown:
- `docs/` — the requirements target + sizing methodology (the shared math).
- `catalog/` — datasheet-level specs per component category.
- `configurations/` — complete, costed builds that reference the catalog.
- `decisions/` — this ADR log for choices/pivots.
- `templates/` — to add parts and configs consistently.

## Consequences
- Cheap to compare alternatives (config files) and to swap parts (catalog rows).
- The "why" behind a pivot is preserved as an ADR, not lost in chat.
- Requires discipline: verify specs/prices against live datasheets before buying,
  and record real pivots here.
