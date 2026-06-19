# Chapter 26: 6.0 Crosscutting Technical Management

## Core Idea
Eight technical management processes (Technical Planning, Requirements Management, Interface Management, Technical Risk Management, Configuration Management, Technical Data Management, Technical Assessment, and Decision Analysis) form the structural backbone of the systems engineering engine, enabling integration of design activities and connecting project management to the technical team's execution.

## Frameworks Introduced
- **The Eight Crosscutting Technical Management Processes** (Processes 10–17 in the NASA SE Engine):
  - Process 10: Technical Planning
  - Process 11–17: Requirements Management, Interface Management, Technical Risk Management, Configuration Management, Technical Data Management, Technical Assessment, Decision Analysis
  - When to use: These processes operate concurrently across all lifecycle phases and are essential for any NASA project. They are not sequential — they run parallel to design processes and to each other, providing the governance and integration infrastructure.

**Note:** Section 6.0 is introductory/navigational; detailed process descriptions are in subsequent sections (6.1–6.8). This chapter establishes the conceptual foundation and management philosophy.

## Key Concepts
- **Crosscutting Technical Management**: The eight functions (beyond design processes) that enable a coherent, controlled, integrated technical program across all lifecycle phases — from concept through disposal.
- **SE Engine Integration**: Technical management processes are bridges between project management (budgets, schedules, contracts) and the technical team (design, analysis, realization).
- **Concurrent Execution**: Unlike sequential lifecycle phases, these processes occur simultaneously throughout the program and may overlap with any other process.
- **Indirection vs. Direct Involvement**: Not every team member directly executes technical management processes, but all team members depend on them (technical planning, requirements tracking, interface control, risk monitoring, configuration control, data governance, milestone assessment, and decision governance).
- **Product Lifecycle Scope**: Technical management applies from concept through disposal — spanning Pre-Phase A through program termination.
- **Design Solution Realization**: Without these eight processes, individual tasks cannot integrate into a functioning system that meets the Concept of Operations (ConOps) within cost, schedule, and risk constraints.

## Mental Models

**Think of technical management as the "glue"** — individual engineers execute design and analysis tasks (Chapters 4–5 processes); technical management ensures those tasks align, don't conflict, stay within scope, and are tracked to closure.

**Use early, extensive planning** — NASA emphasizes investing time upfront in technical planning (Pre-Phase A) to establish the product breakdown structure, schedule, resource constraints, and team role clarity. This foundation reduces rework downstream.

**Configuration control is leverage** — Once you control the baseline configuration, you can trace the impact of any change (design, requirement, environment) on all downstream analysis and verification work. Without it, you risk invalidating completed work without knowing it.

**Milestone reviews are checkpoints, not ceremonies** — Reviews should have explicit entrance criteria (design maturity, analysis completion, risk closure) and serve critical assessment, not just contractual box-checking. Poor entrance criteria lead to rework post-review.

## Anti-patterns
- **Insufficient upfront planning**: Postponing detailed technical planning until Mid-Phase A or Phase B forces reactive replanning and schedule slips. NASA stresses early, thorough planning in Pre-Phase A.
- **Uncontrolled requirements and interfaces**: Allowing requirements and interface definitions to drift without formal change control leads to incompatibilities, late discovery of design conflicts, and untracked scope creep.
- **Analysis without configuration control**: Running analysis against outdated or uncontrolled design baselines invalidates results without visibility. Invalidated analysis undermines verification and validation confidence.
- **Shallow milestone reviews**: Conducting reviews on schedule without entrance criteria met leads to rework and false progress signals. Reviews must assess actual technical readiness, not administrative compliance.
- **Ignoring biases, assumptions, and constraints in analysis**: Analysis results are only valid under specific assumptions. Failing to document and track these (e.g., operating environment, model fidelity, load cases) obscures when results become invalid after changes.

## Key Takeaways
1. **Technical management is not optional or secondary** — these eight processes enable the design team to function as an integrated system and provide project management with reliable technical status and risk visibility.
2. **Invest heavily in Pre-Phase A planning** — establish the team structure, technical breakdown, schedule, resource plan, and SEMP upfront. This planning is recursive and will be refined, but the early foundation is critical.
3. **Configuration control is mission-critical** — configuration and data management enable you to understand the impact of changes and track when previous analysis remains valid or must be reevaluated.
4. **Define interfaces explicitly and early** — all interfaces (intra-organizational and inter-organizational) must be identified, assigned to interface authorities, and managed through the lifecycle. Incompatibilities and transition processes must be explicit.
5. **Baseline analysis under configuration** — all technical analysis, trade studies, and models must be placed under configuration control so that changes (design, requirements, environment) can be traced and impact assessed.
6. **Conduct rigorous milestone reviews** — reviews with explicit entrance criteria (design maturity, analysis completion) provide critical assessment. Reviews conducted without entrance criteria met are waste and hide real issues.
7. **Every team member depends on these eight processes, directly or indirectly** — even if not all team members actively participate in requirements management or risk assessment, they rely on these functions to keep the program coherent and controlled.

## Connects To
- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: Defines the 17 common technical processes, of which 8 are crosscutting management processes. This handbook translates NPR 7123.1 into detailed NASA guidance.
- **ISO/IEC/IEEE 15288 (Systems and software engineering – System and software engineering lifecycle processes)**: Defines equivalent lifecycle and technical management processes in a standards-neutral language. NASA's eight processes map to or extend ISO 15288 categories.
- **Project Management Institute (PMI) / PMBOK**: Technical management processes bridge NASA's design-focused SE engine to traditional project management (scope, schedule, budget, risk). The two are interdependent but operate on different planes.
- **NASA NPR Documents (e.g., NPR 8705.2B – Safety and Mission Assurance Processes and Requirements)**: Technical management processes (especially Technical Risk Management and Technical Assessment) must integrate with SMA requirements and processes.

---

**Scope of This Section**: Section 6.0 establishes the conceptual foundation and role of the eight technical management processes. Sections 6.1–6.8 (subsequent chapters in this handbook) provide detailed process descriptions, inputs, activities, and outputs for each of the eight.
