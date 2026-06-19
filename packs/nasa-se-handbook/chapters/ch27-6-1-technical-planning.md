# Chapter 27: 6.1 Technical Planning

## Core Idea
Technical planning converts mission goals into a tangible, executable project scope by defining *what* work will be done (Work Breakdown Structure), *how long* it will take (scheduling), *what it will cost* (budgeting), and *how it will be managed and verified* — producing the Systems Engineering Management Plan (SEMP) and supporting technical plans that serve as the baseline for execution.

## Frameworks Introduced

- **Work Breakdown Structure (WBS)**: A hierarchical, product-oriented decomposition of the total project into clearly defined, logically sequenced work components, organized by project level, higher-level integration point, and cost account number. Derived from the Product Breakdown Structure (PBS), which reflects the system's physical and system architectures.
  - When to use: Required for all projects; provides the organizing framework for planning, scheduling, cost estimation, and status reporting across the entire project lifecycle.

- **Systems Engineering Management Plan (SEMP)**: The primary top-level technical management document, developed early in Formulation and updated throughout the lifecycle, specifying technical processes, activities, organizational structure, cost, and schedule for the technical effort. Must be tailored to project type, phase, development risks, and complexity.
  - When to use: Mandatory for all projects; serves as the "rule book" for how technical work will be conducted; contractor and NASA field Centers each maintain their own SEMP.

- **Network Scheduling**: A method for defining activities, their dependencies, durations, and precedence relationships (using activity-on-arrow PERT or precedence diagrams), producing a critical path and resource-constrained schedule for the project. Scheduling is essential for understanding dependencies, calculating project duration, and identifying the critical path — activities that directly determine project completion date.
  - When to use: Applied to every WBS element to establish feasible baseline schedules, identify resource bottlenecks, and forecast schedule impacts of technical or resource changes.

- **Budgeting and Cost Estimation**: Process of combining workforce, equipment, materials, and overhead costs (direct labor, overhead, subcontracts, travel, management, systems engineering, integration & verification, contingency) to establish a baseline budget aligned to the WBS and network schedule. Three primary methods: parametric (early stages, limited definition), analogous (similar historical programs), and engineering/grassroots (bottom-up, highly detailed).
  - When to use: Parametric in Phases Pre-A/A for initial estimates; analogous when historical data exist but definition is incomplete; grassroots in Phase B onward when detailed scope and estimates are available. Integrate multiple models to produce complete Life-Cycle Cost (LCC) estimate.

- **Verification Plan**: Specifies the method (analysis, inspection, demonstration, test) and procedures for verifying that each product conforms to its specified requirements. Verification is performed on realized artifacts (breadboards, brassboards, prototypes, engineering units, qualification units, flight units) at the appropriate level and phase, with documented success/failure criteria and controlled environments.
  - When to use: Developed during Technical Planning and baselined at PDR; refined as design matures; methods and procedures documented before verification is conducted.

- **Validation Plan**: Specifies the method (analysis, inspection, demonstration, test) and procedures for validating that the end product satisfies stakeholder expectations (ConOps, NGOs). Validation is typically performed on higher-fidelity units (prototypes, qualification, flight) in the intended operational or relevant environment; methods differ from verification in purpose and focus on behavior vs. compliance to spec.
  - When to use: Developed during Design Solution Process; validated against baselined stakeholder expectations, not technical requirements; includes off-nominal operational scenarios alongside nominal cases.

- **Integration Plan**: Identifies system interfaces, establishes environments (natural and induced), defines system analysis, test strategy, and assembly/integration sequences. Captures organizational interaction, test/assembly/maintenance functions, and closeout activities for decommissioning and disposal.
  - When to use: Captures cross-cutting system interactions; updated as design evolves and integration complexity becomes clearer.

- **Joint Confidence Level (JCL)**: An integrated uncertainty analysis combining cost, schedule, and risk into a single probabilistic model that outputs the probability of meeting both targeted cost *and* targeted schedule simultaneously. Required at KDP-C for all NASA projects above $250M.
  - When to use: Required at KDP-C; probabilistic range estimates at KDP-B; can be re-run if project requires rebaselining.

## Key Concepts

- **Technical Planning Strategy**: A foundational roadmap addressing communication, NASA procedural requirements, planning documentation, work sequencing, deliverables, capture methods, risk management, tools/methods/training, stakeholder involvement, contractor interface, milestone entry/exit criteria, interface definition/control, lessons learned, technology development, technical metrics, make/buy/reuse decisions, contingency planning, status reporting, decision analysis approach, and human-element management.

