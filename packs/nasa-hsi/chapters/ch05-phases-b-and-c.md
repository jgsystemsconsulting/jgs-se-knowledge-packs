# Chapter 5: By-Phase HSI Activities — Phases B and C

## Core Idea
Phase B locks in the preliminary design solution and Phase C finalises fabrication-ready detailed design; HSI practitioners transition from concept-level function allocation to design evaluation, HITL testing at increasing fidelity, and preparation for production — with CDR marking the shift from design to operations optimisation.

## Frameworks Introduced
- **Phase B: Preliminary Design and Technology Completion**: Matures Phase A work to a selected design solution via the Preliminary Design Review (PDR); characterised by increasing HITL testing, trade studies, and requirements refinement.
  - When to use: When requirements and technology selection need to be locked before detailed design begins; PDR is the milestone gate.
- **Phase C: Final Design and Fabrication**: Finalises the detailed design through CDR, PRR, and SIR; characterised by production-ready documentation, manufacturing plans, and verification/validation activities.
  - When to use: Once the baseline design is selected; all design specialty audits, interface finalisation, and production preparation occur here.

## Key Concepts
- **Preliminary Design Review (PDR)**: KDP C milestone for projects. HSI success criteria: top-level human requirements agreed and finalised, requirement flow-down complete, operational concept technically sound including human systems, trade studies mostly complete, modelling/analytical results incorporated.
- **Critical Design Review (CDR)**: Primary Phase C gate; KDP D for projects. HSI success criteria: detailed human requirements and verification requirements baselined, interface definitions consistent with technical maturity, trade studies complete to detailed design level, components/interfaces modelled and validated against ConOps.
- **Production Readiness Review (PRR)**: Phase C review confirming readiness for full-scale production; HSI inputs include finalised manufacturing, logistics, and training plans.
- **System Integration Review (SIR)**: Phase C review ensuring integrated HSI inputs have evolved from individual component-level inputs to system-level integrated inputs.
- **Phase B HITL Testing**: Increased-fidelity mockup and software simulator testing in Phase B compared to Pre-Phase A/A. HITL activities conducted here can be "pre-declared" for V&V credit in Phase D.
- **Crew Task Analysis**: A human-centred decomposition technique applied under SEE 3 in Phase B to derive lower-level design requirements from operational tasks.
- **Preliminary Hazard Analysis**: A Phase B safety analysis ensuring that safety requirements have been adequately addressed in the preliminary system design.
- **Human-System Interface Design**: The iterative design of controls, displays, and information presentations to optimise operator workload, situational awareness, and error tolerance; evaluated through Phase B/C HITL activities.
- **Operate-to Documents**: Procedures and operational documentation initiated in Phase A (Draft), developed through Phase B (Draft), and baselined in Phase C (Initial); define how humans will operate and maintain the system.
- **V&V Planning (Verification and Validation)**: Phase B establishes the V&V framework; Phase C matures it. "Pre-declared" HITL from Phases B/C is assessed in Phase D for formal V&V closure.

## Mental Models
- Use Phase B to transition from trade-study-driven architecture decisions to HITL-informed design evaluation; if a trade study has not been closed by PDR, document its open status and potential impact.
- Use Phase C to maximise "residual" HSI value: after CDR, design changes are expensive. Focus effort on training, operations planning, and maintenance optimisation rather than hardware redesign.
- Use the "pre-declaration" mechanism: identify high-risk HITL activities in Phase B/C that will count for Phase D V&V credit, reducing Phase D schedule risk.

## Anti-patterns
- **Attempting major human allocation changes after PDR**: The HSIPG notes that PDR is when "the first full review of system design from concept through verification, validation, and operations" occurs. Post-PDR human allocation changes carry significant cost.
- **Treating CDR as the end of HSI influence**: CDR marks the shift in HSI focus, not the end of HSI. After CDR, HSI optimises training, operations, and maintenance; finding design flaws at this stage is "very expensive" per the guide.
- **Separating logistics and training planning from Phase B**: Manufacturing, logistics, training, and testing plans must be at least initiated in Phase B (PDR deliverable); deferring them to Phase C creates Phase D schedule pressure.

## Key Takeaways
1. PDR marks the point where the HSI team must demonstrate that preliminary human requirements are agreed, the V&V plan for human requirements is established, and trade studies are nearly complete.
2. Phase B is the prime HITL testing opportunity; higher-fidelity mockups and simulators in Phase B provide design feedback at a cost point still ahead of fabrication.
3. Phase C's CDR is the final opportunity to influence hardware design economically; HSI emphasis shifts post-CDR from hardware design to operations, training, and maintenance optimisation.
4. Crew task analyses in Phase B are a key input to deriving lower-level system requirements; they are the human-centred equivalent of functional decomposition in hardware SE.
5. The V&V framework must be established in Phase B; pre-declared HITL activities provide Phase D closure evidence and reduce late-phase verification risk.
6. Phase C SIR confirms that individual component-level HSI inputs have been integrated into system-level HSI products — a key integration milestone before Phase D assembly.

## Connects To
- **NPR 7123.1B, Appendix G, Tables G-6 through G-9**: PDR, CDR, PRR, and SIR entrance and success criteria.
- **NPR 7120.5E**: KDP milestone definitions (KDP C for PDR, KDP D for CDR/PRR/SIR).
- **NASA/SP-2007-6105 (SEHB) wall chart**: Shows Phase B/C tailoring of SEE activities from "selected and baselined architecture" to "end product."
- **NASA/TP-2014-218556 (HIDP)**: Lists potential human-centred design evaluations for SEE 7 and SEE 8 activities in these phases.
