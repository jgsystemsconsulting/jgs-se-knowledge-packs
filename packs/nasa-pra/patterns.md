# NASA PRA Procedures Guide — Patterns & Techniques

Concrete, named techniques drawn from the *PRA Procedures Guide* (NASA/SP-2011-3421, 2nd ed.). Each gives when to reach for it, how to apply it, and the trade-offs.

## Pattern 1: Scenario Logic Stack (MLD → ESD → ET → FT → MCS)
**When to use**: Whenever a performance risk must be turned from a qualitative concern into a quantified frequency.
**How**: Identify initiating events deductively with a Master Logic Diagram (plus FMEA reasoning). Draw a success-oriented Event Sequence Diagram per initiator, then abridge it into a quantitative Event Tree. Expand each complex pivotal event with a Fault Tree whose top event is the Boolean complement of the system success criterion. Link the trees, reduce to minimal cut sets, and quantify. (Ch 1, Ch 2)
**Trade-offs**: Each artifact is a graphical Boolean equation, so the stack stays computer-tractable while preserving dependencies through shared basic events — but completeness must be assessed at the scenario level first, because a missing dominant scenario corrupts both the frequency and the prevention insight.

## Pattern 2: Tree-Style Selection (large-ET vs. large-FT)
**When to use**: At model setup, once you know whether the system is repaired during the mission.
**How**: For maintenance-precluded, time-ordered missions where reliability decays monotonically, favor a large or linked event tree carrying status through transition states. For repairable facilities that settle into a time-independent availability, favor large fault trees under a small event tree. (Ch 2, Ch 8)
**Trade-offs**: Large FTs cannot say *when* a failure end state occurs; large/linked ETs strain on complex repairable systems. The physics of repair, not analyst taste, should pick the method.

## Pattern 3: Two-Step Bayesian Parameter Estimation
**When to use**: Every time a basic-event parameter (failure rate, demand probability, initiator frequency) must be quantified with its uncertainty.
**How**: Fit a prior from generic/class-level information, then update it with system-specific evidence via a likelihood matched to the data-generating process (Poisson for time-based counts, Binomial for demand-based counts, lognormal for handbook/expert values). Report the posterior as a credible interval. (Ch 3, Ch 8)
**Trade-offs**: Conjugate pairs (Gamma–Poisson, Beta–Binomial) give closed-form arithmetic; mismatched pairs force numerical or MCMC solutions. Sparse data leaves the posterior near the prior; abundant data pulls it toward the evidence and converges on the MLE.

## Pattern 4: Sequential / Compounding Updates
**When to use**: When evidence arrives in batches over time.
**How**: Treat today's posterior as tomorrow's prior. Updating on batch 1 then batch 2 yields the same posterior as a single pooled update. (Ch 3)
**Trade-offs**: Order-independence makes staged updating a bookkeeping convenience, not a separate method — but only when the total information is genuinely additive.

## Pattern 5: Population-Variability Modeling for Heterogeneous Sources
**When to use**: When several generic data sources for the same parameter disagree.
**How**: Treat the spread as real parameter variability across a non-homogeneous population — represent it as its own distribution instead of pooling the sources into one estimate. (Ch 3)
**Trade-offs**: Avoids erasing genuine variability, at the cost of a more elaborate two-stage (generic-then-system-specific) inference.

## Pattern 6: CCBE Fault-Tree Expansion
**When to use**: For any redundant set built from identical (coupled) components.
**How**: Replace each component basic event with an OR of common-cause basic events (independent failure plus the shared-failure subsets). Apply the symmetry assumption so a CCBE's probability depends only on how many units fail. Solve the expanded tree; standard quantification then applies with no residual CCF worry. (Ch 4)
**Trade-offs**: Converting dependence into an explicit basic event makes ordinary independent-event math valid — but in truncated models the tiny all-independent product gets dropped while the larger common-cause term survives, which is exactly why a global screening event is inserted first so the dominant contributor is not silently lost.

## Pattern 7: Two-Phase CCF Treatment (screen, then detail)
**When to use**: Whenever redundancy is present and dependence could defeat it.
**How**: Screen qualitatively (conservatively flag every common-cause component group; discard only with an obvious reason) and quantitatively (insert a bounding global/maximal event). Then perform detailed analysis on the survivors with CCBE-expanded trees and the Alpha Factor model, estimating parameters via the Impact Vector Method when system-specific CCF data are too sparse. (Ch 4)
**Trade-offs**: Conservative screening protects against discarding a real vulnerability; detailed analysis is reserved for the few groups that survive, controlling cost.

