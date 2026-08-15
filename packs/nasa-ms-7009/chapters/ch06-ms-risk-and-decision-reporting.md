# Chapter 6: Risk Assessment and Decision-Maker Reporting

## Core Idea
Using M&S for decisions requires an explicit risk assessment tied to criticality and analysis findings, plus disciplined reporting: warnings for envelope violations and defects, uncertainty estimates and methods, capability and results assessment outcomes, review findings, people qualifications, development/use records, and risk-acceptance rationale.

## Frameworks Introduced
- **M&S-based analysis risk record**: Assessed risks from relying on the analysis, maintained as evidence.
- **Mandatory warning catalog**: Explicit warnings to decision makers for criteria violations, assumption/limit breaches, runtime issues, unfavorable use assessment, setup problems, waivers, and open defects.
- **Uncertainty in the report**: Estimate of results uncertainty plus description of processes used to obtain it.
- **Assessment outcomes in the report**: Capability assessment and results assessment (and gaps to thresholds).
- **Review and qualification narrative**: Technical-review findings and developer/user/analyst qualifications.
- **Appendix A records bundle**: Development and use records included as required by the compliance matrix pattern.
- **Risk acceptance statement**: Assessment of and rationale for accepting risks of the M&S-based analysis.

## Key Concepts
- **Decision makers need caveats, not just plots**: The standard enumerates warning classes.
- **Gap-to-threshold reporting**: Where capability/results sit versus acceptance thresholds matters.
- **People are part of credibility**: Qualifications of builders and analysts are reportable.
- **Waivers are visible**: Exceptions to requirements are not silent.
- **Risk acceptance is explicit**: Someone owns residual risk with rationale.
- **Handbook influence**: Appendices and assessment methods shape how factors are judged and presented.

## Mental Models
- Reporting is a safety control, not a communications afterthought.
- If a warning condition exists and is omitted, the report is noncompliant in spirit and letter.
- Risk ties criticality (ch01) to residual analysis weaknesses (ch05/ch04).
- Traceability from requirement IDs to report sections is the audit path.

## Anti-patterns
- **Executive summary with only nominal results**: Strips required warnings and uncertainty.
- **Hiding open defects**: Directly contrary to warning and risk expectations.
- **Capability score without threshold comparison**: No sense of good enough.
- **Anonymous analysis**: No qualifications, no review findings.

## Key Takeaways
1. Maintain an assessed risk record for M&S-based analysis use.
2. Include explicit warnings for the standard listed violation classes.
3. Report uncertainty estimates and the methods behind them.
4. Include capability and results assessment outcomes and threshold gaps.
5. Include review findings, qualifications, and required development/use records.
6. State risk-acceptance rationale when presenting results to decision makers.

## Connects To
- **ch01**: Criticality and acceptance thresholds.
- **ch02-ch05**: Evidence that populates the report.
- **nasa-risk**: RIDM/CRM framing for acceptance decisions.
- **nasa-system-safety**: Broader safety-case style argumentation when required.
