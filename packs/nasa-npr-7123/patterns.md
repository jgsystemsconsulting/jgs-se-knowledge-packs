# NASA NPR 7123.1D Patterns & Techniques

## Pattern 1: Recursive SE Engine Application

**When to use**: Any time a system is decomposed into lower-level products; whenever a new product layer is identified in the breakdown hierarchy.

**How**: Apply all 17 common technical processes to *each* product layer, not just the top level. System design processes flow top-down (expectations → requirements → logical decomposition → design solution); product realization processes flow bottom-up (implement/integrate → verify → validate → transition). Technical management processes run in parallel at every layer throughout.

**Trade-offs**: Applying the full SE Engine at every layer increases process overhead; customise the depth of application at lower levels based on risk and complexity, but never eliminate a process category entirely without ETA approval.

---

## Pattern 2: Tailoring vs. Customizing Decision

**When to use**: Whenever the standard SE approach does not fit the program/project; before assuming a deviation is needed.

**How**: First determine whether you are seeking *relief from what must be done* (tailoring — requires ETA-approved waiver or deviation) or *choosing how to do what must be done* (customizing — no waiver, document in SEMP). Write the rationale, get ETA concurrence on the approach, and capture the decision in the SEMP's compliance matrix (Appendix H).

**Trade-offs**: Misclassifying tailoring as customizing creates a compliance gap; over-classifying customizing as tailoring adds unnecessary approval burden. The key test: does the NPR requirement still get met in spirit? If yes → customizing. If no → tailoring.

---

## Pattern 3: ETA Independence Preservation

**When to use**: When appointing or working with a program-level ETA; when managing a program/project where engineering decisions intersect with cost or schedule pressure.

**How**: Ensure the ETA is funded independently of the program budget. The ETA seeks concurrence from the program manager when appointed, but the ETA cannot be the program manager. ETAs raise dissenting opinions through the formal dissent process (NPR 7120.5). Technical Authority flows from the Administrator through the Chief Engineer to Center Directors — not from the program.

**Trade-offs**: Independent ETA adds overhead and can create friction; this friction is the intended check-and-balance. Reducing ETA independence to streamline decisions is a risk acceptance that must itself go through the TA process.

---

## Pattern 4: Event-Based Review Scheduling

**When to use**: When planning program/project life-cycle reviews; when there is pressure to schedule reviews to meet calendar milestones.

**How**: Schedule reviews only when entrance criteria are satisfied (technical baseline maturity). Identify entrance criteria early using Appendix G guidance; customise them for your program type and risk posture. Build the review schedule around technical readiness milestones, not arbitrary calendar dates. If products are not ready, delay the review rather than proceeding with incomplete entrance criteria.

**Trade-offs**: Event-based scheduling can make program plans harder to commit to early; offset by building conservative float around review milestones and tracking TPMs/leading indicators as predictors of review readiness.

---

## Pattern 5: MOE → MOP → TPM Cascade

**When to use**: When establishing the performance measurement framework for any system or subsystem.

**How**: (1) During Stakeholder Expectations Definition, work with stakeholders to define MOEs — qualitative measures of mission/product acceptability. (2) During Technical Requirements Definition, translate each MOE into two or more quantitative MOPs that serve as "design-to" targets. (3) From the MOPs, select the subset most predictive of technical health to become TPMs — the measures actively tracked against plan through the life cycle. (4) From TPMs, designate leading indicators (minimally: mass and power margins for hardware/powered systems).

**Trade-offs**: Too many TPMs creates reporting burden without adding insight; too few risks missing early warning signals. Target 6–12 TPMs for a typical project, ensuring leading indicators are included.

---

## Pattern 6: SEMP as Living Technical Contract

**When to use**: At programme/project inception and at every major life-cycle review milestone.

**How**: Establish the initial SEMP early in Formulation. At each major life-cycle review (through SIR), update the SEMP to reflect the current SE strategy, customisation decisions, TPM status, and team structure. Have both the ETA and the program/project manager reapprove. Present the SEMP at each review as evidence of continuous technical planning — not just as a one-time compliance deliverable.

**Trade-offs**: Keeping the SEMP current requires ongoing effort; the cost is offset by the benefits of having a single authoritative reference for the technical approach. A stale SEMP signals a disengaged technical team.

---

## Pattern 7: Bidirectional Requirements Traceability

**When to use**: Throughout the Technical Requirements Definition and Requirements Management processes; especially before any major life-cycle review.

**How**: Establish traceability from every derived requirement upward to a parent requirement or stakeholder expectation, and downward to the design elements or lower-level requirements it is allocated to. Manage this traceability in a requirements management tool. At each review, demonstrate that no orphan requirements exist (no parent) and no unallocated requirements exist (no children below the allocation level).

