# Chapter — Data Collection and Bayesian Parameter Estimation

## Core Idea

A PRA model is only as credible as the numbers feeding it. This chapter covers how those numbers are produced: collecting field and test information, classifying it consistently, and then converting it into the probability-model parameters the risk model needs. The guiding principle is that gathering data and analyzing it are not separable activities — the analyst has to understand how the results will be used (and which decisions they will inform) before designing the collection and estimation scheme. In PRA terms, data analysis is the work of estimating the parameters of the model's epistemic layer: the failure rates, initiator frequencies, demand probabilities, and human error rates that turn structural logic into quantified risk.

The source frames the database-building effort in two phases — information collection and classification, then parameter estimation — and four supporting steps: model-data correlation, data collection, parameter estimation, and documentation. The estimation engine throughout is Bayesian. Classical (frequentist) estimation appears only in a narrow, restricted role; the Guide states plainly that it describes only the Bayesian approach. This is what deepens the qualitative risk material elsewhere in the nasa-risk pack: where that work establishes scenario logic and risk framing, this chapter supplies the quantitative machinery that puts defensible, uncertainty-bearing numbers on the basic events.

## Frameworks Introduced (exact source names, when/how)

- **Two-phase / four-step PRA database process** — The Guide structures database development as two phases (Information Collection and Classification; Parameter Estimation) and four steps (Model-Data Correlation, Data Collection, Parameter Estimation, Documentation). Model-data correlation identifies what data each model needs given component boundaries and failure modes; documentation records how the uncertainty distributions were derived, which sources were used, and what was assumed.

- **Table 5-1, Typical Probability Models in PRAs and Their Parameters** — Introduced in Section 5.1 as the catalog mapping each basic-event type to its probability model and the data needed to estimate it. Examples: an initiating event uses a Poisson model (needs a count of events *k* in time *t*); a component that fails on demand uses a constant failure-on-demand probability *q* (needs failures *k* in *N* demands); standby and operating components use standby and operating failure-rate models; unavailability from test or maintenance has its own forms. Parameters carrying epistemic uncertainty are flagged in bold.

