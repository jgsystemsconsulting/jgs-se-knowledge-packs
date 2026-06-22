# NASA PRA Procedures Guide Glossary

Key terms from the *Probabilistic Risk Assessment Procedures Guide* (NASA/SP-2011-3421, 2nd ed.). Chapter references point to this pack's `chapters/` files.

**Aleatory Uncertainty** — The irreducible, stochastic variability of a physical process; it persists even with perfect knowledge and is described by a probability distribution (the "model of the world"). Contrast with epistemic uncertainty. (Ch 4, Ch 7)

**Alpha Factor Model** — The recommended multi-parameter common-cause-failure model. It expresses dependent failure through failure ratios for each multiplicity and a total component failure rate; preferred for handling any redundancy level, easier parameter assessment under sparse data, and better uncertainty distributions. (Ch 4)

**Basic Event** — The lowest-resolution element of a fault tree, directly quantifiable from data (a component failure mode, an undeveloped fault, a human action, a software fault, or a phenomenological event). (Ch 1, Ch 2)

**Bayesian Updating** — Combining a prior distribution over a parameter with a likelihood derived from new evidence to produce a posterior distribution; the standard estimation engine throughout the Guide. (Ch 3, Ch 4)

**Beta-Factor Model** — The oldest, simplest common-cause model: a single fraction of a component's total failure frequency is allocated to the common-cause part. Useful for two-unit redundancy and for screening. (Ch 4)

**Birnbaum Measure (BM)** — An importance measure equal to the partial derivative of the risk metric with respect to an event's probability; pure structural sensitivity, independent of the event's own probability. (Ch 7)

**Casualty Expectation (E_C)** — A collective public-risk measure: the expected number of casualties for a single launch, capped (without waiver) at 30 in a million per launch by range-safety requirement EWR 127-1. (Ch 6)

**Common Cause Failure (CCF)** — Simultaneous failure of multiple components from a shared root cause and a coupling factor (same design, hardware, function, people, procedures, location, or environment). (Ch 4)

**Common Cause Basic Event (CCBE)** — An explicit fault-tree event representing the joint failure of a specific subset of a redundant group; inserting CCBEs converts an awkward dependence into ordinary independent-event arithmetic. (Ch 4)

**Conditional Software Failure** — A software response that is wrong only because of the mission condition it encountered; the code met its specification but the specification was wrong for that condition. Dominates the real failure history. (Ch 5)

**Conjugate Prior** — A prior whose family is preserved under updating, giving a closed-form posterior (Gamma–Poisson, Beta–Binomial). Avoids numerical integration. (Ch 3, Ch 4, Ch 8)

**Context-based Software Risk Model (CSRM)** — A framework that models software risk as the logic intersection of a system entering a condition and the software responding, capturing conditional and recoverable-vs-critical failures; run at Specification and Design levels. (Ch 5)

**Credible Interval** — A Bayesian probability interval between two percentiles of a posterior (a 90% interval runs from the 5th to the 95th percentile). (Ch 3, Ch 8)

**Cut Set** — A combination of conditions whose joint occurrence causes the top event. (Ch 1)

**Differential Importance Measure (DIM)** — An importance measure that ranks both basic events and fundamental parameters, is additive across element groups, and overcomes the extreme-value limitation of the classical measures. (Ch 7)

**Dynamic Flowgraph Methodology (DFM)** — A multi-valued, discrete-time logic representation of hardware/software variables used inside CSRM to find time-dependent prime implicants of function failure. (Ch 5)

**End State** — The terminal outcome of an event sequence, classified by consequence (OK, Loss of Crew, Loss of Vehicle, Loss of Mission, and others). (Ch 1, Ch 2)

**Epistemic Uncertainty** — Reducible uncertainty reflecting limited state of knowledge about parameters and model validity; shrinks as data accrue and is the layer Bayesian updating moves. (Ch 4, Ch 7)

**Error Factor (EF)** — A multiplier on a median that sets the lognormal uncertainty band (the ratio of the 95th percentile to the median). (Ch 1, Ch 7)

**Event Sequence Diagram (ESD)** — An inductive, success-oriented flowchart mapping every path from an initiating event to its end states; communication-friendly and built before the event tree. (Ch 2)

**Event Tree (ET)** — The quantitative inductive tree (one per initiating event) whose mutually exclusive paths are scenarios; the structure to which fault trees are linked. (Ch 2)

**Failure Initiator** — In abort modeling, the loss of a critical ascent function that begins an abort scenario, carrying its component, manifestation, severity, timing, and probability from the general PRA. (Ch 8)

**Failure Manifestation** — The intermediate critical stage between initiator and hazard environment past which vehicle or mission integrity is irrevocably lost (e.g., contained vs. uncontained engine failure). (Ch 8)

