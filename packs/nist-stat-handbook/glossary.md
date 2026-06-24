# Glossary — NIST/SEMATECH e-Handbook of Statistical Methods

Key terms, alphabetical, with the chapter where each is developed. Definitions are
synthesized from the Handbook; symbols and formula details live in the chapters and the
original source.

| Term | Meaning (as the Handbook uses it) | Ch |
|---|---|---|
| **4-Plot** | A four-panel diagnostic (run-sequence, lag, histogram, normal probability plot) that checks the four univariate assumptions at a glance. | ch01 |
| **Acceptance sampling** | Deciding to accept/reject a lot from a sample, characterized by an OC curve and AQL/LTPD/risks. | ch06 |
| **Accuracy vs. bias** | Accuracy is a *qualitative* judgement of agreement with truth; bias is the *quantitative* average offset from the true value. | ch02 |
| **Acceleration model** | Maps stress (temperature, voltage, cycling) to a time-rescaling factor so accelerated-test life predicts field life — e.g. Arrhenius, Eyring, Coffin-Manson. | ch08 |
| **ANOVA (Analysis of Variance)** | Partitions total variation into components to draw conclusions about means; one-way, two-way, fixed/random/mixed effects. | ch03, ch05, ch07 |
| **AOQ / AOQL / ASN / ATI** | Acceptance-sampling metrics: average outgoing quality, its limit, average sample number, average total inspection. | ch06 |
| **AQL / LTPD** | Acceptable Quality Level (good lot quality the producer wants accepted) and Lot Tolerance Percent Defective (bad quality the consumer wants rejected). | ch06 |
| **Average Run Length (ARL)** | Expected number of samples before a control chart signals; the currency for comparing chart sensitivity. | ch06 |
| **Bathtub curve** | Hazard-rate-over-life shape: decreasing (infant mortality) → flat (useful life) → increasing (wear-out). | ch08 |
| **Bias (measurement)** | Quantitative difference between a process's long-term average and the reference/true value; reduced by calibration traceable to the reference base. | ch02 |
| **Black-box process model** | A process drawn as inputs/controlled factors/uncontrolled noise → output, used to frame characterization and DOE. | ch03, ch05 |
| **Box-Behnken / Central Composite (CCD)** | Three-level response-surface designs for fitting quadratic (curvature) models. | ch05 |
| **Calibration design** | A redundant least-squares intercomparison schedule (restraint = known reference value) that assigns values to standards/test items while cancelling instrument bias/drift. | ch02 |
| **Censoring (Type I / Type II)** | Reliability data truncated by time (Type I) or by failure count (Type II); information scales with the number of *failures*, not units on test. | ch08 |
| **Check standard** | A database of measurements on a stable artifact that stands in for unseen test items, enabling statistical control and uncertainty estimation. | ch02 |
| **Confounding (aliasing)** | In fractional designs, effects that cannot be separated; managed via the defining relation and design resolution. | ch05 |
| **Control limits vs. specification limits** | Control limits come from the *process's own* variation (voice of the process); specs come from requirements (voice of the customer) — never the same thing. | ch06 |
| **Continuous Linear Model (CLM)** | The Handbook's umbrella for regression/ANOVA-type models with continuous response and a linear-in-parameters structure. | ch03 |
| **Confidence interval / test duality** | A two-sided test rejects exactly when the hypothesized value falls outside the matching confidence interval. | ch07 |
| **CUSUM chart** | Cumulative-sum control chart (with V-mask) tuned to detect small sustained shifts faster than Shewhart. | ch06 |
| **Design of Experiments (DOE)** | Deliberately structured runs that vary factors together to estimate effects efficiently; objective classes: comparative, screening, response-surface, regression. | ch05 |
| **DOE design resolution (III / IV / V)** | How severely effects are aliased: III confounds main effects with two-factor interactions; IV keeps mains clear of two-factor interactions; V keeps mains and two-factor interactions clear of each other. | ch05 |
| **Duane / AMSAA (NHPP Power Law)** | Reliability-growth models for repairable systems under test-analyze-and-fix (TAAF); the Power Law is *not* a "Weibull process." | ch08 |
| **EDA (Exploratory Data Analysis)** | An approach/philosophy: look at the data graphically and let it reveal the model before imposing one. | ch01 |
| **EWMA chart** | Exponentially Weighted Moving Average control chart; memory depth (λ) tunes sensitivity to small shifts. | ch02, ch06 |
| **Error propagation** | Combine *variances*, never standard deviations; sensitivity coefficients are the partial derivatives. | ch02, ch03 |
| **Expanded uncertainty (U = k·u)** | Standard uncertainty multiplied by a coverage factor k (≈2 for 95% at high d.o.f.). | ch02 |
| **Fishbone (cause-and-effect) diagram** | A structured brainstorm of the factors feeding a process output; built after the black box. | ch03 |
| **Foldover design** | Adds a mirror-image fraction to a screening design to de-alias effects (full or partial foldover). | ch05 |
| **Fractional factorial** | A carefully chosen subset of a full factorial that trades resolution for fewer runs. | ch05 |
| **Goodness-of-fit test** | Tests whether data follow a hypothesized distribution: Anderson-Darling, Kolmogorov-Smirnov, chi-square, Shapiro-Wilk W. | ch07, ch08 |
| **Grubbs' test** | A formal test for a single outlier. | ch07 |
| **GUM / VIM (ISO uncertainty framework)** | The governing structure for uncertainty: every component a standard deviation, RSS combination, Type A/Type B grouping. | ch02 |
| **Hazard rate / failure rate h(t)** | Instantaneous failure propensity of survivors — a *speedometer*, defined only for non-repairable units (not repairable systems). | ch08 |
| **Hotelling's T²** | Multivariate control-chart statistic for monitoring several correlated characteristics jointly. | ch06 |
| **Individuals chart** | A Shewhart chart of single observations (used in measurement control because subgroups capture precision, not long-term variation). | ch02, ch06 |
| **Lifetime distribution** | Model for time-to-failure of non-repairable units: Exponential, Weibull, Lognormal, Gamma, Extreme Value, Birnbaum-Saunders. | ch08 |
| **LOESS / LOWESS** | Local regression smoother — a model-building family for capturing structure without a global parametric form. | ch04 |
| **Multiple-comparison procedure** | Controls family-wise error across many pairwise comparisons: Tukey, Scheffé, Bonferroni, Tukey-Kramer, Marascuilo. | ch07 |
| **Out-of-Control Action Plan (OCAP)** | A pre-agreed flowchart of what to do when a chart signals — decided before, not during, the excursion. | ch06 |
| **OC curve (Operating Characteristic)** | Probability of accepting a lot vs. its true defect level; the "fingerprint" of a sampling plan. | ch06 |
| **Parameter / Tolerance design (Taguchi)** | Two-stage robust design: first set factor levels to minimize sensitivity to noise (parameter design), then tighten tolerances only where needed. | ch05 |
| **Phase I vs. Phase II (SPC)** | Phase I establishes/validates limits from retrospective data; Phase II monitors new data against fixed limits. | ch06 |
| **Process capability (Cp, Cpk)** | How well a process's spread fits within specs; meaningful only after the process is stable, and Cp alone ignores centering. | ch03, ch06 |
| **Process model `y = f(x; β) + ε`** | The general statistical model — deterministic function plus random error — underlying regression and DOE analysis. | ch04 |
| **Randomized block design (RBD)** | Blocks out a known nuisance factor so it does not inflate experimental error. | ch05 |
| **Reliability R(t)** | Probability of surviving past time t; "quality over time." For a series system it is the *product* of component reliabilities. | ch08 |
| **Repeatability / reproducibility** | Short-term (within-time, level-1) vs. day-to-day (level-2) variation; the Handbook uses neutral "Level" labels to avoid the contested word *reproducibility*. | ch02 |
| **Response surface (RSM)** | Designs and models that map curvature near an optimum to locate the best operating point. | ch05 |
| **Restraint** | The known reference value(s) that anchor a calibration design's least-squares solution. | ch02 |
| **Run-sequence plot** | Plot of measurements in collection order — the front-line check for fixed location/scale over time. | ch01 |
| **Sensitivity coefficient** | The partial derivative weighting a component's standard deviation in propagation of error. | ch02, ch03 |
| **Series / parallel / k-out-of-n / standby model** | Reliability block structures for building system reliability bottom-up from components. | ch08 |
| **Shewhart chart (X-bar & R / X-bar & s)** | The classic control chart: center line plus ±3σ-style limits estimated from the process itself. | ch06 |
| **Statistical Process Control (SPC) / SQC** | Using control charts to distinguish common-cause from special-cause variation and keep a process in control. | ch06 |
| **Stratification** | Dividing a population into homogeneous strata to sharpen sampling precision and expose systematic effects. | ch03 |
| **Three-level standard deviation model (Level 1/2/3)** | Short-term / day-to-day / run-to-run variability decomposition used throughout measurement characterization. | ch02 |
| **Type A / Type B uncertainty** | Components grouped by *data source* — statistical (A) vs. other-means (B) — not by error type; combined identically. | ch02 |
| **Univariate model `Y = c + ε`** | The simplest process model (constant + random error) whose four assumptions EDA is built to test. | ch01 |
| **WECO rules** | Western Electric run/zone rules that add sensitivity to a Shewhart chart at the cost of more false alarms. | ch06 |
| **Weibull distribution** | The workhorse lifetime model whose shape parameter spans infant-mortality, random, and wear-out failure modes. | ch08 |
| **Welch-Satterthwaite** | Approximates effective degrees of freedom for a combined uncertainty (and for the unequal-variance two-sample t-test). | ch02, ch07 |
