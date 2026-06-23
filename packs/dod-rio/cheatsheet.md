# DoD RIO Management Guide — Cheatsheet

Fast-reference decision rules, selection tables, and tells & smells. Scores, scales, and
gate names are the guide's own.

---

## The three RIO objects (the diagnostic lens)

| Object | Question | Characterized by | Process |
|---|---|---|---|
| **Risk** | What can go wrong? | Likelihood **and** consequence | Five-step risk process |
| **Issue** | What has gone / will certainly go wrong? | Consequence only (likelihood = 5 / prob = 1) | Parallel issue process |
| **Opportunity** | What can be improved? | Likelihood (rises with effort) and benefit | Six-activity opportunity loop |

## The five-step risk process

```
Plan → Identify → Analyze → Mitigate → Monitor
        └──────── continuous Communication & Feedback ────────┘
```
Same steps across all life-cycle phases and AAF pathways; the *detail* of each varies.

## Scoring rules (do / don't)

- Likelihood = 1–5 probability band (Table 2-2). Consequence = 1–5 (Table 2-1, tailored).
- Consequence = **maximum** of cost/schedule/performance — never an average.
- Score **unmitigated** (as if fully realized, no further mitigation).
- Use **fully burdened** costs (include burn-rate overhead for schedule slips).
- KPP / APB threshold breach ⇒ **Level 5** performance consequence.
- **No fractional scores** (2.4 is invalid — ordinal only).
- Risk level (matrix) ≠ priority. Add cost-effectiveness, frequency, time frame, inter-risk
  relationships, and EMV/ROI; **always rank KPP-threatening risks high**.

## Risk matrix → level

5×5 grid of likelihood × max-consequence ⇒ **Low (green) / Moderate (yellow) / High (red)**.
Build the **risk register** early as the single source of truth; combining risk/issue/
opportunity registers is allowed.

## Four mitigation options (pick one or hybrid)

| Option | Essence | Watch-outs |
|---|---|---|
| **Accept** | Bear it, but keep tracking (Watch Item) | Pre-identify resources/schedule if realized; acceptance ≠ ignoring |
| **Avoid** | Alternate path / defer / substitute mature tech | Defer only if system would ship without it; tackle hard performance early |
| **Transfer** | Reassign task (MOA/MOU) | Hardest option; never fully removes Government schedule/performance exposure |
| **Control** | Drive likelihood/consequence down | Default; must produce *real* reduction, not relabeled baseline work |

## Burn-down plan (6 steps)

1. Sequence activities (realistic precedence) → 2. Make each objective & measurable →
3. Assign planned L/C → 4. Estimate dates → 5. Load into **IMS** → 6. Chart level vs. time.
Required for all high/moderate + selected low risks. **Meetings don't burn down risk — results do.**
Front-load high-**consequence** risks.

## Issue correction options

Score consequence only. Options: **Ignore** (after business-case analysis) or **Control**
(Avoid/Transfer rarer; Avoid often subsumed by Control). Plan = corrective action / POA&M with
an **EAC** in the IMS; re-assess for spawned risks.

## Opportunity decision

Six-activity loop (plan → identify → analyze [business case] → decide → monitor → feedback).
Options: **Pursue / Defer / Reevaluate / Reject** on benefit-vs-risk. Drives **should-cost**
(vs. staying inside **will-cost**). Aggregate small wins; reject short-term-gain/long-term-loss.

## AAF pathway → risk posture

| Pathway | Instruction | Risk move | Key levers |
|---|---|---|---|
| **UCA** (<2 yr) | DoDI 5000.81 | Accept deficiencies for speed | Operational risk first-class; ends in disposition analysis |
| **MTA** (2–5 yr) | DoDI 5000.80 | Fail early, descope | Op demo ≥1 yr before completion; trade off complex requirements |
| **MCA** (milestone) | DoDI 5000.85 | Front-load hard decisions | Entry milestone by where risk lives; burn down T/E/I in TMRR; SETR gates; TRA/MRA/SRA |
| **Software** | DoDI 5000.87 | Bake risk reduction into pipeline | Automation up front; MVP→MVCR; User Agreement; technical-debt tracking |
| **DBS** | DoDI 5000.75 | Fit commercial to process | Fit-gap analysis; ATP gates; validate funding before Functional Requirements ATP |
| **Services** | DoDI 5000.74 | Risk is the requirement | Seven steps; ARRT→PWS/QASP; CPARS annual performance |

