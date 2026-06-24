# Chapter 3: Cost Methodology Tasks (Tasks 4-7: GR&A, Methodology Selection, Models/Tools, Data Normalization)

## Core Idea
Part 2 of NASA's cost-estimating process is where the estimator decides *how* the estimate will be built. Four sequential tasks set the rules of the road and then equip the estimator to follow them: Task 4 fixes the **Ground Rules and Assumptions (GR&A)** that bound the estimate's scope; Task 5 selects the **estimating methodology** (analogy, parametric, or engineering build-up) that fits the data on hand; Task 6 selects or constructs the **model/tool** that mechanizes the chosen methodology; and Task 7 **gathers and normalizes the data** that feeds it. The through-line is that *credibility and defensibility come from documentation* — every bound, choice, equation, and adjustment must be written down so the estimate can be defended, repeated, and compared.

## Frameworks Introduced
- **Global vs. element-specific GR&A** (Task 4) — every estimate carries two layers of ground rules: *global* rules that apply across the whole estimate (base-year dollars, schedule, inclusions/exclusions, total quantities) and *element-specific* rules attached to individual WBS elements as each is estimated (unit quantities, element schedules).
  - When to use: at the outset, to bound scope; element-specific rules accrete as you work down the WBS.
- **The three (plus one) cost estimating methodologies** (Task 5) — *analogy*, *parametric*, and *engineering build-up* (a.k.a. "grassroots" / "bottom-up"), with *extrapolation from actuals via Earned Value Management (EVM)* as a fourth source once a program is underway. The prevalent method shifts across the life cycle because the quantity of available data changes.
  - When to use: analogy and parametric early (sparse data); build-up later (detailed definition); EVM once actuals exist.
