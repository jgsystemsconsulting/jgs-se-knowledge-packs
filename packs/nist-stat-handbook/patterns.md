# Patterns — NIST/SEMATECH e-Handbook of Statistical Methods

Reusable techniques the Handbook teaches, framed as *when to use / how / trade-offs*.
Each maps to the chapter that develops it. These are the recurring moves of applied
statistics for engineering and metrology, not a formula reference.

---

## P1 — Run the 4-Plot before any model (EDA gate)
**When** — at the start of any univariate analysis, before fitting or testing anything.
**How** — produce the run-sequence, lag, histogram, and normal-probability plots together
and read them as four questions: is location fixed? is scale fixed? is the data random
(no autocorrelation)? is the distribution as assumed? Pass on all four ⇒ the data are "in
statistical control" and a single summary plus prediction interval is defensible.
**Trade-offs** — graphical, fast, and assumption-revealing, but qualitative; confirm
borderline calls numerically. A failed panel is a *finding*, not a nuisance — it tells you
which assumption (and which physical cause) to chase. (ch01)

## P2 — Black box first, fishbone second (characterization framing)
**When** — beginning a production-process or measurement characterization study.
**How** — draw the process as a black box (inputs, controlled factors, uncontrolled noise,
output) to bound the problem, *then* expand suspected drivers with a cause-and-effect
(fishbone) diagram. Decide what to measure from the diagram, not from habit.
**Trade-offs** — spending effort on planning up front saves far more on wasted data
later; the discipline is resisting the urge to collect first and think second. (ch03)

## P3 — Combine uncertainty by adding variances, never standard deviations
**When** — propagating error through any function of measured quantities, or summing
calibrated values.
**How** — square each component's standard deviation (weighted by its sensitivity
coefficient = the partial derivative), sum, then take the root: `u = sqrt(Σ aᵢ²sᵢ²)`.
Include covariance terms only when estimated from sufficient data (calibrated values from a
design often carry non-zero covariances that matter when you add items).
**Trade-offs** — top-down estimation (replicate the final result directly) automatically
captures covariances and unsuspected sources; propagation is the fallback when the result
can't be replicated. Adding standard deviations directly is a classic, silent error. (ch02, ch03)

## P4 — Build an uncertainty budget the GUM way
**When** — you must state the uncertainty of a *specific reported result*.
**How** — list every component as a standard deviation; group by data source (Type A =
from statistical analysis, Type B = from other means) not by error type; assume biases
corrected (or assess an uncertainty for an uncorrected one); RSS to a standard uncertainty;
multiply by k (≈2 for ~95% at high d.o.f.) for the expanded uncertainty. Use
Welch-Satterthwaite when the combined degrees of freedom are unknown.
**Trade-offs** — Type B half-widths converted under an assumed shape (a/√3 uniform is most
conservative, a/3 normal least) carry judgement; document the assumption. Uncertainty is a
property of a result, not of a method — don't quote a method's precision as a result's
uncertainty. (ch02)

## P5 — Establish control before claiming capability
**When** — before reporting Cp/Cpk or any capability claim.
**How** — bring the process into statistical control first (Phase I: build and validate
limits from retrospective data; confirm stability on a control chart). Only a stable
process has a meaningful, predictable capability. Then compute capability against specs in
Phase II monitoring.
**Trade-offs** — capability indices on an out-of-control process are meaningless; Cp alone
ignores centering, so pair it with Cpk. Don't recalculate control limits without a
compelling, documented reason. (ch03, ch06)

## P6 — Match the control chart to the shift you fear
**When** — choosing an SPC chart.
**How** — Shewhart (X-bar & R / s, or individuals) for large, abrupt shifts and broad
diagnosis; CUSUM or EWMA when small sustained drifts must be caught quickly (tune the V-mask
or λ memory depth). Attributes charts (p, np, c, u) for count/defect data; Hotelling's T²
for correlated multivariate characteristics. Compare candidates by Average Run Length (ARL).
**Trade-offs** — sensitivity is *bought with false alarms*: WECO/zone rules and small λ
catch more but signal falsely more often. Write an OCAP so the response is decided before
the chart signals. (ch06)

## P7 — Sequence DOE as a staircase, never one big experiment
**When** — improving or optimizing a multi-factor process.
**How** — screen many factors cheaply with a low-resolution fractional or Plackett-Burman
design; add center points to test for curvature; foldover to de-alias the survivors; then
spend three-level response-surface runs (CCD / Box-Behnken) only near the optimum. Always
randomize run order, and finish with confirmation runs.
**Trade-offs** — one-factor-at-a-time is a trap: it misses interactions and wastes runs.
Resolution is the confounding dial — III is cheapest but aliases mains with two-factor
interactions; spend on V only where you need clean interaction estimates. Three levels cost
a lot, so reserve them for the optimization stage. (ch05)

## P8 — Pick the comparison test by "how many processes?"
**When** — comparing means, variances, or proportions across groups.
**How** — branch on the count. **One** process vs. a standard: one-sample t/z (mean),
chi-square (s.d.), exact binomial/Wilson (proportion). **Two**: two-sample t (Welch when
variances differ), paired t, F-test (variances), two-proportion z / Fisher exact.
**Three+**: ANOVA (means), then a multiple-comparison procedure (Tukey/Scheffé/Bonferroni)
to find *which* differ; Kruskal-Wallis if non-normal. Lean on test/interval duality: ask
"is the boring value inside the interval?"
**Trade-offs** — "failure to reject" is not proof of equality. Use exact methods for small
samples, approximations (with their validity gates) for large. ANOVA is a gate that says
*something* differs, not a destination. (ch07)

## P9 — Keep non-repairable and repairable reliability separate
**When** — any reliability assessment.
**How** — for non-repairable units fit a *lifetime distribution* (Weibull, lognormal,
exponential…) and reason with R(t), the hazard rate h(t), and censoring (information scales
with the number of *failures*). For repairable systems use a *repair-rate* model (HPP, or
NHPP Power Law / Duane-AMSAA for reliability growth under TAAF) and reason with N(t), M(t),
m(t). Build system reliability bottom-up from series/parallel/k-of-n/standby blocks.
**Trade-offs** — mixing the two is the central error: a repairable system has no single
"failure rate," and the Power Law model is *not* a "Weibull process." Make physical sense of
the failure mode first, fit the distribution second. Accelerated tests need a justified
acceleration model (Arrhenius, Eyring, Coffin-Manson) that rescales time. (ch08)

## P10 — Use a check standard to make a measurement process auditable
**When** — running an ongoing calibration, certification, or production-metrology process.
**How** — build a check-standard database (≈100+ values to set a baseline) on a stable
artifact, monitor bias and long-term variation with an individuals Shewhart (and EWMA for
small shifts) chart, and decompose variability into Level-1/2/3 standard deviations. The
check standard both controls the process and supplies the Type A uncertainty components.
**Trade-offs** — the method needs a stable surrogate, so one-time, special, and destructive
tests are hard to characterize. Statistical control guarantees *comparability*, not
correctness, if the process was mis-specified or mis-calibrated to begin with. (ch02)
