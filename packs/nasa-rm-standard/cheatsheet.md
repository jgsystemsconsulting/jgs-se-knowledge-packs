# NASA R&M Standard Cheatsheet

Quick reference for NASA-STD-8729.1A (Revision A, 2017-06-13).

## Quick Decision Rules

**"Does this standard apply to my program?"**
- NASA Headquarters / Centers → **built-in** (approved for use).
- JPL, contractors, grant recipients, agreement parties → **only if** the contract, grant, or agreement specifies or references it.
- Facilities → **out of scope**, except critical technical facilities for Space Flight Systems per NPR 7120.5.

**"What does the standard actually mandate?"**
- It mandates **engagement** with the R&M objectives and strategies in planning, a **justification** of how deeply each is addressed (commensurate with accepted risk), and a **demonstration** at review — **not** any single method. It is objectives-driven, not process-prescriptive.

**"Where do R&M requirements live?"**
- Inside the **SMA Plan** required by NPR 7120.5 (addressing Appendix A objectives/strategies and Appendix B tables). There is **no** separate freestanding R&M plan.

**"Inherent or Operational availability?"**
- Designer's world, design only → **Ai = MTTF / (MTTF + MTTR)**.
- Adds logistics, spares, ready/admin downtime, both maintenance types → **Ao = MTBF / (MTBF + MDT)**; the bridge between readiness and supportability.

**"Failure space or success space?"**
- How it breaks / how breakage propagates → **failure space**: FMEA/FMECA (bottom-up, inductive), FTA (deductive top-down).
- Conditions under which it keeps working → **success space**: RBDA (unbroken input→output path = success).

**"Verification or validation?"**
- Meets its requirements → **verification** ("building the system right?").
- Reflects requirements and is acceptable to the user → **validation** ("building the right system?").

**"How much scope for an evidence method?"**
- Default-full at the **top-level mission class** (human spaceflight / Class A robotic); **reduce** for higher-risk classes. Floor set by **Appendix B**.

---

## The Objectives Hierarchy in One Picture

```
Top Objective  (sustain required performance over the lifecycle → mission success)
   ├─ SubObjective (a) conform to design intent, nominal & failed conditions
   ├─ SubObjective (b) stay functional over intended life / environment / usage
   ├─ SubObjective (c) tolerate faults, failures, anomalies (internal & external)
   └─ SubObjective (d) reach R&M sufficient to satisfy the availability requirement
        each Objective ── paired with ──▶ Strategy (≥1)   [alternation rule]
        block types: Objective · Strategy · SubObjective · Requirement · Context
```
Evidence and scope hang off the **bottom-level strategies** (leaves), not the top objective.

---

## The Failure Causal Chain

```
cause → fault → mechanism → mode → failure → effect
            (failure propagation crosses product boundaries;
             fault propagation spills one fault into others)
```
Locate an observed problem on this pipeline to know whether it is a root issue, an intermediate state, or a downstream symptom — and which analysis (FMEA, FTA) to point at it.

---

## Governance & Review Gates (Section 5)

| Stage | The project/program does | The SMA Technical Authority does |
|---|---|---|
| **Before work** (5.1.3) | Establish R&M requirements in SMA Plan; scope to mission class | **Concur** plan is sufficient |
| **Independent eval** (5.2.1) | Implement the independent-evaluation strategy | **Verify** it was actually implemented |
| **Milestone review** (5.2.2) | Show objectives/strategies addressed; products at maturity & meet standards; technical risks acceptable | **Concur** |
| **Readiness review** (5.2.3) | Show objectives/strategies addressed; **residual** risks acceptable | **Concur** |

Maturity + standards-conformance dominate the **milestone** gate; **residual-risk** acceptance dominates the **readiness** gate.

---

## Reliability Analysis Methods (Appendix C, reliability table — selected)

FMEA / FMECA · Fault Tree Analysis (FTA) · Availability Analysis · Reliability Modeling (Prediction/Allocation) · Reliability Tradeoff Studies · Worst Case Analysis (WCA) · Part Electrical Stress Analysis (PSA) · Thermal Analysis to part level · Structural Stress Analysis · Thermal Stress/Fatigue Analysis · Sneak Circuit Analysis · Physics of Failure · Single Event Effects (SEE) · Deep Dielectric Charging / IESD · Surface Charging / ESD · Micrometeoroid/Debris Analysis · Approved Parts List · Parts Control Plan · Parts Traceability · Limited-Life Item Analysis · Trend Analysis · Human Error Risk / Human Factors Task Analysis · Alert Reporting.

## Maintainability Analysis Methods (Appendix C, maintainability table)

Maintainability Modeling (Prediction/Allocation) · Maintenance Concept · Maintenance Plan · Maintenance Engineering Analysis · Reliability Centered Maintenance (RCM) · Logistics Support Analysis/Plan · Testability Analysis · Link Analysis · Tradeoff Studies.

**Each method has five columns**: *what is done / why / in what circumstances / when performed / NASA Preferred Reliability Practice number*. The table indexes the method; the referenced practice holds the procedure. **Gate on the "circumstances" column before spending.**

---

## Outcome Words vs. Method Words

- **Outcome (goal state)**: reliability · maintainability · availability · dependability · operational readiness · sustainability.
- **Method (how you get there)**: FMEA · FMECA · FTA · RBDA · RCM · LORA.

Sort any defined term into one bucket — it reflects the standard's objectives-first posture.

---

## Tells & Smells

- **Looking for a required procedure in the standard** → wrong layer; it owns intent and approach families, you supply the method.
- **An objective addressed with no recorded justification** → fails the demonstration at the review gate.
- **A standalone "R&M Plan"** → R&M requirements belong inside the **SMA Plan** (NPR 7120.5).
- **Self-asserted independent evaluation** → the SMA Technical Authority must *verify* independence happened.
- **One "availability" number** → say whether it is **Ai** (design) or **Ao** (with logistics); the gap is a supportability decision.
- **Running every analysis regardless of circumstance** → the "circumstances" column is a cost gate; reserve the expensive ones for critical hardware.
- **Program-defined criticality/severity assumed standard** → the standard leaves those classifications to each program/project.

---

## Source Anchors

- **Applicable government document**: NPR 7120.5 (the only one; no non-government applicable documents).
- **Facility R&M routes elsewhere**: NPD 8831.1, NPR 8820.2, NPR 8831.2, NASA RCM Guide, NASA RCBEA Guide.
- **Appendices**: A — Objectives Hierarchy; B — Hierarchy with Scope Identification; C — R&M Evidentiary Methods; D — References. (52 pages total.)