**Fault Tree (FT)** — A deductive logic model decomposing a top event (the Boolean complement of a success criterion) through gates to basic events. (Ch 1, Ch 2)

**Fussell-Vesely (F-V)** — An importance measure giving the fractional reduction in baseline risk when an event's probability is set to zero; flags where reliability investment buys the most benefit. (Ch 7)

**Human Error Probability (HEP)** — The quantity HRA produces for each human basic event, carried into the PRA with an uncertainty band (typically a lognormal error factor). (Ch 5)

**Human Reliability Analysis (HRA)** — The five-step method (problem definition, task analysis, error identification, error representation, quantification/integration) that turns human-system interactions into quantified basic events. (Ch 5)

**Importance Measure** — A quantitative ranking of how the risk metric responds to changes in an event or parameter (F-V, RRW, Birnbaum, RAW, DIM). (Ch 7)

**Initiating Event (IE)** — A departure from the desired operational envelope to a state requiring control intervention; the start of a scenario. (Ch 2)

**Latin Hypercube Sampling (LHS)** — Stratified sampling without replacement that covers an input domain more uniformly than crude Monte Carlo with fewer samples; the Guide's preferred sampling method. (Ch 7)

**Limit-State Function (g)** — In probabilistic structural analysis, a function written so failure is always g ≤ 0; the probability of failure is the volume of the joint density in the failure region. (Ch 6)

**Master Logic Diagram (MLD)** — A deductive, hierarchical technique for generating a comprehensive candidate initiating-event list, terminating at pinch points. (Ch 1, Ch 2, Ch 8)

**Minimal Cut Set (MCS)** — A cut set from which no member can be removed without the top event no longer occurring; the target of Boolean reduction and the basis for quantification. (Ch 1, Ch 2)

**Model of the World** — The aleatory model (deterministic or stochastic) that converts observable data into information; step one of any PRA. (Ch 4)

**Most Probable Point (MPP)** — In structural reliability, the point on the limit state nearest the origin in transformed space; FORM/SORM/AMV locate it, and the reliability index β is its distance. (Ch 6)

**Performance Risk** — The probability of a shortfall against a performance requirement in any mission-execution domain (safety, technical, cost, schedule). (Ch 1)

**Performance Shaping Factor (PSF)** — A context factor (training, stress, time, ergonomics) that raises or lowers a human error probability; method-specific lists. (Ch 5)

**Phenomenological Model** — A physics-based, deterministic-plus-probabilistic model that quantifies logic-tree branch points governed by physical processes rather than random part failures. (Ch 6)

**Pressure–Impulse (P-I) Curve** — A two-dimensional blast vulnerability criterion adding wave duration (impulse) to peak overpressure; expressed in reflected terms. (Ch 6, Ch 8)

**Pivotal Event** — A success/failure of a response, or occurrence/non-occurrence of a phenomenon, along a scenario between the initiator and the end state. (Ch 1, Ch 2)

**Population Variability Distribution** — The distribution capturing real parameter variability across a non-homogeneous population when heterogeneous generic sources disagree; not to be averaged away by pooling. (Ch 3)

**Rare-Event Approximation** — Approximating the probability of a union of minimal cut sets by the sum of their probabilities, valid for small probabilities (λt ≲ 0.1). (Ch 2, Ch 8)

**Risk Achievement Worth (RAW)** — The ratio of risk with an event forced to failure (probability one) to baseline risk; flags elements whose unexpected failure hurts most. (Ch 7)

**Risk-Informed Safety Case (RISC)** — A body of evidence plus operating commitments assembled as the best obtainable proxy for safety, since complex-system risk cannot be proven. (Ch 1)

**Risk Reduction Worth (RRW)** — The ratio of baseline risk to risk with an event set to zero; algebraically linked to F-V. (Ch 7)

**Risk Triplet** — Risk as a set of triplets (scenario, likelihood, consequence) answering what can go wrong, how likely, and the consequences; the conceptual backbone of PRA. (Ch 1, Ch 2)

**Software Reliability Growth Model (SRGM)** — A black-box model estimating how reliability improves as defects are found and removed during test; used in Design-Level CSRM. (Ch 5)

**Stress-Strength Formulation** — Quantifying a binary branch point by the probability that capability ("strength") exceeds demand ("stress"), both random variables. (Ch 6)

**Structure Function** — The Boolean switching function mapping the binary input vector of component states to the top-event state. (Ch 8)

**THERP** — Technique for Human Error Rate Prediction; a comprehensive HRA method built on an HRA event tree with five dependency levels, best for routine proceduralised tasks. (Ch 5)

**Transition State** — A sequence outcome that hands an under-developed scenario to another tree, or carries critical-system status across linked event-tree phases, rather than terminating. (Ch 2, Ch 8)

**Warning Time** — The interval an abort buys between abort initiation and the onset of an immediate crew threat; a first-order survivability variable. (Ch 8)
