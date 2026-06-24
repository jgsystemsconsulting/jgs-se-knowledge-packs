# Chapter — Process Monitoring and Control

## Core Idea

This chapter is the NIST/SEMATECH handbook's treatment of how to watch a process while it runs and decide when to intervene. The unifying question is a comparison across time: how does the process behave today versus how it behaved before? You take a snapshot of typical performance (or build a model of expected performance), derive limits for the expected measurements, then collect fresh data and check whether it stays inside those limits. Most measurements should land within the limits; points that fall outside are flagged for investigation and may later be discarded, after which the limits are recomputed. The source names this two-stage workflow explicitly: establishing and cleaning the limits from historical data is **Phase I**, and real-time monitoring against the locked Phase I limits is **Phase II**.

The chapter splits the territory along two complementary disciplines that the handbook is careful to distinguish. **Statistical Process Control (SPC)** monitors the process as it produces, aiming to catch shifts early and act on them. **Statistical Quality Control (SQC)** inspects finished product, lot by lot, to decide acceptability in a cost-efficient way without inspecting every unit. A third strand, **process capability**, answers a different question entirely: granted the process is stable, is its natural spread narrow enough to live inside the customer's specification? Throughout, the source insists on a separation that beginners routinely blur — control limits describe what the process *is doing* (its voice), while specification limits describe what the product *must do* to function. The two are computed from different inputs and answer different questions.

## Frameworks Introduced (exact source names, when/how)

- **Statistical Process Control (SPC)** — the handbook's umbrella for real-time, comparison-against-history monitoring. Its supporting toolkit, attributed by the source to Montgomery (2000), lists histograms, check sheets, Pareto charts, cause-and-effect (fishbone) diagrams, defect concentration diagrams, scatter diagrams, and control charts. The chapter then narrows to four control-chart families: classical Shewhart charts, Cumulative Sum (CUSUM), Exponentially Weighted Moving Average (EWMA), and multivariate charts.

- **Statistical Quality Control (SQC) / Lot Acceptance Sampling (LASP)** — used for inspecting product after processing. The source credits its popularization to Dodge and Romig, with the canonical origin story being the U.S. military testing bullets in World War II: test every bullet and none remain to ship; test none and you risk battlefield malfunctions. Acceptance sampling is framed as "the middle of the road" between zero inspection and 100% inspection.

- **Shewhart control charts** — proposed by Dr. Walter A. Shewhart of Bell Telephone Laboratories. The handbook dates his first memorandum sketching a modern control chart to May 16, 1924, and his foundational book to 1931. The general Shewhart model places a center line at the mean of a sample statistic w, with control limits set k standard-deviation units away. With k = 3 — the accepted industry standard per the source — these are called **3-sigma control charts**.

- **X-bar and s / X-bar and R charts** — the variables-chart workhorses. The s chart (or R chart) is run first to confirm the spread is stable before trusting the mean chart. The R-based approach uses the d2, d3, A2, D3, D4 factors (tabulated by sample size n) and is recommended for small subgroups (n up to about 10); for larger subgroups, subgroup standard deviations are preferred.

- **Individuals control charts** — for sample size n = 1, using the **moving range** MR_i = |x_i − x_{i−1}| of two successive observations to estimate variability (the constant 1.128 is d2 for n = 2).

- **CUSUM (Cumulative Sum) charts** — the source presents these as a more efficient alternative to Shewhart for detecting small mean shifts (2 sigma or less). Includes the **V-Mask**, a visual overlay proposed by Barnard in 1959, though the source notes the tabular form is more often preferred in practice.

- **EWMA (Exponentially Weighted Moving Average) charts** — the governing equation is attributed to Roberts (1959). The statistic weights all prior data with exponentially decaying weight controlled by λ; the source cites Hunter (1986) for the usual λ range of 0.2–0.3 and Lucas and Saccucci (1990) for tables to select λ and the limit factor k.

- **Attributes control charts** — for go/no-go data: **c charts** (count of defects), **p charts** (proportion/fraction defective), and **u charts** (defects per unit). Count charts rest on the Poisson distribution as an approximation to the binomial; the source cites Woodall (1997) for a review including semiconductor examples.

- **Multivariate control charts / Hotelling's T²** — introduced by Harold Hotelling in 1947. T² is a scalar combining the mean and dispersion of several correlated variables, described as the multivariate counterpart of the Student's-t statistic.

- **MIL-STD-105D / 105E** — U.S. Department of Defense military sampling standard for attributes. The source traces its lineage from WWII Army Ordnance tables through the 1950 Mil. Std. 105A, the 1963 105D, adoption as ANSI Z1.4 (1971) and ISO 2859 (1974), to the 1989 105E revision.

- **Out-of-Control Action Plans (OCAPs)** and **Advanced Process Control Loops** — the two intervention mechanisms named under "What is Process Control?": OCAPs are flowcharts guiding an engineer through corrective procedure; Advanced Process Control Loops are automated, programmed corrections sized to the out-of-control measurement.

- **WECO rules** — Western Electric Company rules, a set of supplementary signaling patterns for detecting non-random behavior beyond the simple 3-sigma rule.

