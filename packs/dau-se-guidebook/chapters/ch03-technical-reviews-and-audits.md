# Chapter 3: Technical Reviews and Audits

## Core Idea
A properly tailored series of **event-driven** technical reviews and audits provides knowledge-based control points across the Major Capability Acquisition life cycle. Each review/audit assesses technical maturity and risk against entrance/success criteria documented in the SEP, supporting milestone decisions and progressively maturing the design and the technical baselines.

## Frameworks Introduced
- **Event-driven review philosophy** — reviews occur when the system meets the entrance criteria, *not* on arbitrary calendar dates; SE is a knowledge-based, event-driven process.
  - When to use: always — the SEP must clarify the timing of events relative to other SE/program events and be updated as actual timing shifts.
- **The technical review process** — a repeatable structure: establish entrance criteria → assess products against success criteria → disposition action items (RFAs) → report results → inform the next decision.
  - When to use: for every review/audit in the sequence.
- **Baseline progression** — reviews establish and verify the three configuration baselines: **functional** (SFR), **allocated** (PDR), and **product** (CDR initial; PCA verifies as-built).
  - When to use: to know what maturity a given review gates.

## Key Concepts — the eight reviews and audits
- **ASR (Alternative Systems Review)**: confirms the preferred materiel solution(s) is technically feasible and the requirements are understood; closes the analysis-of-alternatives loop.
- **SRR (System Requirements Review)**: confirms system requirements are complete, baselined, and traceable to the validated capability need.
- **SFR (System Functional Review)**: establishes the **functional baseline**; confirms the system's functional definition is complete and traceable.
- **PDR (Preliminary Design Review)**: establishes the **allocated baseline**; confirms the preliminary design meets requirements at acceptable risk and is ready for detailed design.
- **CDR (Critical Design Review)**: establishes the initial **product baseline**; confirms the detailed design is mature enough to begin fabrication, integration, and coding.
- **SVR/FCA (System Verification Review / Functional Configuration Audit)**: verifies the system against the functional baseline — confirms the product performs as specified ("did we build it right").
- **PRR (Production Readiness Review)**: confirms the design, processes, and supply chain are ready to enter production at acceptable risk.
- **PCA (Physical Configuration Audit)**: confirms the **product baseline** matches the as-built/as-delivered configuration.
- **Products and criteria**: each review has a defined set of products and entrance/success criteria (the Guidebook provides per-review tables, e.g., ASR/SRR/SFR/PDR/CDR/SVR-FCA/PRR/PCA products-and-criteria tables).
- **RFAs (Requests for Action)**: action items raised at a review; must be dispositioned for the review to be complete.

## Mental Models
- A review is a *gate keyed to knowledge*, not a meeting on a date: if entrance criteria are not met, the right answer is to delay the review, not to hold it and paper over gaps.
- Walk the baselines: functional (SFR) → allocated (PDR) → product (CDR/PCA). If you cannot say which baseline a review establishes or verifies, you do not yet understand its purpose.
- "Did we build it right" (verification, SVR/FCA) is distinct from "did we build the right thing" (validation, operational test) — see ch05.
- Digital engineering changes *how* a review is conducted (models, authoritative source of truth, iterative analysis) but never *which* reviews are required.

## Anti-patterns
- **Calendar-driven reviews**: holding a review because the schedule says so, before the system meets entrance criteria — produces a false sense of maturity.
- **Leaving RFAs open**: declaring a review complete with undispositioned action items.
- **Skipping baseline discipline**: maturing design without establishing the functional/allocated/product baselines at the right reviews, breaking traceability and change control.

## Key Takeaways
1. Technical reviews are **event-driven** — triggered by meeting entrance criteria in the SEP, not by calendar dates.
2. The Major Capability Acquisition sequence: **ASR → SRR → SFR → PDR → CDR → SVR/FCA → PRR → PCA**.
3. Reviews establish/verify the **functional (SFR)**, **allocated (PDR)**, and **product (CDR/PCA)** baselines.
4. Each review has defined products and entrance/success criteria; **RFAs** must be dispositioned for completion.
5. **Verification** (SVR/FCA) ≠ **validation** — the former checks conformance to the functional baseline.
6. Reviews are knowledge-based control points that reduce risk and feed milestone decisions.

## Connects To
- **ch01 / SEP**: the SEP documents review timing and entrance/success criteria.
- **ch04 (Technical Management Processes)**: Technical Assessment conducts the reviews; Configuration Management owns the baselines.
- **ch05 (Technical Processes)**: Verification and Validation underpin SVR/FCA and operational test.
- **`nasa-npr-7123` pack**: NASA's review system (MCR/SRR/PDR/CDR/FRR…) — similar intent, different names and life cycle.
- **Engineering of Defense Systems Guidebook**: guidance on selecting/tailoring reviews per AAF pathway.
