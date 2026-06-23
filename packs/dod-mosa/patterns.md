# DoD MOSA Patterns & Techniques

Reusable patterns drawn from the OUSD(R&E) *Implementing a MOSA in DoD Programs* guidebook (Feb 2025). Each has When / How / Trade-offs. Wording is synthesized, not reproduced.

## Pattern 1: Run the Cost-Benefit Gate Before Committing to MOSA

**When to use**: at the front of the decision, before MOSA is baked into strategy or contract.

**How**: weigh MOSA's long-term advantages (flexibility, lower life-cycle cost, faster technology insertion, competition) against its risks and its effect on near-term cost and schedule, and compare alternative courses of action. Carry the result into the AoA/Economic Analysis so each candidate solution's MOSA approach is on the record.

**Trade-offs**: the analysis costs time up front and can look unfavorable under near-term cost pressure — but committing to (or skipping) modularity without it tends to surface as expensive surprises later. Decide the *desired* level of modularity here rather than defaulting to maximum.

---

## Pattern 2: Work the Five-Step Interface Lifecycle as a Pipeline

**When to use**: continuously across the acquisition life cycle, once MOSA is adopted.

**How**: move through *plan → modularize → identify interfaces → define interfaces → standardize interfaces* (Figure 3-1). Plan measurable MOSA objectives and governance; decompose capability into self-contained functional modules; locate the boundaries where modules exchange data, signals, or commands; turn those boundaries into explicit protocols and data formats on open standards; then lock the specifications to consistent open standards. Keep the framework as a living, maintained artifact.

**Trade-offs**: each step assumes the previous one is done — skip *define* or *standardize* and you get modules that look separate but aren't actually swappable. The framework is a maintenance commitment, not a one-time deliverable.

---

## Pattern 3: Make the WBS the MOSA Taxonomy

**When to use**: early in systems engineering, when setting the system hierarchy.

**How**: build the Work Breakdown Structure (per MIL-STD-881F, with MIL-STD-196G naming) so it aligns to the MOSA principles — modularity, openness, scalability, flexibility, reusability — then refine it to call out modular components, interface points, data-exchange needs, and test/validation (Table 3-1). Prioritize modules, define boundaries (I/O, data formats, APIs/SDKs, test requirements), set up a modular development process, and trace IP and supply-chain consequences at every level of indenture.

**Trade-offs**: a richer taxonomy adds modeling and traceability effort, but it is what converts MOSA principles into structure and lets competition and technology-refresh decisions be made at the right level. Apply the same discipline to software, not just hardware.

---

## Pattern 4: Build Modularity In, Don't Bolt It On

**When to use**: throughout requirements, architecture, and design.

**How**: express MOSA requirements at the right design level (SoS, system, subsystem, or lower) and manage them like any other requirement in the design specification, verified and validated at each technical baseline through design reviews. Follow the iterative dual-path (design and funding) process of Figure 3-2 so modularity attributes are written in from the start. For standards, select consensus-based ones (10 U.S.C. 4401), search ASSIST/MOSS, and write a **profile** to remove interoperability-killing variability. For software, design API-first with hardware-grade rigor.

**Trade-offs**: writing requirements at the proper level early constrains the design and demands engineering judgment — but retrofitting modularity onto a mature design fights the fixed constraints and usually fails to deliver the benefits.

---

## Pattern 5: Target IP-Rights Spending at the Lock-Prone Interfaces

**When to use**: when planning data-rights and IP acquisition under a constrained budget.

**How**: use the KOSS logic — score each subsystem by how often it turns over and how locked-in its supplier is — and direct Government data-rights money at the high-volatility, high-lock components, leaving the rest. Integrate the choice with the IP strategy, Acquisition Strategy, and sustainment strategy so the *desired modularity* is a deliberate cost-benefit point, not a blanket maximum.

**Trade-offs**: this requires judging volatility and lock per component, which is analysis effort — but buying rights everywhere wastes money, and buying them nowhere leaves the program a captive of sole-source vendors at exactly the volatile interfaces.

---

## Pattern 6: Make MOSA Contractual and Enforceable Through Deliverable Data

**When to use**: from RFP development through award and execution.

**How**: state desired modularity and identify modular system interfaces *before* the RFP; carry MOSA into the mandated documents (AoA, RFP, SEP, Acquisition Strategy, CDD) so it becomes a contract obligation. Anchor enforceability in CDRLs backed by DIDs (e.g. OSMP, SEMP, DSM), traced to specific WBS/GRA node levels, and constrain the delivered Digital System Model so it cannot alter Government-designated interfaces. Request a draft OSMP in the proposal so modularity can be evaluated before award. Trace the language up the statutory funnel: Title 10 → DoD → service → PEO → program.

**Trade-offs**: front-loading specification and deliverable data adds proposal-evaluation and contracting work — but omitting CDRLs/DIDs risks not receiving the data and losing the ability to invoke DFARS data-rights clauses; non-FAR vehicles (OTAs) carry none of this automatically while the MOSA mandate still applies.

---

## Pattern 7: Govern Technology Change with Metrics and Two Roadmaps

**When to use**: when justifying MOSA's payoff and planning refresh across the life cycle.

**How**: align MOSA metrics to the five benefit classes (interoperability, technology refresh, enhanced competition, innovation, cost avoidance/savings) and reduce them to the necessary few for the specific application, use case, and maturity phase; use pass/fail for a proposed architecture but switch to metrics-based assessment (Appendix A, or MAUT in Appendix D) when supporting mechanisms exist. Pair a product roadmap (*what value, when*) with a technology roadmap (*what must be ready, when*) to isolate volatile technology, and involve DMSMS practitioners to mitigate obsolescence.

**Trade-offs**: metrics and roadmaps are governance overhead, but without them modularity can't be shown to pay off, refresh slips from dated commitment to vague intention, and DMSMS risk goes unmanaged.
