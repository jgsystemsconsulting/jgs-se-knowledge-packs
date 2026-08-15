# Cheatsheet — MIL-HDBK-338B

## Decision rules
1. **Need a number for a proposal?** Start ch02 prediction with documented assumptions — not a brochure MTBF.
2. **Prediction red?** Try parts/derating/stress (ch03) before redundancy (ch04).
3. **Mission-critical top event?** FTA + FMECA (ch06), not brainstorming alone.
4. **Cannot isolate faults in trial?** Fix testability (ch07) before buying more test time.
5. **Design still changing?** Prefer reliability growth over a one-shot demonstration (ch08).
6. **Field much worse than lab?** Revisit environment/human factors (ch05) and FRACAS quality (ch08).
7. **System metric debate?** Clarify Ai vs Ao / mission reliability (ch01, ch09).
8. **Handbook citation in a contract?** 338B is guidance — do not treat it as a self-executing requirement.

## Topic to chapter
| Topic | Chapter |
|-------|---------|
| MTBF/MTTR/availability math | ch01 |
| Allocation and prediction | ch02 |
| Derating / parts control | ch03 |
| Redundancy / fault tolerance | ch04 |
| Thermal/vibe/human stress | ch05 |
| FMEA/FMECA/FTA/SCA | ch06 |
| Reviews / DFT / safety link | ch07 |
| FRACAS / growth / demo test | ch08 |
| System effectiveness and COTS | ch09 |

## Tells and smells
| Smell | Likely gap |
|-------|------------|
| Single MTBF, no environment | Incomplete specification (ch02) |
| Huge redundancy, hot parts | Skipped derating (ch03) |
| FMEA copy-paste modes | Analysis not design-specific (ch06) |
| Growth test with no redesign budget | Not actually growth (ch08) |
| BIT claims without isolation targets | Weak testability (ch07) |
| Operational availability surprises | Logistics/maintainability ignored (ch01/ch09) |
