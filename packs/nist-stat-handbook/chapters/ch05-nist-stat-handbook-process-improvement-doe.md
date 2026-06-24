# Chapter — Process Improvement (Design of Experiments)

## Core Idea

This chapter is the NIST/SEMATECH handbook's treatment of statistical Design of Experiments (DOE) — the discipline of deliberately changing one or more controllable process variables (factors) to observe their effect on one or more measured outputs (responses), and laying that plan out in advance so the resulting data yield valid, objective conclusions. The governing premise is economy of information: a well-chosen design extracts the maximum amount of usable knowledge from a fixed budget of experimental effort. The mental picture the handbook returns to is a "black box" process model — controllable inputs on one side, continuous measured responses on the other, and an empirical polynomial fitted to connect them. That polynomial is usually first-order (main effects plus interactions) or second-order (adding quadratic curvature terms); the source notes that industrial processes almost never need a third-order model if factor ranges are chosen well.

The chapter's spine is a decision flow: figure out the objective, pick the factors and their level ranges, choose a design matched to that objective and factor count, run it, check the data against assumptions, analyze, and present results — often feeding into another round. A recurring theme is that this is *iterative*, not a single grand experiment. The handbook is emphatic that "putting all one's eggs in one basket" is a mistake; a sequence of smaller experiments, each informing the next, is both more reliable and more economical. The other recurring theme is that real factor effects rarely act in isolation: interactions, where one factor's influence depends on another's setting, are the whole reason the older "change one thing at a time" habit fails.

## Frameworks Introduced (exact source names, when/how)

- **Design of Experiments (DOE) / Experimental Design** — the umbrella discipline. The handbook frames it as an efficient planning procedure and lists seven canonical uses: choosing between alternatives, screening to find key factors, response-surface modeling (to hit a target, reduce variability, maximize/minimize, or make a process robust), seeking multiple goals, and regression modeling.

- **The four design objective classes** — the source organizes all standard designs under *comparative*, *screening*, *response surface method (RSM)*, and *regression* objectives, plus a *mixture* objective for factors that are proportions of a blend. Its Design Selection Guideline (Table 3.1) maps factor count to recommended design: one factor → completely randomized; 2–4 factors → randomized block (comparative), full or fractional factorial (screening), central composite or Box-Behnken (RSM); 5+ factors → fractional factorial or Plackett-Burman, with the advice to screen first.

- **Completely randomized designs** — one primary factor, levels assigned to experimental units in random run order. Defined by three numbers: k (factors, = 1 here), L (levels), n (replications), with total runs N = k·L·n. Balance (equal replication per level) is recommended to maximize the sensitivity of the t or F tests.

- **Randomized block designs (RBD)** — one factor of primary interest plus nuisance factors held constant within homogeneous "blocks." The governing maxim the source quotes is **"Block what you can, randomize what you cannot."** Blocking removes the contribution of a few important controllable nuisance variables; randomization handles the rest.

- **Latin square, Graeco-Latin square, Hyper-Graeco-Latin square designs** — efficient comparative designs that block 2, 3, and 4 nuisance factors respectively, arranged in a k×k grid where every row and column receives each treatment once. The source notes these assume no interactions among blocking and treatment variables, require all factors to share the same level count, and are equivalent to specific fractional factorials (e.g., a 4×4 Latin square equals a 4^(3-1) fraction).

- **Full factorial designs** — every combination of factor levels is run; for two-level designs the standard layout uses +1/−1 coding for high/low, with center points coded 0. The source presents the model matrix (the design matrix augmented with an "I" intercept column and interaction columns) and notes that coding produces *orthogonal* columns, where the dot product of any pair is zero.

- **Fractional factorial designs** — a chosen fraction (half, quarter, eighth, …) of the full 2^k design, written 2^(k−p), constructed by assigning each of the p extra factors to a higher-order interaction column. The source develops the 2^(3−1) half-fraction in detail as the teaching case.

- **Plackett-Burman designs** — economical screening designs from R.L. Plackett and J.P. Burman's 1946 *Biometrika* paper, with run counts that are multiples of four rather than powers of two. They are resolution III, with main effects heavily confounded with two-factor interactions; the 12-run plan handles up to 11 factors.

- **Response surface designs (RSM)** — second-order designs for fitting quadratic models. The two classical families, both introduced in the 1950s, are **Box-Wilson Central Composite Designs (CCD)** and **Box-Behnken designs**. CCDs embed a factorial/fractional core plus center points and add "star points" at distance α from center; the source names three varieties — Circumscribed (CCC), Inscribed (CCI), and Face-Centered (CCF). Box-Behnken designs place treatments at edge midpoints plus center, are an independent quadratic design (no embedded factorial), and need only three levels per factor.

