# Chapter — Product and Process Comparisons

> Source: NIST/SEMATECH e-Handbook of Statistical Methods, Chapter 7 ("Product and Process Comparisons"). This pack ingests the Handbook as HTML/web-native material; each section is a separate web page rather than a paged document, so cross-references in the original ("see the previous page", "discussed elsewhere", "Chapter 1") point at sibling pages. Many tables, screenshots, and worked figures live in per-block third-party images (EXCEL Goal Seek screens, plotted box plots, ANOVA layout graphics) that do not survive text extraction; where the source clearly depends on such a figure, this chapter describes the procedure rather than reproducing a missing picture. All numeric examples below are paraphrased from the source, not copied verbatim.

## Core Idea

This chapter is about answering one recurring engineering question in many disguises: *is what I am measuring consistent with what I expect, or different from something I am comparing it against?* The Handbook organizes the whole topic by **how many processes are in play**:

- **One process** compared against a known standard, a nominal target, or an assumed distribution (Section 7.2).
- **Two processes** compared against each other (Section 7.3).
- **Three or more processes** compared simultaneously (Section 7.4).

Across all three, the same two inferential machines do the work: the **hypothesis test** (which returns a reject / fail-to-reject verdict against a critical value or p-value) and the **confidence interval** (which returns a plausible range for the parameter). A central theme of the chapter is that these two machines are *equivalent* — for essentially every test there is a corresponding interval, and the null value is rejected if and only if it falls outside the matching interval. The chapter's job is to map each comparison question to the right test statistic, the right reference distribution, and the right caveats about when the approximations hold.

## Frameworks Introduced

The Handbook names a large catalogue of specific tests and procedures. Listed below in roughly the order the source introduces them, with what each is for.

**Introductory machinery (7.1)**
- **Statistical hypothesis test** — the formal structure of a null hypothesis (H0), an alternative (Ha), a test statistic, and a rejection region. Introduced in 7.1.3 with the photomask linewidth and light-bulb-lifetime examples to motivate two-sided vs. one-sided alternatives.
- **Significance level (alpha), error of the second kind (beta), and the operating characteristic (OC) curve** — 7.1.3 frames alpha as the producer-side risk of wrongly rejecting a true null and beta as the risk of failing to detect a real discrepancy, with OC curves attributed to *Natrella (1962)* for summarizing beta across alternatives.
- **Critical values and p-values** — 7.1.3.1 defines the p-value as the probability of a statistic at least as extreme as observed under the null, and stresses deciding the threshold in advance.
- **Confidence intervals and the test/interval equivalence** — 7.1.4 and 7.1.5 establish that a 100(1-alpha)% interval and an alpha-level two-sided test carry the same information.
- **Box plot with inner/outer fences** (7.1.6) for outlier screening, using Q1, Q3, and the interquartile range; points beyond Q ± 1.5·IQ are mild outliers and beyond Q ± 3·IQ are extreme. **Grubbs' Test** is named as the analytic outlier procedure (detailed in the EDA chapter).
- **Reverse Arrangement Test** (7.1.7) — named as a non-parametric trend test, with detail deferred to Chapter 8; the default trend check is fitting a line and testing whether its slope differs from zero (Chapter 4).

**One-process tests (7.2)**
- **Goodness-of-fit family** (7.2.1): **Chi-square goodness-of-fit** (continuous or discrete; requires grouping), **Kolmogorov-Smirnov (K-S) test** (continuous only, based on the empirical CDF; attributed to *Kolmogorov 1933* and *Smirnov 1936*), **Anderson-Darling test** (a K-S modification weighting the tails more, attributed to *Stephens 1974*, with distribution-specific critical values), and **Shapiro-Wilk W test** for normality (proposed 1965; percentage points from *Pearson and Hartley 1972*).
- **One-sample t-test and z-test for a mean** (7.2.2) — t when sigma is estimated, z when sigma is known.
- **Chi-square test for a standard deviation** (7.2.3), using (N-1)s²/sigma0².
- **Proportion-defective test via normal approximation to the binomial** (7.2.4 / 7.2.7), plus the **Wilson interval** for a proportion (7.2.4.1) — historically introduced by *Wilson (1927)*, recommended by *Agresti and Coull (1998)* and *Brown, Cai and DasGupta (2001)*. The chapter explicitly corrects its own earlier terminology: what it now calls the **Wilson method** it formerly labeled Agresti-Coull, and the distinct adjusted-Wald method is the true Agresti-Coull. **Exact binomial (Clopper-Pearson-style) intervals** are given for small samples, with a worked EXCEL Goal Seek and Dataplot recipe.
- **Finite Population Correction (fpc) factor** (7.2.7.1) for sampling without replacement from a small lot.
- **Defect-density test via the Poisson distribution** (7.2.5), with a normal approximation valid when A·D is large.
- **Coverage intervals for population values** (7.2.6): the empirical rule, the distribution-free **Bienaymé-Chebyshev rule** (at least 100(1-1/k²)% within k SDs), **percentile estimation** (with the Handbook's default R6 method and the *Hyndman and Fan (1996)* R1-R9 taxonomy noted), **tolerance intervals for a normal distribution** (Howe's k-factor approximation, *Howe 1969*, with *Guenther 1977* correction and a non-central-t alternative, *Natrella 1963*), and **distribution-free tolerance intervals** from the largest and smallest observations (*Hahn and Meeker*).

