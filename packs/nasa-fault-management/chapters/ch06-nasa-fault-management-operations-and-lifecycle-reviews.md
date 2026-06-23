# Chapter 6 — Operations and Lifecycle Reviews

> **DRAFT SOURCE.** This chapter synthesizes NASA-HDBK-1002 **Draft 2 (April 2, 2012)**, an unapproved working draft. Review names, entrance/success criteria, durations, and the operations outline below reflect that draft and may differ from any later released edition. Note in particular that the Operations and Maintenance section (Section 9) was itself an *unwritten placeholder* in Draft 2 — only its planned topic outline existed. Treat all of this as guidance, not a controlling standard.

## Core Idea

Fault Management is only as good as the scrutiny it survives and the operations team that runs it. This chapter covers two lifecycle-spanning activities the handbook treats as inseparable from FM design: how FM is **operated and maintained** across mission phases, and how FM is **reviewed and evaluated** at milestone gates. The central claim on the review side is that FM is too cross-cutting and too easy to neglect to be assessed only as a sidebar in general program reviews. The handbook therefore recommends a **three-tier review structure** and, within it, a dedicated set of FM-specific technical reviews held throughout the lifecycle — each with its own entrance and success criteria — so that the FM approach, design, test readiness, launch readiness, and critical-event readiness are each affirmatively demonstrated rather than assumed.

The operations side is, in Draft 2, mostly forward-looking: the handbook lays out *what an FM operations treatment should eventually cover* across Phases A through E — concept, requirements, detailed design, V&V, operator certification, contingency planning, anomaly resolution, and lessons learned — but defers the substance to later releases. The reviewable content, by contrast, is fully developed, and it is where the chapter's weight sits.

## Frameworks Introduced

- **Three-tier FM review structure** — the handbook recommends evaluating FM at three levels: (1) FM as a **topic within major program/project lifecycle reviews** (it lists MCR, MDR, SRR, PDR, CDR, SIR, and CERR, per NPR 7123.1A and NPR 7120.8); (2) FM coverage within **system- and subsystem-level technical reviews** for those elements allocated FM functions; and (3) **dedicated FM technical reviews** held throughout the lifecycle. When/how used: the three tiers run in parallel across the program; the dedicated reviews are the layer this chapter specifies in detail.

- **The dedicated FM milestone reviews (Table 20)** — a recommended minimum set of seven FM-specific reviews, each tied to a project gate it should precede:
  - **FM Concept Review (FMCR)** — held in Phase A, before the project MCR (and the text also ties it to occurring before MDR).
  - **FM Architecture/Requirements Review (FMARR)** — held mid-to-late Phase B, before the project SRR/MDR and before PDR.
  - **FM Preliminary Design Review (FMPDR)** — held before the project PDR.
  - **FM Critical Design Review (FMCDR)** — held before the project CDR.
  - **FM Test Readiness Review (FMTRR)** — held before the project SIR/TRR, near the end of Phase C.
  - **FM Launch Readiness Review (FMLRR)** — held before launch.
  - **FM Critical Event Readiness Reviews (FMCERR)** — held as needed before specific mission-critical events.
  - When/how used: each gates entry to the next maturity stage; durations run roughly half a day to two days, scaled by mission class and how much FM is already covered in the program-level reviews.

- **Per-review specification template** — for each review, Sections 10.1–10.7 supply a **Description**, **Entrance Criteria** (the accomplishments and documentation that must be complete to hold a successful review), and **Success Criteria** (what determines the review passed or failed). Each review's criteria are captured in a paired table (Tables 21–27). When/how used: this is the consistent contract for running any of the seven reviews.

- **FM Milestone Review Questions (Table 28)** — a catalog of ~73 probing questions, each tagged with the review(s) it applies to (e.g., FMARR, FMPDR, FMCDR, FMTRR, FMLRR, FMCERR). When/how used: dual purpose — to direct reviewers to specific areas to probe, and to surface the detailed nature of the FM functions under review.

