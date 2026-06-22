# Chapter 1: Introduction

## Core Idea
Systems engineering is a methodical, disciplined, holistic approach to specifying, designing, developing, realizing, technically managing, operating, and retiring a system. The DoD practices it through **16 SE processes** (eight technical management + eight technical) applied across the acquisition life cycle, planned and governed through the **Systems Engineering Plan (SEP)**, and scaled to each program's maturity, complexity, size, pathway, and phase.

## Frameworks Introduced
- **The 16-process SE model** — eight technical processes (top-down design / bottom-up realization, the V) plus eight technical management processes (life-cycle insight and control). Mapped to ISO/IEC/IEEE 15288.
  - When to use: as the structuring framework for *all* technical effort on a program; detailed in Section 4 (this pack's ch04 and ch05).
- **The V-diagram** — operational need enters at top-left; technical processes flow down the left arm (requirements → architecture → implementation) and up the right arm (integration → verification → validation → transition).
  - When to use: to communicate the flow and to locate where each technical process operates.
- **Development planning** — engineering analyses and technical planning *before* a program is officially established, to lay the technical foundation for an informed materiel development decision.
  - When to use: before Milestone/MDD, by the PM (or Service lead) — to ensure a range of technically feasible solutions exists and knowledge transfers to the designated program.
- **The Systems Engineering Plan (SEP)** — the master technical plan documenting the SE approach, risks, processes, resources, metrics, products, organization, design considerations, and review timing.
  - When to use: required for MDAPs and ACAT II/III; recommended for all other development.

## Key Concepts
- **Definition of SE**: a methodical and disciplined approach for the specification, design, development, realization, technical management, operations, and retirement of a system. It applies critical thinking and balances contributions across engineering disciplines into a coherent capability.
- **The system**: an aggregation of system elements and **enabling system elements** that together achieve a purpose or provide a needed capability. Enabling elements deliver the capability into service, keep it in service, or end its service (development, production, test, deployment, sustainment products/processes).
- **The Systems Engineer's balancing act**: balance the conflicting constraints of **cost, schedule, and performance** while maintaining an acceptable level of **risk**, enhancing overall system effectiveness, suitability, survivability, and sustainability.
- **SE policy hierarchy**: DoDD 5000.01 (*The Defense Acquisition System*), DoDI 5000.02 (*Operation of the Adaptive Acquisition Framework*), DoDI 5000.88 (*Engineering of Defense Systems* — the binding SE policy), DoDD 5137.02 (USD(R&E)). This Guidebook is *guidance* implementing that policy, not policy itself.
- **Process scaling**: every organization scales its application of the 16 processes to the program's maturity, complexity, size/scope, acquisition pathway, and life-cycle phase. Lower-risk, less-complex programs use simpler tools, less-frequent reporting, and right-sized activities.
- **Key roles**: the Program Manager (PM), the (Lead) Systems Engineer, and the Lead Software Engineer jointly own the technical effort; the Systems Engineer leads the SE Working-Level IPT (WIPT).

## Mental Models
- SE is *guidance scaled to the program*, not a fixed checklist: the question is never "did we do all 16 the same way" but "did we apply each process at the right depth for this program's risk and complexity."
- The 16 processes run in an **integrated and overlapping** manner — they are not sequential phases. Technical management processes operate continuously *while* the technical processes execute.
- The SEP is the single technical contract between the program and its reviewers: if an SE activity, risk, metric, or review criterion matters, it belongs in the SEP.
- Development planning is "SE before the program exists" — its job is to make sure a feasible, affordable solution space is on the table before money is committed.

## Anti-patterns
- **Treating the Guidebook as policy**: the binding requirements are in DoDI 5000.88 and related issuances; the Guidebook explains *how*, not *what is mandatory*.
- **One-size-fits-all process application**: applying heavyweight SE process and reporting to a small, low-risk program defeats the scaling principle and wastes effort.
- **Skipping development planning**: entering a program without having explored the feasible solution space pushes unmanaged technical risk into execution.

## Key Takeaways
1. SE is composed of **16 processes**: 8 technical management + 8 technical, mapped to ISO/IEC/IEEE 15288.
2. SE balances cost, schedule, and performance at an acceptable level of risk across the whole life cycle.
3. The **SEP** is the master technical plan; required for MDAPs and ACAT II/III, recommended for everything else, and kept as a living document.
4. The 16 processes must be **scaled** to the program — maturity, complexity, size, pathway, and phase.
5. **Development planning** lays the technical foundation *before* the program is established.
6. This Guidebook is OUSD(R&E) *guidance*; the binding SE policy is DoDI 5000.88, *Engineering of Defense Systems*.

## Connects To
- **ch04 (Technical Management Processes)** and **ch05 (Technical Processes)**: the detailed treatment of all 16 processes introduced here.
- **ch03 (Technical Reviews & Audits)**: the SEP defines the timing and entrance criteria of the reviews.
- **DoDI 5000.88 (*Engineering of Defense Systems*)**: the policy this Guidebook implements.
- **DoDI 5000.02 / Adaptive Acquisition Framework**: the acquisition pathways the SE effort is tailored to.
- **NASA NPR 7123 (`nasa-npr-7123` pack)**: the parallel — but distinct (17-process) — civil-agency SE process standard.
