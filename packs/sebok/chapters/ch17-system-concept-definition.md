# Chapter 17: System Concept Definition

## Core Idea
System Concept Definition is the set of systems engineering activities where the problem space, stakeholder needs, and business/mission objectives are closely examined before any formal system-of-interest (SoI) definition. It answers the "why" and "what" before determining "how."

## Frameworks Introduced
- **Business or Mission Analysis**: Strategic analysis that identifies the problem, threat, or opportunity, establishes mission/goals/objectives (MGOs), measures of success, and explores candidate solution classes. When to use: at project inception to understand organizational strategic drivers and business context.
- **Stakeholder Needs Definition**: The process of identifying and documenting an integrated set of needs from major stakeholders, grounded in life cycle concepts, drivers, constraints, and risk mitigation. When to use: after business analysis is clarified to capture what stakeholders require the SoI to accomplish.
- **Mission-Goals-Objectives (MGOs) Hierarchy**: A structured decomposition where the mission statement answers "why," goals break the mission into achievable pieces, and objectives provide concrete details on what must be done. When to use: to establish clear strategic intent and create shared understanding across the project team.
- **Stakeholder Register**: A documented list of stakeholders with key information about each and their involvement with the SoI, updated throughout the project lifecycle. When to use: to track stakeholder engagement and ensure no critical voices are missed during elicitation.
- **Life Cycle Concepts Analysis**: Concurrent architectural and behavioral modeling that matures preliminary solution concepts and ensures consistency, correctness, completeness, and feasibility. When to use: to validate that the problem definition and proposed solutions are technically sound and aligned.

## Key Concepts
- **Problem/Threat/Opportunity Statement**: Clear articulation of why the SoI is needed—the organizational strategic driver that authorizes the project.
- **Measures of Effectiveness (MOE)**: Quantitative metrics used to validate the SoI against objectives and manage development across the lifecycle.
- **Integrated Set of Needs**: A consolidated list of stakeholder needs reflecting feasible system life cycle concepts, drivers, constraints, and risk mitigation—the direct input to System Requirements Definition.
- **Green-field System**: Development starting with a blank slate, requiring as-is/to-be characterization of the problem space.
- **Brown-field System**: Evolution of an existing system where legacy data and the current state serve as inputs for analysis.
- **Drivers and Constraints**: External factors (standards, regulations, environment, technology maturity, budget, schedule, human factors) that bound the solution space and are identified concurrently with stakeholder elicitation.
- **Life Cycle Stakeholder Engagement**: Identification of stakeholder roles across all lifecycle stages (validation, logistics, operation, disposal) to ensure needs address the complete lifecycle, not just initial implementation.
- **Approving Authorities**: Stakeholders with formal responsibility for certifying, qualifying, and approving the system for operational use—often overlooked but critical.

## Mental Models
- **Use push vs. pull paradigm to frame the problem**: Pull paradigm solves an identified gap (e.g., missing defense capability); push paradigm creates a solution to seize an opportunity (e.g., anticipated market). Most systems combine both; understand which drives your problem definition.
- **Think of concept definition as concurrent, not sequential**: Business analysis and stakeholder needs definition occur side-by-side with early architecture exploration. Problems and solutions inform each other; neither can be locked independently.
- **View needs as the bridge, not the destination**: Needs statements capture what stakeholders require without prescribing implementation. They answer "what the SoI must do" (not "how to do it"); requirements come later and introduce technical constraints.

## Key Takeaways
1. **Concept definition answers "why" and "what" before "how"**: The problem, mission, and needs must be clear and agreed before architectural or design decisions. Rushing this phase leads to building the wrong system.
2. **Approving authorities often differ from customers**: Identify regulators, safety personnel, and external certifiers early—they have veto power over deployment and must be engaged as stakeholders.
3. **Life cycle perspective is mandatory, not optional**: Stakeholder needs span validation, logistics, operation, and disposal. A system optimized only for initial use will fail in maintenance and end-of-life.
4. **Drivers and constraints shrink the solution space**: External regulations, existing technology, budget, and schedule are not negotiable wish-lists; they are hard boundaries on what is feasible. Identify them upfront.
5. **Needs require rationale and prioritization**: Ask "why" for every need and classify it (critical vs. nice-to-have). Rationale often reveals the real need hiding behind an implementation suggestion.
6. **Models (MBSE) ensure completeness and consistency**: Architectural and behavioral models catch interdependencies and omissions that textual needs lists miss. Use them to mature life cycle concepts and validate feasibility.
7. **Traceability chains the entire lifecycle**: Every need must trace to its source (stakeholder, MGO, risk, driver); every requirement must trace back to a need; every design element must trace to a requirement. Broken chains signal incomplete analysis.

## Connects To
- **ISO/IEC/IEEE 15288 Architecture Definition process**: System Concept Definition feeds directly into this process; the mature life cycle concepts from concept definition guide architectural decomposition.
- **ISO/IEC/IEEE 29148 (Requirements Engineering)**: The integrated set of needs defined here is the input that System Requirements Definition transforms into design input requirements.
- **System Requirements Definition**: Concept definition outputs (needs, drivers, life cycle concepts, risk mitigations) are the raw material for writing and allocating system requirements.
- **Risk Management**: Risks identified during concept definition drive the definition of mitigation concepts and safety/security requirements in later stages.
- **Configuration Management**: The baseline established in concept definition (problem statement, MGOs, needs, approved solution classes) must be under configuration control to track scope creep.
- **INCOSE Needs and Requirements Manual (NRM)**: Canonical reference for needs elicitation techniques, stakeholder registers, and traceability structures.