- **Optional quality-control reviews** — beyond the seven process reviews, the handbook names supplementary reviews that focus more on quality control than on the FM process: fault-analysis result reviews (e.g., PRA, FTA), FM phase/mode reviews (e.g., safe-mode, time-critical sequence), FM implementation peer reviews (e.g., flight-software walk-throughs), subsystem-specific FM reviews (e.g., GN&C, power), and FM test-procedure reviews. When/how used: added at the project's discretion based on scope and specifics.

- **Phased FM operations outline (Section 9, planned)** — a Phase-A-through-E plan for FM operations: Phase A (system operation guidelines; develop FM operations approach), Phase B (FM ConOps; revise operations approach; develop operations requirements), Phase C (refine operations requirements; detailed operations design; respond to allocated FM functionality from the flight/ground split), Phase D (operations V&V; define operating constraints such as flight rules; operator/team certification; contingency planning), and Phase E (vehicle operation; anomaly resolution; updating system behavior; critical events; lessons learned). When/how used: in Draft 2 this is an outline only — the section was explicitly deferred to later releases.

## Key Concepts

- **Why dedicated FM reviews exist.** The handbook lists six distinct rationales (a–f in Section 10): **Mind-Set** — an FM review's board and agenda are committed to asking "What if?" and "What performance is required in the presence of a failure?", whereas in a nominal-focused review failure scenarios are treated as a schedule tax with little time allotted; **Content** — FM agendas carry many FM-centric topics spanning the project's off-nominal behavior, and although the agenda is systems-level, key subsystems (flight software, GN&C, power) are covered so subsystem-FM and system-FM interactions and crosscutting issues become visible; **Logistics** — concentrating all FM issues in one focused 1–2 day review lets a 5–10 member board of NASA FM experts actually attend, which is hard to arrange across a long multi-week program review plus separate system/subsystem reviews; **Completeness** — reviewing FM in piece parts makes gaps nearly inevitable, because no one attends every fragment to integrate the whole; **Follow-Through** — FM reviews generate action items whose closure and approval are established metrics of review confidence and a key channel for modifying FM content; **NASA Lessons Learned** — the dedicated FM review evolved from informal/critical-event reviews into the forum where lead system engineers, institutional chief engineers, and FM experts work difficult system issues, catching disconnects early.

- **Entrance vs. success criteria.** Every review separates *what must be done to hold it* (entrance) from *what determines it passed* (success). The handbook supplies the general NASA SE Handbook entrance/success criteria as the baseline and then layers FM-specific criteria on top.

- **The documents that gate each review.** The entrance criteria are keyed to specific FM artifacts maturing over time: FMCR keys on the FM Concept Document, FM Development and Analysis Plan, and FM Technology Plan/Assessment; FMARR on the FM Requirements Document, preliminary FM V&V Plan, and FM Architecture Document; FMPDR on preliminary fault/scenario analyses, the preliminary FM Design Specification, and the FM V&V Plan with verification and validation matrices; FMCDR on final fault/scenario analyses, the final FM Design Specification, and completed V&V plan and matrices; FMTRR on the V&V plan/matrices and FM Test Procedures; FMLRR on the FM Verification and Validation Matrices, FM Test Procedures, the FM Operations Plan, and contingency procedures; FMCERR on the FM Strategy and contingency procedures.

- **What each review is really testing.** FMCR checks that FM's **scope/boundary matches the available resources and risk posture** (and reviews the safing strategy, the FM ConOps, the critical-events list, applicable technologies with TRL estimates, and the work plan). FMARR checks that **architecture and requirements are mutually consistent** and that requirements coverage is sufficient, with key drivers being the time-/mission-critical events list, the flight-and-ground hardware/software needed for diagnostics, expected ground response time, and the degree of allowed ground interaction. FMPDR demonstrates the **preliminary design meets requirements at acceptable risk within allocated constraints**, that the system has been adequately analyzed for faults, and that the FM team and project agree on a defined fault set to be managed. FMCDR demonstrates the **design maturity is consistent across subsystems so implementation can proceed**, and that the verification plan, system-level test plan, and operability (ConOps) are consistent with constraints and risk. FMTRR confirms the **system-level test plan and procedures are ready** and that prior subsystem testing/results/issues do not undermine the system-level FM design. FMLRR confirms **FM maturity is sufficient to launch** — testing, analysis, demonstrations, and contingency procedures complete. FMCERR confirms **FM readiness for a specific critical event**, covering the event timeline, predicted subsystem behavior, predicted FM responses, operational constraints, and pre-/post-event reconfiguration plans.