- **The Parametric Cost Modeling Process** (Task 5, the handbook's Figure 6) — a seven-step loop: define the estimating hypothesis, collect relationship data, evaluate and normalize the data, analyze it for candidate relationships, perform regression (statistical) analysis, test the relationships, and select the estimating relationship.
  - When to use: whenever you intend to build or apply a Cost Estimating Relationship (CER).
- **Cost Estimating Relationship (CER)** (Task 5) — a documented equation linking a dependent variable Y (cost) to one or more independent variables X (the "cost drivers"), produced by regression. Drivers are chosen for both strong statistical correlation *and* a sound logical reason for the relationship.
  - When to use: as the core output of a parametric estimate; must be re-checked over the estimate's life to confirm inputs stay within the data range.
- **Engineering Build-Up method** (Task 5, the handbook's Figure 8) — decompose the CBS/WBS into work packages, estimate each at the lowest discernible level (labor separate from material), aggregate, test for omissions and duplications, sanity-check the total, then apply overhead factors (ODCs, G&A, materials burden, fee).
  - When to use: production estimating, negotiations, mature projects, resource allocation — where detail exists and defensibility per element matters.
- **The Delphi method** (Task 5) — a structured expert-opinion technique used *only in the absence of empirical data*: a group of experts iterates toward a converged value using controlled feedback, with individuals typically kept anonymous to outsiders and sometimes to each other.
  - When to use: as a fallback within build-up when hard data are missing; the estimator's interview skill is what captures and documents the judgment.
- **Cost Models and Tools Utilization Guide** (Task 6, the handbook's Table 4) — a catalogue mapping NASA-sponsored and commercially licensed tools to the methodologies they support and to ONCE Model Portal availability (e.g., PCEC, NAFCOM, NICM, QuickCost on the NASA side; ACEIT, SEER-H/SEER-SEM, PRICE TruePlanning on the licensed side; ONCE and REDSTAR as databases).
  - When to use: when choosing a tool; no single model serves all purposes.
- **Three Cost Model Best Practices** (Task 6) — when an estimator builds a model: (1) check and recheck data entry and formulas before and after running, documenting each input and formula for the Basis of Estimate (BOE); (2) run a cross-check estimate using an alternative methodology against the point estimate as a sanity check; (3) keep the estimate current to ease defense, shorten turnaround, and support "what-if" drills.
  - When to use: any time you construct your own model rather than adopting an existing one.
- **The dollar-type vocabulary** (Task 7, the handbook's Table 6) — Base Year (BY), Constant Year (CY), Then Year / Real Year (RY) dollars, plus inflation index, outlay profile, weighted/composite inflation. The handbook flags that NASA's "Real Year" usage is the opposite of DoD's, where "Real" means Constant.
  - When to use: whenever presenting or converting cost figures across years.

## Key Concepts
- **GR&A communicate scope, context, and environment.** They tell everyone which costs are in and which are out, let estimators bound the work and focus on the dominant elements, and provide temporary resolution for technical/programmatic questions that cannot yet be answered with certainty.
- **GR&A are a living document.** They are established with the NASA Program/project Manager (P/pM) and technical team, approved by that point of contact, agreed with stakeholders, and documented continuously *as they evolve* through the entire estimate.
- **GR&A topics are broad.** The handbook enumerates a long list including scope and WBS, make-vs-buy, GFE/GFI, development philosophy, contractors and their roles, test hardware, budget profile, schedule and milestones, labor resources/rates and overhead, risk and mitigation, profit/fee, design heritage/technology, management/acquisition approach and program-level "wraps," production quantities, the dollar-and-inflation description, life-cycle-cost considerations, implementation approach, facilities, and operations concept.
- **Methodology follows data availability.** With little definition, analogy or parametric methods dominate; as definition matures and detail emerges, engineering build-up becomes feasible; EVM extrapolation enters once a program produces actuals.
- **Analogy** adjusts the known cost of a similar fielded system up or down for differences. It leans heavily on expert opinion, which makes it less tenable as the required adjustments grow larger; it still requires normalization to be accurate.
- **Parametric** rests on the assumption that the forces driving past cost will drive future cost. Its strengths are speed, replicability, and statistically grounded confidence; its weakness is that it loses credibility outside its relevant data range and is opaque to non-statisticians.
- **Engineering build-up** is intuitive, defensible, and severable (one element's error does not poison the whole), and it exposes the major cost contributors. But it is costly and slow to produce, prone to omission/double-counting, not responsive to "what-if" changes, and cannot by itself yield a statistical confidence level.
- **A model mechanizes a methodology, but does not replace judgment.** Models vary widely in automation and data needs; commercially available parametric models use normalized (sometimes proprietary) industry datasets and **should be calibrated to comparable historical data** so the estimate reflects the actual project environment (Earth-orbiting, planetary, etc.).
- **Three obligations when selecting/building a model:** review the choices and select (or build if nothing suitable exists); ensure the model is validated before use; and be prepared to defend the choice.
- **Data collection is the hard part.** It is among the most difficult, time-consuming, and costly activities; data needs are often unclear at the start and evolve as the estimate develops. Because uncertainty drives cost-risk analysis, *risk data must be collected at this stage* — meeting experts early and often can surface risks sooner and reduce later collection effort.
- **Normalization makes raw data fit for use.** Inflation adjustment (to BY, CY, or RY dollars) is the most common technique, but learning/cost-improvement curves, production-rate effects, scope consistency, anomalies, technology advancement, and reporting-system differences (mapping accounting categories to WBS) all may require adjustment.
- **NASA has authoritative inflation sources.** The Cost Analysis Division (CAD) issues an annual **NASA New Start Inflation Index** for estimating new efforts and normalizing prior-mission cost; it is *not* for civil-servant personnel costs or for already-contracted work, where DCAA-approved forward pricing indices apply.
- **Data protection is a gating requirement.** Non-disclosure agreements must be in place before non-government personnel can access Confidential Business Information; federal employees fall under the Federal Trade Secrets Act.

## Mental Models
- **GR&A are the fence before the field.** Set the boundary first — what's in, what's out, in which year's dollars, on what schedule — and every later choice has a place to stand. Undocumented assumptions are silent scope, and silent scope is where estimates diverge.
- **The methodology choice is a data-availability question, not a preference.** Ask "what do I actually know?" before "which method do I like?" Few known parameters point to parametric or analogy; a fully defined WBS unlocks build-up; live programs unlock EVM.
- **A CER is an argument, not just an equation.** Its defensibility rests on logical correlation and disciplined research — a driver that correlates but has no causal rationale is a coincidence waiting to mislead.
- **Always estimate it twice.** The cross-check with an alternative methodology is the cheapest insurance against a wrong point estimate; a number that survives a second method earns trust.
- **Garbage normalized is still garbage — but un-normalized good data is unusable.** Raw cost data from different years, scopes, and reporting systems cannot be compared until adjusted; the normalization step is what makes "apples to apples" literally true.

## Anti-patterns
- **Subjective analogy adjustment.** The handbook warns against subjective upward/downward tweaks to a comparable system's cost: such tweaks weaken how valid and how defensible an estimate is, so they are best avoided. Historical data and analysis are more credible and defendable than expert "adjustment factors."
- **Misapplying a CER.** Applying a CER improperly — or outside the input range for which it was built — can produce a serious estimating error; CERs must be detailed, documented, and periodically re-examined.
- **Using an unvalidated model.** A model must be validated (and corrections incorporated) *before* the estimator relies on it to generate estimates.
- **Skipping the cross-check.** Producing a single point estimate with no alternative-methodology sanity check is called out explicitly as a gap the best practices exist to close.

## Key Takeaways
1. **Tasks 4-7 are the "how" of the estimate:** bound it (GR&A), choose the method, choose/build the tool, then feed it normalized data.
2. **GR&A come in two layers** — global and element-specific — and are documented continuously as they evolve, with P/pM and stakeholder agreement.
3. **Three core methodologies** (analogy, parametric, engineering build-up) plus **EVM extrapolation**; which one prevails is governed by how much data exists, and that shifts across the life cycle.
4. **Parametric work centers on the CER** — a regression-derived Y-vs-X equation whose drivers need both correlation and a sound logical basis, valid only inside its data range.
5. **Build-up is detailed and defensible but costly and "what-if"-resistant;** Delphi is the documented expert-judgment fallback when empirical data are absent.
6. **No single model fits all purposes;** calibrate parametric models to comparable history, validate before use, and be ready to defend the choice — the Three Cost Model Best Practices (recheck, cross-check, keep current) apply when you build your own.
7. **Collect risk data during data collection,** not later — uncertainty is the driver of the eventual cost-risk analysis.
8. **Normalize before use:** inflation (BY/CY/RY) is primary, but learning curves, production rates, scope, anomalies, and reporting differences all matter; use the NASA New Start Inflation Index for new efforts and DCAA forward pricing for contracted work.

## Connects To
- **ch02 / Part 1 tasks (this pack):** Tasks 4-7 inherit the project definition, technical baseline, and CADRe assembled in the earlier tasks; GR&A "should be in sync" with the CADRe.
- **Task 8 (inflation) and Task 9 (sensitivity analysis):** normalization here is the first inflation pass; the full estimate is adjusted again in Task 8, and GR&A feed the Task 9 sensitivity work.
- **`nasa-risk` pack (pairs with):** the directive to collect risk data during data collection — because uncertainty drives the cost-risk assessment — is the explicit handoff into the risk-informed cost-uncertainty analysis; GR&A on risk and mitigation activities are part of the baseline cost estimate.
- **`gao-cost` pack:** GAO's cost-estimating best practices cover the same methodology trio, CER discipline, and normalization principles from an oversight-audit perspective.
- **`nasa-schedule` / `gao-schedule` packs:** schedule and milestone GR&A, phasing methods, and schedule-data collection tie the cost estimate to the integrated schedule (Appendix K in the source).
- **`nasa-se-handbook` / `nasa-npr-7123` packs:** the WBS that organizes scope, make-vs-buy, and GFE/GFI decisions is the same systems-engineering work-breakdown backbone used across the life cycle.
