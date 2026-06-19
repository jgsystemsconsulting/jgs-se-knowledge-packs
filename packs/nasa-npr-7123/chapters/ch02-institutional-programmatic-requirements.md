# Chapter 2: Institutional and Programmatic Requirements

## Core Idea
Chapter 2 defines the organisational roles and responsibilities for SE at NASA — from the Chief Engineer through Center Directors to technical teams — and distinguishes tailoring (formal relief from requirements) from customizing (implementation choices), establishing the ETA as the independent engineering authority that approves both.

## Frameworks Introduced
- **Engineering Technical Authority (ETA) Framework**: A three-line authority structure (Engineering, Safety and Mission Assurance, Health and Medical) in which ETA is funded independently from programs to provide checks and balances on technical decisions.
  - When to use: Whenever a technical decision requires independent engineering review, a waiver/deviation is needed, or dissenting technical opinions must be formally raised.
- **Tailoring vs. Customizing Distinction**: Tailoring = adjusting or seeking relief from NPR requirements via waiver/deviation (ETA approval required); Customizing = selecting how to implement requirements (no waiver needed, document in SEMP).
  - When to use: At the start of any program/project to establish which SE practices require formal relief and which are implementation choices.

## Key Concepts
- **Engineering Technical Authority (ETA)**: Individuals with formally delegated technical authority flowing from the Administrator through the NASA Chief Engineer to Center Directors; funded independently of programs to serve as checks and balances. The ETA establishes and is responsible for engineering processes, specifications, rules, and best practices.
- **Programmatic Authority**: The Mission Directorate Associate Administrator's authority over policy, programs, projects, budgets, and schedules; distinct from the Institutional Authority held by engineering and safety organisations.
- **Institutional Authority**: The authority held by Center Directors and their engineering, SMA, and health/medical organisations; responsible for establishing processes, human capital, facilities, and infrastructure.
- **Waiver**: A documented authorisation releasing a program/project from meeting a requirement *after* the requirement has been placed under configuration control.
- **Deviation**: A documented authorisation releasing a program/project from meeting a requirement *before* the requirement is placed under configuration control.
- **SEMP (Systems Engineering Management Plan)**: The primary vehicle for documenting tailoring results, customisation decisions, roles, and the application of the 17 common technical processes; must be ETA-approved.
- **Compliance Matrix (Appendix H)**: The technical team, with the ETA, is responsible for completing this matrix and including it in the SEMP; records how each NPR requirement is met or tailored.
- **Human Systems Integration (HSI)**: An interdisciplinary integration of the human as a system element; co-owned by the ETA, the SMA Technical Authority, and the Health and Medical Technical Authority; approach must be documented in the SEMP or a stand-alone HSI Plan.

## Mental Models
- Use tailoring when a specific NPR requirement genuinely cannot or should not apply; document the risk rationale and get ETA approval. Use customizing when you are choosing *how* to apply a requirement; no approval needed but document the choice.
- The ETA cannot approve waivers to non-technical requirements established by Programmatic Authority — that boundary must be respected.
- For multi-Center programs, SE compliance must be jointly negotiated and captured in the lead Center's SEMP; it does not happen automatically.

## Anti-patterns
- **ETA and program manager being the same person**: ETA independence is structural; the ETA's concurrence is sought *by* the program/project manager when a program-level ETA is appointed, preserving the check-and-balance function.
- **Undocumented customization**: Even though customization does not require a waiver, it must be captured in the SEMP; undocumented deviations from handbook practices create audit and review failures.
- **Skipping the compliance matrix**: Completion of the Appendix H compliance matrix is a technical team responsibility; omitting it leaves tailoring decisions untracked and invisible to reviewers.

## Key Takeaways
1. ETA is the cornerstone of NASA's engineering checks and balances; its independence from program funding is non-negotiable.
2. Tailoring requires formal ETA-approved waivers or deviations with documented risk rationale; customizing does not, but must still be documented in the SEMP.
3. The compliance matrix in Appendix H must be completed by the technical team and ETA for every program/project.
4. HSI is co-owned across three Technical Authorities and must be planned and documented from early in the project life cycle.
5. Considerations for tailoring include system size, complexity, criticality, human involvement, cybersecurity impact, and available industrial capacity.

## Connects To
- **NPR 7120.5 (Space Flight Program and Project Management Requirements)**: Defines roles and responsibilities for program and project managers that complement the ETA roles defined here.
- **NPR 7150.2 (NASA Software Engineering Requirements)**: Technical team must ensure software systems comply; the ETA process governs software engineering tailoring.
- **NASA/SP-6105 (Systems Engineering Handbook)**: Provides examples and guidance for tailoring and customizing the 17 SE processes; referenced explicitly for tailoring considerations.
- **NPR 8000.4 (Agency Risk Management Procedural Requirements)**: Risk evaluation is a required element of the tailoring rationale documentation.
