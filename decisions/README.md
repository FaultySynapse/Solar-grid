# Decision Log

Lightweight decision records (ADRs). One file per meaningful choice or **pivot**,
so the reasoning behind a change survives even after the change.

Write one whenever you: fork the architecture, pick between components in a way
that constrains the rest of the build, retarget the requirements, or reverse an
earlier decision.

| # | Decision | Status |
|---|----------|--------|
| [0001](0001-record-architecture-decisions.md) | Use this repo + ADR log to track product selection | Accepted |
| [0002](0002-ac-unit-power-path.md) | AC unit power path: AC-inverter vs 48 V DC vs 12/24 V DC | DC/no-inverter settled; **bus voltage 12/24/48 V still open (researching)** |
| [0003](0003-retarget-to-desert-tent.md) | Retarget to desert tent, daytime solar-direct cooling | Accepted |
| [0004](0004-active-ac-is-the-required-baseline.md) | Active refrigerant AC is the required baseline; efficiency add-ons parked | Accepted |

## Format

Copy an existing file. Each record has: **Status** (Proposed/Accepted/Superseded),
**Context** (what forces the decision), **Options** (with tradeoffs), **Decision**
(what we chose and why), **Consequences** (what it commits us to), and links to
affected configs/catalog entries. When a decision is reversed, set the old one to
*Superseded by NNNN* rather than deleting it.
