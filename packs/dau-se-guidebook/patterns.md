# DoD Systems Engineering Guidebook Patterns & Techniques

Reusable patterns drawn from the DoD SE Guidebook (OUSD R&E, February 2022). Each has When / How / Trade-offs.

## Pattern 1: Scale the 16 Processes to the Program

**When to use**: at Technical Planning, and whenever a program's risk, size, or pathway differs from the heavyweight default.

**How**: assess the program's maturity, complexity, size/scope, acquisition pathway, and life-cycle phase. Right-size each of the 16 processes — simpler tools, less-frequent reporting, leaner products for lower-risk/less-complex programs — and document the scaled approach in the SEP. Never delete a process category; scale its depth.

**Trade-offs**: under-scaling buries a small program in process overhead; over-scaling strips a complex/high-risk program of the insight and control it needs. The SEP is where the scaling rationale is recorded and defended at review.

---

## Pattern 2: Event-Driven Review Gating

**When to use**: planning and conducting any of ASR/SRR/SFR/PDR/CDR/SVR-FCA/PRR/PCA.

**How**: define entrance and success criteria for each review in the SEP. Hold the review only when the system meets the entrance criteria. Assess products against success criteria, disposition all RFAs, report results, and feed the milestone decision. If entrance criteria are not met, delay the review rather than hold a hollow one.

**Trade-offs**: event-driven gating can slip the schedule when maturity lags — but holding a calendar-driven review produces false confidence and pushes risk downstream. The honest slip is cheaper than the hidden gap.

---

## Pattern 3: Keep the SEP a Living Document

**When to use**: throughout the program; especially before each technical review and whenever the technical strategy changes.

**How**: treat the SEP as the single source of technical truth — approach, risks, processes, resources, metrics, products, organization, design considerations, and review timing. Update it as the approach evolves; as a best practice, reapprove it before each technical review. Keep it consistent with the APB, TEMP, PPP, LCSP, IMP/IMS, WBS, and Risk Management Plan, in plain language with no redundancy.

**Trade-offs**: maintaining the SEP is ongoing effort; a stale SEP, however, misaligns reviewers and program reality and undermines every review keyed to it.

---

## Pattern 4: RIO Triage — Risk vs. Issue vs. Opportunity

**When to use**: continuously, whenever uncertainty or a problem surfaces.

**How**: ask *has it happened yet?* Not yet & bad → **risk** (likelihood × consequence matrix; accept/avoid/transfer/control). Already happened/happening → **issue** (consequence matrix; corrective-action burn-down). Not yet & good → **opportunity** (opportunity matrix; pursue/reject with cost-benefit). Route each to its own matrix and playbook.

**Trade-offs**: the discipline costs a moment of classification; misclassifying an issue as a risk wastes effort "mitigating" something already realized, and missing opportunities forfeits cost/schedule/performance upside.

---

## Pattern 5: TPMs with Leading Indicators

**When to use**: across development, to know early whether the design will meet requirements.

**How**: define TPMs with planned profiles (not just current values) and roll them into the TPM hierarchy. Add leading indicators that show the *trend toward* a threshold, so mitigation can start before a breach. Feed both into Technical Assessment and the reviews.

**Trade-offs**: defining good leading indicators takes analytical effort; without them you only learn of a shortfall after the threshold is already crossed, when options are fewer and costlier.

---

## Pattern 6: Engineer Design Considerations In, Don't Bolt On

**When to use**: from the earliest architecture decisions, for each of the 24 relevant design considerations.

**How**: in Technical Planning, identify which considerations apply and assign owners and SEP treatment. Generate design requirements and trades for each (safety, security, HSI, R&M, supportability, producibility, MOSA…) and balance them within Architecture Design and Implementation. Assess manufacturing readiness (MRLs) in parallel with TRLs. Carry evidence to reviews.

**Trade-offs**: early integration competes for the cost/schedule/performance budget up front — but retrofitting a consideration after CDR is far more expensive and sometimes infeasible.

---

## Pattern 7: Put SE on Contract via the RFP

**When to use**: when shaping a solicitation/contract.

**How**: the Systems Engineer drives the RFP technical content — SOW/PWS tasks, technical requirements, data deliverables (CDRLs/DIDs), required technical reviews, MOSA and data-rights provisions, and evaluation criteria — so the contract obligates the SE activities and products the program needs.

**Trade-offs**: thorough RFP technical content takes effort and can raise bid cost; omitting it means the program cannot reliably obtain required reviews, data, or rights after award.

---

## Pattern 8: Identify the SoS Type Before Setting Authority

**When to use**: when the "system" is actually multiple independently managed/operated systems.

**How**: classify the SoS as virtual, collaborative, acknowledged, or directed — this determines your real authority over constituent requirements, funding, and interfaces. Manage interfaces formally (Interface Management); negotiate rather than dictate where constituents are independent.

**Trade-offs**: acknowledging limited authority slows decisions and requires negotiation — but assuming central control you do not have leads to interface failures and unmet integration commitments.
