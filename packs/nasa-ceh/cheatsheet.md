# NASA Cost Estimating Handbook (CEH) Cheatsheet

## Quick Decision Rules

**"Where do I start an estimate?"**
**Project Definition** — understand the request, build the WBS, write the technical baseline. Settle the four critical elements (resources, data, schedule, expectations) before choosing any method.

**"Which estimating methodology?"**
By **data availability**: sparse data → analogy / parametric · fully defined WBS → engineering build-up · live program with actuals → EVM extrapolation. Cross-check with a second method always.

**"Is a single cost number the deliverable?"**
No. A point estimate is the *start* of cost-risk work. Build the S-curve (CDF), read the confidence level, size the UFE reserve. Summing most-likely values understates the total.

**"How good must my documentation be?"**
Good enough that an **independent analyst could rebuild the estimate** from the BOE and its cited sources. That is the acceptance test for Task 10.

**"What does a JCL actually measure?"**
The probability of finishing at or under **both** the cost target **and** the schedule target — jointly. Not the product of two separate confidences.

**"Cost as output or cost as input?"**
Affordability and CAIV make cost an **input/constraint**: design converges on cost, not cost on design — while still meeting threshold performance.

---

## The 12-Step Process (3 Parts)

| Part | Tasks | Purpose |
|---|---|---|
| **1 — Project Definition** | 1 Customer request · 2 WBS · 3 Technical description | Scope and define *what* is estimated (Ch 2) |
| **2 — Cost Methodology** | 4 GR&A · 5 Methodology · 6 Models/tools · 7 Data & normalization | Decide *how* the estimate is built (Ch 3) |
| **3 — Cost Estimate** | 8 Develop estimate · 9 Cost-risk · 10 Document · 11 Present · 12 Update | Produce, harden, justify, brief, maintain (Ch 4) |

*Presented in order for teaching; in practice iterative and rarely linear. GR&A is the most frequently revisited task.*

## Estimating Methodologies (Task 5)

| Method | Best when | Strength | Weakness |
|---|---|---|---|
| **Analogy** | early, one close analog | fast, intuitive | subjective adjustment erodes defensibility |
| **Parametric (CER)** | data for a relationship exists | fast, replicable, statistical confidence | invalid outside data range; opaque |
| **Engineering build-up** | detailed WBS, mature project | defensible, severable, exposes drivers | costly, slow, "what-if"-resistant |
| **EVM extrapolation** | program producing actuals | grounded in real performance | needs an underway program |

*Delphi = documented expert-judgment fallback only when empirical data are absent.*

## Dollar Types (Task 7 / inflation)

Base Year (BY) · Constant Year (CY) · Then Year / Real Year (RY, includes inflation). **NASA "Real Year" = DoD "Then Year"** — opposite of DoD, where "Real" means Constant. Use the **NASA New Start Inflation Index (NNSI)** for new efforts; **DCAA forward pricing** for already-contracted work.

---

## Cost-Risk Chain (Tasks 8–9)

**Point estimate → S-curve (CDF) → UFE reserve.**
- Point estimate (Task 8) = one deterministic sample.
- S-curve / CDF (Task 9) = the full probability distribution of cost.
- **UFE** = the reserve bought to lift the plan to the chosen confidence level; phase it where risk realizes (PDR→CDR, Integration & Test).
- In trades, pin one axis: hold confidence and read cost, *or* hold cost and read confidence — consistently.

## JCL (Joint Cost & Schedule Confidence Level)

**Method**: Probabilistic Cost-Loaded Schedule (PCLS). **Steps**: 0 goals · 1 schedule · 2 cost-load · 3 risk list · 4 uncertainty · 5 results.
- **TD vs. TI cost**: does the cost grow if the schedule slips? Yes → Time-Dependent ("marching army"); No → Time-Independent (materials).
- **Risk** = discrete probability-and-impact event. **Uncertainty** = indefiniteness of the baseline (triangular low/most-likely/high; usually dominates variance).
- **Scatterplot**: lower-left quadrant fraction (at/under both targets) = the JCL. Frontier lines = chosen confidence levels. Snapshot of the current plan only.
- **Policy**: ABC = 70% JCL · MA ≥ 50% · reviewed by Standing Review Board · set at KDP-C (projects) / KDP-I (programs).

## Decision-Support Analyses (Ch 6)

Five categories: **Sensitivity · Trade Studies · Affordability · CAIV · Economic Analysis** (procedures in Appendix N).
- **Sensitivity**: vary one element at a time vs. a fixed point estimate; finds sensitive vs. insensitive requirements. Gives **no probabilities** and **cannot capture dependencies**.
- **Trade study**: plot alternatives in the trade space; seek *optimal balance* of cost and performance, not minimum cost.
- **Make-vs-buy** (in-house vs. outsource) · **Lease-vs-buy** (lease vs. debt financing, OMB Circular A-94).
- **CAIV**: design converges on cost; meet *threshold* performance; "performance is not sacred." Commercial analog = target costing.

## Economic Analysis (Ch 7)

EA = LCCE + **discounting** + **cost-vs-benefit** + **measures of merit**. Seven steps; step 6 is sensitivity **and risk** analysis.
- **FV = PV(1 + i)^n** · **PV = FV / (1 + i)^n** (discount factor 1/(1+i)^n, End-of-Year).
- Keep **inflation** (NNSI, purchasing power) separate from **time-value-of-money** (discount rate, opportunity cost ≈ government borrowing cost).
- Match the rate: **nominal** with current/then-year dollars, **real** with constant/base-year dollars.
- **OMB Circular A-94** prescribes the rate and makes **NPV** the standard criterion (most-positive NPV wins).
- Benefits won't quantify (science missions) → pivot to **cost-effectiveness analysis**.

---

## Tells & Smells

- **Pricing before defining** → error relocated into the estimate; settle the four critical elements first.
- **Picking a method you "like"** → methodology follows *data availability*, not preference.
- **Subjective analogy tweaks** → erodes defensibility; prefer historical data and analysis.
- **CER applied outside its data range** → serious estimating error.
- **Unvalidated model** → validate before relying on it; no cross-check is a named gap.
- **A single cost number in a trade study** → hides overrun potential; use a probabilistic view.
- **Naively summing most-likely values** → understates the total.
- **Documentation only at the end** → fares badly at NARs; document continuously to the rebuild standard.
- **Reading a stale JCL scatterplot as guidance** → it is a snapshot of the current plan only.
- **Confusing inflation with time-value-of-money** → double-counts or omits an effect; nominal vs. real rate exists to keep them straight.
- **Treating an NPV ranking as the decision** → EA informs; the manager decides.
