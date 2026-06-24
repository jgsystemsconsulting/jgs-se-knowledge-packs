# Chapter 8 — Assessing Product Reliability

## Core Idea
Reliability is **quality watched over time** — the fraction of a population that is still meeting its specifications after a week, a month, or a warranty period, not just the fraction that passed at time zero. This chapter supplies the vocabulary, the probability models, and the estimation machinery needed to quantify and predict how a product population fails as it ages. Its central tension is what the source calls the *paradox of reliability analysis*: a high-reliability product, almost by definition, surrenders very few failures, and without failures the evidence that would demonstrate that reliability is hard to come by. Most of the chapter's frameworks exist to fight that paradox — through accelerated testing, censored-data methods, bottom-up modeling, growth modeling, and Bayesian use of prior knowledge.

A persistent distinction runs underneath everything: **non-repairable populations** (a failed item leaves the population permanently — modeled by *lifetime distributions* with a *failure/hazard rate*) versus **repairable systems** (an item is restored and keeps running — modeled by a *repair rate* or *ROCOF*, the rate of occurrence of failures). The source is emphatic that failure-rate and hazard-rate language applies only to first failures of non-repairable items, and that conflating the two is a modeling error.

## Frameworks Introduced (named in the source)

**The Bathtub Curve.** The empirical failure-rate-versus-age curve observed across decades of mechanical and electronic data, named for its shape. It has three regions: the *Early Failure (Infant Mortality) Period* with a high but rapidly falling rate; the long flat *Intrinsic (Stable) Failure Period* at the *intrinsic failure rate*, where most systems spend most of their lives; and the rising *Wearout Failure Period*. The source notes the same curve also applies to repairable systems, with the vertical axis becoming the repair rate / ROCOF.

**Acceleration models.** Models that relate failure at high stress back to failure at use stress, introduced to manufacture failures fast enough to learn from. Used when highly reliable parts would otherwise yield no failures in an affordable test. The chapter presents:
- **Arrhenius** — temperature-driven acceleration governed by a single activation-energy parameter ΔH; the acceleration factor between two temperatures rises exponentially with ΔH.
- **Eyring** — a chemistry/quantum-mechanics-based model that can carry temperature plus several additional stresses; its temperature term reduces to Arrhenius, and most practical versions drop interaction terms (so per-stress acceleration factors can be multiplied).
- **Other models** (six, presented as simplified Eyring forms unless noted): an inverse-power law driven by voltage; an exponential-in-voltage form; a pair of combined temperature-and-voltage forms; a dedicated electromigration model; a three-stress form adding humidity to temperature and voltage; and — outside the Eyring family — the **Coffin-Manson** model for crack growth and fatigue under temperature cycling.

**Lifetime distribution models for non-repairable populations.** Seven named models, chosen from physical argument, prior success, or empirical fit:
- **Exponential** — one parameter, the *only* distribution with a constant failure rate; models the flat bathtub region; mean = MTTF = 1/λ.
- **Weibull** — flexible two-parameter (shape γ, characteristic life α) model that reduces to the exponential when γ = 1; justified theoretically as an extreme-value / "weakest link" model.
- **Extreme value (Type I)** — limiting distribution of the minimum of many unbounded observations; the natural log of Weibull data is extreme-value data.
- **Lognormal** — flexible model whose logs are normal; theoretically derived from the *multiplicative degradation* argument for many semiconductor wear-out mechanisms.
- **Gamma** — flexible model that arises naturally as the time-to-first-fail for standby exponential backups, and is the conjugate prior used in Bayesian reliability.
- **Fatigue life (Birnbaum-Saunders)** — derived (1969) from random crack growth across independent stress cycles; consistent with Miner's Rule.
- **Proportional hazards (Cox, 1972)** — a survival-analysis model where an explanatory variable multiplies the baseline hazard; mostly medical, limited engineering use.

**Repair rate models for repairable systems.** Defined by choosing a form for M(t), the expected cumulative number of failures, then differentiating to get the repair rate m(t):
- **Homogeneous Poisson Process (HPP)** — constant repair rate λ, exponential inter-arrival times; the only model for the flat bathtub region, hence the workhorse of system reliability planning; 1/λ = MTBF.
- **NHPP Power Law** — a flexible polynomial M(t) = at^b that contains the HPP as a special case; also called the **Duane model** and the **AMSAA model** (after the U.S. Army Materials System Analysis Activity).
- **NHPP Exponential Law** — an alternative growth model to try when a Duane plot shows curvature.