## Key Concepts

**Phase I vs Phase II.** Phase I uses historical data to compute and clean initial limits — investigate out-of-limit points, possibly discard them, recompute. Phase II is live monitoring against the limits frozen at the end of Phase I. The source ties recommended chart-setup volumes to this: Shewhart's own rule of thumb was that one is seldom justified in declaring statistical control until obtaining, under essentially the same conditions, at least twenty-five samples of size four that are in control.

**Control limits vs specification limits.** Control limits determine whether the process is in a state of statistical control (producing consistent output). Specification limits determine whether the product will function as intended. The source warns that these are conceptually distinct — a nonconforming unit (out of spec) may still function fine, and an in-spec unit can still be defective.

**Process capability indices.** Capability compares the specification width to the process width, where process width is taken as 6 standard-deviation units. The chapter defines Cp (spec spread over 6σ), Cpk (the worse of the two one-sided indices, capturing off-center processes), and Cpm (which penalizes departure from a target T). One-sided variants are Cpu and Cpl, with Cpk = min(Cpl, Cpu). The source's worked example (USL = 20, LSL = 8, mean = 16, s = 2) gives Cp = 1.0 but Cpk = 0.6667 because the process is off-center — illustrating that a capable-looking Cp can mask an uncentered process. The indices assume normality and a "large enough" sample, given as roughly 50 independent values (and n of at least 100 for full capability studies). The source's reject table links Cp values to defect rates: Cp = 1.00 implies about 0.27% rejects, Cp = 1.33 about 64 ppm, Cp = 1.66 about 0.6 ppm, Cp = 2.00 about 2 ppb (assuming a centered distribution).

**Average Run Length (ARL).** ARL is the average number of points plotted before a signal occurs. For a Shewhart X-bar chart with no real change, the false-alarm probability per point is about 0.0027, giving an ARL near 371 points between false alarms. The source uses ARL as the lens for comparing chart families: CUSUM beats Shewhart at catching small shifts.

**WECO rules and the false-alarm tradeoff.** The WECO supplementary rules (any point beyond ±3σ; 2 of last 3 beyond ±2σ; 4 of last 5 beyond ±1σ; 8 consecutive on one side of the center line; plus trend rules such as 6 in a row trending or 14 alternating) each correspond to a rare event of comparable probability. The source is explicit about the cost: adding the WECO rules raises Shewhart sensitivity to drifts but drops the false-alarm interval from about 1 in 371 points to about 1 in 91.75 points (attributed to Champ and Woodall, 1987). Users must decide whether the price is worth paying; some adopt the rules but treat them "less seriously" in troubleshooting effort.