**Two-process tests (7.3)**
- **Two-sample t-test for means** (7.3.1), in pooled-variance form (equal SDs) and **Welch-Satterthwaite** form (unequal SDs, with the approximate degrees-of-freedom formula).
- **Paired-sample t-test** (7.3.1.1) on the per-pair differences.
- **F-test for the ratio of two variances** (7.3.2), with the reciprocal-and-swap rule for looking up critical values.
- **Two-proportion z-test** (7.3.3, large samples) and the **Fisher Exact Probability Test** (small samples, via the hypergeometric distribution on a 2×2 contingency table), plus **Tocher's modification** (*Tocher 1950*) which randomizes to make Fisher's conservative test hit the nominal alpha.
- **Comparison of two exponential life distributions** (7.3.4), framed as comparing means or hazard rates, with **Type II censoring** defined.

**Three-or-more-process tests (7.4)**
- **Kruskal-Wallis test** (7.4.1) — named as the non-parametric way to compare several populations of unknown distribution.
- **Tests for equal variances across groups** (7.4.2) — the section header names the "same variance?" question for normal data (Bartlett- and Levene-type tests in the Handbook's structure).
- **One-way ANOVA** (7.4.3), with the SS(Total) = SST + SSE decomposition, the ANOVA table, the F = MST/MSE test, the **fixed-effects vs. random-effects models**, **contrasts and orthogonal contrasts**, and confidence intervals for treatment-mean differences and contrasts.
- **Two-way ANOVA** (7.4.3.7-8) — factorial layout partitioning SS(Total) into SS(A) + SS(B) + SS(AB) + SSE.
- **Variance components** (7.4.4) — method-of-moments estimates from expected mean squares (EMS), plus **REML** as the preferred estimator (*Searle 2006*), noting method-of-moments can yield a nonsensical negative variance estimate.
- **Contingency-table chi-square** (7.4.5 independence; 7.4.6 homogeneity of proportions), using expected cell frequency = row total × column total / grand total and (r-1)(c-1) degrees of freedom.
- **Multiple-comparison procedures** (7.4.7): **Tukey's method** (all pairwise differences via the studentized range q; **Tukey-Kramer** for unequal n), **Scheffé's method** (all possible contrasts), **Bonferroni's method** (a pre-chosen finite set of g comparisons, each at alpha/g), and the **Marascuilo procedure** (all pairwise proportion differences after a contingency-table rejection).

## Key Concepts

**The test/interval duality is the spine of the chapter.** 7.1.5 works through the photomask example: rejecting H0 that the mean linewidth equals 500 micrometers is algebraically the same as 500 falling outside the interval Ybar ± z·sigma/sqrt(N). Every later section reuses this — the proportion section builds its interval by inverting its test; the two-mean section notes that zero inside the difference interval means the means are equivalent; the two-variance section notes that one inside the variance-ratio interval means the SDs are equivalent. The interval is presented as the more informative object because, as the proportion section says, it has value in its own right and need not be used only for testing.

**Approximations come with explicit validity gates.** The chapter is unusually disciplined about saying when a normal approximation is allowed to stand in for a discrete distribution. For a proportion the gate is min{N·p0, N(1-p0)} ≥ 5 (so p0 = 0.1 needs N ≥ 50, p0 = 0.01 needs N ≥ 500). For defect density the gate is A·D > 10 for a reasonable approximation and > 20 for a good one. When these gates fail, the chapter routes you to an exact method (binomial for proportions, the small-sample exact interval), and it openly notes that whether such an interval is *truly* exact depends on the software solving it.

**Choosing the null is a strategy decision, not a mechanical one.** 7.3.1 states the heuristic plainly: put what you hope to prove in the alternative so that rejecting the null is the affirmative finding, and keep the traditional/safe claim as the null unless strong evidence overturns it. The wafer-defect example (new process, 26 of 200 defective, 0.13 vs. a historical 0.10) is deliberately set up as a one-sided test guarding against degradation; the test statistic (1.41) falls short of 1.645, so the chapter refuses to conclude the new process is worse — it stresses that failing to reject is not proof of equality, only an absence of sufficient evidence.

**Sample-size planning balances two risks and usually requires a guess.** For means, N depends on alpha, beta, and the shift delta (often expressed in standard-deviation units), and when sigma is unknown the t-based formula must be iterated because its degrees of freedom depend on the very N being solved for — one iteration is normally enough. For proportions the worst-case guess p = 0.5 maximizes the required N, giving the most conservative (and most expensive) plan. For variance the procedure (following *W. Diamond 1989*) is stated in terms of a variance discrepancy and solved by scanning degrees of freedom in a table or by root-finding.

**ANOVA analyzes variances to draw conclusions about means.** The chapter anticipates the obvious confusion (why study variances to compare means?) and answers it via the SS decomposition: when the group means are truly equal, the treatment mean square and the error mean square both estimate the same error variance, so their ratio F should sit near 1; a large F is evidence the treatment mean square has been inflated by real mean differences. The resistor-temperature example (three temperatures, F = 9.59 against a 3.89 critical value, p = 0.00325) rejects equality — but the chapter immediately flags that ANOVA alone cannot say *which* means differ, which is precisely what the multiple-comparison section exists to resolve.

**Fixed vs. random effects changes the inferential target.** If the factor levels are the only ones of interest (specific temperatures, ITS-90 fixed points), they are fixed effects and the tau_i are parameters. If the levels are a random sample standing in for a larger population (operators, days, batches, lots), they are random effects and the tau_i are random variables; the goal shifts from comparing specific levels to estimating **variance components** — how much of total variability each source contributes. The batch example apportions 86.7% of variance to between-batch differences and 13.3% to within-batch error.

**Multiple comparisons trade breadth of coverage against interval width.** All four procedures control the *family-wise* error rate, but they differ in scope and therefore in conservatism. The chapter's comparison rules are concrete: Tukey gives the narrowest intervals when *only pairwise* differences matter; Scheffé covers *all possible contrasts* (an infinite set) and is widest but guarantees finding at least one significant contrast whenever ANOVA rejects; Bonferroni fits a *pre-chosen finite* set and beats Scheffé when the number of contrasts is small (roughly, fewer than twice the number of factors). The standing advice: many packages compute all three, so pick the method giving the smallest band for your situation.

## Mental Models

**The "how many processes" decision tree.** Treat Section number as a router. One thing measured against a fixed expectation → 7.2. Two things measured against each other → 7.3. Three or more at once → 7.4. Within each branch the sub-question (mean? variability? proportion? distribution shape?) selects the specific test. This mirrors how an engineer actually arrives at the question.

**Test statistic = (signal) / (noise), compared to a reference distribution.** Nearly every statistic in the chapter is a standardized distance: (estimate − hypothesized value) divided by a standard error, then read against the normal, t, chi-square, or F distribution as appropriate. t when a standard deviation is estimated; z when it is known; chi-square for a single variance or for counts in cells; F for a ratio of two variances or the ANOVA mean-square ratio. Knowing which distribution supplies the critical value is most of the battle.

**The "is the boring value inside the interval?" check.** For a mean difference, the boring value is 0. For a variance ratio, it is 1. For a proportion against a target, it is the target p0. If the boring value sits inside the corresponding confidence interval, you cannot distinguish the processes; if it sits outside, you can. This single habit collapses many of the chapter's tests into one visual.

**Exact when small, approximate when large.** The recurring fork: discrete data (counts, defectives, failures) gets an exact distribution (binomial, hypergeometric, Poisson) when N is small, and a normal stand-in once N clears the validity gate. The exact path is more work and often needs root-finding software; the approximate path is a clean table lookup but only trustworthy above the threshold.

**A lower bound that can't physically occur is a defect in the method.** The chapter elevates this to a principle when arguing for the Wilson interval over the textbook Wald interval: an interval whose lower limit can be negative for a proportion (an impossible parameter value) is an inferior construction, and the same critique applies to control-chart limits in Chapter 6.

**ANOVA is a gate, not a destination.** The F test tells you only whether *some* difference exists. If it fails to reject, you stop — there is nothing to dissect. If it rejects, it opens the door to the real questions (which groups, by how much), answered by contrasts and multiple-comparison procedures. Running pairwise t-tests over every pair instead is a trap: it inflates the family-wise error rate beyond the nominal alpha.

## Anti-patterns

The source names these explicitly:

- **Using a confidence-limit method that can return an impossible parameter value.** The chapter calls the common Wald proportion interval (phat ± z·sqrt(phat(1-phat)/n)) an *inferior approach* precisely because its lower limit can go negative, and extends the criticism to the analogous control-chart limits in Chapter 6.
- **Repeating pairwise comparisons to substitute for a multiple-comparison procedure.** 7.4.7 warns that doing pairwise tests over and over for all pairs will not, in general, work, because the overall significance level is no longer what a single-pair comparison specifies.
- **Deciding which contrasts to examine after seeing the data, when you needed pre-planned contrasts.** The chapter cautions that pre-planned contrast investigations are only valid if chosen *in advance* of observing results; otherwise the stated confidence levels do not hold (which is exactly the situation the post-hoc Tukey/Scheffé/Bonferroni machinery is built for).
- **Treating "failure to reject" as proof of equality.** Both the proportion example and the one-sample mean example state outright that not rejecting only means insufficient evidence — the new process "may, indeed, be worse" but more data would be needed.
- **Assuming the standard deviation is known without checking it.** The one-sample mean section carries an explicit *Caution* that if sigma is assumed known for the test, that assumption should itself be verified with a test on the standard deviation.
- **Assuming a distribution shape when the stakes make a wrong assumption dangerous.** The tolerance-interval section flags that for something like airplane-windshield glass strength, where a large fraction of the population must fall within limits, making unwarranted assumptions about the exact distribution is particularly hazardous — favoring the distribution-free interval despite its greater width.
- **Trusting the Tocher randomization to give reproducible decisions.** The chapter notes a real drawback: because Tocher's modification draws a random number, a second analyst working the same data could draw differently and reach a different conclusion about H0.

## Key Takeaways

- Map the question to the number of processes first (one / two / three-plus), then to the parameter in question (mean, variability, proportion, distribution, failure rate), then to the matching test statistic and reference distribution.
- Every hypothesis test has an equivalent confidence interval; the interval is the more informative deliverable and lets you test by checking whether the "boring" value (0, 1, or the target) lies inside it.
- Normal approximations to discrete distributions are only valid above stated gates (min{N·p0, N(1-p0)} ≥ 5 for proportions; A·D > 10-20 for defect density); below them, use the exact binomial / hypergeometric / Poisson methods.
- Prefer the Wilson interval over the Wald interval for proportions — the Wald interval can produce an impossible negative lower limit, which the Handbook judges an inferior construction.
- Form the null so that rejecting it is your affirmative finding, choose alpha and beta deliberately, and remember that sample-size formulas for unknown sigma must be iterated.
- ANOVA's F test only signals *that* a difference exists; use contrasts and a family-wise-controlled multiple-comparison procedure (Tukey for all pairwise, Scheffé for all contrasts, Bonferroni for a small pre-chosen set, Marascuilo for proportions) to find *which* differences and *how large*.
- Distinguish fixed effects (specific levels of interest) from random effects (levels sampled to represent a population); the latter shifts the goal to estimating variance components, with REML preferred over method-of-moments because the latter can return a negative, nonsensical variance.
- For small samples or non-normal data, reach for the exact and non-parametric tools the chapter names: Fisher's exact test (two proportions), Kruskal-Wallis (several populations), and tolerance intervals from the extreme observations (any distribution).

## Connects To

- **Chapter 1 (Exploratory tools / basics)** — the source repeatedly defers the underlying tables (t, chi-square, F, normal critical values) and the foundational treatment of hypothesis testing, significance levels, and critical regions to Chapter 1.
- **EDA chapter** — outlier detection (box plots, scatter plots, Grubbs' Test) and the chi-square goodness-of-fit computation formulas are housed there.
- **Chapter 4 (Process Modeling / regression)** — the slope-significance method behind trend detection.
- **Chapter 6 (Process Monitoring / control charts)** — the chapter's critique of impossible lower limits is extended explicitly to control-chart limits there.
- **Chapter 8 (Reliability)** — the Reverse Arrangement Test for trends and, by topic, the censored-lifetime and exponential-comparison material.
- **Design of Experiments** — two-way and n-way ANOVA, factorial layouts, and contrasts are the on-ramp to formal DOE.
- **Systems-engineering practice** — these methods are the quantitative backbone of acceptance testing, supplier/lot qualification (two-proportion and homogeneity tests), process-change verification (one- and two-sample mean tests, proportion-defective tests), tolerance-limit setting against engineering specifications, and measurement-system comparison (paired t-test) — i.e., the statistical evidence layer beneath V&V and quality assurance.