- **The fault-set agreement.** A recurring FMPDR/FMCDR success item is a program-accepted fault-set record — variously a Design-for-Minimum-Risk list, a single-point-failure exemptions list, or a fault-tolerance list — that formally captures which faults are managed and which single-fault-tolerance exemptions the project has accepted.

- **Requirements quality goals (from FMARR criteria).** System-level FM requirements should be a **complete flow-down from project-level requirements**, allocated down to subsystems, demonstrate adequate coverage for the analyzed faults, achieve a **reduction from the full fault list** (most requirements being one-to-many with faults rather than one-symptom-to-one-fault), and form a **safety-net structure** that guards against failures however they manifest.

- **TRL gating.** FM technology readiness is explicitly gated: the FMCR success criteria require a feasible plan to reach **TRL 6 by PDR**, with fallback options identified if it does not; FMPDR success requires any required new technology to actually be at TRL 6.

- **Test-as-you-fly and off-nominal injection (Table 28 themes).** The review questions repeatedly press on flight-representative testing — does the tested system represent the flight configuration ("test as you fly"), do tests inject sufficient off-nominal conditions to confirm robustness, do tests cover all operating modes, does the acceptance test plan screen for anticipated failure modes, and is FM software tested with high-fidelity hardware-in-the-loop in the flight configuration.

- **Configuration control of FM models, tools, and software.** Multiple questions across FMARR/FMPDR/FMCDR/FMTRR ask whether FM models, tools, analyses, software, and database parameters are validated and placed under configuration control, and whether reused/modified FM code is independently verified.

- **Centralized vs. distributed architecture probing.** The late Table 28 questions interrogate the architectural philosophy itself: the rationale for centralized vs. distributed FM, how centralized and distributed functions were allocated, how interactional problems in a distributed architecture are handled, and what criterion established that the top-level FM architecture is complete.

## Mental Models

