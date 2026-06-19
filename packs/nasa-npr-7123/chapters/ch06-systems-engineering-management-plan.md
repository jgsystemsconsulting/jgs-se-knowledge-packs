# Chapter 6: Systems Engineering Management Plan

## Core Idea
The SEMP is the living master technical plan for a program/project — established early in Formulation, ETA-approved, updated through SIR, and serving as the communication bridge between program management and the executing technical team — that documents how the 17 common technical processes will be recursively applied, tailored, and resourced across every product layer and life-cycle phase.

## Frameworks Introduced
- **SEMP as Living Document**: The SEMP is not a one-time deliverable but a document continuously updated to reflect the current and evolving SE strategy, reapproved by both ETA and program/project manager at major life-cycle reviews through SIR.
  - When to use: At every major life-cycle review; update scope, tailoring decisions, TPMs, and team responsibilities as the program evolves.
- **Technical Performance Measure (TPM) Tracking Framework**: The technical team establishes TPMs that track current state versus plan; a mandated subset — "leading indicators" — must include mass margins (hardware projects) and power margins (powered projects).
  - When to use: From MDR/SDR onwards; TPMs are reported to the Program/Project Manager on an agreed reporting interval to provide continuous technical health visibility.

## Key Concepts
- **SEMP (Systems Engineering Management Plan)**: The primary technical planning document that establishes what common technical processes will be used, how they will be applied, who is responsible, what resources are required, and what the key technical tasks, milestones, and success criteria are for each life-cycle phase.
- **ETA Approval of SEMP (SE-06)**: The ETA must approve the SEMP, waiver/deviation authorisations, and other key technical documents to ensure independent assessment of technical content; this is one of the few requirements retained from earlier NPR versions with its original number.
- **Technical Plan Consistency Requirement (SE-59)**: All technical discipline plans (e.g., integration plan, V&V plan, HSI plan) must be consistent with the SEMP and treated as fully integrated parts of the technical effort — not standalone documents.
- **Recursive Application Documentation (SE-58)**: The SEMP must define how the 17 common technical processes will be recursively applied to every product layer of the system structure during each applicable life-cycle phase.
- **Technical Leading Indicator**: A forward-looking subset of TPMs; mass margins and power margins are the two mandated leading indicators (SE-62, SE-63); they must be reported and tracked through closure.
- **Review Trend Tracking (SE-64)**: The technical team must create and maintain a set of review trends, including closure of all review action documentation (RIDs, RFAs, Action Items) established by the project.
- **Baseline Timing**: For spaceflight projects under NPR 7120.5 — SEMP is baselined at SRR for projects and single-project programs; at SDR for loosely coupled, tightly coupled, and uncoupled programs.
- **SEMP for External Work**: When work is contracted, the NASA SEMP must include details on developing source selection requirements, monitoring performance, and transferring/integrating externally produced products; it also provides the basis for determining what contractor SE documentation is required.

## Mental Models
- The SEMP is the "contract" between management and the technical team: management reads it to understand what SE work will be done and by whom; the technical team uses it to execute and communicate.
- A SEMP that only covers the current phase is insufficient: it must summarise planned technical efforts for future phases as well, even if at lower fidelity.
- TPMs and leading indicators are not reporting overhead; they are the early-warning system for technical budget erosion; if mass or power margins are trending wrong, the SEMP should trigger corrective action before a review.
- The SEMP is updated *at* major life-cycle reviews, not *after* them; the update reflects the outcome of the review and is reapproved by ETA and program manager before the next phase.

## Anti-patterns
- **Treating the SEMP as a formulation-only document**: The SEMP must be actively maintained and updated through SIR; a SEMP that is written once and shelved does not fulfil SE-58 or SE-59.
- **Technical discipline plans inconsistent with the SEMP**: Integration plans, V&V plans, and HSI plans that conflict with or are developed independently of the SEMP violate SE-59 and create process gaps at reviews.
- **Omitting the SEMP for small projects**: For small projects, the SEMP material may be incorporated into the Project Plan, but only if the ETA approves the incorporated SEMP material; elimination without ETA approval is not permitted.

## Key Takeaways
1. The ETA must approve the SEMP — this is a binding requirement (SE-06), not a courtesy review.
2. The SEMP is a living document updated and reapproved by both ETA and program manager at each major life-cycle review through SIR.
3. Every technical discipline plan must be consistent with the SEMP; discipline plans are integrated parts of the technical effort, not parallel documents.
4. The SEMP must describe recursive application of all 17 processes across every product layer and every applicable phase — not just top-level activities.
5. Mass and power margins are the two mandated technical leading indicators; they must appear in the SEMP's TPM section and be reported on a defined interval.
6. For contracted work, the SEMP is the NASA-side planning document that governs source selection requirements, surveillance, and product transition — not just the contractor's SE plan.

## Connects To
- **Chapter 3 (17 Common Technical Processes)**: The Technical Planning process (SE-16) produces the SEMP; the SEMP must describe how all 17 processes are applied.
- **Chapter 5 (Life-Cycle Reviews)**: SEMP baseline timing is tied to specific reviews (SRR or SDR depending on program type); the SEMP is updated at and through SIR.
- **Appendix J of NASA/SP-6105**: Provides the annotated outline for the SEMP; the technical team should use it as a guide, not a template to be rigidly followed.
- **Chapter 4 (Contracted Projects)**: For contracted work, the NASA SEMP provides the basis for determining contractor SE documentation requirements (Section 4.2.3).