- **Product Breakdown Structure (PBS)**: The system architecture decomposed into prime products, systems, segments, subsystems, and lower-level hardware/software items — the foundation from which the WBS is derived by adding enabling functions (management, systems engineering, integration & verification).

- **Critical Path**: The longest sequence of dependent activities in a network schedule, determining the shortest possible project completion time. As tasks complete or slip, the critical path evolves; continuous monitoring and updates are essential to forecast schedule impacts.

- **Cost Account**: A subdivision of a WBS element to which detailed planning, budgeting, and earned value management are applied. May contain multiple work packages (units of work with defined products, schedule, and budget) or planning packages (high-level scope with budget allocated for later refinement).

- **Contingency**: Unallocated future expenses (UFE) included in budget and schedule reserves to accommodate unforeseen technical, cost, or schedule risks; based on complexity and criticality of effort.

- **Earned Value Management (EVM)**: A project performance technique that compares actual work progress (earned value) to planned progress (budgeted cost of work scheduled) and actual cost (budgeted cost of work performed) to detect variances and forecast final cost/schedule at completion.

- **Work Package**: A unit of work within a cost account that can be scheduled and budgeted independently; the basic building block for EVM. Each work package has a clearly defined scope, schedule, and budget contributing to earned value.

- **Lessons Learned**: Knowledge or understanding gained from experience — either successful tests/missions or mishaps/failures — compiled as historical documents, requirements rationales, and supporting analyses to inform current and future project planning and risk mitigation.

## Mental Models

- **Think of the WBS as a "map of all the work"**: Every product, service, and enabling function the project will deliver must appear exactly once in the WBS. If work is missing or if the same work appears at multiple levels (duplication), the project lacks visibility and control. Use the WBS to cascade requirements, allocate resources, and trace impacts of scope or schedule changes.

- **Understand the 50-70-90 cost-lock-in rule**: By the time the preferred system architecture is selected, 50–70% of life-cycle cost is already locked in. By preliminary design, this rises to 90%. This means early architectural and design decisions have outsized cost impact; front-load analysis effort on trade studies, risk reduction, and lessons learned in Phases Pre-A and A.

- **Treat scheduling as a forecasting tool, not a constraint**: Network schedules reveal dependencies and critical path, but they are only accurate when resource-leveled and risk-buffered. Without sufficient schedule reserve (float) on non-critical-path activities, the project becomes brittle — any slip on a near-critical task cascades into delays. Build in contingency margins and re-plan when new information arrives.

- **View cost estimation as a progressive refinement**: Parametric estimates in Phase A are ±30–50% uncertain; grassroots estimates in Phase B can be ±10–15% if based on detailed scope. Maturity of the Life-Cycle Cost Estimate evolves: Pre-Phase A (70% confidence, high uncertainty) → Phase A (cost/schedule range) → Phase B (70% joint confidence at KDP-C for projects >$250M). Recognition of uncertainty is more important than false precision.

## Anti-patterns

- **Function-based WBS (Error 1)**: Organizing the WBS by activities or processes (e.g., "Design," "Testing") rather than deliverable products (e.g., "Spacecraft," "Flight Software," "Ground Segment") causes only the project manager to hold accountability for products; lower-level managers are accountable for tasks, not outcomes. This fractures traceability and responsibility.

- **Misaligned WBS/PBS branch points (Error 2)**: Separating hardware and software as independent WBS branches when they will be integrated at lower levels creates accountability gaps and masks integration costs. Branch points should align with how subsystems will physically or functionally be assembled and tested.

- **Inconsistent WBS and PBS (Error 3)**: If the WBS structure does not align with the physical/system architecture (PBS), the PBS may not be fully implemented, and traceability between design architecture and cost/schedule control is lost.

- **Underestimating planning effort**: Many projects historically under-resource planning activities and then enter continuous crisis management. Proper planning requires time to define scope, estimate effort (HWIL contingency, software debugging staff, HITL testing), negotiate external dependencies, and integrate stakeholder commitments. This is not optional overhead.

- **Separating cost and schedule estimates**: Treating cost and schedule as independent leads to infeasible plans (high cost but no resources to execute on time, or aggressive schedule with insufficient budget for rework). WBS, network schedule, and budget are interdependent; they must be mutually consistent and re-baselined together.

