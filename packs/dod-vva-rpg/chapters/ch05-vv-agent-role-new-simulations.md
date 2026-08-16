# Chapter 5: V&V Agent's Role in VV&A of New Simulations

## Core Idea
The V&V Agent plans and performs verification and validation to show the M&S meets intended-use needs, reduces development/operational risk, enhances credibility, and supports accreditation—with enough independence to be believable.

## Frameworks Introduced
- **Unified V&V agent preference**: one organizational entity spanning verification and validation avoids dual learning curves and late validation starts; specialists (SMEs, test labs) plug in as needed.
- **Objectives set**: meet intended use; reduce risk; enhance credibility; support accreditation.
- **Cooperative independence**: work with the Developer without becoming the Developer’s QA department only.

## Key Concepts
- **V&V plan**: scope, methods, resources, schedule, products, and linkage to accreditation criteria.
- **Verification activities**: requirements trace, design/code analysis, test against specs, configuration audits.
- **Validation activities**: comparison to referent (data, reality, higher-fidelity model, SME face validation) for relevant behaviors.
- **Reporting**: findings, limitations, uncertainty, and open risks in forms accreditation can use.
- **Lifecycle timing**: engage from early development so validation is not bolted on at the end.

## Mental Models
- **Plan the questions, then the tests**: each activity answers a credibility question tied to intended use.
- **Independence is graded**: organizational separation, technical authority, and reporting path matter more than org-chart cosmetics alone.
- **Negative results are success**: finding inadequacies early is the job, not a program failure by itself.

## Anti-patterns
- Splitting verification and validation agents without integration, then discovering validation is unprepared.
- Rubber-stamping developer test reports as validation.
- Method shopping (only techniques that will pass).
- Delivering a V&V report that never states residual limitations.

## Key Takeaways
1. V&V Agent owns the evidence engine for credibility and accreditation support.
2. Early single-thread V&V responsibility beats fragmented late heroics.
3. Methods must match intended-use questions and referent availability.
4. Reports must be decision-grade: clear findings, limits, and risk implications.

## Connects To
- **ch03**: developer artifacts and access.
- **ch06**: accreditation package consumes V&V results.
- **ch07–ch09**: fidelity, validation fundamentals, data V&V techniques.
- **ch10**: risk framing for residual issues.
