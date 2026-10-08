# Chapter 5: 2.6 Human Systems Integration (HSI) in the SE Process

## Core Idea

Human Systems Integration (HSI) maps human-element considerations into the full systems engineering lifecycle—Requirements Definition, Stakeholder Expectations, Logical Decomposition, Design Realization, and all other SE processes—with the same systematic rigor applied to hardware and software, ensuring human operators and maintainers are designed-in from the start, not retrofitted after.

## Frameworks Introduced

- **HSI Plan (as part of SEMP)**: A documented programmatic approach to HSI integration, either embedded in the Systems Engineering Management Plan or as a standalone subset.
  - When to use: Early in the program/project lifecycle to establish HSI goals, metrics, standards, deliverables, processes, roles, and responsibilities. Updated continuously through the program lifecycle.

## Key Concepts

- **Human Systems Integration (HSI)**: Systematic consideration of human elements (operators, maintainers, support personnel) alongside technical systems throughout requirements definition, design, and realization.
- **HSI Plan**: A formalized document describing planned HSI goals, metrics, standards, deliverables, processes, and the roles/responsibilities of parties responsible for HSI implementation.
- **Stakeholder Expectations**: User and operator needs, constraints, and acceptance criteria that feed into the HSI process.
- **Requirements Definition (HSI context)**: Translation of human operational and maintenance needs into technical requirements (e.g., ergonomic, cognitive load, training demands).
- **Logical Decomposition (HSI context)**: Allocation of human responsibilities and interfaces across system hierarchy layers.
- **Design Realization (HSI context)**: Embodiment of human-centered design decisions—control layouts, feedback mechanisms, maintainability features, usability considerations.
- **System Integrators (HSI-skilled)**: Technical leads responsible for managing HSI implementation, with explicit competency in human-element design and development.
- **Measures of Effectiveness (MOEs)**: High-level metrics capturing whether the system meets stakeholder/human operator mission goals.
- **Technical Performance Measures (TPMs)**: Lower-level metrics tracking human-relevant performance (e.g., operator reaction time, maintenance downtime, training time).

## Mental Models

- **Think of HSI as a design constraint like thermal or power budget**: HSI considerations (operator workload, cognitive demands, maintainability, ergonomics) are engineering constraints that must be flowed down from top-level requirements into lower-level design decisions—not optional add-ons tested at the end.
- **Use HSI when defining interfaces between humans and systems**: Any point where an operator, maintainer, or support person interacts with hardware or software is an HSI touchpoint requiring explicit design and validation against human capability and training.

## Key Takeaways

1. **Plan HSI early**: Develop an HSI Plan at program start and baseline it in the SEMP (or as a companion document). Do not defer HSI to later phases—operator needs drive requirement-level decisions.

2. **HSI is crosscutting, not a separate specialty**: Human elements are mapped into every SE process—stakeholder expectations elicitation, requirements definition, decomposition, design, realization, and verification—just as hardware and software considerations are.

3. **Assign HSI responsibility and expertise**: Designate system integrators with explicit HSI training and human-factors knowledge to own HSI implementation. This avoids accidental omission and ensures continuity across the lifecycle.

4. **Keep the HSI Plan current**: Update the plan throughout the program/project lifecycle as requirements evolve, design solutions mature, and human factors discoveries emerge.

5. **Define HSI success metrics from the start**: Establish quantitative and qualitative measures (MOEs, MOPs, TPMs) tied to operator effectiveness, training efficiency, and maintenance burden to drive design trade decisions.

## Connects To

- **Section 7.9 (Human Systems Integration in the SE Process)**: Detailed treatment of HSI as a crosscutting topic in the Crosscutting Topics chapter; provides extended guidance beyond this overview.
- **Requirements Definition (2.1)** and **Stakeholder Expectations**: HSI feeds into—and is fed by—the initial elicitation of human operator and maintainer needs.
- **Design Realization (2.3)** and **Product Verification (2.5)**: HSI constraints drive design solutions and must be validated against human performance requirements.
- **NPRs (NASA Procedural Requirements)**: Governance and compliance frameworks for HSI planning and execution.
