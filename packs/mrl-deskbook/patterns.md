# MRL Deskbook Patterns & Techniques

Reusable patterns drawn from the DoD MRL Deskbook (Version 2022). Each has When / How / Trade-offs.

## Pattern 1: Map MRL Targets to the Acquisition Milestone

**When to use**: at the start of planning any Major Capability Acquisition (or MTA/UCA) effort, to fix what maturity each gate expects.

**How**: pin a target MRL to each gate. For MCA: MRL 4 on each competing solution at MSA/Milestone A, MRL 6 by Milestone B, MRL 7 by CDR, MRL 8 for LRIP at Milestone C, MRL 9 for FRP. For Rapid Prototyping (MTA), enter at MRL 4 and climb through MRL 6 and MRL 8; for Rapid Fielding, enter at MRL 8. For UCA, hit MRL 7 at the Course of Action point, MRL 8 at the Development Milestone, MRL 9 in production. Assess against the current target while reviewing the *next* level's criteria to find gaps early.

**Trade-offs**: the numbers and timing shift by pathway, but the discipline is constant — assess, plan maturation, fund it, reassess before transitioning. Forcing a fixed template across pathways misreads where manufacturing risk actually bites.

---

## Pattern 2: Run the Eight-Activity Assessment Flow

**When to use**: whenever you conduct an MRL Assessment, scaled to the program's size and risk.

**How**: follow the Figure 4-1 sequence — determine initial scope; determine taxonomy and schedule; form and orient the team; orient the contractors; request a contractor self-assessment; set the site-visit agenda; conduct the assessment; prepare the report. Use the nine filtering questions (Materials, Cost, Design, Manufacturing Process, Quality, Schedule, Facilities, Supply Chain, Industrial Base) to decide *what* to assess, and the on-site selection criteria to decide *where* to spend scarce visit effort. Assess top-down through the hierarchy, then report bottom-up.

**Trade-offs**: visiting every supplier is rarely feasible — high-risk locations go on-site, the rest use written self-assessments analyzed by the team. Skipping the self-assessment step loses the contractor's own baseline of where each technology and process stands.

---

## Pattern 3: Resist the Single-Number and Weakest-Link Rollup

**When to use**: when reporting the maturity of a technology, product, or whole system.

**How**: report a level-by-level picture, with each MRL identified to expose its specific risks, rather than collapsing the whole element to one number. Treat the threads as a tripwire — a component reported below target signals where component-level detail is needed to explain the shortfall and find the steps to mature it.

**Trade-offs**: a level-by-level read is more work than quoting one number, but a single MRL usually adds little value (maturity varies widely element-to-element), and a naive weakest-link rollup overstates risk and misleads worst for complex subsystems and systems.

---

## Pattern 4: Build a Manufacturing Maturation Plan for Every Shortfall

**When to use**: whenever an assessment finds an element below its target MRL.

**How**: write an MMP per below-target element using the 12-item outline — title; problem statement (risk vs. cost/schedule/performance); solution options; a maturation plan with schedule and funding; key activities; fallback preparations; the latest date a fallback can be chosen; funding status; specific actions with owners; prototypes/test articles with how the test environment maps to the manufacturing environment; threshold performance; and the MRL criteria to be met and when. Prepare it jointly with the contractor and attach it to the assessment report; prefer housing it inside the program's Risk Management Plan rather than as a separate CDRL.

**Trade-offs**: an MMP per shortfall is more planning overhead than a single risk register entry, but a low MRL early is acceptable only *because* the MMP turns it into funded, scheduled, owned action; an assessment with no MMP for its gaps is an unfinished thought.

---

## Pattern 5: Decide What to Do at a Milestone Shortfall

**When to use**: when an assessment finds risk areas below the milestone target (e.g., MRL 6 before Milestone B, MRL 8 before Milestone C).

