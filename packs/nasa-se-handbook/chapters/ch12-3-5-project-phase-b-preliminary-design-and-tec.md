# Chapter 12: 3.5 Project Phase B: Preliminary Design and Technology Completion

## Core Idea
Phase B is where the project team matures technology, validates preliminary designs against mission needs, and establishes the initial project baseline—the moment at which the project and Agency formally commit to cost, schedule, and technical objectives. By PDR, all design decisions must be unambiguous and traceable to requirements, because changes beyond this gate become exponentially expensive.

## Frameworks Introduced
- **The Phase B Baseline (technical and business)**: A collection of evolving baselines covering system and subsystem requirements, specifications, designs, verification plans, operations plans, schedules, cost projections, and management plans, all under configuration management control.
  - When to use: Phase B is the phase in which to establish this formal baseline. Configuration management procedures must be implemented to track and control changes.

- **The PDR (Preliminary Design Review)**: A series of reviews structured as system-level PDR and lower-level end-item PDRs that reflect successive refinement of requirements into designs.
  - When to use: Held at the end of Phase B; design issues must be resolved before PDR so that Phase C (final design) can begin with unambiguous design-to specifications.

- **Successive Refinement Doctrine**: The principle that changes should represent incremental refinement of baselines, not fundamental rewrites. Significant design changes become increasingly expensive beyond Phase B.
  - When to use: Validate design decisions against original goals, objectives, and ConOps at each level; lock requirements under configuration control during Phase B.

## Key Concepts
- **Technology Development**: Activities in Phase B to mitigate risks identified in the Formulation Agreement, including engineering prototyping and heritage hardware/software assessments.
- **Preliminary Design**: A feasible design solution that includes internal and external interfaces, supported by analyses and development testing; must comply with all requirements and be validated against ConOps.
- **Design-to Specifications**: Unambiguous requirements and specifications that define what Phase C fabrication and coding must deliver; ambiguity at this boundary causes rework.
- **Initial Project Baseline**: The formal commitment to cost, schedule, and technical objectives; for projects with LCC > $250M, this becomes the Agency Baseline Commitment (ABC), also approved by Congress and OMB.
- **Successive Refinement of Requirements**: The flow-down of project-level performance requirements to complete sets of system and subsystem design specifications for flight and ground elements.
- **Life-Cycle Consideration**: Design decisions in Phase B must account for all downstream lifecycle aspects—training, operations, human factors, safety, habitability, maintainability, and supportability.

## Mental Models
- **Think of Phase B as the "prove it works in concept" gate.** Engineering prototyping and development tests validate that the selected preliminary design is feasible; the PDR is where you convince the Agency (and Congress, for large programs) that you can build it for the cost and schedule you committed.
- **Use configuration management as the baseline integrity tool.** Once Phase B requirements and designs are baselined, every change must be formal and traceable. Informal changes at this stage hide cost and schedule creep.
- **Recognize the cost-of-change curve.** Figure 2.5-3 in the handbook shows that significant design changes become orders of magnitude more expensive beyond Phase B. Phase B is the last chance for fundamental trades before fabrication begins.

## Key Takeaways
1. **Phase B completes technology development and risk mitigation.** Heritage assessments, engineering prototyping, and trades identified in Formulation must be closed before the project can transition to final design (Phase C).

2. **Establish one feasible preliminary design, not multiple candidates.** Analyses of candidate designs are performed to select a single solution; this selection is validated by human systems integration assessments and must address all lifecycle considerations (training, ops, safety, maintainability, etc.).

3. **Baselines must be formal and under configuration control.** The Phase B baseline includes technical (requirements, specs, designs, verification plans), operational, and business (schedule, cost) components. All changes post-Phase B must be formally managed; informal changes hide true cost and schedule.

4. **PDR is the gate between preliminary and final design.** Design issues discovered in PDR must be resolved before Phase C begins; unambiguous design-to specifications prevent rework during fabrication and coding.

5. **Operations plans must be mature by end of Phase B.** Define system operations, PI/contract management, and contingency planning based on the matured ConOps, so that training, procedures, and resource allocation can be finalized in Phase C.

6. **Cost and schedule estimates harden at Phase B and lock the Agency commitment.** After PDR changes are incorporated and costed, the result becomes the Agency Baseline Commitment (ABC). For large programs, this commitment involves Congress and OMB and cannot be easily revised.

7. **Safety, security, and mission assurance work must be documented at Phase B.** Develop the appropriate level safety data package and security plan; perform orbital debris assessment and preliminary decommissioning/disposal plans to prepare for mission close-out.

## Connects To
- **NPR 7120.5 (NASA Program and Project Management Requirements)**: Mandates the content and flow-down discipline for Phase B baselines and specifies the technical activities required.
- **NPR 7123.1 (NASA Systems Engineering Requirements)**: Specifies the entrance and success criteria for Phase B reviews (PDR and safety review).
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering—System and Software Life Cycle Processes)**: Aligns with the concept of design baseline and review gates; Phase B corresponds to the "design" phase in the lifecycle.
- **Section 4.4.1.2 (Successive Refinement Doctrine)**: Reinforces the principle that requirements-to-design flow-down must preserve traceability and prevent fundamental changes post-PDR.
- **Section 6.5 (Configuration Management)**: Requires formal CM procedures to manage Phase B baseline changes and maintain the integrity of design-to specifications.
