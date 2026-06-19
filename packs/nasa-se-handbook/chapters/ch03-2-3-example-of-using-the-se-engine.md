# Chapter 3: 2.3 Example of Using the SE Engine

## Core Idea

The SE engine is applied recursively across all project lifecycle phases and through successive decomposition passes of the product hierarchy. Each pass refines stakeholder expectations, requirements, designs, and validation artifacts to progressively lower tiers of the Product Breakdown Structure (PBS), demonstrating feasibility and reducing risk at each stage before moving to the next phase.

## Frameworks Introduced

- **The SE Engine (Recursive Application)**: A cyclic process applied iteratively through the project lifecycle from Pre-Phase A (Formulation) through Phase F (Closeout). The engine has a left side (system design: stakeholder expectations, requirements, functional analysis, design solutions) and a right side (product realization: implementation, integration, verification, validation, transition). Each phase and each tier in the product hierarchy spawns a complete new engine pass.
  - When to use: Every project phase requires recursive engine passes; each product element in the PBS requires its own passes; any new capability, upgrade, or design change re-enters the engine at the first process.

- **Product Breakdown Structure (PBS)**: A hierarchical decomposition of all products (end products and enabling products) the project will produce, organized in tiers, layers, or levels. Higher-numbered tiers represent lower-level, more detailed products in the hierarchy (e.g., Tier 0 = system; Tier 1 = major subsystems; Tier 2+ = progressively smaller components).
  - When to use: Guides the recursion depth; determines which elements need separate SE engine passes; identifies where the lowest feasible level sits (varies by product complexity: some projects bottom at Tier 2, others at Tier 8).

- **Phase Products vs. End Products**: Phase products are generated within a lifecycle phase to support development (mockups, interactive models, simulations, prototypes, additive manufacturing models); end products are delivered to the final user. Both undergo SE engine passes, but phase products provide evidence of feasibility and planning inputs for end-product realization.
  - When to use: Phase products (Pre-Phase A through Phase B) provide a lower-cost, lower-risk means to validate concepts and plan final production; Phases C and D work with the actual end product itself.

- **Recursive Design Passes (First Pass, Second Pass, ... Final Pass)**: Each pass through the system design side brings one tier of the PBS into focus: stakeholder expectations are detailed, requirements are flowed down and derived, functional diagrams are developed, and design solution concepts emerge—without yet having enough detail to actually build. Subsequent passes decompose each tier 1 element as if it were a separate product, repeating the process. Product realization passes then move bottom-up: implementing, integrating, verifying, and validating each tier before moving upward to the next tier.
  - When to use: Phase A typically requires 3+ passes to converge the first-order cost, technical, and schedule trade space; subsequent phases refine further. Engineering judgment determines the stopping point (when feasibility is demonstrated).

## Key Concepts

- **Stakeholder Expectations and Needs, Goals, and Objectives (NGOs)**: High-level statements of what stakeholders require. Pre-Phase A captures general ideas ("delivery of payloads to and from orbit"); Phase A details these into agreed-upon expectations ("the orbiter will transport payloads weighing up to 65,000 lbm into near-Earth orbit").

- **Concept of Operations (ConOps)**: A formal document describing how the system (or sub-system) will operate, including roles, responsibilities, numbers, and skillsets of humans interacting with it. Generated for each product tier and refined through recursive passes; used as the basis for validation (showing the product meets stakeholder expectations).

- **Requirement Flowdown and Allocation**: Tier 1 requirements applicable to lower-tier products are flowed down and validated. Requirements too general to implement are decomposed and allocated; new requirements derived from stakeholder expectations or applicable standards (safety, workmanship, quality, maintainability, ground processing, etc.) are added at each tier.

- **Feasibility Convergence**: In early phases (Pre-Phase A, Phase A), design detail is kept at the level necessary to demonstrate feasibility and reduce risk; academic completeness (e.g., decomposing down to circuit-board level for every system) is avoided. Engineering judgment determines when sufficient detail has been reached to satisfy the project's cost, schedule, and risk posture.

- **Verification (Built Right)**: Proof of compliance with approved requirements via test, analysis, inspection, or demonstration. Relates to approved specifications and configuration baseline. Performed at each tier to ensure integrated products meet their allocated requirements before moving upward; phase products can be formally verified against their own requirements.

- **Validation (Built the Right Product)**: Proof that the product accomplishes its intended purpose in the intended environment and meets stakeholder expectations, as documented in the ConOps. Performed at each tier using phase products in early phases and end products in later phases. Critical during Pre-Phase A and Phase A when design corrections are still cost-effective.

- **Technical Management Processes (SE Engine Processes 10–17)**: Risk management, interface control, human-system integration (HSI), configuration management, and decision analysis run throughout all phases and passes. These processes ensure proper planning, control, assessment, and balance between competing interests; they can generate additional requirements and significantly impact design.

- **Product Implementation, Integration, Verification, and Validation (PIVV)**: Product Implementation occurs only at the bottom-most product tier (phase products are bought, built, coded, or reused). All subsequent product realization passes use Product Integration (combining already-realized lower-tier products). After each integration, verification confirms the integrated product meets requirements, and validation confirms it meets stakeholder expectations; the product is then transitioned to the next tier up.

- **Configuration Baseline and Control**: Established by approved specifications, drawings, and parts lists. Without a verified baseline and appropriate controls, later modifications risk cost overruns or performance problems. Maintained throughout the project lifecycle, including Phases E (Operations) and F (Closeout).

