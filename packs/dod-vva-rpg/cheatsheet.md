# Cheatsheet — DoD M&S VV&A RPG

## Decision rules
1. **No intended use written?** Stop — do not scope V&V or accredit.
2. **Verification or validation?** Built right (vs specs/conceptual model) vs right thing (vs referent for use).
3. **Ready to accredit?** Need evidence + configuration identity + residual risk/constraints — not “tests ran.”
4. **How much fidelity?** Enough to change or stabilize the decision; specify by attribute.
5. **Data trusted?** Pedigree + verification checks + validation where decision-sensitive.
6. **Independence enough?** Graded by consequence; developer-only V&V is a risk flag on high stakes.
7. **Reuse OK?** Only after delta gap analysis for the new use and configuration.
8. **Which pack?** NASA M&S standard depth → nasa-ms-7009; enterprise T&E → dote/dod-te; DoD VV&A roles/practices → this pack.

## Role quick map
| Role | Owns |
|------|------|
| User | Intended use, acceptability, SME/operational truth |
| Developer | Implementation, CM, developer test evidence |
| M&S PM | Plan/resources/contracts/gates integrating VV&A |
| V&V Agent | V&V plan, execution, decision-grade reports |
| Accreditation Agent | Package, recommendation, criteria trace |
| Authority | Accept / constrain / reject |

## Type I / Type II (M&S focus)
| Error | Meaning | Typical concern |
|-------|---------|-----------------|
| Type I | Reject correct evidence | Wasted rejection of good M&S |
| Type II | Accept incorrect evidence | Wrong operational/acquisition decision |

## Tells & smells
| Smell | Likely gap |
|-------|------------|
| Accreditation letter with no intended use | ch01, ch06 |
| Validation = developer demo only | ch05, ch08 |
| “High fidelity” with no attributes | ch07 |
| Dataset not versioned with build | ch09, ch03 |
| No residual risk in package | ch10, ch06 |
| VV&A starts after code complete | ch04, ch05 |
| Old accreditation after major change | ch06 |
| User absent from criteria setting | ch02 |
