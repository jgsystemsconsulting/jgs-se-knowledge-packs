# Chapter 3: Developer's Role in VV&A of New Simulations

## Core Idea
The Developer builds the M&S so that it can be verified and validated: controlled design, implementable conceptual model, testable units, configuration baselines, and transparent limitations.

## Frameworks Introduced
- **Build-for-V&V**: architectures, interfaces, and logs that expose state for verification and validation experiments.
- **Developer testing vs independent V&V**: internal quality activities feed, but do not replace, V&V Agent evidence.
- **Configuration management**: baselines for software, models, parameters, and known defect lists tied to versions under accreditation.

## Key Concepts
- **Conceptual model realization**: trace design artifacts to the agreed conceptual model and requirements.
- **Verification support**: inspections, static analysis, unit/integration tests, requirement-to-implementation trace.
- **Problem reporting**: defects, workarounds, and uncertainty documented for accreditation visibility.
- **Collaboration with V&V Agent**: shared schedules, access to builds, instrumentation, and subject experts on the implementation.
- **Releases for validation**: stable candidates with release notes describing fidelity claims and limits.

## Mental Models
- **Instrument then claim**: if a behavior cannot be observed or logged, it is hard to verify or validate.
- **Version is part of the claim**: accreditation attaches to a configuration, not a living branch.
- **Limitations are features of honesty**: undocumented limits become hidden operational risk.

## Anti-patterns
- Treating V&V Agent requests as adversarial noise rather than co-design for credibility.
- “Works on my scenario” without regression suites tied to requirements.
- Silent parameter changes between validation and delivery.
- Equating code coverage with validation against the referent.

## Key Takeaways
1. Developers create the verifiable implementation and the configuration identity of what will be accredited.
2. Internal testing is necessary evidence, not sufficient accreditation.
3. Traceability and CM make V&V and accreditation tractable.
4. Explicit limitations protect Users and Accreditation Authorities.

## Connects To
- **ch04**: PM integrates developer milestones with VV&A gates.
- **ch05**: V&V Agent plans verification using developer artifacts.
- **ch07–ch08**: fidelity claims and validation cases need stable builds.
- **ch09**: developer data pipelines require data V&V.