**Trade-offs**: Full bidirectional traceability is labour-intensive to establish and maintain; automate where possible. The cost of not maintaining it — discovering missing allocations at CDR — is typically much higher.

---

## Pattern 8: Verification Before Validation

**When to use**: When planning a V&V programme; when interpreting review exit criteria involving V&V results.

**How**: Always sequence product verification (does it meet its specifications?) before product validation (does it work in the intended environment for the intended purpose?). Verification is performed against requirements/specifications; validation is performed against baselined stakeholder expectations and ConOps. Verification anomalies must be resolved before validation proceeds; validation anomalies must be resolved before product transition.

**Trade-offs**: Sequential V&V takes time; for lower-risk systems, some overlap may be acceptable if customised into the SEMP and approved by the ETA. However, skipping verification and relying solely on validation is not acceptable — non-conformance to specification may not be caught in operational test.

---

## Pattern 9: Technology Maturity Gating

**When to use**: When incorporating any new or evolving technology into a program/project; when reviewing a Technology Development Plan.

**How**: Assess TRL at programme formulation and update at every status review. Establish explicit TRL gates tied to life-cycle KDPs — typically TRL 6 minimum at system PDR for critical technologies, TRL 7+ before CDR for mission-critical elements. For non-TRL maturity scales, maintain a documented mapping to TRL.

**Trade-offs**: Rigid TRL gates can delay programmes when one critical element is immature; manage via targeted Technology Development Plans with independent resourcing, rather than accepting schedule pressure that forces incorporation of immature technologies.

---

## Pattern 10: Contracted Work SE Governance

**When to use**: Whenever a program/project element is contracted to an external provider.

**How**: (1) Before award: define the 17 common technical processes requirements in the SOW and DRL; specify insight/oversight activities in the surveillance plan; get ETA approval; work through the contracting officer. (2) During performance: execute insight/oversight as contracted; any modifications require the same pre-award SE activities. (3) At completion: participate in acceptance reviews and formal product transition. Document all three phases in the NASA SEMP.

**Trade-offs**: Defining extensive contractor SE requirements increases solicitation complexity and may reduce competition; calibrate requirements to the risk posture of the work, not to a maximum-oversight default.

---

## Pattern 11: Review Completion Protocol

**When to use**: At the close of every life-cycle review.

**How**: Confirm that: all RIDs and RFAs have agreed disposition with TA concurrence; the review board report and minutes are distributed; plans exist for all identified issues and actions; review board chairperson has reported to management; and the Decision Authority has signed a decision memo. Do not treat the end of the review meeting as review completion — the administrative closure steps are mandatory (Section 5.2.3).

**Trade-offs**: Administrative closure adds time after the review event; budget this time into programme schedules rather than treating it as discretionary.

---

## Pattern 12: HSI Integrated Planning

**When to use**: From the earliest life-cycle phase; not as a late-stage add-on.

**How**: Document the HSI approach in the SEMP or a stand-alone HSI Plan (required for Category 1/Class A programmes). Address all human roles: crew, operators, users, maintainers, assemblers, and ground support personnel. Baseline the HSI approach at SRR (SE-66). Co-own the HSI planning across ETA, SMA TA, and HMTA from the start. Use NASA/SP-20210010952 for guidance on HSI content and tailoring criteria.

**Trade-offs**: Early HSI planning requires investment before human interface designs are fixed; this is intentional — late-cycle human factors changes are disproportionately expensive and often safety-critical.

---

## Pattern 13: TPM Leading Indicator Monitoring

**When to use**: Continuously from MDR/SDR onwards; particularly at every periodic technical review.

**How**: Establish mass and power margins as leading indicators in the SEMP (SE-62, SE-63). Track current margin against planned margin trajectory at each technical review. When margins trend outside the expected band, trigger a technical assessment and corrective action analysis before the shortfall becomes unrecoverable. Report TPMs to the Program/Project Manager on the agreed reporting interval (SE-61).

**Trade-offs**: Tracking margins alone is necessary but not sufficient; select additional TPMs that are predictive for your specific system's risk drivers (e.g., thermal margin for deep-space missions, data latency for real-time systems).

---

## Pattern 14: Compliance Matrix Maintenance

**When to use**: From programme/project inception; updated whenever tailoring decisions change.

**How**: Complete the Appendix H compliance matrix for every NPR 7123.1D requirement. Record whether each requirement is met as-written, tailored (with waiver/deviation reference), or customised (with SEMP section reference). Include the matrix in the SEMP. Have the ETA review and concur with the completed matrix. Present the updated matrix at each life-cycle review.

**Trade-offs**: Maintaining the compliance matrix is an overhead activity; the benefit is a clear, auditable record of every tailoring decision that prevents compliance disputes at reviews and audits.