- **Data-source relevance taxonomy** — Section 5.2 classifies information by nature and degree of relevance: identical equipment under identical conditions (direct operational experience), identical equipment under other conditions (test data), similar equipment under possibly-different conditions (handbooks, another program's tests), and general engineering or expert knowledge of the design.

- **Generic data sources** — Section 5.2.1 names NASA repositories (the PRACA system — Problem Reporting and Corrective Action — plus SOARS, the PR/PFR system, Apollo Mission Reports, the Mars Exploration Rover Problem Tracking Database, and PRA archives for Shuttle and ISS) and external compendia (RIAC's NPRD-2011 and EPRD-1997, IEEE Std 500-1984, NUCLARR/NARIS, the nuclear EPIX/RADS system, MIL-HDBK-217F, GIDEP, and ICDE). The ISS PRA is given as a worked example of a mixed source set (MADS, contractor and Russian R&M reports, NPRD, EPRD, FMD, Bellcore TR-332, PRACA).

- **MIL-HDBK-217 Part Stress Analysis Prediction method** — Cited as a way to specialize a base failure rate using multiplicative pi-factors for quality, environment, and part-specific stresses (the semiconductor form in Equation 5-1).

- **Failure taxonomy and component state classification** — Section 5.2.2 introduces a hierarchical classification (System → Component → Failure Mode → Affected Item → Failure Mechanism → Failure Cause) and the component functional-state model of Figure 5-1 (available vs. unavailable, with failed, functionally unavailable, potentially failed, and potentially functionally unavailable sub-states). Henley and Kumamoto's keyword-modifier database scheme is cited; ISO 14224:2006, ISO 6527:1982, and ISO 7385:1983 are named as external taxonomy guidance. Figures 5-2 and 5-3 detail the cause-classification flow and its subcategories (item affected, mechanism, cause).

- **Bayesian parameter estimation** — Section 5.3 defines the two-step method: fit a prior distribution to the parameter from available information, then update it with new data via Bayes' Theorem ("Bayesian Updating"). The schematic relation (Equation 5-2) is posterior ∝ prior × likelihood, normalized.

- **Prior distribution forms** — Section 5.4 lists parametric priors (lognormal and gamma for event rates; beta or truncated lognormal for per-demand probabilities) and numerical priors (histograms, percentile/CDF specifications). The information content can come from prior system-specific estimates, generic data, reliability sources, expert judgment, or a non-informative prior (a uniform prior over the interval being one common choice).

- **Likelihood functions** — Section 5.5 pairs the data-generating "Model of the World" to its likelihood: Poisson for counts from a Poisson process (Eq. 5-6), Binomial for failures-on-demand from a Bernoulli process (Eq. 5-8), and lognormal for expert estimates or handbook values.

- **Posterior development and conjugate priors** — Section 5.6 gives Bayes' Theorem in continuous form (Eq. 5-10). Table 5-2 lists prior/likelihood/posterior combinations; Table 5-3 gives the two workhorse conjugate pairs (Beta–Binomial → Beta; Gamma–Poisson → Gamma) with closed-form posterior mean and variance.

- **Sequential updating** — Section 5.7 establishes that Bayes' Theorem can be applied in stages as evidence arrives, and that staged updating yields the same posterior as a single update on the pooled evidence (demonstrated in Example 6).

- **Multi-source generic prior development** — Section 5.8 splits generic information into Type 1 (failure/success data from similar-but-not-identical components, a non-homogeneous population) and Type 2 (failure-rate estimates or distributions from compendia and expert elicitation). When sources are heterogeneous, the data cannot simply be pooled, and the parameter is described by a population variability distribution.

- **NASA/SP-2009-569** — the companion Bayesian Inference Guide [5-4] (its title names inference for NASA risk and reliability work), referenced as the detailed source for prior-selection tables, population-variability models, uncertain-data handling, and the broader catalog of inference topics (Sections 5.4, 5.8, 5.9).

## Key Concepts

- **Model-data correlation.** Before collecting anything, the analyst maps each PRA basic event to the specific data its probability model requires — component boundaries, which failure modes count, and which parameters (failure rate, MTTR, etc.) must be estimated. Get this wrong and the cleanest data in the world is attached to the wrong model.

- **Event counts plus exposure.** Most parameters need two things: a count of relevant events (failures, demands) and the matching exposure (operating time, number of tests). A Poisson rate needs *k* failures in time *T*; a demand probability needs *k* failures in *N* demands. Counting one without the other gives an unanchored number.

- **System-specific vs. generic vs. surrogate.** The ideal is operational data from the very system being modeled. When that is thin or absent, the analyst falls back to generic data, surrogate data, or expert judgment — alone or blended with limited system-specific data. Generic data is non-specific information about a *class* of items, and most of it covers hardware; human and software probabilities are too context-dependent for generic sources, so they usually have to be built or heavily adapted.

- **Generic data must be evaluated, not just borrowed.** Regardless of source, generic data has to be assessed for applicability and frequently modified before it can serve as surrogate input. The RIAC handbooks, for instance, give point estimates with no uncertainty treatment — usable, but only after the analyst supplies the missing uncertainty.

- **Raw data and consistent reduction.** System-specific data usually arrives "raw" (maintenance logs, test logs, operation records) in a form unfit for direct statistical use. Even pre-reduced data demands care: the failure-mode classification and the count of tests or actual demands must line up with the PRA's modeling assumptions.

- **Functional-state classification.** A component is available or unavailable; unavailability splits into *failed* (the component itself is damaged) and *functionally unavailable* (it is intact but lacks needed support such as motive power). The taxonomy also captures degraded-but-still-working conditions as *potentially failed* and *potentially functionally unavailable*. These distinctions feed directly into how an event is counted.

- **Root cause as the deepest correctable layer.** Cause classification peels back contributing factors — affected item, failure mechanism, then root cause — where root cause is the most basic reason that, if fixed, would stop recurrence. A single-cause description is usually too simplistic; the realistic picture is a chain of causal factors and symptoms.

- **Prior, likelihood, posterior.** The prior encodes belief before the new data; the likelihood carries the new data's evidential weight under an assumed generating process; the posterior is the updated state of knowledge. The likelihood form follows the physics of how data is generated — Poisson for time-based counts, Binomial for demand-based counts, lognormal for expert/handbook values.

- **Conjugacy.** When the prior is conjugate to the likelihood, the posterior stays in the same distribution family, so it has a closed form and avoids numerical integration of the normalizing denominator. Gamma–Poisson and Beta–Binomial are the two standard conjugate pairs; non-conjugate combinations (e.g., lognormal prior with Poisson likelihood) force a numerical posterior.

- **Credible (probability) interval.** Because Bayesian inference yields a full distribution, uncertainty is reported as a credible interval between two percentiles — a 90% interval runs from the 5th to the 95th percentile. The source also calls this a probability interval.

- **Population variability distribution.** When multiple heterogeneous generic sources disagree, that spread is not noise to be averaged away — it is real parameter variability across a non-homogeneous population, represented as its own distribution rather than by pooling.

## Mental Models

- **The two-step Bayesian funnel.** Start broad (a generic prior built from class-level data) and narrow (update with system-specific test or operating data). The posterior becomes the system-specific distribution. If the next batch of data arrives later, today's posterior is tomorrow's prior — knowledge compounds rather than resetting.

- **Order-independence of evidence.** Updating on test 1 then test 2 gives the same posterior as updating once on both tests combined, provided the total information is the "sum" of the pieces. Example 6 shows it numerically: staged Gamma updates and a single pooled update both land on 3.6E-4 failures/hour. Treat sequential updating as a bookkeeping convenience, not a different method.

- **Shift toward the data.** The posterior sits between the prior and what the new data says, pulled toward the operational evidence. Strong, plentiful data moves the posterior a lot; sparse data leaves it near the prior. This is the visual takeaway of Examples 4 and 5 (prior and posterior plotted together).

- **Match the likelihood to the world.** Don't pick a likelihood for convenience — pick the one that matches how the data was actually generated. Failures accumulating over operating time → Poisson. Failures among discrete demands → Binomial. A handbook point estimate or expert's best guess → lognormal.

- **Rare-event leverage.** Bayes' Theorem earns its keep precisely where data is sparse and events are rare — exactly the regime spaceflight risk lives in. It coherently fuses heterogeneous information while keeping the uncertainty explicit, which is why it dominates classical estimation in this domain.

- **Taxonomy as shared meaning.** A failure taxonomy is a parent-child knowledge structure that lets different analysts attach the same meaning to the same event. Without it, two people counting the same logs produce incompatible datasets.

## Anti-patterns

- **Treating collection and analysis as separate, sequenced activities.** The source's opening principle is that they are not done in isolation — the intended use of the results must shape how data is collected and how methods are designed. Collecting first and only later asking what it was for inverts the dependency.

- **Pooling heterogeneous generic sources.** When multiple generic sources describe a non-homogeneous population, the data cannot be pooled into a single estimate; doing so erases the real population variability the parameter actually has.

## Key Takeaways

- PRA database development is two phases (collect/classify, then estimate) over four steps (model-data correlation, collection, estimation, documentation), and the estimation step is Bayesian by default — classical methods get only limited, restricted use.

- Table 5-1 is the lookup that ties each basic-event type to its probability model and the exact data (counts plus exposure) needed to estimate the parameters carrying epistemic uncertainty.

- System-specific operational data is the ideal; generic, surrogate, and expert sources fill the gaps but must always be assessed for applicability and usually modified before use.

- A disciplined failure taxonomy and component-state classification (available/unavailable, failed vs. functionally unavailable, plus the potentially-failed states) is essential so that events are counted consistently and causes are traced to a correctable root.

- Bayesian estimation = fit a prior, then update it with data through Bayes' Theorem; the posterior is a full distribution reported via credible intervals, not a single point.

- Conjugate priors (Gamma–Poisson, Beta–Binomial) give closed-form posteriors; mismatched pairs require numerical solutions.

- Sequential updating is order-independent — staged updates equal a single pooled update — and a posterior naturally becomes the prior for the next round.

- Multiple disagreeing generic sources signal a non-homogeneous population whose spread should be captured as a population variability distribution, not averaged away.

- NASA-SP-2009-569 is the deep-dive companion for prior selection, population variability, uncertain data, and the full inference-method catalog.

## Connects To

- **nasa-risk (deepened here):** This chapter supplies the quantitative parameter-estimation methods that put uncertainty-bearing numbers behind the qualitative scenario and risk logic developed in the nasa-risk material — the explicit deepening this pack is meant to provide.

- **Upstream PRA model-building:** Model-data correlation depends on the event trees, fault trees, and basic-event definitions established earlier in the PRA process; the probability models in Table 5-1 are what those basic events resolve to.

- **Common Cause Failure analysis:** CCF probabilities appear among the target quantities (alpha-style parameters and counts of multi-component events), linking to dedicated CCF treatment such as NUREG/CR-4780 [5-1] and the ICDE data exchange.

- **Uncertainty propagation and quantification:** The credible intervals and posterior distributions produced here are the inputs that downstream uncertainty-propagation steps push through the full risk model.

- **Expert elicitation:** Where data is absent, priors and Type 2 generic inputs come from structured expert judgment, connecting to the elicitation methods discussed in the Guide's Chapter 6 and in NASA-SP-2009-569.

- **External reliability data ecosystems:** Ties PRA practice to RIAC/NPRD/EPRD, MIL-HDBK-217, GIDEP, OREDA, and the ISO reliability-data standards (14224, 6527, 7385), positioning NASA work within the broader reliability-engineering community.