- **Center point ("control") runs** — added to a two-level design to measure process stability/variability and to check for curvature. The rough rule of thumb is 3 to 5 center points; crucially, they are *not* randomized.

- **Foldover designs** — methods to raise a design's resolution by adding runs. The **mirror-image foldover** reverses the signs of all columns, lifting a resolution III design to resolution IV (breaking the alias link between main effects and two-factor interactions). **Alternative (partial) foldovers** break up specific alias patterns.

- **Taguchi designs / Taguchi Methods** — attributed to Genichi Taguchi, who termed DOE "off-line quality control." The source highlights two of his conceptual contributions: **Parameter Design**, using **inner arrays** (controllable design factors) crossed with **outer arrays** (uncontrollable noise factors) to find robust settings; and **Tolerance Design**, the tightening of critical tolerances, recommended only as a last resort after parameter design and analyzed via a Taylor-series expansion of the response.

- **The EDA approach to experimental design** — an exploratory, plot-driven alternative the handbook advocates alongside formal methods, anchored by the **|Effects| plot** and a four-lens reading of effect importance: statistical, engineering, numerical, and pattern significance.

## Key Concepts

**Process models and coding.** DOE rests on fitting an empirical polynomial to the black box. A two-factor linear model is Y = β₀ + β₁X₁ + β₂X₂ + β₁₂X₁X₂ + error, where the cross-product term captures interaction. A quadratic (second-order) model adds squared terms (β₁₁X₁² etc.) to describe curvature and is the standard RSM workhorse; the source notes most software omits cross-product-of-squares terms by default. Coding factor settings to +1/−1 (with 0 at center) is called orthogonal coding and makes the design matrix columns orthogonal, which cleanly separates the estimated coefficients.

**The four pre-experiment assumptions.** Before running, the handbook insists on checking: (1) **measurement capability** — confirm the gauges can actually resolve the changes you expect to see, ideally with an SPC check kept on the instruments throughout; (2) **process stability** — bracket and intersperse control runs at standard setpoints, and if the process drifts, add a trend/run-number term to the model; (3) **a simple model exists** — polynomial approximations only work for smoothly varying responses, so a jagged or only-piecewise-smooth surface must be split into separate experiments; (4) **well-behaved residuals** — residuals (observed minus predicted) should be roughly normal, independent, mean-zero, constant-variance, examined primarily through graphs.

**Confounding (aliasing).** This is the central price of fractionation. When the X₁·X₂ interaction column is reused to set the X₃ factor in a 2^(3−1) design, the estimate of the X₃ main effect can no longer be separated from the X₁X₂ interaction — they are confounded. The shorthand "3 = 12" means X₃'s column equals the product of X₁ and X₂'s columns; multiplying through (any column times itself gives the all-ones identity I) generates the full alias set {1=23, 2=13, 3=12, I=123}. Fractional designs only work under a **sparsity of effects** assumption: the confounding interactions are presumed negligible relative to the main effects of interest.

**Generators, defining relation, and resolution.** A **design generator** (or generating relation), written I = 123, lets you generate the complete confounding pattern. The full collection of generators plus all products formed from them is the **defining relation**; for a 2^(k−p) design it contains 2^p − 1 "words." The **resolution** is the length of the *shortest* word in the defining relation, written in Roman numerals. The source's tiered meaning: **Resolution III** — main effects aliased with two-factor interactions; **Resolution IV** — main effects clear of two-factor interactions, but two-factor interactions aliased with each other; **Resolution V** — no main effect or two-factor interaction aliased with another of those, only with higher-order interactions. Higher resolution means less severe confounding but more runs. Among designs of equal resolution, the one minimizing short words (minimizing two-factor aliasing) has **minimum aberration**.

**Screening vs. RSM strategy.** Screening designs (typically resolution III, sometimes IV; Plackett-Burman is the classic family) economically separate the significant few main effects from the trivial many, assuming interactions are an order of magnitude less important. RSM designs (resolution V and higher, or the dedicated CCD/Box-Behnken families) estimate interaction and quadratic effects to map the local shape of the response surface for optimization, troubleshooting, or robustness.

