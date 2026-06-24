# GAO Cost Estimating Guide Cheatsheet

Quick reference for the GAO Cost Estimating and Assessment Guide (GAO-20-195G). Decision rules, selection tables, and tells & smells.

## Quick Decision Rules

**"What makes an estimate reliable?"**
The **four characteristics**: comprehensive, well documented, accurate, credible. Miss any one and it is not reliable. Each of the **18 best practices** maps to one of the four.

**"Where do I start?"**
Step 1 — **purpose and scope**. The intended use fixes scope and level of detail. Never start with numbers.

**"Which estimating method?"**
By design maturity + data. **Analogy** (similar past system, little detail) · **Parametric** (drivers + cost data, no detailed design) · **Engineering build-up** (mature design, bottom-up, most accurate). Cross-check with a second method + an ICE.

**"Is the point estimate enough to budget?"**
No. A point estimate carries no confidence information and tends to under-fund. Run sensitivity (Step 8) + risk/uncertainty (Step 9), then budget to a defensible **confidence level** off the S curve, carrying **contingency** to cover the gap.

**"Spending looks fine — is the program OK?"**
Spending alone misleads. Add **earned value** (BCWP). Compare planned (BCWS), earned (BCWP), actual (ACWP). CPI<1 or SPI<1 = trouble; forecast the EAC early while recovery is still possible.

**"How do I audit an estimate?"**
Score it against the 18 best practices → roll up to the four characteristics → overall reliability verdict. Compare agency *guidance* against the 12 steps to find process gaps.

---

## The 12-Step Cost Estimating Process

| Phase | Step | Name | Ch |
|---|---|---|---|
| **Plan / define** | 1 | Define the estimate's purpose | 2 |
| | 2 | Develop the estimating plan (team + schedule) | 2 |
| | 3 | Define the program (technical baseline) | 2 |
| | 4 | Determine the estimating structure (WBS) | 2 |
| **Build the number** | 5 | Identify ground rules and assumptions | 3 |
| | 6 | Obtain the data | 3 |
| | 7 | Develop the point estimate | 3 |
| **Quantify confidence** | 8 | Conduct sensitivity analysis | 4 |
| | 9 | Conduct risk and uncertainty analysis | 4 |
| **Finalize / sustain** | 10 | Document the estimate | 5 |
| | 11 | Present the estimate to management | 5 |
| | 12 | Update the estimate | 5 |

## The Four Characteristics → what they demand

| Characteristic | Demands |
|---|---|
| **Comprehensive** | full life cycle, complete WBS, all GR&As documented, nothing omitted/double-counted |
| **Well documented** | sources/methods/calculations captured; a stranger could rebuild it; traced to source data |
| **Accurate** | unbiased, most-likely-cost basis, inflation-adjusted, reconciled to actuals |
| **Credible** | sensitivity + risk analysis, major drivers cross-checked, reconciled to an ICE |

---

## The Three Core Estimating Methods

| Method | Use when | Strength | Weakness |
|---|---|---|---|
| **Analogy** | early; a close similar system exists | fast, low data need | weak without a good analog; subjective adjustments |
| **Parametric** | drivers + cost history, design still vague | data-driven, repeatable (CERs) | needs valid data range; can be extrapolated wrongly |
| **Engineering build-up** | mature design | most accurate, traceable | slow, costly, data-hungry |

Supplement with: expert opinion · extrapolation from actuals (averages, EACs) · **learning curves** (Y = AX^b) for recurring production.

## Risk & Uncertainty Toolkit (Steps 8-9)

- **Sensitivity** (one input at a time) → ranks parameters → **tornado chart**.
- **Three-point estimate** (min / most-likely / max per element) — captures combined uncertainty.
- **Risk-driver approach** (probability × cost effect, from the **risk register**) — ties contingency to discrete risk events. *Don't double-count with three-point.*
- **Monte Carlo simulation** → total-cost distribution → **cumulative distribution (S curve)** → pick **confidence level** → size **contingency**.

## EVM Quick Reference

**Three measures**: BCWS (planned value) · BCWP (earned value) · ACWP (actual cost).

| Index | Formula | Read |
|---|---|---|
| **CPI** | BCWP / ACWP | cost efficiency; >1 favorable |
| **SPI** | BCWP / BCWS | schedule efficiency; >1 favorable |
| **TCPI** | BCWR / (EAC − ACWP) | efficiency needed on remaining work |

**EAC** = ACWP (cum) + (BAC − BCWP (cum)) / efficiency index (cumulative CPI = optimistic/best case; CPI×SPI = worst case).
**Baseline**: PMB (excludes mgmt reserve + fee) → +MR = CBB → +fee = contract price. Validate the system against **EIA-748** (32 guidelines); confirm executability with an **IBR**.

---

## Specialized Techniques (where the cost behaves differently)

- **Software** → size (SLOC / function points / COSMIC / use case) → convert to effort; classify code new/reused/adapted/auto-generated. Watch black-box parametric tools and inconsistent counting.
- **Repetitive production** → learning curves (unit vs. cumulative-average theory); **Anderlohr** + **retrograde** for production breaks.
- **Choosing solutions** → **Analysis of Alternatives** (22 best practices, 5 phases; NPV where benefits monetize).
- **Structuring scope** → WBS templates (MIL-STD-881D, NASA/DOE/PMI handbooks).
- **Internal control** → the **Green Book** (5 components, 17 principles); the estimating process *is* an internal control.

---

## Tells & Smells (overrun risk signals)

- **Numbers before scope** → estimating against an undefined program; do Steps 1-4 first.
- **No WBS, or an inconsistent one** → cost/schedule/EVM/risk can't reconcile.
- **Budgeting to the point estimate** (≈50% or lower confidence) → under-funded; budget to a justified confidence level.
- **No sensitivity or risk analysis** → not credible; limitations hidden.
- **Optimistic GR&As / best-case assumptions** → biased low; accuracy fails.
- **A method used outside its valid range** (extrapolated CER, analogy with no analog) → silent error.
- **Data not normalized** (inflation, recurring vs. nonrecurring) → distorted model.
- **Undocumented estimate** → indefensible, un-reusable, can't be independently reviewed.
- **Stale estimate** (not updated against actuals) → no longer a credible predictor.
- **Spending reports without earned value** → looks fine while badly behind (the railroad trap).
- **Level-of-effort overused in EVM** → variances become meaningless.
- **No IBR / unexecutable baseline** → EVM measures against fiction; consider an over-target baseline.
- **No independent cost estimate** → no reconciliation, lower credibility.
