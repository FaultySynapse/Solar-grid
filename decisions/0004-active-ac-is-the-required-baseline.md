# 0004 — Active refrigerant AC is the required baseline; efficiency add-ons parked

**Status:** Accepted · 2026-07-08 · refines `0003`

## Context
`0003` chose refrigerant AC and listed shade/insulation as a "Step 0" and
evaporative cooling as a considered alternative. Clarifying the intent: the
**active compressor AC is what actually delivers reliable comfort** — cold enough,
and **without high indoor humidity** — in a leaky fabric tent at 100–110 °F.
Shade/insulation and evaporative cooling are attractive for *efficiency*, but the
design must not depend on them to be comfortable.

## Decision
1. **The refrigerant AC is the required core** and is **sized to hit comfort on
   its own**, assuming no added shade/insulation beyond the tent already being out
   of direct sun. This favors **keeping the ~9–11k BTU unit's capacity margin**
   over downsizing to 5–6k BTU — reliability > minimal power here.
2. **Refrigerant, not evaporative**, specifically because it **dehumidifies**;
   evaporative would raise indoor humidity, which is the opposite of the goal.
3. **Shade/insulation and evaporative cooling are parked** as optional efficiency
   add-ons in [`../docs/efficiency-backlog.md`](../docs/efficiency-backlog.md).
   They are documented for later but excluded from active sizing.

## Consequences
- Array/battery are sized against the AC's **measured full running load**, not a
  reduced load that assumes add-ons.
- Config D keeps the larger DC unit and its ~1 kW array.
- The backlog stays available: if add-ons are later installed and measured, we can
  trim the array/battery via a new decision record.

## Affected
- `../docs/requirements.md` (priorities note)
- `../docs/efficiency-backlog.md` (new, parked)
- `../configurations/config-d-tent-solar-direct.md` (Step 0 reframed as optional)
