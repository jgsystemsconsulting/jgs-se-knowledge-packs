# Chapter 13: 3.6 Project Phase C: Final Design and Fabrication

## Core Idea
Phase C transforms preliminary designs into complete, detailed designs and produces the actual hardware and software products. It is the bridge between design validation (Phase B) and integration/test (Phase D), where planning is converted into production readiness.

## Frameworks Introduced
- **Detailed Design Documentation & Data Package**: Fully mature and document hardware and software designs at all levels of the system hierarchy, with supporting trade studies, development testing results, and lower-level specifications integrated into the system architecture.
  - When to use: Throughout Phase C to establish the product baseline and create the foundation for fabrication and coding.

- **Design Review Sequence (Hierarchical CDRs)**: System-level CDR and component-level CDRs, sequenced from lower-level reviews to system-level, with each end item reviewed prior to fabrication/production.
  - When to use: To gate each major design commitment before tooling, manufacturing ramp-up, or software development begins; tailor sequencing to project integration strategy.

- **Production Readiness Review (PRR)**: Validation that production plans, facilities, and personnel are ready to execute manufacturing at scale (if applicable).
  - When to use: When a product will be produced in quantity; PRR precedes or is held in parallel with fabrication start.

- **Configuration Management & Change Control**: Ongoing tracking of design changes as detailed interfaces are defined, preventing scope creep and maintaining baseline integrity.
  - When to use: At each step of design refinement to capture decisions and prevent conflicting changes across subsystems.

## Key Concepts
- **Product Baseline**: The complete, detailed design of all system end products, approved through CDR, ready for fabrication or coding.
- **Detailed Design Specification**: Fully mature designs that add remaining lower-level design specifications to the system architecture and include all interface definitions.
- **Hierarchical Design Review**: A cascading sequence of CDRs—system-level and subsystem/component-level—reflecting the integration structure planned for Phase D.
- **Development Testing (Component/Subsystem Level)**: Engineering test units resembling actual hardware, tested to establish confidence that designs will function in expected environments before full production.
- **Trade Study Archival**: Documented trade study results validating the final design against project goals, objectives, and Concept of Operations (ConOps).
- **Manufacturing Process & Controls Definition**: Establishment of production plans, tooling, assembly procedures, and quality controls to ensure repeatable, compliant fabrication.
- **Systems Engineer as Integration Authority**: The systems engineer ensures final designs of various system components will work together, are compatible, and meet customer expectations and applicable requirements.
- **Safety Data Package & Security Plan**: Finalized documentation of safety-critical design features, hazard analyses, and security measures.

## Mental Models
- **Think of Phase C as "build the master plan before building the product."** All interfaces must be defined, all trade-offs documented, and all manufacturing feasibility confirmed before fabric/code production begins; Phase C is the last opportunity to correct design flaws at reasonable cost.
- **Use hierarchical CDRs as a gating mechanism.** Lower-level CDRs review subsystem readiness; system-level CDR confirms integration compatibility. Tailor the sequence to match how components will be assembled in Phase D.
- **Recognize design maturity as a series of successive refinements.** Phase C is not a single "freeze the design" moment; rather, configurations are progressively controlled and baselined as design evolves from preliminary to detailed, with each refinement tied to corresponding verification and integration planning.
- **Monitor technical parameters, schedules, and budgets closely to catch undesirable trends early.** Unexpected growth in mass, cost overruns, or schedule slippage must be recognized and corrected in Phase C, not discovered in Phase D or later.

## Key Takeaways
1. **Phase C completes detailed design at all levels of hierarchy before fabrication/coding begins.** Hardware design, software specifications, and subsystem interfaces must be fully documented and baselined through CDR before production starts.
2. **Trade studies continue through Phase C and their results validate the design against project ConOps and goals.** Maintain discipline in archiving and approving trade study outcomes to inform design decisions and risk mitigation.
3. **Develop and baseline integration, verification, and validation plans in detail during Phase C.** These plans are implemented in Phase D; having them mature and agreed upon reduces rework and test failures later.
4. **Human factors and operational readiness are verified in Phase C through human subjects representing the user population.** Evaluate design usability, maintenance procedures, training effectiveness, and interfaces with early participation of actual users.
5. **Manufacturing and assembly processes, controls, and facilities must be defined and validated in Phase C.** If production is planned, PRR confirms readiness; if single-unit builds, manufacturing procedures must still be documented and feasible.
6. **Systems engineers act as integration authority and design arbiter throughout Phase C.** Ensure subsystem designs are compatible, interfaces are fully defined, and no latent integration conflicts exist before Phase D assembly begins.
7. **Configuration management and change control must remain disciplined.** Uncontrolled design changes at this stage can invalidate prior analyses, increase cost, and delay the program; every change must be traced, approved, and reflected in documentation.

## Connects To
- **NASA Systems Engineering Handbook (Phase B, Phase D)**: Phase C is the detailed execution of planning laid out in Phase A and refined in Phase B; outputs become the baseline for Phase D assembly, integration, and test.
- **NPR 7120.5 (NASA Program and Project Management Requirements)**: Phase C technical activities and review entrance/success criteria are defined by this policy.
- **NPR 7123.1 (NASA Systems Safety Policy)**: Safety reviews and safety data package finalization occur in Phase C; documented hazard controls and mitigations must meet this policy.
- **ISO/IEC/IEEE 15288 (System and Software Engineering — System and Software Life Cycle Processes)**: Phase C aligns with the design phase and production phase of the standard; detailed design, verification planning, and design review activities are core to this standard.
- **Configuration Management (IEEE EIA 649 or equivalent)**: Baseline control and change management discipline are essential in Phase C to maintain product integrity as designs are finalized.
