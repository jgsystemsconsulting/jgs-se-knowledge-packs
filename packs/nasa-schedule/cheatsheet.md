# Cheatsheet — NASA Schedule Management

Fast decision rules, selection tables, and tells & smells distilled from the handbook.
Wording is this pack's own. Chapter refs in parentheses.

---

## The five sub-functions at a glance (ch01)

| Sub-function | Job | Governing sub-plan | Chapter |
|---|---|---|---|
| Planning | Decide *how* scheduling will run; write the SMP | (the SMP itself) | ch02 |
| Development | Build the IMS from scope | Schedule Development Plan | ch03, ch04 |
| Assessment & Analysis | Validate credibility, then test likelihood | Assessment & Analysis Plan | ch05, ch06 |
| Maintenance & Control | Status, measure, correct | Maintenance & Control Plan | ch07 |
| Documentation & Communication | Record and disseminate | Doc & Comm Plan | ch08 |

## Four breakdown structures = four questions (ch03)

| Structure | Question | Owns |
|---|---|---|
| WBS | What? | product scope, the traceability spine |
| OBS | Who? | the performing organization |
| CBS / RBS | How much? | resources, control accounts |
| IMS | When? | time-phased network |

If the four disagree, the schedule is not yet credible.

## Where the baseline is set (ch04, ch07)

- Pre-Phase A: high-level summary tasks + key milestones.
- Phase A: discrete breakdown, identifiable preliminary critical path, initial margin.
- Phase B (PDR): **final baseline approval** — becomes the EVM performance-measurement baseline.
- Phase C/D: push far-term work into shorter tasks as time advances.
- Baseline at **KDP C** (or Program Approval); ICSRA/JCL required first for LCC > $250M.

## Loading the schedule — pick the method (ch04, ch06)

| Method | Status | Use when |
|---|---|---|
| Resource loading | Best practice; required when a JCL is required | grassroots workforce/equipment data exists |
| Cost loading | Acceptable substitute (less cumbersome) | resource loading impractical (e.g., via TD/TI hammocks) |
| Budget loading | **Not a defined Agency method — avoid** | never (low fidelity, unreliable confidence level) |

## SRA framework — IMS vs. Analysis Schedule (ch06)

| | IMS as framework | Analysis Schedule |
|---|---|---|
| Fidelity | Highest; config-controlled | Lower; surrogate |
| Use when | Feasible (default best practice) | IMS too large/unsuitable/split across servers |
| Size guidance | (full network) | ~100–3000 working tasks |
| Risk | — | can lose logic, mask/create false critical paths; must prove it emulates the IMS |

## Modeling a risk in an SRA (ch06)

- Risk = **Bernoulli likelihood × impact distribution** (triangular, or uniform if little known).
- Default mapping: **Activity Duration Impact** (zero-duration delay milestone).
- Map to the **first** activity in the affected string; let logic ripple it.
- **Correlation**: assess always; default **0.3** (industry range 0.25–0.75).
- Run **uncertainty-only first**, then add discrete risks.
- Zero out margin tasks before simulating.

## Reading the S-curve (ch06)

| Shape | Meaning |
|---|---|
| Flat slope | high uncertainty (typical early) |
| Steep slope | low uncertainty (typical post-PDR) |
| Left-side dog-leg | a backstopped earliest-possible date (e.g., shared test slot) |
| Long right tail | high-impact / low-probability risk |
| Bimodal PDF | two clusters of risk-impact magnitude |

**JCL**: read at the equal-probability **knee** of the frontier curve; 70% JCL knee ≈ 78–84th
percentile on an individual S-curve.

## Sensitivity vs. Criticality vs. Cruciality (ch06)

| Measure | Question | Display |
|---|---|---|
| Sensitivity | "how big" | tornado chart |
| Criticality | "how often" (on critical path) | basis for stochastic critical paths |
| Cruciality | "how big and how often" | sensitivity × criticality |

All are correlations (−1.0 to 1.0), not direct impacts; rankings re-sort as risks change.

## Tiered assessment order (ch05)

- **1st Tier (assessment):** Requirements Check → Health Check → Risk ID & Mapping Check.
- **2nd Tier (assessment):** Critical Path & Structural Check (incl. Shock Test) → Basis Check → Resource Integration Check.
- **3rd Tier (analysis):** SRA → ICSRA.

Credibility (assessment) before likelihood (analysis) — always.

## Corrective-action decision (ch07)

| Action | Touches PMB/ABC? | Authority |
|---|---|---|
| Watch | No | P/p |
| Retain | No (with rationale) | P/p |
| Replan | PMB may change; ABC unchanged | PM, within the MA |
| Rebaseline | ABC (and usually MA, PMB) changes | Decision Authority + OMB/Congress |

Mandated for P/ps > $250M (NPR 7120.5 / NASA Authorization Act 2005): **15%** over ABC → replan;
**30%** → rebaseline; key-milestone slip **> 6 months** → replan.

## Report types — match the lens to the question (ch08)

| Type | Answers | Nature |
|---|---|---|
| Status | "Where are we now?" | actual snapshot, no metrics |
| Progress | "How are we doing vs. plan?" | deterministic, with variance/trend/EVM |
| Forecast | "Where will we likely end up?" | probabilistic (SRA/ICSRA) |

## Tells & smells (construction defects) (ch04, ch05)

- **Hard constraints** (Must-Start/Finish-On) — override logic, inject negative float; replace with soft constraints/ASAP. A single one can invalidate a schedule.
- **Dangling activities** — missing predecessor/successor; corrupts float and critical path.
- **Leads/lags as real tasks** — hide detail, can't be statused, can't carry uncertainty distributions; replace with activities.
- **Non-FS logic without justification** — obscures the critical path.
- **Logic on summary activities** — wrong; summary dates derive from detail.
- **Redundant links** — A→C when A→B→C exists; complicates analysis.
- **LOE on the critical path** — captures no measurable work; remove it.
- **High-duration activities (> ~2 months)** — planned at too high a level for control.
- **Negative float** — usually an artificial constraint or out-of-sequence logic, not a real condition.
- **Stale statusing** — incomplete tasks left in the past, actuals in the future.

## Tells & smells (gaming / process) (ch07, ch08)

- **Late-date baselining** — baselining off late dates to minimize reported variance.
- **Manipulating the IMS for favorable metrics** — destroys its value as a management tool.
- **Rubber baseline** — resetting the baseline without communication/buy-in to mask variance.
- **Retroactive BCRs** — adding completed work to the baseline to flatter SPI while real performance erodes.
- **Reporting from separate sources** — breaks single-database traceability.
- **Summary Schedule used as an IMS** — too coarse for analysis; hides cascading slips.
- **Over-long communication** — gets misread or ignored; keep it short and consistent.

## Quick terminology guardrails

- **Critical path** ≠ **driving path** ≠ **"critical activity"** (ch04).
- **Margin** (working days, reasoned from risk) ≠ **float** (calculated) ≠ **contingency** (non-working days) (ch04, ch07).
- **Funding** (incremental, per fiscal year) ≠ **budget** (time-phased resource value) (ch03).
- **Uncertainty** (no likelihood gate) ≠ **risk** (likelihood × consequence) (ch06).
- **Progress** (where things stand) ≠ **performance** (how well vs. plan) (ch07).
