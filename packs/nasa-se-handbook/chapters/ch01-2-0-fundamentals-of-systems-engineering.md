# Chapter 1: 2.0 Fundamentals of Systems Engineering

## Core Idea
Systems engineering is the discipline of balancing multiple disciplines, conflicting constraints, and opposing interests to produce a coherent design that meets both organizational goals and stakeholder expectations, with the systems engineer serving as the orchestrator who maintains the "big picture" view while preventing any single discipline from dominating the solution.

## Frameworks Introduced
- **The SE Engine (NPR 7123.1)**: A graphical model organizing 17 common technical processes across three categories—system design (4 processes), product realization (5 processes), and technical management (8 crosscutting tools)—that flow together to develop and realize end products from concept through completion.
  - When to use: As the organizing framework for all NASA systems engineering projects; processes 1–9 are executed in sequence per project phase, while processes 10–17 provide crosscutting support throughout.

- **System Design Processes (4 processes)**: Define and baseline stakeholder expectations → generate and baseline technical requirements → decompose requirements into logical/behavioral models → convert requirements into a design solution that satisfies baselined stakeholder expectations.
  - When to use: From project kickoff through architectural definition; applied recursively to each product in the system structure from top to bottom until the lowest-level products are defined to the point they can be built, bought, or reused.

## Key Concepts
- **Stakeholder Expectations**: The operational and business needs expressed by customers and other stakeholders; form the starting point for the systems engineering process and must be baselined to prevent scope creep.
- **Technical Requirements**: Derived from stakeholder expectations; specify what the system must do (functional) and how well (performance, quality, safety); are baselined after definition and serve as the contract between design and validation.
- **Systems Engineer (Role)**: A skilled engineer who identifies and focuses efforts on assessments to optimize the overall design without favoring one system/subsystem over another; balances organizational, cost, and technical interactions; may hold titles such as lead systems engineer, technical manager, or chief engineer.
- **System Architecture**: The logical and behavioral decomposition of requirements that defines system structure and shows how components interact; developed by the systems engineer in close collaboration with the technical team.
- **Design Tradeoffs**: The deliberate analysis and evaluation of competing technical, cost, and schedule options to reach a balanced solution that serves multiple, sometimes conflicting constraints.
- **Verification and Validation (V&V)**: Oversight of testing and demonstration activities to ensure the system is built right (verification) and builds the right system (validation); a key responsibility of the systems engineer.
- **Concept of Operations (ConOps)**: A narrative description of how the system will operate in its intended environment; typically led by the systems engineer and used to guide architectural and design decisions.
- **Systems Engineering Management Plan (SEMP)**: A comprehensive technical planning document authored primarily by the systems engineer that documents the systems engineering approach, processes, and responsibilities for the project.
- **Interface Definition**: The explicit specification of how system/subsystem components interact, including data, physical, and functional boundaries; assessed and managed throughout the lifecycle.
- **Requirement Allocation**: The distribution of higher-level requirements down to lower-level system components and subsystems to ensure complete coverage and traceability.

## Mental Models
- **The "Big Picture" Lens**: Think of the systems engineer as holding a helicopter view of the entire system while specialists focus on their domains; success requires constantly stepping back from any single discipline's perspective to ensure the overall design is coherent and balanced.
- **Design as Negotiation**: Frame systems engineering as a perpetual negotiation between competing interests (cost, schedule, performance, safety, reliability) where the engineer's art lies in knowing when and where to probe for the best overall compromise.
- **Structure Recursion**: Visualize the system as a hierarchical tree where design processes are applied top-down: define the top-level system, then recursively apply the same processes to each subsystem level until reaching components that can be built, bought, or reused.
- **SE as a Cornerstone of Project Management**: Remember that systems engineering is one of two technical cornerstones in project management (the other being Planning and Control); SE provides technical/cost/schedule inputs while PM provides programmatic/cost/schedule constraints; the overlap is where tradeoff decisions happen.

## Anti-patterns
- **Single-Discipline Dominance**: Allowing one engineering discipline (electrical, mechanical, software, etc.) to drive decisions at the expense of others; leads to suboptimal overall designs and unbalanced risk distribution.
- **Skipping Stakeholder Expectation Baselining**: Proceeding to requirements and design without formally capturing and freezing stakeholder expectations; causes scope creep and late-stage rework.
- **Orphaned Requirements**: Defining technical requirements without tracing them back to stakeholder expectations or forward to design; creates gaps in verification and validation coverage.

## Key Takeaways
1. **Systems engineering is fundamentally about balance and tradeoffs**—not about perfecting any single technical domain, but about optimizing the coherent whole in the face of conflicting constraints and multiple disciplines.
2. **The systems engineer is a role, not necessarily a title**—the SE functions must be performed on every project regardless of size; large projects may have dedicated SE staff, while small projects may assign SE responsibilities to the project manager or lead engineer.
3. **The four system design processes are applied recursively** to each level of the system structure, from top-level stakeholder expectations down to the lowest-level products that can be built, bought, or reused.
4. **Stakeholder expectations and technical requirements must be baselined early**—these serve as the contract for the rest of the project and are the foundation for verification, validation, and traceability.
5. **The systems engineer owns the big-picture documentation and oversight**—ConOps, SEMP, HSI Plan, requirements/specifications, V&V plans, and certification packages are typically authored or coordinated by SE, ensuring the technical narrative is coherent.
6. **Systems engineering overlaps with project management in the technical aspects of cost and schedule**—the systems engineer focuses on the success of engineering (technical, cost, schedule realism), while the project manager maintains delivery constraints; this overlap is where technical feasibility meets programmatic reality.
7. **The SE Engine (17 common technical processes) is the operational spine of every NASA project**—processes 1–9 flow sequentially through execution, while processes 10–17 provide crosscutting support (planning, monitoring, risk management, configuration management, quality assurance, and others).

## Connects To
- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: The normative requirement document that defines the 17 common technical processes and the SE Engine; this handbook is an expansion and interpretation of NPR 7123.1 guidance.
- **NPR 7120.5 (NASA Space Flight Program and Project Management Requirements)**: Defines the three-part project management objective (technical, team, cost/schedule) and establishes systems engineering as the technical backbone of project management.
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering—System and Software Engineering—Processes and Terminology)**: The international standard that NASA aligns to; the 17 processes and SE Engine are NASA's interpretation of the 15288 process domain.
- **The NASA Engineering Network (NEN) Systems Engineering Community of Practice**: A peer-support and knowledge-sharing resource where NASA systems engineers access templates, best practices, and peer guidance; referenced as a primary professional development resource.
