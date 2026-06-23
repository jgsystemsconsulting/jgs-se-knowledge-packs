# NASA Fault Management Handbook Patterns & Techniques

Reusable FM patterns drawn from NASA-HDBK-1002 *Fault Management Handbook* **Draft 2 (April 2, 2012)**. Each has When / How / Trade-offs. **Draft source** — treat as provisional guidance, not a ratified standard.

## Pattern 1: Mature FM in Parallel with the Nominal Design

**When to use**: from Pre-Phase A onward, on any mission with off-nominal behavior that matters (i.e., all of them).

**How**: treat each function as having a "light side" of expected behavior and a "dark side" of potential failures, and design both together. Start FM scoping early enough that the *mission* design can still flex to support preferred FM strategies. Run the six FM process activities (conceptual design, requirements, architecture & design, assessment & analysis, V&V, operations) inside the SE lifecycle, each tied to its mission phase and review gate.

**Trade-offs**: parallel maturation competes for early cost/schedule budget when FM seems abstract. But FM added after the system is defined becomes "painted on" rather than "dyed in" — brittle, hard to test, and forced to compensate for design decisions it never influenced.

---

## Pattern 2: Set the Risk Posture, Then Distribute Risk

**When to use**: at mission definition, before architecture is fixed.

**How**: first fix the mission's risk tolerance via its NPR 8705.4 classification (Class A flagship → Class D minimal). Then write fault-tolerance requirements that *distribute* that risk: single-fault tolerance across the whole system is the most capable and most expensive posture; higher-risk missions target redundancy where it matters (health-and-safety functions like pointing and power), accept selected operational risks, and use partial/selective redundancy or single-string elsewhere.

**Trade-offs**: single-fault-tolerance-everywhere maximizes robustness but drives premium parts, full redundancy, and exhaustive FM. Distributing risk saves resources but requires defensible judgment about where limited resources buy the most protection — work it with S&MA and project management.

---

## Pattern 3: Budget Response Latency Against Time-to-Criticality

**When to use**: for every fault, when deciding flight-vs-ground, onboard-vs-operator, automatic-vs-crew.

**How**: decompose each candidate response's latency into its five intervals — observation, detection, decision, execution, recovery — and sum them for each possible implementer (ground operators, ground software, crew, flight software, firmware, hardware). Compare that budget to the failure's TTC. A response is viable only if its summed latency fits inside the TTC clock. Count human latency too; humans performing FM are part of the mechanism. The ground loop (data cadence, storage, comms schedule, light time, processing, human decision, uplink) is usually the longest path.

**Trade-offs**: rigorous latency budgeting is analytical effort. Skipping it produces responses that exist but finish *after* the function is already lost — the difference between "have a response" and "have a response fast enough."

---

## Pattern 4: Write Explicit, One-Concept Top-Down FM Requirements

**When to use**: whenever an FM requirement set is authored or assessed.

**How**: derive requirements top-down from the mission concept and risk posture under one FM lead and one driving document. Default to explicit, one-concept-per-statement requirements with captured rationale and inline definitions. Run the five-step process (Know the Mission → Consider Heritage → Review All Categories → Determine Completeness → run the FM Requirements Checklist) and sweep the Table 11 categories to demonstrate breadth. Target *preserved functions and a safety net*, not a one-to-one map of FMEA faults. Use the worst-case doubling/halving interrogation to set defensible tolerances. Write each requirement's V&V venue as you write the requirement.

**Trade-offs**: explicit, detailed requirements cost authoring effort up front and risk over-specification if pushed too far (too-specific requirements break when design realities shift). But implicit/general requirements ("do FM," "protect against faults") let implementers declare substandard designs "done," fragment interpretation across the flow-down, and dump the V&V burden onto validation. Choose in-house (fewer, general) vs. out-of-house (detailed, minimum-ambiguity) deliberately; default to out-of-house when unsure.

---

## Pattern 5: Make Safe Mode the Universal Fallback

**When to use**: as the final "else" branch of the FM decision logic, across free flight, drift, and surface operations.

**How**: for any failure not covered by a predetermined fault-isolation/reconfiguration capability, fall into a protective safe mode that preserves assets and buys the ground (or onboard crew) time to formulate recovery. A working safe mode must still accept ground commands and transmit data as directed, and may carry rudimentary onboard capability (e.g., sun-pointing to keep generating power) to head off short-TTC effects.

**Trade-offs**: safe mode sacrifices the current mission goal to preserve the asset (a goal change). When TTC is too short even for safe-mode evaluation and the fault is non-recoverable, escalate to abort instead.

---

## Pattern 6: Tailor Redundancy to the Fault Class

