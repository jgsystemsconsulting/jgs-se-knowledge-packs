# FAA-HDBK-006D (RMA) Patterns & Techniques

Reusable patterns drawn from FAA-HDBK-006D (2020). Each has When / How / Trade-offs. The handbook is guidance only and does not mandate any single method.

## Pattern 1: Classify Criticality Before Picking Any Number

**When to use**: at the start of requirements authoring, before any availability or MTTR target is written.

**How**: locate the system by its **service thread** in the NAS Enterprise Architecture, then run a **Service Risk Assessment** to assign one of four **Service Thread Loss Severity Categories** — Safety-Critical, Efficiency-Critical, Essential, Routine. The category, via NAS-RD-2013, hands you the availability floor (down to 0.99999) and restore-time ceiling; only then do you allocate or derive subsystem values.

**Trade-offs**: front-loading the criticality assessment feels slow when stakeholders want a target now — but a number chosen without criticality is arbitrary, and over-specifying a routine service wastes money. The assessment also needs a wide stakeholder convening (operations, safety, logistics, T&E, the NAS Resiliency Team).

---

## Pattern 2: Allocate Through the Reliability Block Diagram

**When to use**: during Requirements Development, once the functional architecture exists, to push system-level RMA targets down to subsystems.

**How**: build the functional architecture (functional analysis per the SEM), derive the **Reliability Block Diagram (RBD)** from it, assign reliability/availability to each block, and model success as an unbroken input-to-output path. For a series target, give each of n independent subsystems the **nth root** of the system figure; for redundancy, model parallel paths. Verify that the product of subsystem availabilities meets the system goal.

**Trade-offs**: series multiplication is unforgiving — a chain of "good enough" subsystems can miss a demanding target, forcing redundancy (cost, complexity). Equal nth-root allocation is simple but rarely optimal; unequal allocation needs heavier math. Top-down allocation is wrong for gracefully-degrading remote/distributed systems and dependency-coupled infrastructure (see Pattern 6).

---

## Pattern 3: Pair Inductive and Deductive Failure Analysis

**When to use**: throughout conceptual and preliminary design, to find design faults the reliability math cannot expose.

**How**: run **FMEA** bottom-up (inductive — from each part/function failure mode outward to effects) and **FTA** top-down (deductive — from a feared top-level event down to contributing causes), and let them meet in the middle where multi-event failure paths appear. Add **criticality** to the FMEA to get a **FMECA** that ranks modes by severity. Use an **Ishikawa** diagram to trace a top event to root causes.

**Trade-offs**: FMEA in isolation has limited validity and misses complex/multiple failures; FTA alone may miss bottom-level failures — neither is trusted alone. Ishikawa clutters and turns subjective on complex systems. Plain FMEA does not rank criticality; you need FMECA for that.

---

## Pattern 4: Predict with Distributions When Real Data Is Missing

**When to use**: when the system is too immature or the data too costly to gather, but a figure of merit is still needed.

**How**: pick the **probability distribution** whose shape matches the phenomenon — Normal (symmetric repair variation), Exponential (memoryless constant-rate failures over time), Poisson (counts of rare events in an interval), Lognormal (positive-only skewed repair times), Binomial (yes/no trials), Weibull (tunable failure-rate trend; reduces to Exponential at shape = 1), or Empirical (nothing parametric fits). Build a **data-collection plan** and treat **confidence intervals** and a **statistically significant sample** as the gate on trusting the result.

**Trade-offs**: distributions are models, not truth — a mismatched distribution makes results useless or misleading. Never use the Normal for time variables (it yields negative times); prefer the Exponential. Tighter confidence and higher availability targets demand more data, traded against time and cost.

---

## Pattern 5: Field-Then-Grow for Software-Intensive Systems

**When to use**: for complex NAS automation software whose reliability cannot be proven statistically before fielding.

**How**: accept that the software will be fielded short of its target, then drive a **reliability growth** program: shift the headline metric from MTBF to **problem-report metrics**, accumulate operating hours across many installations to surface and remove defects, and use **software FMEA / software fault trees / fault taxonomies** (design/code/test) to localize and classify defects. Before vendor selection, use **Government early software reliability prediction** (organizational maturity + process + domain knowledge → defect density, needing a SLOC estimate; IEEE 1633-2016; the Neufelder Full-Scale Model forms A/B/C).

**Trade-offs**: software has no wear-out phase and every new feature/fix temporarily *raises* failures — hardware improvement curves do not transfer. Early prediction supplements but does not replace DO-278A / AMS-mandated development work. Deeper Neufelder forms (94 → 226 → 377 questions) buy confidence at the cost of access to more development artifacts.

---

## Pattern 6: Match the Allocation Method to How the System Fails

**When to use**: when specifying RMA for systems that are not centralized, software-intensive information systems.

**How**: classify the system as **Information**, **Remote/Distributed**, or **Infrastructure**. Use top-down mathematical availability allocation for **Information Systems**. For **Remote/Distributed Systems** (sensors fanning in, services fanning out), achieve availability through diversity and overlapping coverage and set element-level targets from lifecycle cost and SME judgment on element count/placement — not an arbitrary "r of n" threshold. For **Infrastructure Systems** (power, HVAC), use a set of standard configurations matched to the supported Service Threads' availability needs.

**Trade-offs**: forcing top-down "r of n" allocation onto remote/distributed subsystems produces unrealistic requirements (e.g., declaring a 50-radar surveillance subsystem "down" at 48 of 50). Infrastructure violates the independent-failure assumption — it can directly cause failures in systems it supports — so RMA math does not apply. SME-judgment allocation is less auditable than a formula but more faithful to operational reality.

---

## Pattern 7: Bridge Enterprise Requirements to a Procurement Package

**When to use**: on the acquisition side, translating NAS-level RMA requirements into a contract and overseeing a developer.

**How**: run the six RMA technical-management tasks — Preliminary Requirements Analysis (the "bridge"), Procurement Package Preparation (**SSD + SOW + IFPP**), Proposal Evaluation (reliability modeling, fault-tolerant design, performance modeling — with **substantiated recovery-time compliance** as the critical factor), Design Monitoring (formal reviews, TIMs, separate fault-tolerance risk threads), Testing & Verification (fault-tolerance/functional/reliability-growth tests), and Requirements Analysis & Maintenance (keep Service Thread mapping flexible).

**Trade-offs**: heavy up-front specification and oversight cost coordination across every process owner, but a system bought against a weak RMA package will not meet its requirements. Separate risk-management threads for infrastructure, software error-handling, and performance add process overhead that a single risk register would lack.

---

## Pattern 8: Close the Loop After Fielding

**When to use**: in Monitoring and Post-Implementation, once the system is in service.

**How**: treat post-implementation as a control system — feed **NAPRS/NASPAS** data into **DCACAS/FRACAS**, identify and track RMA issues, and emit corrective action by design change, requirement change, waiver, or new investment (tech refresh/sustainment). Use **FMECA ↔ FRACAS** as a reinforcing loop: FRACAS evidence verifies the FMECA was complete; the FMECA supplies the severity framework FRACAS analysis uses.

**Trade-offs**: fielded RMA degrades (added code complexity, traffic growth, end-of-life platforms), so monitoring is continuous, not a filed report. The closed loop costs sustained data discipline, but without it degradation goes undetected until it bites.
