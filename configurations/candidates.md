# Tent Configuration Candidates

Complete candidate builds, each defined by its **key parameter combination** across
the design axes — **architecture × bus voltage × AC unit × inverter class**. These
are options to compare and pivot between — **no pick yet**. (Costs aren't listed
here; per-part pricing lives in [`../catalog/`](../catalog/).)

All share the tent target and the **solar-direct daytime** approach, sizing, Step-0
shade, and playa/dust notes in [`config-d-tent-solar-direct.md`](config-d-tent-solar-direct.md).

## The design axes
- **Architecture:** DC-direct (no inverter) · DC + DC-DC converter · AC-inverter mini-split.
- **Inverter class** (AC path only): **Combined** = all-in-one (inverter + MPPT +
  charger in one box) · **Standalone** = inverter + a separate MPPT charge controller.
- **Bus voltage:** 12 / 24 / 48 V — sets DC current, wiring, and panel stringing.
- **AC unit:** 12 V cooler · native 24/48 V DC mini-split · 115 V AC inverter mini-split/window.

## Shared across every config
~1 kW portable array · bus-matched LiFePO4 pack (4S/8S/16S) · BoS + dust box + mounts
· Step-0 shade. A **separate 60 A MPPT** is needed except where an all-in-one
includes it. See [`config-d-tent-solar-direct.md`](config-d-tent-solar-direct.md).

## Comparison matrix

