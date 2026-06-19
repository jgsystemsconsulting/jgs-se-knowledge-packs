# Chapter 2: 2.1 The Common Technical Processes and the SE Engine

## Core Idea
NASA's Systems Engineering Engine is a structured meta-process that orchestrates 17 common technical processes across four dimensions — System Design, Technical Management, Technical Assessment, and Product Realization — to flow requirements from stakeholder expectations downward through the product structure while flowing realized products upward through integration and validation.

## Frameworks Introduced
- **The Systems Engineering Engine (17 Common Technical Processes)**: A hierarchical process meta-framework that decomposes systems engineering work into System Design processes (requirements and design), Product Realization processes (implementation and integration), and cross-cutting Technical Management and Assessment processes. The engine applies these processes recursively at each level of the product structure.
  - When to use: At program start and throughout the system lifecycle to structure all SE activities, allocate responsibilities, and ensure bidirectional flow of requirements and product evidence.

**Process Families:**
- **System Design Processes** (1–4): Capture and decompose requirements; define logical and design solutions
- **Product Realization Processes** (5–9): Implement, integrate, verify, validate, and transition products
- **Technical Management Processes** (10–15): Plan, control, manage interfaces, risks, configuration, and data
- **Technical Assessment Processes** (16–17): Assess technical maturity and inform design decisions

## Key Concepts
- **System Design Processes**: The upstream half of the engine; include Stakeholder Expectations Definition, Technical Requirements Definition, Logical Decomposition, and Design Solution Definition. These processes flow requirements downward from the level above to the level below.
- **Product Realization Processes**: The downstream half of the engine; include Product Implementation, Product Integration, Product Verification, Product Validation, and Product Transition. Applied to each operational/mission product starting from the lowest structural level and working upward, these processes flow realized products upward through integration and verification.
- **Technical Management Processes**: Cross-cutting governance processes (Planning, Requirements Management, Interface Management, Risk Management, Configuration Management, Technical Data Management) that establish plans, control execution, manage interdependencies, and maintain technical baseline integrity.
- **Technical Assessment Process**: Evaluates technical maturity and readiness across the system to inform decision-makers about risk and progress.
- **Decision Analysis Process**: Applies technical analysis to support selection among design alternatives and lifecycle decisions.
- **Requirements Flow Down**: Allocation of stakeholder expectations and top-level technical requirements progressively to lower levels of the product structure hierarchy.
- **Product Flow Up**: Integration and validation of realized products from lower levels to progressively higher levels of system integration and verification.
- **Cross-Cutting Processes**: Technical Management and Assessment processes that operate in parallel with System Design and Product Realization to provide control, risk mitigation, and visibility.

## Mental Models
- **Think of the SE Engine as a two-way street**: Requirements and constraints flow downward; design solutions, implementation evidence, and validation results flow upward. Both flows must be managed in lockstep to prevent rework and integration surprises.
- **Use the 17 processes as a checklist, not a sequence**: At each product level, System Design processes define *what* is needed; Product Realization processes build and verify *how* it is done; Technical Management processes keep both synchronized and controlled.
- **Recognize recursive application**: The same process framework applies at system level, subsystem level, component level, and lower — with appropriate scope and detail at each tier.

## Key Takeaways
1. **The 17 processes are not sequential stages; they are parallel, overlapping disciplines.** A program applies all of them at each level of the product structure concurrently, with Technical Management and Assessment running continuously across both System Design and Product Realization.
2. **Requirements must flow down; products must flow up.** The SE Engine's bidirectional flow is essential: top-level stakeholder needs are decomposed into lower-level allocations, and lower-level products are integrated and verified upward. Failure to maintain both flows (e.g., skipping verification of integration, or defining design without tracing upward) breaks the integrity of the engineered solution.
3. **Product Realization starts from the lowest structural level.** Implementation and integration are applied bottom-up, not top-down. This ensures that the smallest, most testable units are implemented first, then progressively integrated and validated upward through system hierarchy.
4. **Technical Management is not overhead; it is a core, parallel responsibility.** Planning, Requirements Management, Interface Management, Risk Management, Configuration Management, and Technical Data Management run continuously alongside System Design and Product Realization to maintain control and traceability.
5. **The SE Engine scales with program complexity.** For simple projects, some processes may be lightweight; for complex, safety-critical, or long-duration programs, all 17 processes are exercised in full with rigorous discipline.

## Connects To
- **NPR 7123.1 (NASA Systems Engineering)**: The source standard; the 17 common technical processes and SE Engine diagram are defined in NPR 7123.1 and referenced throughout this handbook.
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering — System and Software Life Cycle Processes)**: International parallel framework defining generic lifecycle processes (planning, analysis, design, implementation, verification, validation, transition). The NASA SE Engine is NASA's instantiation of these concepts for space and aeronautics systems.
- **Requirements Management and Traceability**: Directly enabled by the System Design processes (1–2) and supported by cross-cutting Technical Management (Processes 11, 14, 15).
- **Configuration Management and Baseline Control**: Maintained by Technical Management Process 14 to preserve integrity as the product structure evolves.
- **Technical Risk Management**: Continuous discipline (Process 13) applied to design decisions, integration hazards, and lifecycle uncertainties across all 17 processes.
