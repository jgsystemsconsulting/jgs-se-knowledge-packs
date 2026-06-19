# Chapter 3: Overview of the System Safety Framework

## Core Idea
Chapter 3 presents the NASA system safety framework as four interlocking elements — requirement setting, safety ensurance, safety assurance, and risk acceptance — and maps how Acquirers and Providers interact across the system life cycle through RISC development and evaluation.

## Frameworks Introduced
- **NASA System Safety Framework**: Four-element structured model (requirement setting → safety ensurance → RISC development → RISC evaluation/risk acceptance) that organises all safety activities.
  - When to use: As the governing organising structure for any NASA program or project requiring system safety.
- **Operational Safety Objectives Tree**: A hierarchical decomposition of the two fundamental safety principles (minimum tolerable level + ASARP) into specific, systems-engineering-addressable objectives.
  - When to use: To translate high-level policy into verifiable requirements and traceable RISC claims.
- **Safety Performance Margin Profile**: A decreasing margin applied to the safety threshold/goal over time to set the analytic requirement for known risks; accounts for UU scenarios diminishing as experience accumulates.
  - When to use: When setting probabilistic safety requirements for a system expected to mature through operational experience.

## Key Concepts
- **Safety Ensurance**: Provider activity; reducing and eliminating hazards through design, fabrication, and operation to achieve adequate safety performance.
- **Safety Assurance**: Acquirer activity; developing confidence that safety has been sufficiently ensured to justify risk acceptance.
- **Integrated Safety Analysis (ISA)**: Scenario-based, system-level analysis consolidating HA, PRA, and phenomenological modeling; the central analytical engine for risk-informing all design and operational decisions.
- **Safety-Critical Items (SCIs)**: Elements or attributes (hardware, software, interfaces, procedures, management practices) that must function for the RISC to be valid; identified top-down from the ISA, broader than MIL-STD-882E definition.
- **Risk Drivers**: SCIs that are also significant contributors to safety performance risk (high failure probability combined with critical consequence); a smaller, cost-focused subset of SCIs used when safety concerns involve loss of equipment/mission rather than harm to humans.
- **Allocated Requirements**: Quantitative requirements apportioned from system level to lower levels, same units of measure preserved.
- **Derived Requirements**: Qualitative or quantitative requirements developed at a lower level to implement a higher-level requirement; arise from constraints and design choices.
- **Requirement Tailoring**: Adjusting or seeking relief from a levied requirement; winnowing best practices to those specifically relevant to the mission; produces deviations and waivers.
- **System Safety Requirements Analysis (SSRA)**: Early Provider activity clarifying the detailed requirements to be addressed in development; serves as the Acquirer-Provider handshake on requirement scope and feasibility.
- **Key Decision Points (KDPs)**: System life-cycle milestones at which the Acquirer makes risk acceptance decisions informed by the RISC.

## Mental Models
- Use ISA as the central integration point: design support, SCI designation, requirement allocation, performance monitoring, and RISC evidence all flow from or through the ISA.
- Use the ISA → SCI → RISC chain: the ISA identifies SCIs; managing SCIs gives the RISC its claims; evaluating those claims gives the Acquirer confidence.
- Use a decreasing safety performance margin profile to set time-varying analytic requirements: subtract margin from threshold/goal to get the requirement against which PRA results are compared; as UU risks are discovered and corrected, the margin shrinks and the requirement tightens.
- Use the Acquirer-Provider table (Table 3-1 / 3-2) to structure interaction at each KDP: requirements flow down via SSRA; evidence flows up via RISC; disputes are resolved via negotiated Memoranda of Understanding.

## Anti-patterns
- **Bottom-up SCI derivation only**: Using FMEA exclusively to build the critical items list misses SCIs arising from system-level management practices, interfaces, and organisational factors that are only visible from a top-down ISA perspective.
- **Static RISC**: Treating the RISC as a one-time document rather than a living argument updated at each KDP; a static RISC cannot support incremental risk acceptance or reflect evolving operational experience.
- **Blanket imposition of historical requirements**: Levying all historical engineering requirements without ASARP tailoring can over-constrain novel systems and produce sub-optimal safety outcomes.

## Key Takeaways
1. The framework assigns clear roles: the Acquirer sets requirements and evaluates; the Provider ensures safety and develops the RISC. Both must collaborate continuously.
2. ISA is the system safety engine: everything else — SCIs, requirements, RISC claims, design trades — is risk-informed by it.
3. Safety performance margins are programmatic reserves analogous to mass margins; their magnitude derives from historical experience with UU risk ratios, not from engineering judgement alone.
4. System safety must begin early in the life cycle; late involvement reduces the leverage available to influence design and increases cost of correction.
5. Risk acceptance is RISC-informed but not RISC-based; the decision maker retains authority to accept or reject safety risk regardless of RISC evaluation findings.
6. Organisational and managerial factors are crosscutting SCIs; the framework explicitly requires them to be addressed in the RISC, not just hardware and software items.

## Connects To
- **NPR 7123.1B**: The Technical Requirements Definition Process governs safety requirements development; SE common technical processes house the ensurance activities.
- **NPR 8000.4A**: Continuous Risk Management (CRM) takes over once the RISC baseline is accepted; assurance deficits convert to risk statements managed under CRM.
- **NASA-STD-7009 (M&S Standard)**: Credibility Assessment Scale (CAS) factors govern the validity of analytical models used in the ISA.
