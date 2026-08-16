# Chapter 8: Validation Fundamentals

## Core Idea
Validation determines how accurately a model or simulation and its associated data represent the real world from the perspective of the intended uses—building credibility and reducing User risk.

## Frameworks Introduced
- **DoDI-aligned definition**: accuracy of M&S and data vs real world (present or future) for intended uses; extends to data validation, face validation, and distributed simulation validation.
- **Essential validation steps**: requirements from User objectives; characteristics of the M&S; referent description; comparison on relevant attributes; assessment of adequacy.
- **Referent types**: measured reality, historical data, validated higher-fidelity models, theory, SME consensus—each with different strength.

## Key Concepts
- **Simuland vs referent vs model**: keep the three distinct in planning and reporting.
- **Comparison methods**: quantitative (statistical, error metrics) and qualitative (face validation, structured SME review).
- **Domain of intended use**: validation results apply inside an envelope; outside it, claims expire.
- **Credibility contribution**: validation is necessary evidence for accreditation, not the whole case.
- **Future systems**: “real world” includes anticipated environments and systems not yet fielded—referents must be chosen carefully.

## Mental Models
- **Compare what matters**: validate behaviors that drive the decision, not only easy-to-measure outputs.
- **Uncertainty is part of the result**: report confidence and disagreement, not only pass/fail.
- **Face validation is structured judgment**: SME review needs protocols, not hallway opinions alone.

## Anti-patterns
- Validating against the developer’s own tuning set without holdout or independent referent.
- Declaring global validity from one scenario family.
- Skipping referent documentation so results cannot be reproduced or challenged.
- Using validation theater (plots without criteria) to force accreditation.

## Key Takeaways
1. Validation is intended-use-relative accuracy assessment against a defined referent.
2. Requirements, M&S characteristics, referent, and comparison form the minimal method spine.
3. Results are envelope-bounded; state the domain of applicability.
4. Validation evidence feeds credibility and residual-risk statements for accreditation.

## Connects To
- **ch07**: fidelity attributes under test.
- **ch09**: data validation as part of M&S credibility.
- **ch05–ch06**: who runs validation and how it enters accreditation.
- **ch10**: Type II risk of accepting bad validation comfort.
