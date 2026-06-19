# Chapter 20: 4.4 Design Solution Definition

## Core Idea
Design Solution Definition is the iterative process of generating, evaluating, and refining alternative design concepts through trade studies, then baselining a single preferred design solution with sufficient detail to guide product realization and verification activities.

## Frameworks Introduced
- **Trade Study Process (Section 6.8 reference)**: Systematically generate and rank alternative design concepts using quantitative methods and subjective judgment; document assumptions, models, and results; involves multidisciplinary teams (systems engineers, design engineers, specialty engineers, operators, maintainers, program analysts).
  - When to use: During concept generation and design refinement phases; whenever multiple design paths exist and cost, schedule, risk, or capability tradeoffs must be resolved.

- **Decision Analysis Process (Section 6.8 reference)**: Evaluates alternative design concepts and recommends the "best" design solution by combining quantitative analysis (objective function, cost-effectiveness measures) with subjective factors (robustness, technology maturity, unquantifiable constraints).
  - When to use: At decision gates where a single design must be selected to move forward; integrates cost, effectiveness, schedule, risk, and programmatic constraints.

- **Successive Refinement Loop**: The design is refined iteratively at increasing resolution, with baselined requirements from one level becoming high-level requirements for the next level of decomposition. Each iteration applies the Systems Engineering Engine to achieve analytical validation, cost/operations modeling, and technical feasibility confidence.
  - When to use: Throughout the design process, from initial concept through detailed design; stops when sufficient resolution is achieved to support verification, validation, and review board confidence.

## Key Concepts
- **System Model**: A representation (mathematical, simulation-based, or descriptive) that defines roles of crew, operators, maintainers, logistics, hardware, and software; identifies critical technologies; considers the entire life cycle from fabrication to disposal; supports trade analysis and optimization.

- **Trade Study**: A closed-loop process comparing alternative designs against evaluation criteria (cost, schedule, technology maturity, risk, reliability, performance margin). Results provide bounds on cost-effectiveness; increasing detail in successive refinements reduces spread between upper and lower bounds.

- **Objective Function (Cost Function)**: A mathematical expression combining multiple outcome measures (cost, effectiveness, performance, risk) into a single metric of cost-effectiveness; assigns a real number to candidate solutions; feasible solutions that optimize (minimize or maximize) this function are "optimal solutions."

- **Stakeholder Expectations**: High-level customer and operational needs that drive iterative design loops; the architecture, ConOps, and derived requirements must achieve consistency with stakeholder expectations through recursive validation.

- **Concept of Operations (ConOps)**: The operational environment, mission scenarios, and system behavior under nominal and off-nominal conditions; must be consistent with the strawman architecture and derived requirements.

- **Design Verification**: Confirmation that the design solution is realizable within constraints, has traceable requirements consistent with stakeholder expectations, and embodies decisions aligned with technical requirements and system constraints.

- **Design Validation**: Recursive, iterative process answering: Does the system work as expected? How does it respond to failures and anomalies? Is it affordable? Continues until architecture, ConOps, and requirements meet stakeholder expectations.

- **Enabling Products**: Life-cycle support products, services, and personnel (production, test, deployment, training, maintenance, disposal) that facilitate the operational end product through its life cycle; interdependent with the end product and viewed as part of the system.

- **Technical Data Package (TDP)**: Evolves phase-by-phase from conceptual sketches/models to complete drawings, parts lists, and implementation details; includes specifications, interface definitions, verification/validation plans, logistics procedures, and HSI requirements.

- **Baselining**: Placing a design solution and its requirements under configuration control at an approved point in the design process; enables team focus on one design and initiates a logical branch point to either implement or refine further.

## Mental Models

**Think of design refinement as a pyramid of increasing resolution.** Each level uses baselined requirements from the level above as inputs, applies the full systems engineering cycle again, and produces more detailed specifications. The process stops when sufficient depth exists for analytical validation, cost modeling, and review board confidence.

**Use trade studies before baselining decisions.** Perform rigorous trade studies early, document all assumptions, and place results in the configuration management system before committing to a baseline. This ensures decisions are grounded in analysis rather than whim.

**Validate design against stakeholder expectations; verify design against requirements.** Validation asks "Is this the right system?" (against stakeholder needs); verification asks "Is this the right implementation?" (against technical specs). Both are essential, and validation is recursive throughout design refinement.

