# Chapter 3: HSI in the NASA Systems Engineering Engine

## Core Idea
HSI is layered onto the 17-process NASA Systems Engineering Engine (SEE) in every life-cycle phase; the practitioner must understand which SEE processes carry the highest HSI leverage per phase, then drive product maturity to phase-appropriate baselines through iterative, recursive execution.

## Frameworks Introduced
- **17-Process SEE**: The NASA SE process set defined in NPR 7123.1B, grouped into System Design Processes (SEE 1-4), Product Realization Processes (SEE 5-9), and Technical Management Processes (SEE 10-17).
  - When to use: As the primary execution framework for all HSI activities; every HSI product maps to at least one SEE process.
- **Product Maturity Matrix (Table 3.1-3 and 3.1-4)**: Phase-by-phase D/I/U/X (Draft / Initial baseline / Update / Applicable) maturity schedule for HSI products, keyed to milestone reviews.
  - When to use: To plan and evaluate what products must exist at each review gate and at what level of completeness.
- **HSI-to-SEE Mapping (Table 3.1-2)**: Summary map of all 17 SEE processes to their primary HSI emphasis, enabling the practitioner to identify which SE work carries human-centered considerations.
  - When to use: When onboarding into an existing program or scoping the HSI effort for a new one.

## Key Concepts
- **Systems Engineering Engine (SEE)**: NASA's iterative, recursive, and repeatable SE process framework. HSI runs in "lock-step" with the SEE rather than as a parallel discipline.
- **Human-in-the-Loop (HITL) Testing**: Empirical testing with representative human subjects in a realistic operational context. Key SEE 7/8 (Verification/Validation) method; HITL activities conducted in early phases can be "pre-declared" for V&V credit in Phase D.
- **Concept of Operations (ConOps)**: The first primary HSI product, initiated in Pre-Phase A under SEE 1 (Stakeholder Expectations); describes how the system will be used from an operational perspective and establishes the standard for system validation.
- **Function Allocation**: The assignment of functions to hardware, software, or humans; a fundamental product of SEE 3 (Logical Decomposition). Performed iteratively from Pre-Phase A through Phase B.
- **Measures of Effectiveness (MOEs)**: Customer-satisfaction criteria established under SEE 1/2 in Pre-Phase A; used to derive MOPs and TPMs in subsequent phases.
- **Measures of Performance (MOPs)**: Lower-level metrics derived from MOEs; baselined by SRR and used to develop Technical Performance Measures (TPMs).
- **Technical Performance Measures (TPMs)**: Engineering metrics tracked from Phase A through Phase E to monitor whether the system design is meeting HSI requirements. Final TPM values are reported at Phase F Decommissioning Review.
- **Phase Key Decision Points (KDPs)**: Decision gates (KDP A through F) that authorise progression to the next life-cycle phase; HSI Plan updates and review participation are tied to each KDP.
- **Mission Concept Review (MCR)**: The end-of-Pre-Phase-A milestone. HSI success at MCR requires: initial ConOps draft, preliminary MOEs, initial function allocation, and HSI planning initiated.

## Mental Models
- Use SEE 1 (Stakeholder Expectations) and SEE 2 (Technical Requirements) early to capture human allocation and MOEs; these feed everything downstream.
- Use early-phase HITL mockups and prototypes (SEE 5) to drive requirements and design constraints; invest modestly (wood/foam mockups) and recoup value through design decisions avoided.
- Use the Product Maturity Matrix at each phase-entry to audit whether HSI products are at the required D/I/U maturity; gaps require either a gap-closure plan or explicit tailoring.

## Anti-patterns
- **Skipping Pre-Phase A**: The guide explicitly warns against skipping Pre-Phase A activities even for smaller projects; missing this phase means critical human allocation and ConOps work must be back-filled at higher cost during Phase A.
- **Conflating verification and validation**: Verification (SEE 7) confirms the system meets HSI requirements; validation (SEE 8) confirms it meets the operational intent expressed in the ConOps. Both are required and distinct.

## Key Takeaways
1. The 17 SEE processes are the execution vehicle for HSI; the practitioner maps every HSI activity to at least one SEE process to ensure traceability and phase-appropriate timing.
2. Product maturity must reach D/I/U targets keyed to milestone reviews; products that miss their phase target require a gap-analysis and closure plan.
3. Function allocation to humans is the most critical early-phase HSI output; it flows from SEE 1 → SEE 2 → SEE 3 and cascades into requirements, design solutions, and HITL evaluation.
4. HITL testing conducted in Phases A-C can be pre-declared for V&V credit in Phase D, enabling earlier risk reduction and schedule efficiency.
5. ConOps is the anchor document for system validation; it must be established in Pre-Phase A, baselined in Phase A, and updated at every major review.
6. MOEs → MOPs → TPMs form a cascade of human performance metrics that must be established early and tracked through operations.

## Connects To
- **NPR 7123.1B**: Defines all 17 SEE processes with detailed inputs, outputs, and phase-specific activities.
- **NASA/SP-2007-6105 (SEHB)**: Provides the wall-chart diagram of SEE process flow with HSI additions; referenced throughout Chapter 3.
- **NPR 7120.5E**: Defines KDPs, milestone reviews, and P/P category classifications.
- **NPR 8705.2B, Table 3.1-4**: Human-rated product maturity matrix with additional health, safety, and human rating products.