- **Demand proof; do not assume success.** The MER lesson (NASA Lessons Learned #1743), shaped by the 1999 Mars Polar Lander failure, frames the review philosophy: continuously demand evidence the system will work rather than assuming risks are acceptable until proven otherwise. A review is where that proof is extracted.

- **Concentrate the experts, concentrate the issues.** The logistics rationale is a model in itself: a short, focused FM review is the only practical way to get scarce FM experts and the FM project staff in the same room for real back-and-forth; spreading FM across many long reviews guarantees the right people miss the right discussions.

- **Reviewing in pieces guarantees gaps.** The completeness rationale: off-nominal behavior only integrates into a coherent picture when someone walks the whole thing in one forum. Fragmented coverage means omissions and missed scenarios are near-certain.

- **A review is a gate keyed to a maturing artifact set.** Each FM review is anchored to specific documents reaching specific maturity (concept → requirements/architecture → preliminary design → final design → test readiness → launch readiness → event readiness). The review passes when those artifacts are complete *and* their FM-specific success criteria are met — the documents are the evidence.

- **Match FM scope to risk posture and resources.** The FMCR's job is fundamentally a sizing check: is the size and complexity of FM consistent with the mission's resources and NASA mission-risk classification? FM that outgrows its risk posture or its budget is a finding, not a virtue.

- **Tailor with caution, not by default.** For small Class C/D teams the handbook allows combining dedicated FM reviews with associated project/system reviews — but only if all FM-specific entrance and success criteria are still covered, and only after careful consideration before removing, combining, or tailoring any FM review.

- **Postmortems are how bad habits get unlearned.** The lesson on human capital and facilities (NASA Lessons Learned #1612) argues that failure-contributing habits persist unless personnel do thorough postmortems of failed projects — and that understanding the *successes* of recent missions deserves equal priority.

## Anti-patterns

The slice explicitly names these traps (as Pitfalls and Lessons Learned):

- **Grandfathering legacy/heritage flight-software code without detailed review.** The Section 10.1 Pitfall warns that reusing flight-software source code cuts both ways: it carries prior testing and worked-out bugs, but also any undiscovered bugs, plus fresh risk from interface, compiler, or system differences — made worse because heritage code rarely gets a detailed review and the original experts are often unavailable or too far removed to recall the logic's subtleties. The named **Recommended Practice** is to hold detailed FM code and logic reviews, cross-checking code and logic against the FM description for completeness and correctness.

- **Relying on analysis-by-similarity without genuine inheritance review.** The CONTOUR mishap lesson (NASA Lessons Learned #1385) warns that projects leaning on "analysis by similarity" should instead conduct real inheritance reviews early, evaluating the inherited item's actual capabilities and prior use against all mission-critical requirements — the board judged inadequate oversight especially dangerous when combined with nonstandard engineering practices.

- **Treating failure scenarios as a "tax" on a nominal-content review.** Implicit in the Mind-Set rationale: when FM rides inside a nominal-focused review, failure walk-throughs get squeezed to the occasional scenario because schedule pressure treats them as overhead — which is precisely why dedicated FM reviews exist.

## Key Takeaways

1. **Evaluate FM at three levels** — as a topic in major program reviews, within system/subsystem reviews, and through **dedicated FM technical reviews** — because piecemeal coverage reliably leaves gaps.
2. The handbook defines a **minimum set of seven FM reviews** — FMCR, FMARR, FMPDR, FMCDR, FMTRR, FMLRR, FMCERR — each timed to precede a corresponding project gate and each with its own **entrance and success criteria**.
3. **Dedicated FM reviews are justified on six grounds** — mind-set, content, logistics, completeness, follow-through, and accumulated NASA lessons learned — chiefly because they concentrate scarce FM experts and the full off-nominal picture in one focused forum.
4. **Each review is gated by maturing FM artifacts** (concept doc, requirements/architecture docs, design specs, V&V plan and verification/validation matrices, operations plan, contingency procedures) and by FM-specific success criteria, including a **program-accepted fault-tolerance / single-point-failure-exemption list**.
5. **Technology readiness is gated to TRL 6 by PDR**, and the review questions hammer on **test-as-you-fly**, off-nominal injection, hardware-in-the-loop testing, and **configuration control** of FM models, tools, and software.
6. **Tailoring is allowed but constrained**: small Class C/D projects may combine FM reviews with project/system reviews only if every FM-specific criterion is still satisfied and only after careful consideration.
7. **Operations (Section 9) is a deferred placeholder in Draft 2** — its Phase A–E outline (concept, requirements, design, V&V, operator certification, contingency planning, anomaly resolution, lessons learned) signals intent, not finished guidance.

## Connects To

- **NPR 7123.1A — NASA SE Processes and Requirements**: supplies the major lifecycle gates (MCR, MDR, SRR, PDR, CDR, SIR, CERR) the FM reviews are timed against (`nasa-npr-7123`).
- **NPR 7120.8** — NASA's management requirements for research-and-technology programs and projects: cited alongside NPR 7123.1A as governing the program/project lifecycle reviews FM participates in.
- **NASA SE Handbook (NASA/SP-2007-6105 Rev 1)**: the source of the *general* entrance and success criteria that each FM review layers FM-specific criteria onto (`nasa-se-handbook`).
- **Earlier chapters of this pack**: the FM Concept Document, Requirements Document, Architecture Document, Design Specification, V&V Plan, and Operations Plan (Sections 4.1.1–4.1.6, referenced throughout the review criteria) are the artifacts these reviews gate.
- **Reliability / safety analysis frameworks**: PRA and FTA appear as the basis for the optional fault-analysis result reviews, linking the review structure back to the dependability toolset (`nasa-pra`).
- **Technology Readiness Assessment**: the TRL 6-by-PDR gate in the FMCR/FMPDR criteria connects FM maturity to NASA/GAO technology-readiness practice (`gao-tra`).