| # | Architecture | Inverter class | Bus | AC unit | Battery | Separate MPPT? |
|---|--------------|----------------|-----|---------|---------|----------------|
| [C1](#c1) | DC-direct | — (none) | 12 V | 12 V cooler | 4S | Yes (60 A) |
| [C2](#c2) | DC-direct | — (none) | 24 V | 24 V DC mini-split | 8S | Yes (60 A) |
| [C3](#c3) | DC-direct | — (none) | 48 V | 48 V DC mini-split | 16S | Yes (30–60 A) |
| [C4](#c4) | DC + converter | — (48→12 V DC-DC) | 48 V | 12 V cooler | 16S | Yes (30–60 A) |
| [C5](#c5) | AC-inverter | **Combined** (all-in-one) | 24 V | 115 V mini-split / window | 8S | No (built in) |
| [C6](#c6) | AC-inverter | **Combined** (all-in-one) | 48 V | 115 V mini-split | 16S | No (built in) |
| [C7](#c7) | AC-inverter | **Standalone** + MPPT | 12 V | 115 V window | 4S | Yes (60 A) |
| [C8](#c8) | AC-inverter | **Standalone** + MPPT | 24 V | 115 V mini-split / window | 8S | Yes (60 A) |
| [C9](#c9) | AC-inverter | **Standalone** + MPPT | 48 V | 115 V mini-split | 16S | Yes (60 A) |

---

# DC-direct (no inverter)

## C1 — DC-direct · 12 V · cooler {#c1}
| Parameter | Value |
|-----------|-------|
| Architecture | DC-direct (no inverter, no converter) |
| Bus voltage | 12 V |
| AC unit | 12 V "parking cooler" ([ac-units](../catalog/ac-units.md)) |
| Charge controller | separate 60 A MPPT (cap array ~600 W) |
| Battery | 4S LiFePO4 (e.g. 4× EVE LF206) |

- **Pick when:** simplest, lowest-cost hardware and you accept crude cooling.
- **Watch-outs:** 12 V = high current everywhere (AC feed 60–80 A → thick short cables); weakest humidity control.

## C2 — DC-direct · 24 V · DC mini-split {#c2}
| Parameter | Value |
|-----------|-------|
| Architecture | DC-direct (no inverter, no converter) |
| Bus voltage | 24 V |
| AC unit | 24 V DC variable-speed mini-split (Full Battery 24V 9k) |
| Charge controller | separate 60 A MPPT |
| Battery | 8S LiFePO4 |

- **Pick when:** best comfort/humidity of the DC paths, no inverter or converter.
- **Watch-outs:** DC mini-split is a real split (head + condenser + lineset) to rig in a tent; verify stock.

## C3 — DC-direct · 48 V · DC mini-split {#c3}
| Parameter | Value |
|-----------|-------|
| Architecture | DC-direct (no inverter, no converter) |
| Bus voltage | 48 V |
| AC unit | 48 V DC mini-split (HotSpot DC4812VRF / Full Battery 48V) |
| Charge controller | separate 30–60 A MPPT |
| Battery | 16S LiFePO4 (turnkey rack module or DIY) |

- **Pick when:** lowest DC current; want to grow the array with cheap high-Voc 72-cell panels.
- **Watch-outs:** thin 48 V DC-unit choice; verify HotSpot stock.

---

# DC + converter

## C4 — 48 V bus · 12 V cooler via DC-DC {#c4}
| Parameter | Value |
|-----------|-------|
| Architecture | DC + 48→12 V DC-DC converter |
| Bus voltage | 48 V (12 V at the AC unit) |
| AC unit | 12 V "parking cooler" |
| Converter | 48→12 V, ~100 A ([dc-dc-converters](../catalog/dc-dc-converters.md)) |
| Charge controller | separate 30–60 A MPPT |
| Battery | 16S LiFePO4 |

- **Pick when:** you want the cheap 12 V unit but a clean 48 V bus/panels.
- **Watch-outs:** converter adds ~5–15% loss + heat + a series failure point carrying full AC current.

---

# AC-inverter — Combined (all-in-one)

*Inverter + MPPT + charger in one box. No separate MPPT. Simplest wiring; higher idle.*

## C5 — AC · Combined · 24 V {#c5}
| Parameter | Value |
|-----------|-------|
| Architecture | AC-inverter mini-split |
| Inverter class | Combined all-in-one (LVYUAN / Sungold 24 V) |
| Bus voltage | 24 V |
| AC unit | 115 V inverter mini-split or Midea U window ([ac-units](../catalog/ac-units.md)) |
| Charge controller | built into the all-in-one (~1.4 kW PV window) |
| Battery | 8S LiFePO4 |

- **Pick when:** cheap + efficient AC unit with one-box simplicity.
- **Watch-outs:** all-in-one idles ~20–40 W all day; modest PV window limits panel stringing.

## C6 — AC · Combined · 48 V (EG4) {#c6}
| Parameter | Value |
|-----------|-------|
| Architecture | AC-inverter mini-split |
| Inverter class | Combined all-in-one (EG4 3000EHV / Growatt) |
| Bus voltage | 48 V |
| AC unit | 115 V inverter mini-split (high-EER) |
| Charge controller | built in — **500 V / 5 kW PV** (EG4), strings surplus 72-cell panels |
| Battery | 16S LiFePO4 |

- **Pick when:** most efficient + expandable; one box but with a real high-voltage PV input.
- **Watch-outs:** EG4 idles <70 W operating; verify AC-unit refrigerant is R454B/R32.

---

# AC-inverter — Standalone (inverter + separate MPPT)

*Bare pure-sine inverter + a separately chosen MPPT. More boxes; frugal idle (esp.
Victron ~8–15 W) and free choice of charge controller.*

## C7 — AC · Standalone · 12 V {#c7}
| Parameter | Value |
|-----------|-------|
| Architecture | AC-inverter mini-split |
| Inverter class | Standalone (budget 2 kW 12 V) + separate MPPT |
| Bus voltage | 12 V |
| AC unit | Midea U 8k window (115 V) |
| Charge controller | separate 60 A MPPT (cap array ~600 W) |
| Battery | 4S LiFePO4 |

- **Pick when:** simplest cheap AC path for one small window unit.
- **Watch-outs:** 12 V caps inverter/array size; little headroom to grow.

## C8 — AC · Standalone · 24 V {#c8}
| Parameter | Value |
|-----------|-------|
| Architecture | AC-inverter mini-split |
| Inverter class | Standalone (Victron Phoenix 24/2000, or budget Renogy) + separate MPPT |
| Bus voltage | 24 V |
| AC unit | 115 V inverter mini-split or Midea U window |
| Charge controller | separate 60 A MPPT (free choice — Victron/EPEver) |
| Battery | 8S LiFePO4 |

- **Pick when:** want frugal idle + modular parts at a manageable 24 V current.
- **Watch-outs:** more boxes/wiring than an all-in-one; Victron path is premium.

## C9 — AC · Standalone · 48 V {#c9}
| Parameter | Value |
|-----------|-------|
| Architecture | AC-inverter mini-split |
| Inverter class | Standalone (Victron Phoenix 48/3000) + separate MPPT |
| Bus voltage | 48 V |
| AC unit | 115 V inverter mini-split (high-EER) |
| Charge controller | separate 60 A MPPT (high-Voc unit for surplus-panel strings) |
| Battery | 16S LiFePO4 |

- **Pick when:** lowest current + frugal idle + best-of-breed charge controller for cheap panels.
- **Watch-outs:** most boxes/wiring; highest summed part count of the AC configs.