**When to use**: whenever applying redundancy or claiming fault tolerance.

**How**: pick the redundancy approach against the fault it actually counters — hardware-identical for random part failures and lifetime limits; functional (dissimilar/analytic) for common-cause concerns, detection cross-checks, and workarounds; informational (EDAC) for bit-level corruption like single-event upsets; temporal (repeat-in-time, checkpoint-rollback) for transient faults. Always pair a tolerance claim with the named fault class it tolerates, and justify the mechanism's limits in the FM analysis.

**Trade-offs**: hardware-identical redundancy is simple but powerless against common-mode flaws shared by all strings. An unqualified "single fault tolerant" claim invites false confidence — a triplex voter handles random part failures but not the systematic bug that defeats all three channels.

---

## Pattern 7: Select V&V Scenarios Top-Down, Then Prioritize by Risk

**When to use**: when scoping FM verification and validation, early and inside system V&V planning.

**How**: use the three-step top-down method — identify mission activities, identify each activity's objectives (mission goals plus asset/crew/operator health), then select failure cases that threaten each objective. Sort objectives into safety-critical / mission-critical / noncritical. Prioritize the selected scenarios Required / High / Medium / Low by the risk of *not* exercising them, and define the minimum certifying set before schedule pressure forces cuts. Capture an incompressible test list and regression suites up front. Lean on formal modeling, automation, and architectural extrapolation to cover a failure space too large for testing alone.

**Trade-offs**: top-down scenario selection and early coverage decisions cost planning effort and confront uncomfortable risk trades early. Deferring them is the classic driver of "the Bump" — the large, unplanned spike in test-phase effort when integration surprises surface. Keep validation and analysis teams independent of the design team.

---

## Pattern 8: Hold Dedicated FM Reviews Keyed to Maturing Artifacts

**When to use**: throughout the lifecycle, ahead of each project gate.

**How**: run the seven dedicated FM reviews (FMCR, FMARR, FMPDR, FMCDR, FMTRR, FMLRR, FMCERR), each timed to precede its project review and each gated by specific maturing FM artifacts (concept doc → requirements/architecture → preliminary design → final design → test readiness → launch readiness → event readiness). Use the entrance criteria (what must be complete to hold the review) and success criteria (what determines a pass), plus the Table 28 question catalog. Gate new technology to TRL 6 by PDR. Secure a program-accepted fault-tolerance / single-point-failure-exemption list at FMPDR/FMCDR.

**Trade-offs**: dedicated reviews cost the program scarce expert time and calendar. But reviewing FM only as a sidebar in nominal-focused reviews treats failure scenarios as a schedule tax and guarantees gaps — only a focused forum gets the right experts and the whole off-nominal picture in one room. Small Class C/D projects may combine FM reviews with project reviews *only* if every FM-specific criterion is still covered.

---

## Pattern 9: Give FM a System-Level Home with Matching Authority

**When to use**: at program/project formulation, before FM technical work ramps.

**How**: position FM at the system level with authority sized to its area of concern, vertical interfaces up and down the hierarchy, and horizontal integration with the parallel organizations FM depends on (engineering, S&MA, V&V, I&T, operations) — plus a coordinating board/panel with cognizance over *all* of FM. Charter a single FM lead with explicit programmatic and technical duties. Make FM a tracked engineering element with its own WBS, budget, and historical performance measures, and plan for the late-lifecycle staffing bump (the 0.5-FTE-planned-vs-14+-FTE-actual pattern).

**Trade-offs**: a system-level FM organization with real authority and its own budget looks like overhead on a small program. But diffused responsibility — FM as a system engineer's side duty, or pushed down to subsystems without coordination — is the documented source of coverage gaps, late defect discovery, and overruns. An issue with no vertical *and* no horizontal home gets silently dropped, then surfaces at integration at maximum cost.

---

## Pattern 10: Mine the Lessons Learned Database as a Design Input

**When to use**: during FM design and review, before committing the architecture.

**How**: read the categorized FM-relevant entries from the NASA Lessons Learned database (the source mines them in Appendix F). Check the project against the recurring root causes — missing top-down SE, no permanent owner asking "what could go wrong," weak reviews, untested redundancy combinations, state-blind fault responses, omitted watchdog timers, keep-out zones not embedded in software, FM enabled on unused components. Assess failures top-down, bottom-up, *and* middle-out (directed-graph and event-sequence analysis).

**Trade-offs**: the cheapest fault analysis available is reading what already went wrong — the same root causes recur across Mars Observer, CONTOUR, SOHO, Galileo, MRO, Voyager, and more, each with a concrete recommendation. The cost is the discipline to actually consult it rather than trusting heritage by similarity.
