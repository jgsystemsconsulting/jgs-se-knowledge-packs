# Chapter — MRLs in the Adaptive Acquisition Framework

## Core Idea

Manufacturing Readiness Levels are not a free-standing checklist; they are meant to be wired into how the Department of Defense actually buys things. The Adaptive Acquisition Framework (AAF) exists to deliver capability that is timely, effective, suitable, survivable, sustainable, and affordable, and it deliberately gives Milestone Decision Authorities, other Decision Authorities, and Program Managers wide latitude to shape an Acquisition Strategy that fits the thing being bought. The chapter's central argument is that MRL Assessments are a best practice that should be threaded through whichever acquisition pathway a program chooses, with the *target* maturity level and the *timing* of each assessment adjusted to match that pathway's tempo and decision points. Manufacturing risk does not respect pathway boundaries — it accompanies every weapon system across its whole life cycle — so the discipline of assessing it early and repeatedly is constant even when the mechanics are tailored.

The unifying mental move is to map MRL targets onto milestones: each major decision gate has an expected level of manufacturing maturity, and the assessment exists to expose where the program falls short of that level *before* the authority commits to the next phase.

## Frameworks Introduced (exact source names, when/how)

- **Adaptive Acquisition Framework (AAF)** — the overarching defense acquisition construct, governed by **DoDI 5000.02, Operation of the Adaptive Acquisition Framework**. It establishes several distinct acquisition approaches, each with its own implementing instruction.
- **The AAF acquisition pathways**, each cited to its own DoD Instruction:
  - DoDI 5000.85 governs **Major Capability Acquisition (MCA)**.
  - DoDI 5000.80 governs the **Middle Tier of Acquisition (MTA)**, which splits into **Rapid Prototyping** and **Rapid Fielding**.
  - DoDI 5000.81 governs **Urgent Capability Acquisition (UCA)**.
  - DoDI 5000.75 governs **Business Systems**.
  - DoDI 5000.74 governs the **Defense Acquisition of Services** pathway.
- **DoDI 5000.88, Engineering of Defense Systems** — introduced as the instruction that mandates both Systems Engineering Technical Reviews (SETRs) and Independent Technical Risk Assessments (ITRAs) for major capability acquisitions.
- **DoD Independent Technical Risk Assessment (ITRA) Framework** (Under Secretary of Defense for Research and Engineering, June 2018) — cited as the document under which MRL Assessments are recognized as a best-practice input to the ITRA.
- **Manufacturing Maturation Plan (MMP)** — introduced as the planning artifact a program builds from its initial assessment to drive toward the target MRL, or to hold risk to an acceptable level within schedule and budget.
- The chapter applies all of the above across the **MCA phase structure**: Materiel Solution Analysis (MSA), Technology Maturation and Risk Reduction (TMRR), Engineering and Manufacturing Development (EMD), and Production and Deployment — bracketed by the MDD entry and Milestones A, B, and C.

**When/how they are used:** The chapter scopes MRL Assessments to the three pathways where they add value — MCA, MTA, and UCA — and explicitly excludes them as a requirement for Business Systems and Defense Acquisition of Services, while still treating them as best practice for the three covered pathways.

## Key Concepts

**Pathway scoping.** MRL Assessments are generally not required for the Business Systems or Services pathways, but are considered best practice for MCA, MTA, and UCA. The instruction that compels SETRs and ITRAs is DoDI 5000.88, and the ITRA Framework is what positions the MRL Assessment as a best-practice feed into the ITRA.

**MRL-to-milestone mapping (MCA).** The MCA pathway pins specific maturity expectations to gates:
- **MSA Phase** — begins at the Materiel Development Decision (MDD), the mandatory entry into MCA. An Analysis of Alternatives (AoA) selects the viable solution(s); an **MRL 4** assessment should be run on each competing materiel solution. The Alternative Systems Review (ASR) may close out the AoA, and manufacturing risk for each alternative is judged by how closely it meets MRL 4 and how hard it would be to reach MRL 6 by the end of TMRR. The phase ends with a completed AoA, a conducted ITRA, a draft Acquisition Strategy, and a Milestone A decision.
- **TMRR Phase** — entered at Milestone A. Technologies entering below MRL 4 need special maturation attention to reach the **MRL 6** target by Milestone B. The MSA-era assessment serves as the MRL 4 baseline. Three SETRs typically run here — System Requirements Review, System Functional Review, and Preliminary Design Review (PDR) — and the MRL Assessment feeds the Milestone B ITRA. The phase ends when the development RFP can be released for a low-risk entry into EMD, with maturity expected to be at least MRL 6.
- **EMD Phase** — readies the program for production. SETRs include CDR, Test Readiness Review, System Verification Review, Functional Configuration Audit, and the Production Readiness Review (PRR). **MRL 8** is the appropriate maturity for Low-Rate Initial Production (LRIP); **MRL 9** for Full-Rate Production (FRP). Pilot-line articles in EMD should use production materials, components, tooling, facilities, and personnel. The MRL Assessment feeds both the PRR and the pre-Milestone-C ITRA, flagging anything short of MRL 8.
- **Production and Deployment Phase** — entered at Milestone C, where the MDA decides LRIP versus FRP. Best practice is MRL 8 for LRIP and MRL 9 for FRP. If LRIP is planned, it should drive toward MRL 9 before the FRP decision; the FRP decision demands that processes be capable, in statistical control, and affordable, with a pre-FRP MRL Assessment feeding the ITRA.