- **Missing contingency or confusing contingency with "padding"**: Contingency is not a hidden reserve to be spent down; it is a risk mitigation strategy. Contingency on critical-path activities protects schedule. Contingency on cost protects against unforeseen rework, supplier failures, or design changes. Without adequate contingency, any risk realization cascades into overrun.

- **Ignoring lessons learned**: Searching the NASA Lessons Learned Information System (LLIS) at project start is inexpensive insurance. Rebaselining a program (orbit change, descope, thermal control redesign) without re-running systems engineering processes from requirements definition risks repeating costly mistakes (e.g., Chandra's Teflon thermal control surfaces causing electrostatic discharge in the changed environment).

## Key Takeaways

1. **Technical Planning is not ceremonial**: The primary value of the SEMP and technical planning is *in the work of planning*, not the document. Planning forces the team to think through dependencies, estimate realism, and align on approach. This alignment is the true product; the plan is evidence of that alignment.

2. **WBS must be product-oriented, recursively decomposed, and consistent with the PBS**: Every work element must be traceable to a physical or functional product; the WBS dictionary must document objectives, descriptions, and dependencies. Use the WBS to organize all downstream planning (schedules, budgets, risk, verification, configuration management).

3. **Scheduling is constraint-driven**: Build network schedules from the bottom up (six-step process: identify activities, negotiate external dependencies, estimate durations, calculate critical path, integrate lower-level schedules, level resources). Maintain schedule reserves and update the critical path as the project progresses.

4. **Cost estimation matures with design definition**: Use parametric models in Phase A (limited definition, high uncertainty); transition to analogous or grassroots in Phases B/C as scope clarifies. Integrate multiple cost models, account for inflation, and apply learning curves for recurring production. LCC includes development, operations, maintenance, and disposal — not just acquisition.

5. **Contingency and risk reserves are essential controls, not optional**: Budget and schedule reserves must be based on risk analysis and complexity; they protect against unforeseen rework, supplier failures, and design changes. Contingency should be tracked and consumed transparently (e.g., via Earned Value Management) to forecast final cost and schedule.

6. **Verification and Validation are distinct and both necessary**: Verification answers "Did we build it right?" (does the product meet its specification?). Validation answers "Did we build the right thing?" (does the product satisfy stakeholder expectations?). Methods differ (test, analysis, demonstration, inspection), and verification credit may only be taken on controlled (flight-equivalent) units for official sign-off.

7. **Stakeholder commitment and integration are critical**: Technical plans are reviewed and approved with the project manager and stakeholders *before* work begins. Formal agreements (Internal Task Agreements, Memoranda of Understanding, or contracts) establish roles, responsibilities, deliverables, and Measures of Effectiveness (MOEs). Without stakeholder buy-in at the start, plans are likely ignored and disputes erupt when deliverables don't meet expectations.

## Connects To

- **ISO/IEC/IEEE 15288 (Systems and Software Engineering Lifecycle Processes)**: Technical planning aligns to processes for requirements management, design solution, and verification/validation; WBS and SEMP are primary artefacts for lifecycle management and traceability.

- **NPR 7120.5 (NASA Space Flight Program and Project Management Requirements)**: Mandates WBS structure (Level 2 standard for space projects), SEMP content, LCC reporting, and KDP reviews; defines technical planning as a prerequisite for cost estimation and budget approval.

- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: Requires application of 17 common technical processes to all levels of the PBS; WBS is the vehicle for allocating these processes across the project hierarchy.

- **NASA Cost Estimating Handbook**: Provides detailed methodology for parametric, analogous, and grassroots cost estimation; addresses life-cycle cost, learning curves, inflation, and integration of multiple cost models.

- **NASA Schedule Management Handbook (NASA/SP-2010-3403)**: Expands on network scheduling techniques, critical path analysis, resource leveling, and earned value performance measurement.

- **NASA Work Breakdown Structure Handbook (NASA/SP-2010-3404)**: Provides detailed WBS development techniques, examples, and common errors; emphasizes product-based hierarchy and cost account structure.

- **Configuration Management (Section 6.5)**: Technical plans are managed and baselined via CM; requirement and design changes flow through CCB; traceability is maintained in CM tools and matrices.

- **Technical Assessment Process (Section 6.7)**: Status reporting (schedule/cost variance, earned value, progress to Technical Performance Measures) is the feedback mechanism to detect plan deviation and trigger replanning.

---

*Synthesis of NASA/SP-2016-6105 Rev 2, Section 6.1 (Technical Planning). Eight major processes/frameworks and seven key concepts captured; reference depth appropriate for systems engineering practitioners initiating or auditing technical plans.*
