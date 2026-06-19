# Chapter 8: Appendix E — Technology Readiness Levels

## Core Idea
Appendix E defines the nine-level TRL scale for both hardware and software, providing specific descriptions, examples, and success criteria for each level so that programs and projects can consistently assess technology maturity throughout the life cycle, gate technology advancement decisions, and reduce the risk of incorporating immature technologies into operational products.

## Frameworks Introduced
- **TRL Scale (1–9)**: A nine-level ordinal scale measuring technology maturity from basic principles (TRL 1) to flight-proven operational systems (TRL 9); separate hardware and software descriptions are provided for each level; success criteria define what evidence is needed.
  - When to use: At every technology assessment milestone — initially in Formulation, and updated at every status review; required by NPR 7123.1D Section 5.1.6 for all programs and projects.
- **Relevant Environment Concept**: Not all testing must occur in the full operational environment; the "relevant environment" is the specific subset of the operational environment needed to stress the critical risk aspects of the technology — defined by TRL 4–7 progression.
  - When to use: When planning TRL advancement test campaigns; focus resources on stressing the specific technology risk, not replicating the full operational system.

## Key Concepts
- **TRL 1 — Basic Principles Observed**: Scientific knowledge underpins hardware concepts or software mathematical formulations; success criterion is peer-reviewed documentation.
- **TRL 2 — Technology Concept Formulated**: Practical application identified but speculative; no experimental proof; for software, basic algorithm properties are defined and basic principles coded.
- **TRL 3 — Analytical/Experimental Proof-of-Concept**: Laboratory studies validate predictions for critical functions; for software, limited functionality developed to validate critical properties using non-integrated components.
- **TRL 4 — Component Validation in Laboratory**: Low-fidelity breadboard built and operated; for software, key functionally critical software components integrated and validated; architecture development begins; relevant environments defined.
- **TRL 5 — Component Validation in Relevant Environment**: Medium-fidelity brassboard built and operated in relevant environment; for software, end-to-end software elements implemented and interfaced with existing systems; operational environment performance predicted.
- **TRL 6 — System/Subsystem Prototype in Relevant Environment**: High-fidelity prototype demonstrates performance under critical environmental conditions; for software, prototype implementations demonstrated on full-scale realistic problems; engineering feasibility fully demonstrated.
- **TRL 7 — System Prototype in Operational Environment**: High-fidelity prototype or engineering unit functions in actual operational environment and platform (ground, airborne, or space); for software, prototype with all key functionality available, well integrated with operational hardware/software systems.
- **TRL 8 — Actual System Completed and Flight Qualified**: Final product in final configuration successfully demonstrated through test and analysis for intended operational environment; for software, all software debugged, integrated with all operational hardware/software, V&V completed.
- **TRL 9 — Actual System Flight Proven**: Final product successfully operated in an actual mission; for software, all documentation complete, sustaining support in place.
- **Breadboard**: Low-fidelity unit demonstrating function only, without respect to form or fit; commercial/ad hoc components; not intended to provide definitive operational performance information (TRL 4 artefact).
- **Brassboard**: Medium-fidelity functional unit using as much of the final product design as possible; begins addressing scaling issues; structured to operate in simulated operational environments (TRL 5 artefact).
- **Laboratory Environment**: An environment that does not address the operational environment in any manner; tests in laboratory are solely for demonstrating underlying technical principles.
- **Relevant Environment**: The specific subset of the operational environment required to demonstrate critical risk aspects of the technology; not the full operational environment.
- **Engineering Unit**: High-fidelity unit closely resembling the final product; built and tested to establish confidence the design will function in expected environments; may become the final product if proper traceability is maintained.

## Mental Models
- TRL 1–3 = laboratory science; TRL 4–6 = engineering demonstration (lab → relevant environment); TRL 7 = operational environment demonstration; TRL 8 = flight qualification; TRL 9 = operational mission success. The jump from 6 to 7 (relevant → operational) is often the hardest and most expensive step.
- Use TRL to communicate risk, not schedule: a technology at TRL 4 entering a CDR-level system is a high risk regardless of how long it has been in development.
- When a program uses a maturity scale other than TRL, it must map back to TRL; NASA's TRL definitions take precedence in conflict with other directives.
- Life testing (where required) should start as early as TRL 5 to enable completion by TRL 8; do not defer life testing to late-phase qualification.

## Anti-patterns
- **Assuming TRL 6 = operational readiness**: TRL 6 demonstrates performance in a relevant environment with a prototype; operational readiness requires TRL 7–9 depending on the mission criticality.
- **Using a single TRL for an entire system**: TRL applies at the technology/component level; a system can have elements at different TRL levels; the system TRL is typically constrained by its lowest-TRL critical element.
- **Conflating software and hardware TRL criteria**: Each TRL level has separate hardware and software descriptions; a software element at TRL 5 requires end-to-end system integration and environment testing, not just algorithm coding.

## Key Takeaways
1. TRL 1–9 is a mandatory assessment scale for all NASA programs; initial assessment is done in Formulation phase and updated at every status review.
2. Hardware and software have distinct TRL descriptions at each level; both must be assessed separately.
3. The relevant environment concept allows focused testing on critical risk aspects without requiring full operational environment replication until TRL 7.
4. TRL 6 is the minimum demonstration in a relevant environment; TRL 7 requires actual operational environment; TRL 8 requires flight qualification; TRL 9 requires successful mission operations.
5. When non-TRL maturity measures are used, they must be mapped back to TRL — NPR 7123.1 takes precedence over other directives in TRL definition conflicts.
6. Life testing for worn-out mechanisms, temperature stability, and extreme-environment performance should begin at TRL 5 and must be complete by TRL 8.

## Connects To
- **Chapter 5 (Life-Cycle Reviews)**: TRL tracking is required throughout the life cycle and reported at status reviews; Section 5.1.6 mandates TRL use.
- **Chapter 6 (SEMP)**: Technology development plans capturing TRL advancement approaches are typically captured in the SEMP or a standalone Technology Development Plan.
- **NASA/SP-6105 (Systems Engineering Handbook)**: Provides additional guidance on measures for assessing technology maturity and mapping to TRLs.
- **NPR 7120.5 (Space Flight Program and Project Management Requirements)**: Defines when TRL gate requirements apply at KDPs for space flight programs.