- **Technical Performance Measures (TPMs)**: Defined in early development stages and monitored throughout the operational phase (Phase E) to ensure the product continues to perform as designed and expected. Part of ongoing systems management during operations and sustainment.

## Mental Models

- **Think of the SE engine as a recursive template for product hierarchy**: Each tier in the PBS gets its own complete engine cycle—stakeholders, expectations, requirements, design—before moving to the next tier down. No product element is left without a formal design basis.

- **Use "first-order convergence" to know when to stop decomposing**: Don't require academic completeness at every level during Phase A. Stop when enough detail exists to verify feasibility, reduce high-risk requirements to acceptable levels, and establish cost/schedule/technical trade-space bounds. The right stopping point varies by product complexity.

- **Think of Phase Products as dress rehearsals for End Products**: Computer models, prototypes, and simulations in Phase A–B let you verify and validate designs cost-effectively before committing to final fabrication. Mistakes found in mockups are far less costly to fix than in flight units.

- **Use validation continuously from Pre-Phase A onward**: Asking "Are we building the right product for our users and stakeholders?" throughout design—not just at delivery—enables course corrections when they are still affordable.

## Anti-patterns

- **Skipping recursive passes or stopping decomposition too early**: Failing to bring each tier of the PBS through the SE engine creates orphaned requirements, unmapped interfaces, and integration surprises. Conversely, decomposing deeper than engineering judgment warrants (e.g., circuit-board detail during Phase A for a feasibility study) wastes resources without proportional risk reduction.

- **Separating verification and validation or treating them as the same activity**: Verification alone proves the product meets its specifications; validation alone proves it meets stakeholder expectations. Both are necessary. Testing component parts does not guarantee the integrated product will work correctly; integration-level verification and validation are essential.

- **Delaying validation to final delivery**: Validating concepts against ConOps late in the lifecycle (Phases C–D) makes design corrections expensive. Phase A and Phase B are the cost-effective windows for identifying and correcting misalignment with stakeholder expectations.

- **Treating phase products (models, mockups, prototypes) as schedule burdens rather than risk reduction investments**: Phase products cost time and money upfront but prevent far costlier late-stage rework. They are essential to planning the verification and validation strategy for end products.

- **Losing track of long-lead items and integration dependencies**: If products at different tiers have very different development timelines (e.g., one product is ready for integration weeks or months before a partner product), poor upstream planning can cause idle time or storage costs. Good planning of the PBS and scheduling is critical to manage integration sequences.

## Key Takeaways

1. **Apply the SE engine recursively to each lifecycle phase and each tier of the Product Breakdown Structure.** Pre-Phase A through Phase F all follow the engine's left-side (requirements and design) and right-side (realization and validation) processes. Each product element in the PBS undergoes the same cycle.

2. **Develop conceptual designs only to the level necessary to demonstrate feasibility and reduce risk.** In Phase A, this typically means 3+ recursive passes through the system design side before moving to product realization. Engineering judgment determines the appropriate depth; avoid academic completeness if it consumes resources without proportional benefit.

3. **Flow down tier 1 requirements to lower tiers, decompose those that are too general, and add derived or new requirements for each tier.** This ensures traceability and completeness across the PBS hierarchy. New requirements emerge from stakeholder expectations, interface constraints, and applicable standards at each tier.

4. **Use phase products (mockups, prototypes, simulations, interactive models) in Pre-Phase A through Phase B to validate concepts and plan verification and validation strategies for end products.** This approach reduces cost and risk compared to discovering design flaws in later phases.

5. **Perform both verification (built right) and validation (built the right product) at every tier of the PBS, not only on the final end product.** Component-level verification does not guarantee integrated-product performance. Integration-level verification and validation are essential gates before moving upward in the hierarchy.

6. **Maintain configuration baselines and controls throughout the project lifecycle, including Phases E (Operations) and F (Closeout).** Uncontrolled modifications to a baselined product can cause costly performance problems. When upgrades or new capabilities are needed, re-enter the SE engine at the first process.

7. **Continue technical management processes (risk management, interface control, configuration management, decision analysis) throughout all phases.** These processes ensure proper planning, control, assessment, and balance between competing interests. They are not "overhead"—they directly influence design and reduce program risk.

## Connects To

- **ISO/IEC/IEEE 15288 (Systems and Software Engineering—System and Software Lifecycle Processes)**: The NASA SE engine implements the planning, design, and verification processes defined in 15288. The recursive application across lifecycle phases and product tiers is consistent with 15288's structured lifecycle model.

- **NASA NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: This standard requires the use of the SE engine across all phases of NASA projects. The handbook section provides detailed guidance on how to apply NPR 7123.1's mandate.

- **Product Breakdown Structure (PBS) and Work Breakdown Structure (WBS)**: The PBS organizes products by hierarchy; the WBS organizes work and schedule. Good PBS design (identifying tiers and stopping points) directly enables efficient WBS planning and integration scheduling.

- **Verification and Validation (V&V) Strategy Development**: The example illustrates how V&V methods evolve through phases: early phases use analysis, simulation, and phase products; later phases conduct formal testing on end products. Phase A V&V planning sets the stage for all downstream V&V activities.

- **Configuration Management and Baseline Control**: Emphasized throughout the example as essential to preventing costly late-stage modifications. Baselines are established in Phase A (system requirements and ConOps baseline) and refined through Phase C. Phase E operations rely on configuration control to manage sustainment and upgrades.
