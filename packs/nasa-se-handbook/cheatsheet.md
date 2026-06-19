# NASA SE Handbook Cheatsheet

## Decision rules (when X, do Y, because Z)
- Stakeholder expectations not baselined? Stop — do not write requirements. Unbaselined expectations cause scope creep and orphaned requirements.
- Requirement can't be verified by test/analysis/inspection/demonstration? Rewrite it. "Minimize noise" is unverifiable; "< Y dB" is.
- Spec tighter than the mission needs (e.g. recharge <3h when 12h works)? Loosen it. Over-spec eliminates viable designs and adds cost for no value.
- Requirement has no parent and isn't an approved self-derived one? Audit it out — it's gold-plating.
- Reusing a heritage/OTS product in a new environment? Requalify against the new environment. Pedigree does not transfer; OTS qualified for Earth fails in vacuum/radiation/launch loads.
- Change requested after baseline? Route through CCB with impact analysis. Late changes cost exponentially more than early ones.
- Found a problem during verification? Stop immediately; decide via Decision Analysis whether the *product* is nonconforming or the *procedure/environment* is flawed — they have different fixes.
- Discrepancy logged but root cause open? Do not dismantle the test setup — you lose the live system to investigate.
- Verification ≠ validation: run both. Verification proves "built right" (meets spec); validation proves "right thing built" (meets ConOps). A system can pass verification and fail validation.
- Defer packaging/handling/transport to after build? No — bake into design requirements; bolt-on handling forces rework.

## Life-cycle phases, gates & reviews
| Phase | Purpose | Entry gate (KDP) | Key review(s) |
|---|---|---|---|
| Pre-A | Concept studies, NGOs, feasibility | — | MCR |
| A | Concept & tech development; baseline SEMP | KDP A | SRR, SDR/MDR |
| B | Preliminary design; firm baselines | KDP B | PDR |
| C | Final design & fabrication | KDP C | CDR, (PRR), SIR |
| D | Assemble, integrate, test, launch | KDP D | TRR, SAR, ORR, FRR |
| E | Operations & sustainment | KDP E | (PLAR, decommissioning) |
| F | Closeout / disposal | KDP F | DR/DRR |

- KDP = gate that approves the *next* phase. Reviews must verify maturity **before** approval, never rubber-stamp after.
- Run the **SE Engine recursively**: one full pass (left = stakeholder→requirements→logical→design; right = implement→integrate→verify→validate→transition) per PBS tier, per phase. Implement only at the bottom tier; integrate upward bottom-up.
- Stop decomposing when engineering judgment says feasibility is shown — going to circuit-board detail in Phase A wastes resources.

## Trade studies & decision analysis
- Sequence: state selection rule → build trade tree of alternatives → collect data → quantify MOE/MOP/cost → sensitivity + uncertainty → robustness ("reality") check → recommend with cost/schedule/risk/technical impacts → team endorsement.
- Let **primary** factors define distinct alternatives; secondary factors only refine within one. Mixing them bloats the option set.
- Normalize heterogeneous units to a common scale (e.g. 1-3-9) with explicit operational definitions for every value, e.g. "high" = P ≥ 67%, "low" ≤ 33%.
- Scale method to stakes: discussion for binary low-risk; AHP/MAUT for high-stakes architecture. Don't over- or under-formalize.
- A selection is sound only if **robust** — rank holds across reasonable input ranges. If not robust, reduce uncertainty before deciding.
- Recommending a lower-ranked option? Your criteria/weights were wrong — fix them, don't override the matrix unexplained.

## Thresholds & defaults
- Fixing a flaw at verification costs **50–1000×** vs. preventing it in design — invest early.
- Project LCC **> $250M** → Initial Baseline becomes the Agency Baseline Commitment (Congress/OMB); **JCL required at KDP-C** (joint P(cost AND schedule)).
- Qualification test = worst-case load **+ design margin**; Acceptance test = operational level, **no added margin** (workmanship screen).
- Track **leading indicators** (mass margin, power margin, RID/RFA burndown) from SRR through SAR.
- Keep a **small** TPM set (per KPP + key MOE/MOP); too many dilute focus.
- Specify **threshold + baseline** performance, not a point value, to preserve trade space.
- WBS must be **product-oriented** and aligned to the PBS — not organized by activity ("Design", "Test").

## Tells & smells
- **Bad requirements:** "minimize/maximize", TBDs left in objectives, no rationale/verification-method metadata, no parent trace, only functional+performance (missing environmental/safety/-ilities).
- **Integration risk:** functional test skipped after assembly; interfaces integrated without a controlled ICD; integration sequence never revisited as schedules slip; HSI considered late.
- **Review not ready:** entrance criteria unmet, RID/RFA count spiking near a milestone, requirement volatility still high post-baseline, spending tracked instead of earned value (BCWP).
- **Governance breakdown:** "no dissent in the record" in CCB minutes; uncontrolled redlines as floor-control; vendor changes without integrator approval; verification data not traceable to a released part number (Columbia-class failure).
- **Tailoring smell:** blanket-tailoring "because it's small" with no stated risk posture; customization not captured in SEMP/Compliance Matrix; Type misclassified to dodge rigor.