**Bottom-up evaluation.** A set of building-block models to go from component failure modes to system failure rate, all assuming independence:
- **Competing risk model** — within a component, independent failure mechanisms "race"; the first to reach failure causes the component to fail. Multiply mode reliabilities, add mode failure rates.
- **Series model** — same math as competing risk, but components within a system; the first component failure fails the system.
- **Parallel (redundant) model** — system survives until the last component fails; multiply component CDFs.
- **R-out-of-N model** — system survives while at least r of n identical components work; generalizes series (r = n) and parallel (r = 1) via binomial probabilities.
- **Standby model** — a backup in an off-state is switched in on failure; identical exponential backups produce a gamma system lifetime (via convolution).
- **Complex systems** — reduced by successive application of the above; the source flags that some operational-logic structures need formal methods (event trees, cut sets, Boolean/coherent-structure analysis) beyond the Handbook's scope.

**Reliability growth modeling.** For the *Reliability Improvement Test* (also called **TAAF** — Test, Analyze And Fix), where a cross-functional team finds and fixes failure causes so the repair rate improves during the test. Modeled by the NHPP Power Law, visualized with **Duane plots** (log-log cum-MTBF vs. time of failure; straight line ⇒ Power Law). The line's slope β is the *reliability growth slope*.

**Bayesian methodology.** Treats unknown model parameters (e.g., MTBF, λ) as *random* rather than fixed, combining a *prior distribution* with current data via *Bayes formula* to produce a *posterior*. Introduces *credibility intervals* (genuine probability statements about parameters) and *conjugate priors* — notably the gamma prior for the exponential/HPP failure rate, the pair used heavily in Bayesian system reliability.

**Model-choice arguments and the distribution-free option.** For *choosing* a life distribution: the *extreme value argument* (→ Weibull), the *multiplicative degradation argument* (→ lognormal), and the *fatigue life argument* (→ Birnbaum-Saunders), each applied at the **failure-mode level**. When no model assumption is wanted, the distribution-free **Kaplan-Meier** approach lets the data speak — at the cost of needing much more data and making acceleration modeling much harder.

## Key Concepts

- **Quality vs. reliability.** Quality is conformance at the start of use — a single fraction defective, a snapshot. Reliability is the day-by-day motion picture: defects that appear over time are *reliability fallout*, described by a *life distribution model*. Time-zero defects are escaped manufacturing mistakes; later defects are reliability defects.

- **The core functions and their identities.** From a PDF f(t) on [0, ∞) come the CDF F(t) (probability of failing by t), the reliability/survival function R(t) = 1 − F(t), and the hazard rate h(t) = f(t)/R(t) — the *conditional* instantaneous failure rate among survivors. The cumulative hazard H(t) = −ln R(t) ties them together via F(t) = 1 − e^(−H(t)). The *average failure rate* AFR over an interval condenses the changing rate into a single specification-friendly number.

- **System reliability is a product.** For independent components, system reliability is the product of component reliability functions (two identical microprocessors give R²). This single rule underpins the series, parallel, and bottom-up models.

