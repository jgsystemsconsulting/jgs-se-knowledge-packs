# NASA PRA Procedures Guide — Cheatsheet

Decision rules, selection tables, and tells & smells distilled from the *PRA Procedures Guide* (NASA/SP-2011-3421, 2nd ed.).

## The Risk Triplet (what PRA answers)

| Question | PRA element |
|---|---|
| What can go wrong? | Scenario (IE → pivotal events → end state) |
| How likely is it? | Frequency (IE frequency × conditional path probability) |
| What are the consequences? | End state (OK, LOC, LOV, LOM, …) — each with explicit uncertainty |

## PRA Task Flow (one pass; iterate)

1. Familiarize with the system (depth scales with design maturity).
2. Define mission and system success criteria.
3. Identify initiating events (MLD + FMEA), screen, and group.
4. Develop scenarios (ESD → ET), expand pivotal events (FT).
5. Collect data; estimate parameters (Bayesian).
6. Quantify (reduce to MCS, compute top-event probability).
7. Propagate uncertainty; rank with importance measures.
8. Present results; assemble the Risk-Informed Safety Case.

## Choosing the Logic-Model Style

| Situation | Style |
|---|---|
| Repairable facility reaching steady-state availability; crewed/maintained | Small ET + large FTs |
| Maintenance-precluded mission; reliability decays with time | Large / linked ETs with transition states |
| Highly time-dependent or conditional behavior (almost-failed states, convolutions) | Discrete-event simulation |
| Complex time-dependent hardware/software interaction | Dynamic Flowgraph Methodology (DFM) |

## Matching the Likelihood to the Data

| Data-generating process | Likelihood | Conjugate prior → posterior |
|---|---|---|
| Failures accruing over operating time | Poisson | Gamma → Gamma (α += failures, β += time) |
| Failures among discrete demands | Binomial | Beta → Beta (α += failures, β += successes) |
| Random durations | Exponential | Gamma → Gamma |
| Handbook point estimate / expert best guess | Lognormal | (nonconjugate — numerical/MCMC) |

Noninformative default: Jeffreys prior — beta(0.5,0.5) for binomial, gamma(0.5,0) for Poisson. Use only when data-dominated or as a deliberate reference; don't default to it when you actually know something.

## Uncertainty: Two Layers, Kept Separate

| | Aleatory | Epistemic |
|---|---|---|
| Nature | Irreducible variability of observables | Reducible limit of knowledge |
| Shrinks with data? | No | Yes (via Bayes) |
| Represented by | The model of the world (a distribution) | A distribution over parameters/assumptions |
| In results | The risk curve itself | The fan of percentile curves around it |

## CCF Quick Reference

- A CCF needs **root cause + coupling factor** (same design, hardware, function, people, procedures, location, environment).
- Identical redundancy almost guarantees coupling factors → identical-redundant CCFs are the priority.
- Screen conservatively, then detail with the **Alpha Factor** model (recommended). Beta-factor and Basic Parameter are simpler precursors; global/maximal is for screening.
- Generic screening β ≈ 0.1 (Shuttle orbiter anomaly data gave ≈0.13) when no data exist.

## Importance Measures — Read the Right One

| Measure | Answers | Computed by |
|---|---|---|
| Fussell-Vesely (F-V) | Where does improvement pay off? | Risk benefit of setting event probability to 0 |
| Risk Reduction Worth (RRW) | Same (ratio form; F-V = 1 − 1/RRW) | Baseline ÷ risk with event at 0 |
| Birnbaum (BM) | Where is the model most sensitive? | ∂Risk/∂(event probability) |
| Risk Achievement Worth (RAW) | What hurts most if it fails? | Risk with event at 1 ÷ baseline |
| DIM | Rank parameters; sum across groups | Fraction of total ΔRisk attributable to the element |

A passive, ultra-reliable part can rank bottom on F-V yet top on Birnbaum. **Exclude frequency-type IEs from conventional importance ranking** (their probability has no upper bound).

## HRA Method Selection

| Need | Method |
|---|---|
| Routine, proceduralised ground tasks | THERP (5 dependency levels, error-factor bounds) |
| Cognitive-error screening of a known task in a new setting | CREAM |
| Quantification anchored in real human-error data, generic tasks only | NARA (18 EPCs, refines HEART) |
| Repeatability across analysts; tasks not yet detailed | SPAR-H (8 PSFs, worksheets) |
| Hard-time-window action (abort, command destruct) | Time-Reliability Model / Time Response Curve |

## Abort Modeling Chain

Initiator → Manifestation → Hazard environment → Detection / warning time → Crew-module vulnerability → Descent & landing risk → integrated LOC + abort effectiveness.

- **Abort effectiveness** = P(crew survives | loss-of-mission failure). For fixed booster reliability, this is what separates an acceptable crew goal from an unreachable one.
- **Speed beats severity**: a detected slow failure is survivable; a fast or undetected one is not.
- Blast: quantify against a **reflected** P-I vulnerability curve, not incident values.
- Integration: spreadsheet early → Monte Carlo hybrid (e.g., GoldSim) as detail grows.

## Tells & Smells (anti-patterns to catch in review)

- **"Adequate, therefore safe enough"** from a design-basis check with no integrated risk model — the un-isolatable / off-nominal case may dominate.
- **Citing only the mean top-event frequency** — decisions usually hinge on percentiles and importance measures.
- **Treating dependent components as independent** — understates both the mean result and its spread (the worked example shows ~5% mean bias for identical-device coupling).
- **Pooling heterogeneous generic sources** — erases real population variability.
- **Forcing a failure-rate model onto conditional software failures** — they are failures-on-demand; the failure-rate form hides the failures that actually matter.
- **False confidence from re-running passed tests** — repeated successes are not new evidence.
- **Statistical/steady-state methods on dynamic, unsteady physics** — use time-dependent phenomenological models instead.
- **Over-modeling on placeholder data** — a coarse model with honest uncertainty is more useful.
- **Overlapping (non-mutually-exclusive) IEs** — many PRA codes cannot Boolean-reduce them, creating internal inconsistency.
- **Rare-event approximation outside its range** — F(t) ≈ λt holds only for λt ≲ 0.1.
- **A converged Monte Carlo run treated as validated** — convergence buys precision, not validity; completeness and model uncertainty remain.

## Credibility of a PRA (NASA-STD-7009 factors)

Peer review · input pedigree · uncertainty analysis · robustness · analyst qualifications · Technical Authority. Because results cannot be *proven*, credibility rests on completeness, scrutability, and the Risk-Informed Safety Case (evidence + operating commitments).
