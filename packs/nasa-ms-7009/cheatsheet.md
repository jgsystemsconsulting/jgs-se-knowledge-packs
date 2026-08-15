# Cheatsheet — NASA-STD-7009B / HDBK-7009B

## When this pack applies
- M&S informs critical decisions (or TA/program pulls it in scope).
- Need credibility, V&V domains, uncertainty, or decision reporting discipline.

## Life-cycle spine
1. Programmatics: intended use, criticality, plan, metrics, acceptance criteria, reviews, defects.
2. Development: RWS/pedigree, data/software CM, units, assumptions, math, limits, permissible uses, capability assessment, guidance.
3. V&V + uncertainty: verify/validate with domains; characterize referent and model uncertainty.
4. Use: proposed use, appropriateness, input pedigree, setup, envelope control, messages, results assessment.
5. Risk + report: risks, warnings, uncertainty+method, assessments, reviews, qualifications, records, acceptance.

## Decision-maker report must-haves (memory aid)
- Warnings for violations / open defects / waivers
- Uncertainty estimate + process
- Capability and results assessment outcomes (vs thresholds)
- Review findings + people qualifications
- Required development/use records
- Risk acceptance rationale

## Tells and smells
- **Smell**: Validated with no domain or referent criteria.
- **Smell**: New mission question, same permissible-use paragraph.
- **Smell**: Beautiful plots, no uncertainty process.
- **Tell**: Defect log with open items called out in the briefing.
- **Tell**: Explicit gap-to-threshold discussion on capability/results.

## Pair with
- nasa-risk / nasa-pra for risk and quantitative uncertainty depth
- nasa-npr-7150 for software requirements on model code
- nist-ai-rmf when M&S includes AI/ML components
