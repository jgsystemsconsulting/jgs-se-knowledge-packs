# NASA R&M Standard Patterns & Techniques

Reusable patterns drawn from NASA-STD-8729.1A (Revision A, 2017-06-13). Each has When / How / Trade-offs. These reflect the standard's objectives-driven posture — they tell you how to engage with the objectives and strategies, not which single method to run.

## Pattern 1: Address Every Objective with a Justification Ledger

**When to use**: during R&M planning, when deciding how deeply to treat each of the standard's objectives and strategies.

**How**: walk the R&M objectives hierarchy (Appendix A) and, for each objective, record an explicit entry — how it is addressed, to what depth, and why that depth fits the program's accepted safety-and-mission-success risk. The standard does not check that you ran a specific analysis; it checks that you reasoned about each objective and can defend the result at review.

**Trade-offs**: building the ledger is up-front effort and forces you to commit a rationale in writing; skipping it leaves you unable to demonstrate, at the milestone and readiness gates, that the objectives were satisfied to an acceptable level.

---

## Pattern 2: Plan by Reference, Not by Restatement

**When to use**: when establishing R&M requirements inside the SMA Plan (Section 5.1.2).

**How**: treat the R&M plan as a coordinating index. Specify and/or reference the other program plans, documents, and models that already carry the detail — derived R&M criteria, functional/performance requirements, applicable design and process standards, the deliverables schedule, organizational interfaces, and the evidence products — rather than duplicating them. Calibrate each activity's scope against the Appendix B minimums and document any alternative evidentiary method.

**Trade-offs**: a reference-based plan demands disciplined cross-document traceability and can break if linked documents drift; restating everything in the R&M plan creates redundancy that goes stale and contradicts the source documents.

---

## Pattern 3: Dial Scope by Mission Class

**When to use**: choosing how much of each evidence method to perform (Appendix B, Section 5.1).

**How**: take the top-level mission class (human spaceflight / Class A robotic) as the default-full scope baseline, then reduce scope as appropriate for higher-risk mission classes. Scope is a tailoring knob set by mission class and the Appendix B floor — not by the practitioner's preference. Record where on the dial you landed and why.

**Trade-offs**: scaling down saves cost on lower-criticality missions but transfers residual risk that must be accepted explicitly; scaling up everywhere wastes limited R&M resources on evidence the mission class does not warrant.

---

## Pattern 4: Separate the Doer from the Concurrer

**When to use**: throughout planning and at every review gate (Sections 5.1.3, 5.2.1–5.2.3).

**How**: keep the project/program (which produces the plan and the evidence) structurally distinct from the SMA Technical Authority (which concurs the plan is sufficient, verifies that independent evaluation was actually implemented, and concurs in the evidence at gates). Obtain concurrence on sufficiency *before* the work proceeds; obtain concurrence on adequacy and acceptable risk at each gate.

**Trade-offs**: the separation adds coordination overhead and a dependency on an external authority's schedule; collapsing the two roles produces self-assessed assurance that the standard explicitly refuses to accept.

---

## Pattern 5: Choose the Analysis by Failure Space vs. Success Space

**When to use**: selecting a reliability analysis for a given question (Ch 2, Ch 6).

**How**: first ask which space the question lives in. If you are reasoning about how things break and how breakage propagates, use a failure-space tool — FMEA/FMECA (bottom-up, inductive) or FTA (deductive, top-down from a failure event). If you are reasoning about the conditions under which the system keeps working, use a success-space tool — RBDA (an unbroken input-to-output path is success). Then check direction: inductive bottom-up tells you effects from parts; deductive top-down tells you causes from a defined event.

**Trade-offs**: picking the wrong space wastes the analysis — a success-space model will not enumerate single-point failures, and a bottom-up FMEA will not efficiently prove a top-event probability; running both costs more but cross-checks the result.

---

## Pattern 6: Gate Each Evidentiary Method Before Spending

**When to use**: selecting from the R&M Evidentiary Methods catalogue (Ch 6).

**How**: read the method's "in what circumstances it is called for" column as a cost-control gate before committing resources. Reserve expensive, specialized analyses (e.g., Sneak Circuit Analysis) for the most safety- or mission-critical hardware; invoke environment-specific analyses (IESD, surface ESD, SEE, micrometeoroid/debris) only when that threat is present; treat always-on low-cost analyses (part stress) as part of the basic design process. Then sequence the method against design maturity — functional FMECA and FTA early, piece-part FMECA and worst-case analysis once candidate flight designs exist.

**Trade-offs**: gating risks under-analyzing if the circumstances test is applied too strictly; running every method regardless of circumstance exhausts the R&M budget on evidence the objective did not require.

---

## Pattern 7: Distinguish the Two Availabilities by Stakeholder

**When to use**: whenever an availability requirement or number is in play (Ch 2).

**How**: ask whether the figure is the designer's world or the logistician's world. Use Inherent Availability — Ai = MTTF / (MTTF + MTTR) — for what the design alone controls. Use Operational Availability — Ao = MTBF / (MTBF + MDT) — when spares, logistics delay, ready time, and administrative downtime matter; Ao is the quantitative bridge between readiness objectives and supportability. The gap between the two is exactly the slack governed by supportability decisions, not design decisions.

**Trade-offs**: tracking both numbers is more work and demands logistics data the design team may not own; collapsing them to one figure hides whether a shortfall is a design problem or a sustainment problem.

---

## Pattern 8: Build the Parts-Pedigree Chain for Forensic Traceability

**When to use**: controlling reliability through parts selection on critical hardware (Ch 6).

**How**: chain Approved Parts List → Parts Control Plan → Parts Traceability. Restrict parts to those with known failure rates and lifetimes, control how part lots and characteristics are managed, and trace pedigree from manufacturer to user so a failure can be walked back to its source and production lot. Reliability evidence then becomes both predictive (known rates) and forensic (lot traceback after a failure).

**Trade-offs**: maintaining traceability records and an approved-parts discipline is administrative overhead and can constrain part choices; without it, a part failure cannot be tied to a lot, blocking effective corrective action across the fleet.