**Rotatability and the star-point distance α.** A design is **rotatable** when the variance of the predicted response depends only on distance from the design center, not direction — so the design biases the search toward no particular direction, which matters when the optimum's location is unknown. In a rotatable design the prediction-variance contours are concentric circles. For a CCD, rotatability is achieved by setting α = (number of factorial runs)^(1/4); for a full factorial core this is (2^k)^(1/4). Three-level factorial designs notably *lack* rotatability, and their alias structure is harder to define than the two-level case — motivations for preferring CCD/Box-Behnken. (The handbook illustrates the information function with figures adapted from Box and Draper's *Empirical Model Building and Response Surfaces*; those are third-party figures, not original to NIST.)

**Why three levels cost so much.** A two-level design with center points can *detect* quadratic curvature but cannot *fit* (estimate individual) pure quadratic effects, because the center-point arrangement confounds all quadratic effects together. To fit curvature you need at least three levels per factor — but a full 3^k factorial explodes: 3 factors = 27 runs, 4 = 81, 6 = 729, far beyond the parameter count of a quadratic model (15 terms for four factors). This run explosion is exactly the motivation for fractional and dedicated response-surface designs.

**The DOE analysis flow.** The handbook's five-step analysis: look at the data graphically (outliers, time order, factor-effect magnitude); state the theoretical model the experiment was designed for; fit and simplify the model (stepwise regression, p-values, normal/half-normal effect plots); validate via residual graphs; then use the result to answer the objective. It stresses that this flow is a guideline, not a hard rule — "art" remains in both design and analysis, and engineering judgment should not be underestimated.

**Confirmation runs.** When analysis yields a "best" setting, you must verify the prediction by running confirmation runs — at least three, to estimate variability at that setting — in an environment as close as possible to the original experiment (same operator, temperature, warm-up state, materials). If confirmation surprises you, first check that nothing changed and that the settings were applied correctly.

**The four lenses of effect significance (|Effects| plot).** The EDA section reads effect importance four ways. **Statistical significance** uses ANOVA or t-based confidence intervals, drawing a cutoff at c·sd(effect), where sd(effect) = 2σ/√n for two-level designs; σ is estimated from prior knowledge (rarely available), replication (preferred when affordable), or by assuming three-factor-and-higher interactions are zero. **Engineering significance** draws the cutoff at a value the engineer declares *before* seeing data — a change large enough to matter in the response's own units, often a rough 5–10% of current production output. **Numerical** and **pattern** significance round out the set; the |effects| plot shows a characteristic L-shape, its vertical arm holding the important factors and its horizontal arm the unimportant ones.

## Mental Models

**The black box with knobs.** Every DOE reduces to a box whose internal mechanism is unknown (deriving the true physico-chemical model is "best left to Nobel-prize winners," the source quips), so you twist the controllable knobs, measure the outputs, and fit an empirical surface good enough for a local approximation. The whole apparatus is about cheap, local, actionable models — not universal truth.

**One-factor-at-a-time is a trap.** The handbook's sharpest conceptual lesson: the traditional OFAT habit (fix all inputs, vary one, lock its best value, move to the next) only works if the true surface is a flat "main effects" model with no interactions. The moment the surface has a "twist" — where X₁'s best setting depends on X₂'s level — OFAT leaves you in the dark about that interaction, which is precisely where the cheap improvement often hides.

**Sequential experimentation as a staircase.** Rather than one big experiment, move through stages: a screening design first (sift the significant few from twenty-or-so candidates, assuming effect sparsity), then experiments to find a direction of improvement from local response-surface contours, then a focused response-surface design near the optimum to characterize its shape and stability. Each stage answers a different kind of question and points to the next.

**Resolution as a confounding dial.** Picture a slider: low resolution buys cheap screening at the cost of tangled aliases; high resolution untangles the aliases but costs runs. The shortest word in the defining relation is the numeric readout of where the slider sits. Foldovers are how you push the slider up after the fact by spending a few more runs.

**Rotatable design as an unbiased searchlight.** Before you know where the optimum is, you want a design whose precision is the same in every direction — a circular searchlight, not an oval one — so it doesn't quietly favor one corner of the factor space. That is what rotatability buys, and why α is tuned to deliver it.

**Inner vs. outer arrays (Taguchi).** Reframe a robustness problem not as one flat factor list but as two crossed grids: the inner array of knobs you control by design (armature turns, wire gauge, alloy content) and the outer array of conditions you only control in the lab (temperature, voltage). Running the outer array at each inner-array corner reveals which design settings stay on-target despite the noise — the essence of robust, "off-line" quality.

## Anti-patterns

The source does not label a formal "anti-patterns" section, but it explicitly warns against several practices:

