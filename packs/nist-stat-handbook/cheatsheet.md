# Cheatsheet — NIST/SEMATECH e-Handbook of Statistical Methods

Decision rules, selection tables, and tells & smells. Quick routing only — the chapters
carry the reasoning and the source carries the formulas.

---

## The Handbook at a glance (8 chapters)

| Ch | Topic | Use it for |
|---|---|---|
| 1 | Exploratory Data Analysis | Look before you model; check the four univariate assumptions |
| 2 | Measurement Process Characterization | Bias, precision, calibration, gauge R&R, **uncertainty (GUM)** |
| 3 | Production Process Characterization | Frame & characterize a process; stability vs. capability |
| 4 | Process Modeling | Regression (LS / WLS / NLS / LOESS); model assumptions & residuals |
| 5 | Process Improvement (DOE) | Design experiments; screening → response surface; Taguchi |
| 6 | Process Monitoring & Control | SPC charts; capability; acceptance sampling |
| 7 | Product & Process Comparisons | Hypothesis tests & intervals: 1 / 2 / 3+ groups |
| 8 | Assessing Product Reliability | Lifetime & repair-rate models; accelerated tests; growth |

---

## The four univariate assumptions (EDA / 4-Plot)
Run-sequence, lag, histogram, normal-probability plots answer, in order:
1. **Fixed location?** (mean stable over the run-sequence)
2. **Fixed scale?** (spread stable)
3. **Random?** (no autocorrelation — lag plot structureless)
4. **Fixed distribution?** (histogram + normal-probability plot match the assumed shape)
All four hold ⇒ "in statistical control" ⇒ a single summary + prediction interval is valid.

## Choose a comparison test by group count (ch07)
| Question | 1 process | 2 processes | 3+ processes |
|---|---|---|---|
| **Means** | one-sample t / z | two-sample t (Welch if unequal var), paired t | ANOVA → Tukey/Scheffé/Bonferroni; Kruskal-Wallis if non-normal |
| **Variances** | chi-square for s.d. | F-test | tests for equal variances (Levene-type) |
| **Proportions** | exact binomial / Wilson | two-proportion z / Fisher exact | contingency-table chi-square; Marascuilo |
| **Distribution fit** | Anderson-Darling, K-S, chi-square, Shapiro-Wilk W | — | — |

Spine: **test ⇔ interval duality** — reject iff the hypothesized value is outside the interval.
Small n ⇒ exact methods; large n ⇒ approximations (mind their validity gates).

## Pick a control chart (ch06)
| Need | Chart |
|---|---|
| Large abrupt shift, variables data | Shewhart X-bar & R (n<10) or X-bar & s; **Individuals** for single measurements |
| Small sustained drift, fast | CUSUM (V-mask) or EWMA (tune λ) |
| Count / defect data | p, np (defectives) · c, u (defects) |
| Several correlated characteristics | Hotelling's T² (multivariate) |
- **Phase I** builds & validates limits from history; **Phase II** monitors new data.
- Compare charts by **ARL**. More sensitivity (WECO rules, small λ) ⇒ more false alarms.
- Write the **OCAP** before the chart signals.

## DOE design selector (ch05)
| Goal | Design |
|---|---|
| Compare a few options | Comparative / randomized block |
| Screen many factors cheaply | Fractional factorial / Plackett-Burman (Res III) |
| Estimate main effects cleanly | Resolution IV / full factorial |
| Map curvature near optimum | CCD / Box-Behnken (response surface) |
| Make output robust to noise | Taguchi parameter design → tolerance design |
- **Resolution dial:** III (mains aliased w/ 2-factor) < IV (mains clean) < V (mains + 2-factor clean).
- Add center points to test curvature; foldover to de-alias; **randomize**; end with confirmation runs.

## Reliability model fork (ch08)
| System type | Reason with | Models |
|---|---|---|
| **Non-repairable** (replace, not fix) | R(t), hazard h(t), censoring | Exponential, Weibull, Lognormal, Gamma, Extreme Value, Birnbaum-Saunders |
| **Repairable** (fix in place) | N(t), M(t), repair rate m(t) | HPP; NHPP Power Law / Duane-AMSAA (growth, TAAF) |
- **Series** system reliability = product of parts; add **parallel / k-of-n / standby** for redundancy.
- Acceleration model (Arrhenius, Eyring, Coffin-Manson) rescales time stress→use.
- Information scales with the number of **failures**, not units on test.

## Uncertainty in one screen (ch02, GUM)
- Every component is a **standard deviation**; group by **Type A** (statistical) / **Type B** (other).
- Combine by RSS with sensitivity coefficients: `u = sqrt(Σ aᵢ² sᵢ²)`. **Add variances, not s.d.s.**
- Type B half-width a → s: `a/√3` uniform (largest), `a/√6` triangular, `a/3` normal (smallest).
- Expanded `U = k·u`, k≈2 ⇒ ~95% at high d.o.f.; use **Welch-Satterthwaite** for unknown d.o.f.
- Levels of variability: **L1** short-term · **L2** day-to-day · **L3** run-to-run.

---

## Tells & smells (anti-patterns the Handbook flags)
- **Reporting Cp/Cpk on an out-of-control process** → capability is meaningless until stable. (ch03/ch06)
- **Cp alone = "capable"** → ignores centering; check Cpk. (ch06)
- **One-factor-at-a-time** → misses interactions, wastes runs; use a factorial. (ch05)
- **One big definitive experiment** → sequence it; screen, then optimize. (ch05)
- **Randomizing center-point runs** → they should be spread to detect drift, not randomized. (ch05)
- **Adding standard deviations** → add variances. (ch02/ch03)
- **"Failure to reject" = equality** → it isn't proof. (ch07)
- **Assuming σ known without checking** → validate it. (ch07)
- **A "failure rate" for a repairable system** → use repair rate / ROCOF. (ch08)
- **Calling the Power Law a "Weibull process"** → it isn't. (ch08)
- **Recalculating control limits with no compelling reason** → erases the baseline. (ch06)
- **Trusting chart/plan properties from too little data** → ARL/limits need enough d.o.f. (ch06)
- **Skimping on planning, then drifting from the plan** → the most expensive mistake. (ch03)
- **Imposing a model before looking** → run the 4-plot first. (ch01)