- **Two censoring types and the failure-count rule.** *Type I* fixes the test time T and lets the number of failures r be random (the common case, "right-censored"). *Type II* fixes r and lets time be random (rare, but you know in advance how many failures you'll get). Beyond exact times there is *readout/interval* data and the general *multicensored* case. Crucially, estimate precision scales with √r — the *number of failures*, not the sample size or test length. A test with 5 of 10 failing beats one with 1000 units and 2 failures.

- **True (physical) acceleration is a time rescaling.** When raising stress simply multiplies time-to-fail by a constant *acceleration factor* AF, you have linear acceleration: t_u = AF·t_s, F_u(t) = F_s(t/AF), and so on. A consequence the source stresses: the *shape parameter* of Weibull/lognormal data does **not** change across stress cells, so probability plots from different stresses line up parallel. Each failure mode has its own AF — so separate the modes before analyzing.

- **N(t), M(t), m(t) for repairable systems.** N(t) is one system's step-function failure count; M(t) is the averaged (expected) count across many systems; m(t) = M'(t) is the repair rate / ROCOF. Repair-rate modeling means picking M(t) and differentiating.

- **Conjugate priors and the gamma-exponential pair.** When prior and posterior belong to the same family, the prior is *conjugate*. The Beta is conjugate for a binomial proportion; the **gamma is conjugate for the exponential failure rate** — the workhorse of Bayesian reliability, motivated chiefly by saving test time and cost.

## Mental Models

- **Speedometer, not odometer.** The source compares the instantaneous failure rate to glancing at a car speedometer reading 45 mph: it is the rate *right now* among survivors, and it can change the next instant. Failed units have already "fallen over the cliff" and no longer count.

- **The race with no looking sideways.** In the competing risk model, failure mechanisms race to failure, each going as fast as it can without watching the others; the first to arrive fails the component. This image justifies the two rules — multiply reliabilities, add failure rates — and the practice of analyzing each mode separately (treating other modes as censored), with the model as the "glue" that reassembles the component.

- **Piecewise-exponential approximation.** Just as a curve can be approximated by straight segments, any failure-rate curve can be approximated by month-by-month constant rates — patching exponential segments together. This is why the constant-rate exponential/HPP is so widely usable.

- **The snowball rolling downhill.** For multiplicative degradation, each increment of damage is proportional to damage already present; the bigger the snowball, the faster it grows. Take logs, invoke the Central Limit Theorem, and the time-to-critical-degradation is lognormal — explaining the lognormal's success for corrosion, diffusion, migration, electromigration, and crack growth.

- **Make sense first, fit second.** A model must "make sense" before it fits: don't model a wear-out mechanism with a constant-rate exponential. Because the lognormal and Weibull are both flexible enough to fit a small sample equally well — yet can diverge by orders of magnitude when extrapolated to use conditions far below the test stress — finding a *theoretical* justification is more than an academic exercise.

## Anti-patterns (as the source frames them)

- **Talking about a "failure rate" for a repairable system.** The source calls this incorrect: hazard/failure-rate language belongs to first failures of non-repairable items; repairable systems get a repair rate / ROCOF.

- **Calling the Power Law model a "Weibull Process."** The source warns this name is confusing and should be avoided, because it mixes a non-repairable lifetime model with a repairable inter-arrival model — even though the first-fail time of a Power Law process is Weibull.

- **Letting Bayesian priors masquerade as fact.** The source's own pro/con table flags the cons: an inaccurate prior produces misleading conclusions; there is no single "correct" way to input prior information and different choices give different results; customers may reject the prior's validity; and the results are not objective and do not stand by themselves.

- **Reading the reliability paradox backwards.** Treating a clean test (few or no failures) as proof of reliability ignores that little or no information was actually obtained — high reliability makes failures scarce, which is exactly why accelerated and well-planned testing is needed.

## Key Takeaways

1. **Reliability is quality over time** — a life distribution model F(t) describes fraction-fallout, where a single fraction-defective sufficed for quality.
2. **Keep non-repairable and repairable separate** — lifetime distributions and hazard rate h(t) for the former; M(t) and repair rate/ROCOF m(t) for the latter.
3. **The bathtub curve** organizes a product's life into infant-mortality, flat-intrinsic, and wear-out periods; the exponential/HPP owns the flat middle where systems spend most of their lives.
4. **Information scales with the number of failures**, not units-on-test or test length — which forces accelerated testing and acceleration models when parts are highly reliable.
5. **Physical acceleration is a constant time rescaling**, leaves shape parameters unchanged, and applies per failure mode — so always separate modes before fitting.
6. **System reliability is built bottom-up** from failure modes via competing-risk, series, parallel, r-out-of-n, and standby models — independence assumed, reliabilities multiplied.
7. **Reliability growth (TAAF)** is modeled by the NHPP Power Law / Duane plot; growth slopes empirically fall between 0.3 and 0.6.
8. **Bayesian methods** trade objectivity for the use of prior knowledge (gamma-conjugate-to-exponential), yielding credibility intervals and potential test savings — but only if the prior is trustworthy.

## Connects To

- **Earlier Handbook chapters**: the chapter explicitly notes that reliability terminology, distributions, and models *differ* from those used elsewhere in statistics — extreme value, Weibull, and lognormal here extend the Handbook's general distribution and probability-plotting material to time-to-failure data.
- **Goodness-of-fit, likelihood-ratio, and trend tests** (Section 8.2): the assumption-testing toolkit that validates a chosen life-distribution or growth model before it is trusted for extrapolation.
- **Maximum likelihood and graphical estimation** (Section 8.4): how the named models are actually fit to censored data, including degradation-data fits and use-condition projection.
- **DoD/Army reliability practice**: the AMSAA/Duane lineage of the Power Law connects this material to defense reliability-growth programs and MIL-standard test planning.
- **Systems engineering V&V and RAM**: bottom-up series/parallel/standby modeling feeds reliability allocation, redundancy decisions, and availability analysis in system design — the engineering side of the reliability budgets verified during test.
- **Caveat on this slice**: the NIST/SEMATECH e-Handbook is HTML/web-native and ingested per chapter; figures (bathtub plot, PDF/CDF shapes, probability plots, Duane plots) and the Dataplot/R code blocks referenced throughout are external assets not reproduced here — treat numeric example outputs as illustrative, third-party figure content as out of scope, and consult the live Handbook section for the plots and runnable code.
