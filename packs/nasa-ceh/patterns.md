# NASA Cost Estimating Handbook (CEH) Patterns & Techniques

Reusable patterns from the NASA CEH v4.0 cost-estimating process. Each has When / How / Trade-offs.

## Pattern 1: Define Before You Price (Project Definition first)

**When to use**: at the very start of any estimate, before reaching for a methodology or model.

**How**: work the three Project-Definition tasks in order — understand the customer request, build or obtain the WBS, and establish the technical description (baseline). Settle the **four critical elements** (resources, data, schedule, expectations) with the decision maker, and capture them. Use the standard NASA Level 2 WBS, extend it below Level 2 with the CADRe standard, and build a WBS dictionary.

**Trade-offs**: front-loading definition feels slow when stakeholders want a number now — but skipping it relocates the error into the estimate, where it is harder to detect and costlier to fix. A shared technical baseline is what lets a Project Office estimate and an independent estimate be compared at all.

---

## Pattern 2: Choose the Methodology by Data Availability, Not Preference

**When to use**: at Task 5, once scope is defined and you know what data you actually have.

**How**: ask "what do I know?" Sparse definition → **analogy** or **parametric**; a fully defined WBS → **engineering build-up**; a live program with actuals → **EVM extrapolation**. For parametric work, run the seven-step parametric process to build a CER whose drivers have both statistical correlation and a sound logical rationale. Use **Delphi** only as a documented fallback when empirical data are absent.

**Trade-offs**: parametric is fast and replicable but loses credibility outside its data range and is opaque to non-statisticians; build-up is defensible and severable but costly, slow, and "what-if"-resistant. No single method is right everywhere — the right one is the one the data support.

---

## Pattern 3: Normalize Before You Compare

**When to use**: at Task 7 (data gathering), before any data feeds a model.

**How**: adjust raw data so it is comparable — inflation to BY/CY/RY dollars (the most common adjustment, using the NASA New Start Inflation Index for new efforts and DCAA forward pricing for contracted work), plus learning/cost-improvement curves, production-rate effects, scope consistency, anomaly removal, and mapping reporting-system categories to the WBS. Collect **risk data at this stage**, because uncertainty drives the later cost-risk analysis.

**Trade-offs**: normalization is among the most difficult, time-consuming activities, and data needs evolve as the estimate develops — but un-normalized data from different years, scopes, and reporting systems simply cannot be compared.

---

## Pattern 4: Treat the Point Estimate as a Starting Line, Then Build the S-curve

**When to use**: after Task 8 produces the deterministic LCC point estimate.

**How**: do not stop at the single number. Run the Task 9 six-activity cost-risk assessment to produce a credible **CDF / S-curve** across the project's cost range, read the confidence level off it, and size the **UFE** reserve needed to reach the management-chosen confidence. Phase that reserve where risk realizes — typically the PDR-to-CDR window and Integration and Test, not evenly across the calendar. Develop the deterministic and probabilistic efforts in parallel and iteratively, not strictly serially.

**Trade-offs**: summing the most-likely values of components understates the total, so a probabilistic roll-up is required, not naive addition — that costs analysis effort, but a single number hides the potential for overruns from a decision maker.

---

## Pattern 5: Document So an Independent Analyst Could Rebuild It

**When to use**: continuously from the start of the estimate, formalized in Task 10.

**How**: capture the **Basis of Estimate (BOE)** — GR&A, cost drivers, model inputs, analogy rationale, CER citations with descriptive statistics — to the standard that a stranger with the BOE and its cited sources could regenerate the number without phoning you. Include a comparison cost track explaining any deviation from a prior estimate, validate with cross checks and a peer review before briefing.

**Trade-offs**: documenting continuously is more discipline than writing it all up at the end — but poorly documented analyses fare badly at formal reviews (NARs), and an estimate nobody can reproduce is an assertion, not an estimate.

---

## Pattern 6: Produce a JCL with a Probabilistic Cost-Loaded Schedule

**When to use**: at KDP-C (projects) / KDP-I (programs), where NASA policy requires a JCL.

**How**: run the six-stage process — set goals (Step 0), build a logic-networked summary schedule, cost-load it by **Time-Dependent vs. Time-Independent** classification (does the cost grow if the schedule slips?), layer in the risk register, add baseline uncertainty (typically a triangular low/most-likely/high distribution), then simulate. Read the JCL as the fraction of runs landing in the lower-left (at or under both targets) quadrant of the scatterplot; use frontier lines for chosen confidence levels.

**Trade-offs**: the discipline of building the JCL improves the underlying plan, but the scatterplot is a snapshot valid only for the current plan — change funding or schedule and it must be rerun. Take care to segregate uncertainty caused by modeled risks from baseline uncertainty to avoid double-counting variability.

---

## Pattern 7: Make Cost a Constraint with Affordability and CAIV

**When to use**: in early life-cycle phases, when shaping requirements and architecture.

**How**: invert the default flow. Instead of letting cost emerge from a fixed design, fix the cost target and let **design converge on cost** (CAIV) while still meeting *threshold* performance — "performance is not sacred" above threshold, and both performance and schedule may be traded. Establish the affordability process early, because LCC concentrates in O&S (human systems) or Phases C/D (robotic). Plot alternatives in the trade space and seek the leverage points, avoiding both gold-plating past the cost boundary and cheap options that miss the performance floor.

**Trade-offs**: challenging requirements against cost is organizationally harder than accepting them as given — but it is the documented mechanism for delivering within constraints, and the trade space makes the cost-performance leverage visible.

---

## Pattern 8: Compare Alternatives with a Discounted Economic Analysis

**When to use**: when choosing among investment alternatives or justifying a departure from the status quo.

**How**: run the seven-step EA — objective, assumptions/constraints, alternatives, benefit/cost estimates, rank by measures of merit, **sensitivity and risk analysis (step 6)**, document. Discount each year's net cash flow with the OMB Circular A-94 rate (PV = FV / (1 + i)^n), match nominal rates to current-dollar flows and real rates to constant-dollar flows, and prefer the most-positive NPV. When benefits resist quantification (typical of science missions), pivot to a cost-effectiveness analysis grounded in LCCE quality and expert-judged science value.

**Trade-offs**: an EA quantifies and clarifies but never decides — treating the NPV ranking as the verdict misreads the tool. Document thoroughly because IG and GAO review of major decisions is a real possibility.
