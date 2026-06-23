# FAA Systems Engineering Manual — Patterns & Techniques

Reusable SE patterns drawn from the FAA Systems Engineering Manual (SEM) v1.0.1. Each has When / How / Trade-offs. These render the SEM's practices as the FAA institutionalizes them inside the Acquisition Management System (AMS) and the National Airspace System (NAS).

## Pattern 1: Ride the Maturity Ratchet Through the AMS Lifecycle

**When to use**: planning any FAA acquisition from a recognized service need through fielding.

**How**: treat each of the five AMS phases (Service Analysis & Strategic Planning → Concept and Requirements Definition → Investment Analysis → Solution Implementation → In-Service Management) as a zoom level that raises the resolution of the same few things — the need, the requirements, the alternatives, the cost estimate, the safety picture. Carry the same artifacts forward (ConOps, shortfall analysis, requirements) and *revise and quantify* them each pass rather than re-creating them. Use requirements maturity (pPR → iPR → fPR → system specs) as the program's pulse.

**Trade-offs**: the ratchet keeps every decision point fed with progressively firmer evidence, but it punishes teams that freeze an artifact early and let requirements and architecture drift around it. Skipping the early, cheaper passes pushes deficiency discovery into Solution Implementation, where rework is expensive.

---

## Pattern 2: Keep the Front End Implementation-Free (Concept → Function → Requirement → Allocation)

**When to use**: Operational Concept Development and Functional Analysis, before any architecture commitment.

**How**: split three questions cleanly — the ConOps fixes *what the solution is for and how it will be used*; Functional Analysis fixes *what it does*; physical architecture answers *how*. Never hang a function on a box: convert each function to a Primitive Requirements Statement, mature it to a Mature Requirements Statement, then allocate the *requirement* (not the function) to the physical architecture. Keep preliminary requirements solution-agnostic so alternatives can be compared without bias.

**Trade-offs**: the discipline prevents premature commitment to a single-point solution, but it costs front-end rigor and patience; teams under schedule pressure are tempted to write solution-bound requirements that quietly foreclose the trade space.

---

## Pattern 3: Model Control and Data Together (FFBD + N²)

**When to use**: building a complete functional model during Functional Analysis.

**How**: use the Functional Flow Block Diagram to capture sequencing — a function cannot begin until its predecessor(s) finish, with AND / Exclusive-OR / Inclusive-OR logic — and the N² matrix to capture interfaces (data sent clockwise to the right, feedback to the left). Reapply the N² at each lower decomposition level until every entity has been compared against every other. Carry the administrative data (date, author, decimal-delimited function number) on both.

**Trade-offs**: maintaining two complementary views is more work than one, but either alone leaves the model incomplete — sequencing without interfaces, or interfaces without sequencing — and integration surprises follow.

---

## Pattern 4: Diagnose Alternative Failures to Pick the Right Loop

**When to use**: the evaluate-alternatives step of Architectural Design Synthesis, when candidate architectures fail to comply.

**How**: read the *pattern* of non-compliance. If **all** alternatives fail the **same** requirements, the functional architecture is the suspect — run the **design loop** back to Functional Analysis. If compliance **varies** across alternatives, the requirements are the suspect — run the **requirements feedback loop** per design. Assess constraint compliance and any adverse emergent properties from element interaction before scoring effectiveness, trade-offs, and risk; baseline the preferred (often "best value") architecture under CM.

**Trade-offs**: the diagnosis saves wasted iteration by attacking the real cause, but it demands honest evaluation across a documented set of four-to-six distinct alternatives; collapsing to one alternative too early hides which loop you actually needed.

---

## Pattern 5: Gate the Full Investment Decision on Requirements Stability

**When to use**: approaching the Final Investment Decision (FID).

**How**: measure stability — a requirements set is "stable" when at least 80% of requirements are unchanged, with the recommendation of no change for the last quarter before requesting FID. Track stability against TBD counts and change-prone requirements. Finalize Critical Performance Requirements in the fPRD and copy them verbatim into the Acquisition Program Baseline.

**Trade-offs**: holding for stability slips the FID when requirements churn, but committing capital against a moving target is the failure the gate exists to prevent; an unstable set invites baseline breaches downstream.

---

## Pattern 6: Triage Risk, Issue, or Opportunity by One Temporal Question

**When to use**: at every RIO identification point — every stage and whenever plans or status change materially.

**How**: ask "has it happened yet?" Not yet and bad → **Risk** (write `if [cause], then [impact]`; score likelihood A–E × impact 1–5; give it a realization date). Already or certainly → **Issue** (write `due to [cause], [impact] was experienced`; skip likelihood, score impact only). Not yet and good → **Opportunity**. Classify by root cause, not symptom. Pick a plan strategy (Avoid / Transfer / Control / Accept / Research and Knowledge), and project mitigation on a burn-down ("waterfall") chart.

**Trade-offs**: the single question keeps the three objects from blurring, but it requires discipline to state items by root cause and to keep the risk statement separate from its mitigation plan — the SEM explicitly warns against stating a risk in terms of how you'll mitigate it.