**How**: the PM has the same three courses of action at every gate — (1) request a delay in the milestone decision to buy time for risk reduction; (2) switch to a lower-risk manufacturing approach or alternative design; or (3) carry the higher risk forward into the decision, accompanied by an MMP that includes the funding to close the gap.

**Trade-offs**: delaying costs schedule; switching approach may forfeit a preferred design; carrying risk forward needs an honestly funded plan. The MRL Assessment informs the decision but does not make it — decision-makers weigh the risk to program success.

---

## Pattern 6: Put MRL Maturity into the Contract

**When to use**: when writing an RFP or solicitation so manufacturing maturity shapes who wins and what the winner must do.

**How**: use Section L to define what the offeror submits (manufacturing maturity, recognized risks, quality level, ideally a self- or independent assessment against the MRL criteria) and the matching Section M rubric to score it. Bind performance through SOW "shall" statements: conduct MRL Assessments, develop and track MMPs, schedule assessments in the IMS, integrate risk into the program risk system, and flow requirements down to key and critical suppliers. Task work through AS6500A (with MIL-HDBK-896A for implementation) and quality through AS9100D/ISO 9001/IATF 16949 — the MRL Criteria Matrix grades maturity but does not direct work. Keep deliverable DIDs minimal; tailor DI-MGMT-81889B, DI-SESS-81974, and DI-QCIC-81794A onto the DD Form 1423 CDRL only as needed.

**Trade-offs**: Sections L and M act once at award; the SOW, DIDs, and CDRLs act continuously after award — a program needs both halves or it leaks risk. Demonstrate conformance via a cross-reference matrix backed by objective evidence, not assertions; over-generating DIDs when the same evidence lives in command media is wasteful.

---

## Pattern 7: Tailor Criteria Without Burying Risk

**When to use**: when applying the criteria to an S&T effort, a single/limited-system build, a ship, a sustainment activity, or an industry product line.

**How**: copy and trim the questionnaire to the item under assessment, limited to the target MRL or one level below. Keep traceability to the criteria, document and justify any criterion you cannot assess, and hand that justification to the transition customer. When one criterion is infeasible (often because it reaches into a follow-on program the effort does not fund), look within the same thread for a sibling criterion that *can* be assessed. Front-load maturity where there is no second chance: single/limited systems target system-level MRL 8 at CDR; space systems add full as-built traceability and a quality/reliability emphasis; ships follow the Navy 2-pass, 6-gate map (MRL 6 at SD1/PDR, MRL 7 by Milestone B/CDR, MRL 8 for PRR before keel-laying).

**Trade-offs**: tailoring is legitimate and expected, but tailoring out a criterion without assessment converts it into a buried known-unknown that surfaces in a costlier phase. Assess to the phase rather than skipping what looks hard — and don't pour scarce S&T resources into maturation that isn't feasible.

---

## Pattern 8: Screen Operational-Technology Cybersecurity in the Assessment

**When to use**: whenever an MRL Assessment exercises the OT cybersecurity criteria embedded in the threads.

**How**: first resolve two routing questions — what information the facility handles (classified → FAR 52.204-2; Controlled Technical Information → DFARS 252.204-7012) and whether it is a Federal System (FISMA / FIPS 200 / NIST SP 800-53) or a Non-Federal System (NIST SP 800-171 for CUI, assessed under DFARS 252.204-7019/7020 with results in SPRS). Then ask top-level, common-sense questions from the NIST SP 800-82 concepts: layered networks, corporate/IT/OT separation, a DMZ architecture, redundant networks for the process control system, protection of process data and non-conformance information, and operator authentication. Pull in a cybersecurity expert when the discussion turns highly technical.

**Trade-offs**: this is a screen, not an audit — the goal is to surface major gaps, not certify compliance, so SMEs need not be cyber specialists. Treat CMMC as the certification process over NIST SP 800-171, not the source of the requirements; small manufacturers should use PTAC/MEP/CSET support and run an internal self-audit before external audits.