**The three courses of action on a shortfall.** When an assessment finds risk areas below the milestone target (MRL 6 before Milestone B, MRL 8 before Milestone C), the PM has the same three options at each gate: (1) request a delay in the milestone decision to buy time for risk reduction; (2) switch to a lower-risk manufacturing approach or alternative design; or (3) carry the higher risk forward into the decision, accompanied by an MMP that includes the funding required to close the gap.

**MTA targets.** The MTA pathway fills a gap for capabilities mature enough to be rapidly prototyped or rapidly fielded within five years of program start.
- *Rapid Prototyping* — minimum entry target of **MRL 4**; as it matures to **MRL 6** with mitigated risk, the prototype can be inserted at Milestone B; at **MRL 8** it can be inserted at Milestone C or fielded. A more mature entry (e.g., assessed at MRL 7) shifts the target straight to MRL 8 and a Milestone C insertion or fielding. Virtual prototyping models are acceptable if they yield a fieldable residual operational capability.
- *Rapid Fielding* — minimum entry target of **MRL 8** with risk mitigation in place; production must begin within six months and all product must be in manufacturing within five years.

**UCA targets.** UCA resembles MCA but enters at Milestone B with a sub-two-year completion horizon. The preferred solution must rest on proven, available technology, avoid substantial development, be fieldable within two years, and be acquirable under a fixed-price contract. At the Course of Action Decision Point, minimum maturity should be **MRL 7** (only days remain to the Development Milestone); at the Development Milestone it should be assessed to **MRL 8** with gaps identified; the objective is **MRL 9** during production and fielding within two years.

## Mental Models

**The milestone is a maturity gate, not just a funding gate.** Each major decision point carries an implicit "you should be at MRL N by now" expectation. The assessment's job is to test that expectation honestly and surface where the program is behind.

**Baseline early, then track the delta.** The first MRL Assessment (MRL 4 in MSA) becomes the reference point. Later phases do not start fresh — they measure progress against that baseline, and any technology that never got assessed should get an early baseline assessment so nothing enters a phase unmeasured.

**Intensify as you go.** Consideration of manufacturing risk should start early and ramp up as development proceeds, so that maturity is sufficient to support rapid, affordable transition into a fielded system rather than being discovered late.

**Tailor the level, keep the discipline.** Across MCA, MTA, and UCA the *numbers and timing* shift, but the underlying practice — assess against MRL criteria, plan maturation, fund it, reassess before transitioning — stays the same. MRLs must be integrated with each program's objectives and time constraints rather than applied as a fixed template.

**The MRL Assessment is a feeder, not a terminus.** Its outputs are inputs — to the ITRA, the SETRs, the Acquisition Strategy, the Systems Engineering Plan, the Risk Management Plan, quality and manufacturing plans, industrial base assessments, contracting strategy, and the technical-review reports (e.g., the PDR report feeding Milestone B). It earns its keep by what it informs downstream.

## Anti-patterns

- **Ignoring manufacturing risk to "save" the assessment cost.** The chapter directly addresses the return-on-investment question for running MRL Assessments and argues a program cannot afford to ignore manufacturing risk, because the consequences of doing so may be too severe. Skipping the assessment to economize is treated as a false economy.

## Key Takeaways

- MRL Assessments are a best practice across the MCA, MTA, and UCA pathways, and are generally not required for the Business Systems or Defense Acquisition of Services pathways.
- For MCA, DoDI 5000.88 requires both SETRs and ITRAs, and the ITRA Framework recognizes the MRL Assessment as a best-practice input to the ITRA; MRL criteria should also be used in source selection to gauge each offeror's manufacturing maturity and risk, with separate assessments for each prototype configuration when multiple are used.
- The MCA maturity targets map cleanly to gates: MRL 4 at MSA, MRL 6 by Milestone B, MRL 8 for LRIP, MRL 9 for FRP.
- A shortfall against the target at a milestone gives the PM the same three choices every time: delay the decision, pick a lower-risk approach, or proceed carrying the risk with a funded Manufacturing Maturation Plan.
- MTA entry targets depend on path: MRL 4 for Rapid Prototyping (rising through MRL 6 and MRL 8) and MRL 8 for Rapid Fielding, all inside a five-year window.
- UCA compresses the same logic into under two years: MRL 7 at the Course of Action decision, MRL 8 at the Development Milestone, MRL 9 in production.
- Manufacturing risk is a whole-life-cycle concern; assessing it early and often is how a program manages risk well enough to deliver weapon systems on time and affordably.

## Connects To

- **gao-tra (MRL 1–10):** This chapter deepens the GAO Technology Readiness Assessment material by showing *where* on the AAF timeline each MRL value is expected and *what decision* it informs. Where the GAO TRA guidance frames the MRL 1–10 scale and the parallel concept of readiness assessment as risk evidence for a milestone, this chapter supplies the acquisition-pathway scaffolding — MDD, Milestones A/B/C, MSA/TMRR/EMD/Production phases — and the specific target levels (MRL 4/6/8/9) the program is judged against at each gate. Read together, the scale (gao-tra) and the milestone mapping (here) form the full picture of how manufacturing maturity is graded and consumed in defense acquisition.
- The Systems Engineering Technical Reviews named here (ASR, SRR, SFR, PDR, CDR, TRR, SVR, FCA, PRR) connect to broader SE technical-review and design-review practice, with the MRL Assessment positioned as a manufacturing-risk input to each.
- The ITRA, Acquisition Strategy, Systems Engineering Plan, and Risk Management Plan are the downstream artifacts that the MRL Assessment feeds, linking manufacturing readiness to program-level risk and planning governance.
