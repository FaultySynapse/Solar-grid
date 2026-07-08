# Component row template

Copy the relevant row shape into the matching `catalog/*.md` table. Keep values at
datasheet level so sizing math stays trustworthy. Mark fit: ✅ good · ⚖️ tradeoff · 🚫 avoid.

## AC unit
```
| Model | Type | BTU/h | SEER2/EER | Running W (typ) | Startup surge | Supply V | ~Price | Fit | Notes |
```

## Solar panel
```
| Model | W (STC) | Voc | Vmp | Imp | Isc | Cells | Dimensions | ~$/W | ~Price | Fit | Notes |
```

## Battery
```
| Model | Nominal V | Ah | kWh (nom) | Usable @80% | BMS | Cont. discharge | Cycles | Form | ~Price | Fit | Notes |
```

## Inverter
```
| Model | Cont. output | Surge | Batt V | Waveform | MPPT built-in | Max PV | ~Price | Fit | Notes |
```

## Charge controller
```
| Model | Type | Rated A | Max battery V | Max PV Voc | Max PV W | ~Price | Fit | Notes |
```

## Balance-of-system item
```
| Item | Spec | Purpose | ~Price | Notes |
```

### Reminders
- Verify every spec against the current datasheet; verify price at a live retailer.
- Prices are approximate USD, marked `~`.
- One row per specific model+capacity.