**Acceptance sampling vocabulary.** A single plan is denoted (n, c): inspect n items, reject if more than c are defective. The plan's behavior is summarized by the **Operating Characteristic (OC) curve** — the probability of accepting versus the lot fraction defective — described as the primary tool for displaying a plan's properties. Two design points anchor a plan: the **AQL** (Acceptable Quality Level, the producer's baseline) paired with **Producer's Risk** (Type I error, α, rejecting good lots), and the **LTPD** (Lot Tolerance Percent Defective) paired with **Consumer's Risk** (Type II error, β, accepting bad lots). Related rectified-inspection metrics: **AOQ** (Average Outgoing Quality) and its worst-case maximum **AOQL**; **ATI** (Average Total Inspection); and **ASN** (Average Sample Number). The underlying probability model is the hypergeometric distribution, commonly approximated by the binomial.

**Escalating sampling schemes.** The chapter lays out a ladder of increasing sophistication: single → double → multiple → sequential, plus skip-lot. Double sampling gives a questionable lot "another chance" via a second sample when the first is inconclusive. Multiple sampling extends this to up to k samples (the source notes MIL-STD-105D suggests k = 7). Sequential sampling inspects item by item, plotting cumulative defectives between two parallel decision lines, typically truncated at three times the corresponding single-sample size. Skip-lot inspects only a fraction of submitted lots. The choice is a tradeoff: smaller average sample sizes versus added complexity and day-to-day uncertainty about how much inspection will actually occur.

**The estimator bias subtlety.** The source flags that while sample variance s² is an unbiased estimator of σ², the sample standard deviation s is *not* unbiased for σ — under normality it estimates c4·σ, where c4 is a sample-size-dependent constant. This is why control-limit formulas divide by c4 to recover an unbiased σ estimate.

## Mental Models

**The process has a "voice" separate from the customer's "demands."** Control limits are the process speaking about its own consistency; specification limits are the customer stating what is needed. Conflating them is the most common conceptual error the chapter guards against. A chart can be perfectly in control yet produce out-of-spec product (the "in control but unacceptable" case the introduction names), or be wandering out of control while every unit still happens to be in spec.

**Compare today to yesterday.** The entire SPC apparatus reduces to a disciplined before-versus-now comparison. The snapshot becomes the limits; the limits become the yardstick.

**The bullet dilemma.** The WWII bullet-testing story is the source's mental anchor for why acceptance sampling exists: destructive testing forces a middle path between testing everything (nothing left to ship) and testing nothing (field failures). Sampling is the principled compromise.

**Memory depth as a tuning knob.** EWMA's λ is a dial for how far back the chart "remembers." Set λ = 1 and only the latest point matters — the chart degrades to a Shewhart chart. Lower λ pulls older data in and makes the chart sensitive to slow drift. This frames Shewhart, CUSUM, and EWMA as points on a memory spectrum rather than unrelated tools: Shewhart is memoryless and best for large abrupt shifts; CUSUM and EWMA accumulate memory and excel at small, gradual shifts.

**Sensitivity is bought with false alarms.** Schilling's image (quoted by the source) contrasts a lone sniper (an individual sampling plan, short-run) with a fusillade (a sampling scheme over the long run). More broadly, every gain in detecting subtle changes — WECO rules, tighter charts — is paid for in more false alarms. The ARL numbers make this tradeoff quantitative rather than rhetorical.

**The OC curve is the plan's fingerprint.** Two points (AQL/producer's risk and LTPD/consumer's risk) uniquely pin down an OC curve, and from those the (n, c) pair is solved. Designing a sampling plan is choosing where the curve passes.

## Anti-patterns

The source does not present a formal "anti-patterns" section, but it explicitly names several cautions worth treating as such:

- **Recalculating control limits without a compelling reason.** Because a chart compares current to past performance, the source warns that changing limits frequently negates their usefulness. Limits should only change for a valid, documented reason — accumulating at least 30 more points with no known process change (for a better variability estimate), a major process change, or a known preventable event (power loss, bad consumable).

- **Trusting chart properties computed from too little data.** The source notes that standard chart properties (such as false-alarm probabilities) are derived assuming the parameters μ and σ are known. When limits come from a small data set, actual behavior may differ substantially from what is assumed (citing Quesenberry, 1993).

- **Adding WECO rules without accounting for the false-alarm cost.** Treated above — the source explicitly frames this as a tradeoff the user "has to decide whether this price is worth paying."

- **Reading Cp alone and declaring a process capable.** The worked example deliberately shows Cp = 1.0 alongside Cpk = 0.6667, demonstrating that ignoring centering (the k factor) overstates capability.

## Key Takeaways

- Process monitoring is a structured before-versus-now comparison, formalized as Phase I (set and clean limits from history) and Phase II (monitor live against frozen limits).
- SPC monitors the running process; SQC inspects finished lots; capability checks whether a stable process fits inside spec. Three different questions, three different toolsets.
- Control limits and specification limits are not interchangeable — one describes process consistency, the other product function.
- Shewhart 3-sigma charts (k = 3) are the industry baseline; the X-bar paired with an s or R chart is the variables workhorse, with R-based factors preferred for small subgroups.
- For small, gradual mean shifts, CUSUM and EWMA outperform Shewhart; EWMA's λ tunes how much history the chart remembers, with Shewhart as the λ = 1 limiting case.
- Attributes charts (c, p, u) handle counted/classified data via the Poisson approximation; the source distinguishes a "defect" (nonconformity) from a "defective" (nonconforming unit).
- Hotelling's T² (1947) extends control charting to correlated multivariate data, but locating an assignable cause still requires dropping back to univariate charts.
- Acceptance sampling decides lot disposition, not lot quality; the OC curve is the central design artifact, anchored by AQL/producer's risk and LTPD/consumer's risk.
- Sampling schemes escalate single → double → multiple → sequential (plus skip-lot), trading smaller average sample sizes against operational complexity.
- Sensitivity is never free: ARL quantifies the false-alarm-versus-detection tradeoff, and adding WECO rules roughly quadruples the false-alarm rate.

## Connects To

- **SE verification & validation, and quality management (ISO 9001 / AS9100 lineage):** The control-limit-versus-specification-limit distinction maps directly onto the systems-engineering separation between verifying a system does what it consistently does and validating it meets stakeholder need.
- **Six Sigma and DMAIC:** Capability indices (Cp, Cpk) and the reject-rate table are the statistical backbone of Six Sigma's defect-rate targets; the chapter supplies the underlying definitions.
- **Reliability and acceptance test design:** Lot acceptance sampling, OC curves, and producer/consumer risk underpin acceptance test planning and incoming-inspection regimes in supply-chain and manufacturing readiness.
- **Other chapters of this handbook:** The chapter's tutorials extend into matrix algebra, multivariate analysis, principal components, and time series (moving averages, exponential smoothing, Box-Jenkins ARIMA) — connecting process monitoring to forecasting and exploratory data analysis treated elsewhere in the NIST/SEMATECH e-Handbook.
- **MBSE and digital-thread monitoring:** The Phase I/Phase II monitoring discipline and OCAP/automated-loop intervention model generalize to runtime monitoring of engineered systems, anomaly detection, and closed-loop control beyond manufacturing.

---

*Source caveat: This source is HTML/web-native and ingested per-chapter, which differs from PDF-based packs. Several blocks reference third-party figures, plots, V-Mask diagrams, and tables that do not survive as text in the extract; equations and tabulated factors (d2, d3, A2, D3, D4, c4) were paraphrased and summarized rather than reproduced. All claims above are grounded in the assigned text slice; numeric examples are restated, not copied.*
