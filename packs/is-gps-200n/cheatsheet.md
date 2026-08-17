# Cheatsheet — IS-GPS-200N (ICD exemplar)

## When this pack applies
- Need a worked public ICD/IS (definition / identification / criteria / annex map).
- Need DIST-A + IRN/CCB change-control example.
- Not for writing FAA IRD/ICD outlines (`faa-std-025`) and not for L5/L1C (705J/800J).

## Structure map
| Need | Open |
|------|------|
| What the IS is; DIST-A; IRN | ch01 |
| L1/L2 object; code families | ch02 |
| RF shall pattern | ch03 |
| LNAV vs CNAV families | ch04 |
| Time, URA, CEI, reserved | ch05 |
| Which appendix / do not dump | ch06 |
| Bit maps / PRN tables | official IS Apps II–IV only |

## Tells and smells
- **Smell**: Gold-code taps or CNAV bit fields in agent notes.
- **Smell**: Mixing two CEI issue-of-data sets.
- **Smell**: Treating SAIC’s cover line as a copyright reservation.
- **Tell**: Body points at an annex instead of pasting it.
- **Tell**: Empty §4/§5 left numbered.
- **Tell**: Cross-link to `faa-std-025` when the task is preparation.

## Do not build
- `is-gps-705j`, `is-gps-800j`, `icd-gps-153`, `gps-is-200n`, IS-300