- **Believing one big experiment will give the answer.** Repeatedly flagged — the handbook calls it a mistake and prescribes an iterative sequence of smaller experiments instead.

- **Using one-factor-at-a-time experimentation.** Named directly as the approach that "does not take interactions into account" and fails whenever the true model has a twist; the source notes it was once mistakenly thought to be the only scientific approach.

- **Randomizing center-point runs.** Explicitly called out: center points are guardians against process instability and must be sampled on a regular basis, so there is "no reason to randomize them."

- **Combining measurements into a single response when the components matter.** The variable-selection guidance warns against using only a composite response (e.g., a selectivity ratio of two etch rates) — measure both underlying rates, not just the ratio.

- **Choosing factor ranges by reflex.** Be "bold, but not foolish": extreme settings can produce infeasible runs or push the experiment off a smooth region of the surface into a jagged area or near an asymptote.

- **Keeping only summary averages.** The practical checklist insists on preserving all raw data and recording everything that happens — discarding raw data in favor of averages is named as a mistake.

- **Jumping to tolerance design.** Taguchi's tolerance design (tightening critical tolerances) is flagged as expensive and not a guarantee of better performance; the source recommends it only as a last resort after extensive parameter-design study.

## Key Takeaways

- DOE deliberately varies controllable factors to fit an economical, local empirical model (linear or quadratic) of a "black box" process; the payoff is maximum information per unit of experimental effort.
- Match the design to the objective: comparative (randomized block, Latin squares), screening (fractional factorial, Plackett-Burman), response surface (central composite, Box-Behnken), or regression — with factor count driving the choice via the Design Selection Guideline.
- Check four assumptions before running: capable measurement system, stable process, a smooth-enough underlying surface, and well-behaved residuals.
- Fractional factorials trade runs for confounding; the defining relation's shortest word sets the resolution (III = main effects aliased with two-factor interactions, IV = clear of those, V = clear through two-factor interactions), and minimum aberration picks the least-aliased design at a given resolution.
- Two-level designs with center points detect but cannot fit curvature; fitting quadratic effects needs three levels, which is why dedicated rotatable RSM designs (CCD, Box-Behnken) exist rather than brute-force 3^k factorials.
- Rotatability — prediction variance depending only on distance from center — keeps the search unbiased when the optimum's location is unknown; for a CCD it is set by α = (factorial-run count)^(1/4).
- Foldover designs raise resolution after the fact: a mirror-image foldover (reverse all signs) turns resolution III into IV, freeing main effects from two-factor-interaction aliases.
- Analysis is graphics-first then model-fit-and-validate; the flow is a guideline, and engineering judgment plus confirmation runs (at least three, in a faithfully reproduced environment) are non-negotiable.
- Effect importance is read through multiple lenses — statistical (ANOVA/t-intervals), engineering (a pre-declared cutoff in response units), numerical, and pattern (the L-shaped |effects| plot) — not statistics alone.
- The strongest cross-cutting lessons: experiment iteratively, never one-factor-at-a-time, and respect interactions as the most common source of cheap improvement.

## Connects To

- **Process monitoring and control (this handbook's adjacent chapter):** The stability assumption ties DOE to SPC — control runs at standard setpoints are the SPC check that the process did not drift mid-experiment, and the measurement-capability assumption invokes the gauge studies of the measurement chapter.
- **Regression and ANOVA:** DOE analysis leans entirely on multiple regression (coefficient estimation, R², lack-of-fit tests) and on ANOVA for partitioning variance and testing factor significance; the residual-assumption checks are the same ones underlying classical regression.
- **Six Sigma / DMAIC:** Screening, response-surface optimization, and robustness (parameter design) are the statistical engine of the Improve phase — identifying vital-few factors and tuning them to hit a target while minimizing variation.
- **Robust design and reliability engineering:** Taguchi parameter design (inner/outer arrays, making a system insensitive to noise factors) maps directly onto robustness and margin work in systems engineering — designing a starter motor or any component to perform across uncontrolled field conditions.
- **MBSE trade studies and design-space exploration:** The objective-driven choice of design, the iterative screen-then-optimize staircase, and response-surface/contour-based optimization generalize to model-based trade-space analysis and surrogate-model construction for engineered systems.
- **Ingestion note:** This pack's source is the web-native NIST/SEMATECH e-Handbook, ingested per-chapter as HTML rather than from a paginated PDF; section-number cross-references (e.g., "see Section 5.3.3.6") and figure labels reflect that hyperlinked structure. Several response-surface figures are adapted from third-party texts (Box and Draper) and are attributed as such in the source rather than being original NIST artwork.