---

## Pattern 7: Roll Up the Maximum Risk Through the Schedule

**When to use**: tracking and reporting RIO across a WBS/IMS.

**How**: flag lowest-level tasks with their risk level; let each higher WBS summary inherit the maximum risk present below it. Fold mitigation steps into the program's planning, scheduling, budgeting, and cost-accounting systems and insert them into the Integrated Master Schedule. Show aggregate status on a Probability Impact Diagram; for major programs, feed the OMB Exhibit 300.

**Trade-offs**: max-inheritance turns the schedule itself into a risk dashboard with drill-down, but it can make a summary task look alarming on the strength of one child; reviewers must drill down rather than react to the rolled-up color alone.

---

## Pattern 8: Allocate Dependability by Service Thread, Not by Availability Spec

**When to use**: setting RMA requirements for software-intensive NAS information systems.

**How**: refuse availability as the primary contractual spec (it hides the reliability/maintainability trade, can't be predicted before the software exists, and can't be demonstrated in any practical window). Instead draw a "sensor-to-glass" Service Thread — a reliability block diagram of all equipment delivering a NAPRS service — and classify it by Service Thread Loss Severity Category: Essential (.9999), Efficiency-Critical (.99999), or Safety-Critical (no single thread allowed — split into two independent .99999 threads). Validate via reliability growth with Government-controlled "expunging," accepting that systems field short of target and mature across the fleet.

**Trade-offs**: top-down allocation is right where failure-independence holds, but it is *wrong* for remote/distributed systems (availability is overlapping diversity, not an "r of n" rule) and infrastructure systems (correlated failures break the math) — there, defer to lifecycle-cost reasoning and SME judgment.

---

## Pattern 9: Pull Specialty Engineering to the Front and Wire It Back In

**When to use**: every specialty discipline — RMA, E3/Spectrum, HFE, ISE, SSE, HMM/EE — at concept and requirements time.

**How**: start each discipline's own closed-loop risk cycle at the earliest acquisition phase, because cost is front-loaded and pain is back-loaded (an E3 issue caught in requirements is a spec line; caught after deployment it is a redevelopment). Treat operators and maintainers as first-class system elements (HFE). Then route every specialty output back into the mainstream SE processes — requirements into Requirements Management, concerns into Risk Management, criteria into Verification and Validation. Engage external gatekeepers early (ATC Spectrum Engineering Services for a frequency assignment; the Authorizing Official for security).

**Trade-offs**: front-loading specialty analysis adds early effort and coordination, but bolting it on late converts directly into residual risk, POA&Ms, retrofits, regulatory enforcement, and fines — the most expensive path.

---

## Pattern 10: Run the Categorize-Then-Tailor Security Loop

**When to use**: Information Security Engineering on any FAA IT system.

**How**: categorize the system by impact (FIPS 199/200: low / moderate / high), let the categorization select a control baseline, then tailor down or supplement up — assigning controls as system-specific, common (inherited), or hybrid, and favoring common controls for cost and shared monitoring. Run the NIST RMF six steps (Categorize, Select, Implement, Assess, Authorize, Monitor). Reconcile the fPRD against the standard System Security Plan template; any unreconciled delta becomes a POA&M item. Pursue continuous monitoring (SP 800-137) toward ongoing authorization.

**Trade-offs**: starting from a baseline is faster and more defensible than authoring controls from scratch, but it demands documented rationale for every deviation; a custom design that conflicts with a mandated common/hybrid control costs delay, a policy waiver, and a POA&M.

---

## Pattern 11: Match Decision-Analysis Fidelity to Decision Stakes

**When to use**: any structured choice among alternatives, especially at Investment Analysis gates.

**How**: pick the simplest technique whose output fidelity answers the decision — the common, assumption-heavy tools (Prioritization Matrix, QFD) suit simpler decisions; raise fidelity (TOPSIS, decision trees, influence diagrams, M&S) only when stakes demand. Build consensus in the IMT on criteria, weights, and ratings; keep cost evaluated separately; down-select to four-to-six meaningfully distinct alternatives and run sensitivity analysis if they still don't separate. Document every alternative. DA recommends; the FAA decision authority decides.

**Trade-offs**: too little fidelity yields incomplete information; too much wastes resources — the fidelity dial is the central judgment, and over-tooling a routine decision is as much a failure as under-tooling a consequential one.

---

## Pattern 12: Keep the Compliance Chain Pointing Down, the Change Path Pointing Up

**When to use**: Interface Management as the design evolves.

**How**: enforce the chain — the ICD (as-built design) complies with the IRD (interface requirements), which complies with the fPRD. Place the IRD under Configuration Management. Route every interface change as an Interface Change Request through the Interface Working Group, with impact analyses (performance, lifecycle cost, no new problems introduced); in-scope ICRs return to the originator, out-of-scope ones escalate to the program manager, and approved changes flow back into CM.

**Trade-offs**: the strict chain keeps interfaces coherent across many interoperating NAS systems, but it adds governance latency; teams that route changes around the IWG produce ICD/IRD/fPRD drift that surfaces at integration.
