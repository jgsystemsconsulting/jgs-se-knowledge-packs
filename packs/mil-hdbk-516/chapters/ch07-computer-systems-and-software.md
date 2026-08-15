# Chapter 7: Computer Systems and Software Criteria

## Core Idea
Section 15 provides airworthiness criteria for computer systems and software — development discipline, verification/validation, configuration control, and integration evidence that software performs airworthiness-relevant functions without unacceptable hazard contribution.

## Frameworks Introduced
- **Software airworthiness criteria**: Qualitative expectations for airborne/ground software contributing to airworthiness.
- **Development and V&V evidence**: Plans, specifications, tests, and configuration control typical of certification source data lists.

## Key Concepts
- Software that can affect safe flight is a first-class airworthiness article.
- Development discipline, V and V, and CM are part of the airworthiness argument.
- Flight loads need rigorous release control.
- Integration and flight-test evidence complement unit software tests.
- UAS/ground software may still hazard the system when applicable.

## Mental Models
- Software is a first-class airworthiness article when it can affect safe flight or operation.
- Configuration control of loads/versions is part of staying inside the certification basis.
- Integration tests matter as much as unit software tests.

## Anti-patterns
- **Process theater**: Plans on shelf without bidirectional trace to hazards/criteria.
- **Field reflash culture**: Unofficial software changes outside CM/airworthiness release.
- **Ignoring non-airborne software**: UAS/ground software that can still hazard the system.

## Key Takeaways
1. Identify software items that contribute to airworthiness criteria early.
2. Maintain rigorous CM and release control for flight loads.
3. Align hazard analyses with software failure modes.
4. Include integration/flight-test evidence in closure packages.
5. Coordinate with avionics/E3 criteria (ch06).

## Connects To
- **ch06** for avionics hardware/E3 context.
- **ch02** for SE/CM backbone.
- **ch01** for tailoring software criteria into the basis.
