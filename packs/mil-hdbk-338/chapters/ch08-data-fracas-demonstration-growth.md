# Chapter 8: Reliability Data, FRACAS, Demonstration, and Growth Testing

## Core Idea
Section 8 covers the empirical half of reliability engineering: collecting failure/success data, FRACAS, data analysis, demonstrating requirements, managing reliability growth, and accelerated testing contrasts. Predictions become credible only when this feedback loop is real.

## Frameworks Introduced
- **Reliability data uses**: Verify requirements, discover deficiencies, build history for prediction.
- **FRACAS**: Failure reporting, analysis, and corrective action as a closed loop.
- **Reliability demonstration**: Structured tests against the specified metric and decision rules.
- **Reliability growth**: Test-analyze-and-fix programs that raise reliability over development.
- **Accelerated testing**: Compressed stress to surface mechanisms faster, with analysis caveats.

## Key Concepts
- Reliability data includes success time as well as failure events.
- FRACAS closes the loop only when fixes are owned and verified.
- Demonstration tests a frozen design against a decision rule.
- Growth testing assumes funded test-analyze-fix cycles.
- Accelerated tests need physics-aware interpretation.

## Mental Models
- Success time is data too — not only failure events.
- Growth assumes you will fix root causes; demonstration assumes a frozen design.
- FRACAS without corrective-action authority is a complaint box.

## Anti-patterns
- **Growth in name only**: Logging failures without funded redesign.
- **Demonstration gaming**: Benign profiles that do not match the specification environment.
- **Orphan failure reports**: No root-cause owners or fix verification.

## Key Takeaways
1. Instrument the program for complete failure and operating-time data.
2. Run FRACAS with mandatory root cause and fix verification.
3. Choose demonstration vs growth based on design maturity.
4. Plan economics and timing of growth testing deliberately.
5. Use accelerated methods with physics-aware interpretation.

## Connects To
- **ch02** for the requirements being demonstrated.
- **ch06** for expected failure modes in test.
- **ch01** for statistical interpretation of test data.
