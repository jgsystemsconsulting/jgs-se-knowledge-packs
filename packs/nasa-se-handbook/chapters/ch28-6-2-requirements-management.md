# Chapter 28: 6.2 Requirements Management

## Core Idea
Requirements Management applies systematic control, decomposition, and bidirectional traceability to all stakeholder expectations, customer requirements, and technical product requirements throughout the system lifecycle, from the highest level down to component-level allocations.

## Frameworks Introduced
- **Requirements Management Process**: A systematic process for identifying, controlling, decomposing, and allocating requirements across all WBS levels while maintaining bidirectional traceability and managing baseline changes over the product lifecycle.
  - When to use: Throughout all project phases (Phase A through operations) to govern how expectations and requirements flow from stakeholder and customer sources down through technical allocations, and how changes to established baselines are evaluated and approved.
  - **INPUTS**: Expectations and requirements from Stakeholder Expectations Definition and Technical Requirements Definition Processes; requirement change requests; TPM estimation/evaluation results; Product Verification and Validation results.
  - **KEY ACTIVITIES**: (1) Prepare and organize hierarchical requirement structures; (2) Maintain bidirectional traceability as each requirement is documented, traced to parent sources, and evaluated for completeness; (3) Manage changes to established baselines through impact assessment and Configuration Control Board (CCB) approval; (4) Ensure consistency between requirements, ConOps, and architecture/design; (5) Capture rationale and disposition for all changes.
  - **OUTPUTS**: Requirements Documents (baselined in requirements management tools); Approved Changes to Requirements Baselines; bidirectional traceability matrices; work product records and change disposition reports.

## Key Concepts
- **Traceability**: A discernible association between two or more logical entities (requirements, system elements, verifications, or tasks) that documents their relationships within the requirements hierarchy.
- **Bidirectional Traceability**: The ability to trace any given requirement or expectation both upward to its parent requirement/expectation and downward to its allocated children requirements/expectations, ensuring complete coverage and no orphaned requirements.
- **Requirements Baseline**: A formally reviewed, approved, and configuration-controlled set of requirements placed under formal configuration management (typically after System Requirements Review in late Phase A), against which changes are formally evaluated.
- **Requirements Creep**: The subtle, imperceptible growth of requirement scope during the project lifecycle, often involving innocent incremental changes that collectively result in a system more expensive and complex than originally intended.
- **Configuration Control Board (CCB)**: Organizational body (typically including systems engineer, project manager, and key engineers) that reviews and approves all changes to baselined requirements after Phase A, assessing impacts on cost, performance, schedule, and safety.
- **Requirements Matrix / Traceability Matrix**: A systematic record (usually maintained in a requirements management tool) that documents the relationships between requirements at different levels, their allocation to design/test artifacts, and their verification methods.
- **Self-Derived Requirement**: A requirement locally adopted as a good practice or result of design decisions during Logical Decomposition or Design Solution Processes, traced only to design rationale rather than a parent requirement.
- **Performance Margins**: Quantified buffers (e.g., propellant margin, power budget) used as a tool to assess whether requirement change requests will exceed system resource constraints.

## Mental Models
- **Trace forward then backward**: When a new requirement is added, first trace it backward to verify it has a parent source or is a valid self-derived requirement; then trace forward to ensure all top-level parent requirements are fully allocated downward with no gaps.
- **Think of the Requirements Management Process as lifecycle governance for scope**: It operates in three phases: (1) early definition and organization (Phase A — frequent changes, learning), (2) baseline and formal control (post-SRR — all changes require CCB approval), (3) late design and integration (Phase B–C — changes become costly, scrutiny intensifies). Different approval mechanisms and rigor apply at each phase.
- **Use the impact assessment tripod**: Before approving any requirement change, evaluate it against three axes: cost/schedule impact, technical impact (interfaces, design, ConOps), and risk landscape. If the change cannot fit within resource margins and risk reserves, it should be denied.

## Anti-patterns
- **Gold-plating without parent traceability**: Adding requirements that have no parent source and are not formally approved self-derived requirements. These "orphaned" requirements should be audited out or traced to a legitimate source.
- **Uncontrolled change acceptance during Phase B and C**: Treating post-baseline changes casually without rigorous CCB review. Late changes have exponential cost and schedule impact; treating them like early-phase changes is a primary cause of project overruns.
- **Traceability in name only**: Maintaining a traceability matrix that is not updated when requirements change, or updating it without verifying that the logical relationships remain sound. A stale matrix is worse than no matrix.
- **Ignoring true evolution while defending against creep**: Dismissing legitimate new requirements (e.g., from external stakeholder changes) as creep and refusing to evaluate them formally. Valid evolution must be distinguished from undisciplined scope growth; both should go through the formal change process.

## Key Takeaways
1. **Establish bidirectional traceability from the start**: As each requirement is documented during definition, immediately record its parent source and initiate traceability upward and downward. Traceability added retroactively is incomplete and unreliable.
2. **Baseline at SRR, not before**: Until late Phase A System Requirements Review, allow requirements to mature through iteration and evaluation. Post-SRR, place all requirements under formal configuration control and route all changes through the CCB.
3. **Assess change impact systematically using the CCB tripod**: Cost/schedule, technical impact, and risk landscape must all be evaluated before approval. A single requirement change can have far-reaching ripple effects across the system.
4. **Fight requirements creep with a coherent ConOps and formal change channels**: A well-agreed ConOps signed off by customer and stakeholders is the first line of defense. Combined with formal change-request channels and resource-margin enforcement, this prevents undisciplined scope growth while allowing legitimate evolution.
5. **Self-derived requirements are valid but must be justified**: Design-driven or good-practice-based requirements (e.g., "add fail-safe redundancy") are acceptable if concurrence is sought from next-level stakeholders and design rationale is documented. Do not confuse them with orphaned requirements.
6. **Tool selection and database organization matter**: For small projects, spreadsheets suffice; for larger efforts, a requirements management tool (with attributes for traceability, allocation, verification method/level/phase, and bidirectional links) is mandatory. Database organization has lifecycle-long consequences on team visibility and impact assessment.
7. **Keep requirements, ConOps, and architecture in sync**: Maintain consistency between three artifacts throughout the lifecycle; use change evaluation as an opportunity to initiate corrective actions if inconsistencies are detected.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems and software engineering — System and software engineering — Life cycle processes)**: NASA's Requirements Management Process operationalizes the Requirements Development and Requirements Management activities defined in 15288.
- **Technical Requirements Definition Process (Section 6.1)**: This upstream process generates the requirements that Requirements Management then controls and traces.
- **Configuration Management Process (Section 6.5)**: Post-baseline requirement changes flow through Configuration Management; baseline establishment and change approval are joint responsibilities.
- **Stakeholder Expectations Definition Process and Technical Assessment Process**: Sources for requirement change requests and TPM evaluation results that feed into Requirements Management decision-making.
- **Product Verification and Product Validation Processes**: Verification and validation results must be mapped into the requirements database; traceability between requirements and test plans is a critical output of Requirements Management.
- **System Requirements Review (SRR) and design-review gate**: Requirements Management culminates in SRR (late Phase A), at which point validated requirements are baselined and formal configuration control is imposed for all subsequent changes.
