# Chapter 17: 4.1 Stakeholder Expectations Definition

## Core Idea
Defining stakeholder expectations is the foundational systems engineering activity that clarifies what the customer, users, and other key stakeholders actually want the system to accomplish; this mutual agreement prevents requirements creep and ensures all parties work toward the same goals from the outset.

## Frameworks Introduced
- **Needs, Goals, and Objectives (NGOs)**: A three-tier elicitation and traceability mechanism that translates stakeholder desires into clear, measurable targets without prescribing solutions.
  - When to use: During early concept phases (Pre-Phase A, Phase A) to establish baseline understanding before requirements are written and locked.
- **Concept of Operations (ConOps)**: A narrative and visual description of how the system will be operated to achieve mission objectives, including nominal and off-nominal scenarios, operational phases, timelines, staffing, and logistics.
  - When to use: Early phases to validate stakeholder understanding and inform both technical requirements and long-term cost/operations planning; revisited at each life-cycle phase as new stakeholders join.
- **Measures of Effectiveness (MOEs)**: Stakeholder-centric success criteria that define what constitutes mission success and how well key objectives must be accomplished.
  - When to use: Developed alongside NGOs to translate stakeholder expectations into evaluable success metrics.
- **Space Asset Protection (SAP) Analysis**: Threat-susceptibility-vulnerability fusion framework (threat × susceptibility = vulnerability) integrated into early design to address congested, contested, and competitive space environments.
  - When to use: All NASA projects; extracted viable threats are documented in a Program/Project Protection Plan (PPP) and iterated at each Key Decision Point (KDP).

## Key Concepts
- **Stakeholder**: Any party with vested interest in the system's success, including customers, end users, operators, maintainers, regulators, and organizations with strategic or programmatic stakes; requires identification throughout all life-cycle phases.
- **Need**: A singular problem statement that drives all downstream work; should relate to the problem the system solves without prescribing the solution.
- **Goal**: An elaboration of the need that establishes critical expectations; need not be quantitative but must allow assessment of whether the system achieved them.
- **Objective**: Specific, measurable target levels of system outputs; must be aggressive but attainable, results-oriented (what, not how), and verifiable before requirements are contractually binding.
- **Constraint**: A condition that must be met; typically cannot be changed through trade studies and may stem from orbital mechanics, regulatory restrictions, budget, or existing systems that must be utilized.
- **Design Driver**: Key technical parameters (e.g., launch date, orbit, mission duration, operational configuration) that strongly influence architecture and design choices, rooted in the ConOps.
- **Concept of Operations (ConOps)**: An operational perspective on system behavior and lifecycle that avoids prescribing implementation (the "what," not the "how") and includes scenarios for nominal and off-nominal situations, critical events, and resource allocation.
- **Measure of Effectiveness (MOE)**: A stakeholder-centric success metric (e.g., mission success criteria for science, exploration, or technology demonstration missions); synonymous with project success criteria.
- **Design Reference Mission (DRM)**: A time-sequenced scenario or use case, typically part of the ConOps, that demonstrates how the system will accomplish mission objectives under specific operational conditions.
- **Protection Threat**: Any natural or man-made event, accident, or system with the ability to exploit a susceptibility and cause damage, degradation, destruction, or denial of service.

## Mental Models
- **Think of NGOs as a roadmap that avoids getting lost.** Needs answer "What problem are we solving?"; goals answer "What must we do?"; objectives answer "How well must we do it?" This traceability ensures every requirement traces back to a stakeholder expectation, preventing orphaned or conflicting requirements.
- **Use ConOps as a time-sequenced walk-through of the system's life.** Walk through the mission timeline—from ground integration through launch, deployment, operations, anomaly response, and disposal—to identify requirements and staffing that might otherwise be overlooked (e.g., a communication antenna needed during a specific mission phase).
- **Think of Measures of Effectiveness as the metric your customer uses to grade you.** If the MOE is not met, the stakeholder considers the mission unsuccessful, regardless of technical compliance. MOEs are the bridge between aspirational NGOs and contractual requirements.
- **Vulnerability = Threat × Susceptibility.** Space asset protection is not a separate discipline—it is a fundamental design driver. Identify inherent design weaknesses early and match them against credible threats to determine protection strategies before the system is built.

