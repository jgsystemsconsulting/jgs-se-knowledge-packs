# NASA System Safety Handbook v2 Cheatsheet

## Core Decision Rules

**Is this system adequately safe?**
→ YES only if BOTH: (1) meets minimum tolerable safety level AND (2) is ASARP.
→ If meets minimum but not ASARP → sub-optimally safe; pursue further improvements.
→ If ASARP but below minimum → inherently unsafe system type; requires fundamental redesign.
→ If neither → unsafe as designed; immediate intervention required.

**How deep should my ISA be?**
→ Priority 1 (human spaceflight, >$1B, strategic importance): full PRA + qualitative analysis.
→ Priority 2 ($250M–$1B): qualitative analysis + targeted PRA where appropriate.
→ Priority 3 (<$250M): qualitative analysis only.
→ Within any mission: weight analytic depth toward highest-criticality scenarios.

**Who is responsible for what?**
→ Acquirer: sets requirements, evaluates RISC, accepts risk. Does NOT develop the safety case.
→ Provider: achieves safety, develops RISC, develops SSMP. Does NOT accept risk.
→ When a Provider sub-tasks another organisation, the Provider becomes Acquirer for that relationship and inherits all Acquirer obligations.

**When does a RISC need to be updated?**
→ At every KDP — it is a living document, not a one-time submission.
→ After significant programmatic changes (budget, schedule, scope, technology).
→ After anomalies or test failures that shift the risk picture materially.
→ After ISA updates that change base-claim evidence.

**How do I set the probabilistic analytic requirement?**
→ Initial requirement = Safety Threshold ÷ Safety Performance Factor (SPF).
→ SPF = ratio of actual total loss probability to modelled known-risk probability (from historical analogues).
→ Mature requirement = Safety Goal ÷ SPF_mature (after ~125 flights of burndown).
→ Intermediate requirements follow exponential burndown between first-flight and mature values.

**When is an assurance deficit score acceptable?**
→ Rank 1–2: low deficit; generally acceptable for proceeding.
→ Rank 3: moderate deficit; document and manage as CRM risk; may require conditional approval.
→ Rank 4–5: high deficit; likely blocks RISC acceptance unless compensating evidence exists elsewhere in the tree.
→ Final call is always expert judgement, not mechanical threshold.

**When should I use VOI analysis?**
→ When a significant assurance deficit exists AND the decision maker is unsure whether to accept risk, add controls, or invest in more evidence.
→ VOI frames the three-way choice with expected costs and probabilities; does not replace the decision maker's judgement.

---

## Quick-Reference Table: RISC Components

| Component | Who develops | What it contains | Evaluated by |
|---|---|---|---|
| Operational Objectives Tree | Acquirer + Provider jointly | Hierarchy from fundamental principles to addressable objectives | Acquirer SS function |
| SSRA | Provider | All applicable requirements; feasibility assessment; gap analysis | Acquirer SS function |
| SSMP | Provider | 42-element plan linking requirements to activities, roles, schedules | Acquirer at KDP |
| ISA | Provider | Scenario-based system-level safety analysis; quantified performance measures | Acquirer Evaluation Team |
| Claims Tree | Provider | Top claim → intermediate → base claims, traceable to objectives | Acquirer Evaluation Team |
| Direct Evidence | Provider | Quantitative risk demonstration (PRA results, test data, failure rates) | Acquirer Evaluation Team |
| Supporting Evidence | Provider | Qualitative confidence (personnel quals, V&V, safety culture) | Acquirer Evaluation Team |
| Assurance Deficit Scores | Provider (self-scored) then Acquirer (independently scored) | 1–5 rating per base claim | Acquirer Evaluation Team |
| RISC Report | Provider | Full documented RISC including executive summary, argument, evidence, roadmap, unresolved issues | Acquirer |
| RISC Evaluation Report | Acquirer Evaluation Team | Summary + detailed findings; Acceptable/Unacceptable rating | Decision Maker |

---

## Tells and Smells

**Smell: Safety analysis delivered as a stack of deliverables with no unifying argument**
→ Tell: No claims tree; HAs, FMEAs, and PRA exist as separate documents with no cross-linking.
→ Fix: Build a claims tree linking each analysis to a base claim; document how the totality argues for the top claim.

**Smell: Safety threshold set equal to the PRA result**
→ Tell: No safety performance margin; assumes the ISA captures all risk.
→ Fix: Derive a UU risk margin from historical programme experience; set the analytic requirement below the threshold by the margin.

**Smell: Identical RISC submitted at every KDP**
→ Tell: No updates despite design changes, test results, or anomalies since last review.
→ Fix: RISC must be updated to reflect current system state; stale RISCs are invalid evidence for current risk acceptance.

**Smell: SCI list generated entirely from FMEA**
→ Tell: Bottom-up only; management practices, interface assumptions, and organisational factors absent from SCI list.
→ Fix: Supplement bottom-up FMEA with top-down ISA analysis to capture system-level and managerial SCIs.

**Smell: Evaluation team has deep expertise in one subsystem only**
→ Tell: Evaluation findings miss system-level interactions and cross-subsystem risk.
→ Fix: Evaluation team must include both subsystem experts AND personnel with broad system-level knowledge.

**Smell: RISC accepted but assurance deficits are not tracked**
→ Tell: Deficits noted in RISC Evaluation Report but not assigned to CRM risk owners.
→ Fix: Convert every significant deficit to a CRM risk statement with an assigned owner; track under NPR 8000.4A process.

**Smell: All deterministic requirements levied without tailoring**
→ Tell: Provider receives hundreds of requirements from legacy programmes without relevance assessment.
→ Fix: Acquirer must perform ASARP tailoring; exclude requirements that provide no discernible net safety benefit for this mission or that impose disproportionate cost/schedule penalty.

**Smell: ASARP treated as a checkbox ("we said we're ASARP") rather than demonstrated**
→ Tell: No design trade documentation showing alternatives were evaluated and the chosen design is on the ASARP frontier.
→ Fix: Document ISA-informed trade analyses showing that no remaining alternative provides safety improvement without disproportionate cost/schedule/technical sacrifice.