**Recognize the tension between early exploration and premature baselining.** Baselining too early restricts inventive concept exploration; baselining too late leaves team members designing to a moving target. Baselining should be one of the last steps in the Design Solution Definition Process.

## Anti-patterns

- **Deferring technology assessment until design is mature**: If requirements are defined without understanding available technology and resource realities, the program risks infeasibility. Assess technology maturity iteratively from the outset and align requirements with available resources.

- **Neglecting human factors in capability allocation**: Assuming operators and maintainers can do more than is realistic leads to failures as severe as hardware/software inadequacy. Include Human Systems Integration (HSI) early and allocate functions conservatively; underestimating human capital needs inflates life-cycle cost.

- **Performing reliability analysis only after design is fixed**: Reliability and fault management analysts should participate in design trade studies from the beginning, identifying risk drivers and reliability architecture early. Late engagement results in features added on or outsourced rather than designed in.

- **Overlooking enabling products**: Long-lead items (test chambers, special fixtures, ground facilities) must be identified early and committed to contractually to ensure availability when needed. Late identification risks schedule slip.

- **Treating reused products as verified for new environments**: The "pedigree" of a reused product in its original application does not transfer to a new system, subsystem, or operational context. Reused products must meet the same verification and validation requirements as newly purchased or built products.

## Key Takeaways

1. **Multidisciplinary trade studies are the foundation of design decisions.** Involve systems engineers, design engineers, specialty engineers, operators, maintainers, analysts, and decision scientists. Use quantitative methods rigorously, but acknowledge and document subjective factors like robustness and technology maturity.

2. **System models enhance trade study rigor but are not mandatory.** Models that relate design parameters to performance assessments strengthen decision-making, but formal optimization techniques can be applied without them if creative design space exploration is present.

3. **Objective functions combine multiple measures into a single cost-effectiveness metric.** Even when exact combined measures are unattainable, develop the best expression possible and ensure underlying assumptions and relationships are fully transparent to decision-makers.

4. **Risk distributions and uncertainty must accompany all estimates.** Reliability estimates are probabilities of success with associated uncertainty; bounds on cost-effectiveness (not final values) are appropriate at intermediate refinement levels; uncertainty decreases as system understanding improves.

5. **Successive refinement drives design depth progressively; stop when sufficient resolution is achieved.** The design must penetrate deep enough for analytical validation, cost/operations modeling, and review board confidence in feasibility, performance, cost, and risk margins—but not deeper.

6. **Baseline only when design exploration is adequately complete.** Baselining too early stifles innovation; baselining too late prolongs decision ambiguity. Place results under configuration control with documented trade study rationale.

7. **Verify that design is realizable, traceable, and consistent; validate that design meets stakeholder expectations.** Both verification (against technical requirements) and validation (against operational needs) are recursive throughout design refinement and must be complete before product realization.

8. **Identify enabling products and secure commitments early.** Production facilities, test equipment, training infrastructure, and logistics support must be planned and contracted for in early design phases, with realistic schedule margins.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems and software engineering — System and software engineering — Processes and process assessment)**: Design Solution Definition aligns with the "Architectural Design" and "Detailed Design" processes; the trade study and decision analysis methods support allocation of requirements to design elements.

- **Decision Analysis Process (NASA SE Handbook Section 6.8)**: Provides the formal methodology for trade study execution, objective function development, and alternative evaluation referenced throughout Design Solution Definition.

- **Technical Planning Process**: Generates the Product Verification Plan and Product Validation Plan outputs and defines verification/validation strategy appropriate to life-cycle phase and PBS position.

- **Fault Management (NASA SE Handbook Section 7.7)**: Reliability and fault tolerance architecture decisions emerge from trade studies and must be integrated into design from the conceptual stage, not added on.

- **Human Systems Integration (NASA SE Handbook Section 7.9)**: HSI contributes requirements, function allocation, task analysis, and human-centered design iteration to the Design Solution Definition Process; HFE participation is essential from Pre-Phase A onward.

- **Technology Assessment (NASA SE Handbook Section 4.4.2.1)**: Systematic assessment of technology maturity for each subsystem/component relative to proposed architecture and operational environment; informs make/buy/reuse decisions and risk quantification.

- **Safety and Reliability (NASA SE Handbook Section 4.4.2.3.1)**: Safety and reliability analysis techniques (FMEA, hazard analysis, probabilistic risk assessment) provide risk data for trade studies; analysts must engage early to influence design trades rather than audit completed designs.