## Pattern 8: Screen-then-Detail for Human Reliability
**When to use**: When numerous human-system interactions could affect the risk estimate.
**How**: Classify interactions by timing (pre-initiator / initiator / post-initiator) and cognition (skill / rule / knowledge). Screen with conservative HEPs (≈0.1–1.0, complete dependence among related actions). Quantify only survivors with a method matched to the task: THERP for routine proceduralised work, CREAM/NARA for generic-task screening, SPAR-H for analyst repeatability; combine methods where useful. (Ch 5)
**Trade-offs**: Error identification is the pivot — get the omission/commission enumeration and PSFs wrong and every downstream number is wrong. No single method is universal.

## Pattern 9: Time-Reliability Quantification of Time-Critical Actions
**When to use**: When a human action must complete inside a hard time window (abort, command destruct).
**How**: Build the HEP as the probability that the crew response-time distribution exceeds the available window, via a Time Response Curve. (Ch 5)
**Trade-offs**: Large windows can drive the time-dependent HEP absurdly low, so a floor of non-time-dependent execution errors must still be added.

## Pattern 10: Conditional (Failure-on-Demand) Software Risk via CSRM
**When to use**: When software is risk-significant and a single failure rate would misrepresent it.
**How**: Split software contributions into Type B unconditional/routine cut-sets (quantify with a failure-rate or reliability-growth model) and Type C conditional/triggered cut-sets (quantify as a failure-on-demand conditional probability gated by a trigger). Mark each recoverable or critical, and feed entry-point events back into the event-tree/fault-tree model. (Ch 5)
**Trade-offs**: The trigger-AND-software-response gate bounds the conditional response *given* the trigger, turning a prohibitive test burden into a finite, computable number of targeted samples — but the tests must genuinely sample the variability of the trigger condition, judged by engineering judgement, not by re-running passed tests.

## Pattern 11: Stress-Strength Quantification of Physics-Governed Branch Points
**When to use**: When a logic-tree branch outcome depends on physics (a structure breaking, an operator acting before impact, debris reaching people).
**How**: Cast the branch as the probability that capability ("strength") exceeds demand ("stress"), with both as random variables. Evaluate the integral analytically for normal/lognormal cases or by Monte Carlo / LHS / AIS / FORM / SORM / AMV otherwise, using a limit-state function written so failure is g ≤ 0. (Ch 6)
**Trade-offs**: Replaces opaque factors of safety with a quantitative probability of failure usable for new and existing hardware — but Monte Carlo needs ~10 failures for confidence (so a 10⁻³ target needs ~10⁴ samples), motivating the faster MPP and importance-sampling methods, which must be calibrated against Monte Carlo.

## Pattern 12: Fidelity-to-Maturity Matching
**When to use**: At every life-cycle phase when deciding how detailed a model should be.
**How**: Start with top-down parametric models and honest uncertainty ranges; add physics or logic fidelity only where existing models become insufficient or where uncertainty exposes a risk-driving design weakness. (Ch 1, Ch 6, Ch 8)
**Trade-offs**: A coarse analysis with honest uncertainty beats a detailed analysis built on placeholder data; over-modeling early wastes effort and creates false precision.

## Pattern 13: Conservative-First, Refine-Where-It-Pays Abort Modeling
**When to use**: Estimating how effectively a crewed vehicle escapes its own failures.
**How**: Carry each failure initiator through manifestation → hazard environment → detection/warning time → crew-module vulnerability → descent risk. Early, map every uncertain or fast manifestation to the worst-case environment with zero propagation time; later, recover warning time and re-map to less severe environments only where it visibly improves abort effectiveness. Integrate in a spreadsheet first, migrating to a Monte Carlo hybrid as detail grows. (Ch 8)
**Trade-offs**: Propagation speed and detectability matter as much as hazard severity — a detected slow failure is survivable, a fast or undetected one is not. Detail is justified by sharpening the figure of merit, not by data availability.

## Pattern 14: Importance-Driven Resource Allocation
**When to use**: After quantification, to decide where to invest in reliability or mitigation.
**How**: Rank individual events and parameters with importance measures, reading the one that matches the decision: F-V/RRW for "where does improvement pay off," Birnbaum for "where is the model most sensitive," RAW for "what hurts most if it fails," DIM for ranking parameters and summing across groups. (Ch 7)
**Trade-offs**: Scenario-frequency ranking alone misses a component buried across many low-frequency scenarios; only event-level importance surfaces it. Frequency-type initiating events must be excluded from conventional importance ranking because their probability has no upper bound.
