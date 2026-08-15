# Cheatsheet — MIL-HDBK-516C

## Decision rules
1. **Starting airworthiness planning?** Build a tailored certification basis (ch01) before writing isolated domain reports.
2. **Is 516C a contract section C dump?** No — guidance; tailor and point to specific criteria/methods.
3. **Engine has a credential already?** Still close installation criteria (ch05).
4. **UAS program?** Check avionics + crew-systems applicability to the control segment (ch06, ch08).
5. **Software change?** Re-enter ch07 gates; do not treat as maintenance only.
6. **Dropped a criterion?** If it is not in the basis with rationale, you did not tailor — you omitted (ch01).
7. **Structures repair in the field?** Confirm it stays inside the structural basis (ch03).
8. **E3 fail after avionics add?** Reopen integrated ch06 evidence, not only the new box qual.

## Domain to chapter
| Domain | Chapter |
|--------|---------|
| Tailoring / certification basis | ch01 |
| Systems engineering / CM / tech data | ch02 |
| Structures | ch03 |
| Flight technology | ch04 |
| Propulsion + installation | ch05 |
| Diagnostics / avionics / electrical / E3 | ch06 |
| Computers and software | ch07 |
| Crew systems / escape / life support | ch08 |

## Tells and smells
| Smell | Likely gap |
|-------|------------|
| We follow 516C with no basis doc | Missing tailoring (ch01) |
| Domain reports, no CM linkage | SE criteria weak (ch02) |
| Engine credential used as aircraft closure | Installation ignored (ch05) |
| UAS aircraft-only package | Control segment criteria missing |
| Untracked flight software loads | Software CM/airworthiness gap (ch07) |
| Cockpit redesign without escape re-test | Crew systems re-verification gap (ch08) |
