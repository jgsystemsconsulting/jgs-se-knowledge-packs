# Chapter 3: Requirements for Common Technical Processes

## Core Idea
Chapter 3 mandates that all NASA programs and projects identify and implement seventeen ETA-approved common technical processes — organised into system design (top-down), product realization (bottom-up), and technical management (cross-cutting) groups — collectively called the "SE Engine," which recursively drives the development of system products at every product layer across all life-cycle phases.

## Frameworks Introduced
- **The SE Engine (17 Common Technical Processes)**: The NASA model of three interlocking process groups — System Design (4 processes), Product Realization (5 processes), and Technical Management (8 processes) — applied recursively to each product layer of the system structure.
  - When to use: Throughout every life-cycle phase; all 17 are active during design and realization; the 8 Technical Management processes continue through operations.
- **Product Layer / System Structure**: A horizontal slice of the product breakdown hierarchy comprising an end product and its associated enabling products; the SE Engine is applied once per product layer, not once per project.
  - When to use: When decomposing a system to determine where to apply SE process requirements and who is responsible for each layer.
- **SE Vee Heritage**: The SE Engine evolved from the classic SE Vee; for a simple single-pass waterfall life cycle the left chamber maps to system design and the right to product realization.
  - When to use: When explaining the SE Engine to teams familiar with the traditional Vee model or when using a waterfall lifecycle.

## Key Concepts
- **System Design Processes (4)**: (1) Stakeholder Expectations Definition — elicit use cases, ConOps, and stakeholder expectations including MOE definitions; (2) Technical Requirements Definition — transform expectations into unique, quantitative, verifiable "shall" statements with MOP/TPM definitions; (3) Logical Decomposition — decompose requirements into functional/behavioral/temporal models and derived requirements; (4) Design Solution Definition — translate logical models into preferred design alternatives satisfying derived requirements.
- **Product Realization Processes (5)**: (1) Product Implementation — make, buy, or reuse the lowest-level end product; (2) Product Integration — assemble and integrate verified lower-level products into the next higher-level product; (3) Product Verification — demonstrate conformance to requirements/specifications; (4) Product Validation — confirm the product fulfils its intended use in its intended environment against baselined stakeholder expectations; (5) Product Transition — hand off verified/validated end products to the next higher-level customer.
- **Technical Management Processes (8)**: Technical Planning (generates the SEMP); Requirements Management (bidirectional traceability and change control); Interface Management (formal control of interfaces across teams, contractors, and geographies); Technical Risk Management (risk-informed decisions using NPR 8000.4); Configuration Management (per SAE/EIA-649); Technical Data Management (capture trade studies, analyses, reports across the life cycle); Technical Assessment (monitors progress, feeds life-cycle reviews); Decision Analysis (criteria, alternatives, analysis, and selection for technical issues).
- **Measure of Effectiveness (MOE)**: A qualitative or non-directly-designable measure by which a stakeholder judges satisfaction with the delivered product; defined during Stakeholder Expectations Definition and used as the validation standard.
- **Measure of Performance (MOP)**: A quantitative "design-to" measure that, when met, helps ensure its associated MOE is satisfied; generally two or more MOPs per MOE; defined during Technical Requirements Definition.
- **Technical Performance Measure (TPM)**: A quantitative measure tracked against plan throughout the project to monitor technical progress; required to include mass and power margins as leading indicators.
- **Identify (Chapter 3 usage)**: To either use an ETA-approved process directly or use a customized process that the ETA has approved; not merely acknowledging the process exists.
- **Implement (Chapter 3 usage)**: To document and communicate the approved process, provide resources and training, and monitor and control its execution — including documenting any applications and tools used.
- **Bidirectional Traceability**: The ability to trace any requirement to its parent and to its allocated children; a mandatory output of the Requirements Management process.
- **Enabling Products**: Life-cycle support products and services (test, production, training, maintenance, disposal) that facilitate the progression and use of the operational end product; the program/project is responsible for ensuring enabling products exist at each phase.

## Mental Models
- Use the System Design processes top-down from the highest product layer to the lowest; use the Product Realization processes bottom-up from lowest to highest; the Technical Management processes run in parallel across both directions at every layer.
- When you cannot trace a requirement to a stakeholder expectation (upward) or to a design element (downward), the Requirements Management process has failed.
- Early-phase end products (reports, models, prototypes) are as valid as late-phase hardware; the SE Engine applies in every phase, the form of the output just changes.
- Decision Analysis is not optional for significant technical decisions; it requires documented criteria, alternatives, analysis, and selection — not just a verbal team consensus.

## Anti-patterns
- **Running the 17 processes once for the whole project**: Each product layer in the system structure requires its own application of the SE Engine; a single pass misses derived requirements and integration issues at lower levels.
- **Defining MOEs as design requirements**: MOEs are validation standards (qualitative, stakeholder-facing); they must not be confused with MOPs or TPMs which are design targets.
- **Treating handbook guidance as requirements**: NASA/SP-6105 practices are best practices, not additional mandated requirements; teams customise them under ETA guidance.

## Key Takeaways
1. Every Program/Project Manager must identify and implement all 17 ETA-approved common technical processes — no process may be silently omitted.
2. The SE Engine is recursive: it applies to every product layer of the system structure, not just the top level.
3. System design flows top-down (stakeholder expectations → requirements → logical decomposition → design solution); product realization flows bottom-up (implement/integrate → verify → validate → transition).
4. MOEs drive validation; MOPs and TPMs drive design and performance tracking — these three measurement types serve distinct purposes and must not be conflated.
5. Technical Management processes (especially Risk Management, Configuration Management, and Decision Analysis) are not optional administrative overhead; they are integrated technical processes with NPR-level mandates.
6. "Identify" and "implement" have precise NPR definitions: identifying a process means ETA approval of the approach; implementing it means resourcing, training, monitoring, and documenting it.
7. The Technical Planning process generates the SEMP; it is the linchpin that connects all other processes through documented plans.

## Connects To
- **Chapter 6 (SEMP)**: The Technical Planning process (SE-16) outputs the SEMP; SEMP content must describe how all 17 processes are tailored and applied.
- **Chapter 5 (Life-Cycle Reviews)**: The Technical Assessment process (SE-22) drives the conduct of life-cycle and technical reviews; review work products must demonstrate SE Engine outputs.
- **NPR 8000.4 (Agency Risk Management)**: Referenced as the source document for defining the Technical Risk Management process.
- **SAE/EIA-649 (Configuration Management Standard)**: Referenced for additional Configuration Management guidance.
- **NPR 7150.2 (Software Engineering Requirements)**: Software design process executions must comply; the technical team ensures software products are integrated into the SE Engine.
- **NASA/SP-6105 (SE Handbook)**: The companion handbook providing purpose, inputs, outputs, and activities for each of the 17 processes; best practice only, not additional requirements.