MCA SETR gate set: **ASR/SRR/SFR/PDR → CDR/TRR/SVR/FCA/PRR → OTRR/IOT&E/PCA**.
Contract type follows the risk profile (cost-type = higher risk/Government control; fixed-price
= stable/minimal risk) — **risk is never fully transferred to industry**.

## Specialized methods (each a sensor → funnel into the enterprise register)

| Method | Authority | What it surfaces |
|---|---|---|
| **RMF** (7 steps) | DoDI 8510.01 | Cybersecurity authorization risk; Assess Only below system level; tier per NIST SP 800-39 (L1/L2/L3) |
| **MBCRA / Cyber Table Top** | DoDI 5000.89 | Mission impact of cyber attack, before operational test |
| **Agile / DevSecOps metrics** | DoD Agile Metrics Guide | Delivery risk via Size / Time / Effort / Defects |
| **FMECA** (on digital model) | DoDI 5000.88 | Failure modes flowing design → manufacturing → sustainment |
| **ITRA / DTRAM** | DoDI 5000.88 | Independent technical risk: 8 areas × 7 factors |
| **S&T / Program Protection** | DoDI 5000.83 | Unwanted technology transfer (Essential Technology Elements) |

Roll **micro-risks** up; decompose **macro-risks** down; map every sensor's output to the
program's common consequence language.

## Institutionalization (Appendices B/C/D)

- **PRMP** written at formulation, refreshed at re-baselining / phase change / T&E / sustainment.
- **Boards**: RMB (PM-chaired) · JRMB (mutual Government–contractor risk) · ROMB (handles
  opportunities too) · chartered RWGs from the SE/PM IPT.
- **Tools** (pick early, document in SEP): **Project Recon** (Army) · **Active Risk Manager**
  (Air Force) · **Risk Exchange** (Navy).
- **Roles** (3 tiers): Executive (MDA/PEO) · Management (PM/RMB/Risk Manager) · Working
  (IPTs/Risk Owner). **Every risk has an owner.**
- **Integration**: WBS (MIL-STD-881F) · IMP/IMS · EVM (EIA-748) · TPMs (DoDI 5000.02, kept
  SMART). **SRA/CRA/PRA** (Monte Carlo for SRA/CRA) are *indicators, not verdicts*; gate SRA on
  **DCMA 14-point** schedule health.

---

## Tells & smells (anti-patterns to catch)

- **"Shoot the messenger" culture** — punishing risk-raisers kills the information flow. (ch01)
- **Process for its own sake** — adding machinery that doesn't add value; the output (mitigation
  plans) matters more than the process. (ch01)
- **Mitigation inside the risk statement** — statement must hold only event/consequence/cause. (ch02)
- **Fractional scores** — 2.4 fakes precision and breaks comparison. (ch02)
- **Confusing Technology / Engineering / Integration** technical risk. (ch02)
- **Baseline-activity laundering** — relabeling ongoing contract work as "mitigation" without
  checking it actually reduces the risk. (ch03)
- **Meetings counted as burn-down** — only results burn down risk. (ch03)
- **"Simple" change taken on faith** — ask *why* it wasn't in the original design first. (ch03)
- **Unnoticed relapse of a retired risk** — review closed risks periodically. (ch03)
- **Short-term gain / long-term loss masquerading as opportunity.** (ch04)
- **Letting cross-program risks languish** — escalate early up PM→PEO→SAE→DAE. (ch04)
- **Schedule urgency overriding engineering judgment**; relying on an imposed timeline. (ch05)
- **Deferring software automation / leaving constraints unidentified** — kills velocity. (ch06)
- **Keeping micro-level Agile RIO siloed** and never aggregating it. (ch07)
- **Running an SRA on an unhealthy schedule** — one hard constraint corrupts the result. (ch08)
- **Treating out-of-contract risks as out of mind** — capture them regardless of scope. (ch08)
- **Untraceable mitigation** — not tied to a funded work package + schedule activity = aspiration. (ch08)
