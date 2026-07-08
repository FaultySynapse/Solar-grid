# Component Catalog

Datasheet-level specs for candidate parts, one file per category. Pull real
parts into these tables using [`../templates/component-template.md`](../templates/component-template.md).

| Category | File | What to capture |
|----------|------|-----------------|
| AC units | [`ac-units.md`](ac-units.md) | BTU, SEER2/EER, running/surge W, supply voltage |
| Solar panels | [`solar-panels.md`](solar-panels.md) | W, Voc, Vmp, Imp, Isc, dimensions |
| Batteries | [`batteries.md`](batteries.md) | Chemistry, V, Ah, kWh, DoD, BMS, cycles |
| Inverters | [`inverters.md`](inverters.md) | Continuous/surge W, V, waveform, MPPT built-in? |
| Charge controllers | [`charge-controllers.md`](charge-controllers.md) | Type, A, max PV V, max PV W |
| Balance of system | [`balance-of-system.md`](balance-of-system.md) | Fuses, breakers, wire, disconnects, mounts |

## Conventions

- **Verify before you buy.** Every value here is a representative starting point.
  Confirm against the current manufacturer datasheet and a live retailer price.
- Prices are **approximate USD**, marked `~`, and will drift — treat as ballpark
  for comparison, not quotes. Last-touched dates noted per file.
- Mark a part's fit with a tag: ✅ good baseline fit · ⚖️ tradeoff · 🚫 avoid for this use.
- Keep one row per specific model+capacity (e.g. a 100 Ah and 200 Ah of the same
  line are two rows).
