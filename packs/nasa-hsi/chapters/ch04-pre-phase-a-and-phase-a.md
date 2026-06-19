# Chapter 4: By-Phase HSI Activities — Pre-Phase A and Phase A

## Core Idea
Pre-Phase A and Phase A are the highest-leverage HSI phases: decisions made here lock in the majority of LCC, so the practitioner must establish ConOps, perform initial function allocation, initiate HSI planning, and stand up the HSI team before formal design trades begin.

## Frameworks Introduced
- **Pre-Phase A Concept Studies**: Produces a broad spectrum of ideas and alternatives; the HSI practitioner's role is to ensure human allocation, ConOps, high-level requirements, and initial planning are captured before the MCR.
  - When to use: As the earliest entry point for HSI; do not skip or defer even for small projects.
- **Phase A Concept and Technology Development**: Matures the Pre-Phase A concept through SRR and SDR/MDR, establishing a baseline design and baselined HSI requirements; marks the formal formation of the HSI Team (required for human-rated programs, recommended for most projects).
  - When to use: When transitioning from concept exploration to committed baseline design; SRR is the first formal gate where HSI requirements must be baselined.

## Key Concepts
- **Mission Concept Review (MCR)**: End-of-Pre-Phase-A milestone (KDP A for projects). HSI success criteria: initial ConOps draft, preliminary MOEs defined, function allocation to humans initiated, HSI planning started.
- **System Requirements Review (SRR)**: First formal Phase A gate; HSI success criteria include baselined ConOps, HSI team roster established, HSI requirements addressing all domain areas, MOPs and TPMs established for tracking.
- **System/Mission Design Review (SDR/MDR)**: KDP B for projects (or KDP 0 milestone for programs). SDR for conventional; MDR for robotic missions. HSI is applicable to robotic missions. HSI requirements updated for new human allocation.
- **Human Allocation (Flight Architecture)**: The identification of which flight functions are assigned to humans versus hardware/software; initiated in Pre-Phase A, Draft maturity at MCR, Updated at SRR.
- **Human Allocation (Ground Architecture)**: Identification of human functions in ground crew and ground control; Draft/Initial maturity beginning in Phase A.
- **HSI Decomposition Models**: Models used to derive HSI requirements (e.g., operator task analyses, timing diagrams, crew timelines, behaviour diagrams); selected and applied under SEE 3 starting in Pre-Phase A.
- **HSI Planning for SEMP or HSI Plan**: The planning artifact that documents HSI team structure, roles, products, and resourcing; initiated in Pre-Phase A, Draft at MCR, updated through all subsequent phases.
- **Candidate HSI Requirements**: High-level human-centred requirements produced in Pre-Phase A; classified as "candidate" until baselined at SRR.
- **Low-Fidelity Mockups and Prototypes**: Physical or software representations used in Pre-Phase A and Phase A HITL assessments to validate concepts and drive requirements without high investment; examples include crew vehicle access/reach models and aviation cockpit eye-tracking rigs.

## Mental Models
- Use Pre-Phase A to ensure human operational goals, concepts, and constraints are documented before any design commitment. "Incorporating HSI early sets the stage for a successful design — one that accommodates humans, rather than forces the humans to accommodate to the design."
- Use Phase A to convert candidate concepts into selected, baselined architecture; every HSI product should advance one maturity level (D → I or I → U) by SRR or SDR/MDR.
- Use low-fidelity mockups early and often: modest investment in Pre-Phase A HITL activities provides high-value design feedback at the lowest cost point in the life cycle.

## Anti-patterns
- **Skipping MCR for small projects**: The guide strongly advises against this, even if the project goes directly from Pre-Phase A into Phase A SRR. An informal concept review should still be held to communicate concepts to stakeholders.
- **Deferring HSI team formation**: For human-rated programs, NPR 8705.2B requires the HSI team to be formed before SRR; delaying formation means critical Phase A analyses and requirements are conducted without human-centered input.
- **"Candidate" requirements left unresolved at SRR**: Requirements that remain candidate beyond SRR become a risk at SDR/MDR and must be resolved with a documented plan.

## Key Takeaways
1. Pre-Phase A is the most cost-effective phase for HSI investment; the ConOps, function allocation, and initial HSI planning established here prevent expensive redesign in all later phases.
2. The MCR success criteria are the minimum HSI deliverables for Pre-Phase A; they must be explicitly addressed in the HSI Plan or SEMP.
3. By SRR, the HSI team must be formed, HSI requirements baselined, and MOPs/TPMs established for ongoing tracking.
4. Function allocation decisions made in Pre-Phase A and Phase A have the greatest impact on LCC — changes to human allocation after baseline are expensive.
5. Domain SME participation should be arranged before the MCR so their expertise informs concept decisions; do not wait for the HSI team to be formally stood up.
6. For robotic missions, HSI applies equally — ground crew operations, maintenance, and control-system interactions all require human-centred analysis.

## Connects To
- **NPR 7123.1B, Appendix G, Tables G-1 through G-5**: MCR, SRR, SDR, MDR entrance and success criteria.
- **NPR 8705.2B, paragraph 2.3.8**: Mandate to form HSI team before SRR for human-rated programs.
- **HSIPG Chapter 4, section 4.4.2**: Detailed ConOps development guidance.
- **HSIPG Chapter 4, section 4.4.4**: HSI requirements development guidance.