## Anti-patterns
- **Developing requirements before stakeholder expectations are baselined**: Requirements become disjointed, trace to nothing coherent, and fail to reflect the actual problem the customer needs solved.
- **Treating ConOps as an optional document**: ConOps skipped or developed late reveals critical requirements and staffing needs after design is locked, necessitating costly rework or cost overruns.
- **Neglecting off-nominal scenarios and anomaly response**: Nominal-only ConOps leaves the system unprepared for realistic operations; safe-hold modes, fault management, and anomaly resolution must be explicitly designed and exercised.
- **Writing objectives with "TBD" and deferring decisions**: Objectives must be feasible before requirements are written; unresolved TBDs indicate that the problem is not yet understood and will propagate uncertainty downstream.
- **Overlooking non-obvious stakeholders early**: Space asset protection, human systems integration, quality assurance, and reliability communities often surface late; discovering their expectations after design has locked in is expensive.
- **Losing the business view in Concept of Operations**: ConOps driven solely by technical considerations miss long-term operational staffing, logistics costs, and maintenance strategies; the ConOps must be developed with strategic, cost-conscious intent.

## Key Takeaways
1. **Stakeholder expectations are the foundation of all systems engineering work.** Thoroughly understanding and documenting what the customer and key stakeholders actually need—and achieving mutual agreement—is non-negotiable; it prevents the majority of downstream rework and requirements creep.
2. **Use Needs, Goals, and Objectives to establish bidirectional traceability from problem to objectives.** A well-structured NGO set ensures that every objective traces to a goal, every goal to a need, and later that every requirement and function traces back to an NGO. This prevents orphaned requirements and ensures the team is delivering what is needed.
3. **Develop a Concept of Operations early and iteratively refine it with stakeholders.** Walk through nominal and off-nominal scenarios, timelines, operational phases, staffing, and logistics to catch hidden requirements and validate stakeholder understanding before design locks. Revisit ConOps at each life-cycle phase as new stakeholders (contractors, operators, maintainers) join the project.
4. **Measures of Effectiveness are your customer's definition of success.** Develop MOEs alongside stakeholder expectations to ensure the team's success metrics align with stakeholder expectations. If an MOE is not met, the mission is unsuccessful in the customer's eyes, regardless of technical compliance.
5. **Space asset protection is a systems engineering function, not an afterthought.** Integrate threat analysis and vulnerability assessment early; use the threat × susceptibility = vulnerability framework to identify protection strategies before the design is finalized. Document viable threats and protection strategies in a Program/Project Protection Plan (PPP) and iterate at each KDP.
6. **Identify and engage all stakeholders early and throughout the lifecycle.** New stakeholders emerge in every phase (contractors in B–C, assembly/test/operations in D–E, archivists/disposal teams in F). Revisit stakeholder expectations with each wave of participants to ensure alignment and capture emerging requirements (e.g., operational procedures, training, logistics expectations).
7. **Validate stakeholder expectations through formal or informal concept reviews before baselining.** Concept reviews (scaled to project complexity) present NGOs, MOEs, and ConOps for discussion and refinement. Obtaining signatures or formal commitment from both customer and technical team ensures both parties are accountable to the agreed-upon baseline.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering—System Lifecycle Processes)**: Stakeholder Expectations Definition is the elicitation and requirements origin phase of ISO 15288 lifecycle processes; the NGO and ConOps outputs feed directly into ISO 15288 technical review gates (SDL—System Design and Lifecycle).
- **NASA NPR 7120.5 (NASA Program and Project Management Requirements)**: Mandates the integration of space asset protection requirements and the Program/Project Protection Plan (PPP) as part of project planning; Stakeholder Expectations Definition is the vehicle for capturing viable threats and protection strategies.
- **SysML and Systems Engineering Standards (e.g., IEEE 1220)**: Stakeholder expectations and NGOs form the input to SysML requirement models; traceability between stakeholder expectations and requirements is a core tenet of model-based systems engineering.
- **Human Systems Integration and Crew Operations**: Stakeholder expectations must explicitly include human operator roles, responsibilities, training goals, and staffing levels; ConOps allocation between humans and systems is a critical design driver, especially for crewed missions.
