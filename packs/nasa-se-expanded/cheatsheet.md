# Expanded Guidance for NASA Systems Engineering — Cheatsheet

Decision rules, selection tables, and tells & smells from the *Expanded Guidance* (NASA/SP-2016-6105-SUPPL). This is the depth companion to the base `nasa-se-handbook`.

## Quick Decision Rules

**"Is this re-run iterative or recursive?"**
- Same product, fixing a discrepancy → **iterate**
- Next lower design layer / next upper realization layer / next phase → **recurse**

**"Am I tailoring or customizing?"**
- Changing *whether* a binding "shall" applies → **tailor** → needs a deviation/waiver in the Compliance Matrix
- Changing *how* you satisfy it → **customize** → no waiver (document significant cases in the SEMP)
- Either way, check the governing PM directive (7120.5/.7/.8, 7150.2) separately — it may still require relief.

**"Verification or validation?"**
- Conforms to the requirements baseline, instrumented, controlled environment → **Verification** ("built right")
- Meets stakeholder expectations / ConOps, realistic environment, typical users → **Validation** ("right thing built")

**"How many times do I pay for this V&V activity?"**
- **Verify / Qualify / Certify** → once per **design** (resets if the design changes)
- **Accept** → once per **unit**, forever
- **Certification** is an **audit** of evidence, not a test.

**"Which baseline does this review establish?"**
- **SDR → Functional** · **PDR → Allocated** · **CDR → Product** · **ORR → As-Deployed**

**"Where do I stop decomposing?"**
- When the branch is deep enough to validate analytically *and* convince an independent review team the design is feasible/credible (and to support cost/operations modeling) — a resolution criterion, not a phase boundary. Deeper is waste.

**"Risk-Informed Decision Making (RIDM) or Continuous Risk Management (CRM)?"**
- *Choosing* (architecture, trades, baseline requirements) → **RIDM**
- *Executing* (driving identified risks to closure vs. trigger thresholds) → **CRM**

**"Which cost-estimating method?"**
- Concept + history only → **parametric** · design baselined, thin actuals → **analogous** · detailed scope + actuals → **engineering/grassroots**

**"Do I need formal decision analysis?"**
- Raise rigour when **Complexity, Uncertainty (could flip the ranking), Multiple Attributes, or Diversity of Stakeholders** are high. Scale rigour to consequence.

**"Is reducing this uncertainty worth it?"**
- Only if it could plausibly **change the ranking** *and* the project can afford the schedule slip — i.e., it is **net beneficial**. Otherwise decide on what you know.

---

## The SE Engine (17 processes, NPR 7123.1) — read 10–17 as tools, not steps

| System Design (4) | Product Realization (5) | Technical Management (8) |
|---|---|---|
| Stakeholder Expectations Definition | Product Implementation | Technical Planning |
| Technical Requirements Definition | Product Integration | Requirements Management |
| Logical Decomposition | Product Verification | Interface Management |
| Design Solution Definition | Product Validation | Technical Risk Management |
| | Product Transition | Configuration Management |
| | | Technical Data Management |
| | | Technical Assessment |
| | | Decision Analysis |

**Cadence:** development processes (1–9) run **5 engine cycles** (Pre-Phase A → D); technical-management processes (10–17) run **7 cycles** (Pre-Phase A → F). Phases **C/D are split** — design (left side) in C, realization (right side) in D. Implementation fires **only at the bottom tier**; everything above is Integration.

---

## Life-Cycle Reviews → the gate each earns (space flight)

| Review | Earns / confirms |
|---|---|
| **MCR** | Mission need affirmed; concept supports the need |
| **SRR** | Requirements + concept satisfy the mission; **freezes requirements** |
| **MDR/SDR** | Architecture responds to requirements; requirements allocated; **Functional baseline** |
| **PDR** | Preliminary design at acceptable risk; **Allocated baseline / design-to**; enter Implementation |
| **CDR** | Design mature enough to fabricate; **Product baseline / build-to**; production & verification plans |
| **PRR** | Ready to efficiently produce multiple similar systems |
| **SIR** | Segments, facilities, personnel ready to begin integration |
| **SAR** | End products complete and compliant; authorizes shipment |
| **ORR** | Ready to assume normal operations; **As-Deployed baseline** |
| **FRR** | Technical/procedural maturity for launch authorization |
| **DR/DRR** | Ready to safely decommission and dispose |

Non-7123.1-required but common: **DCR** (design certification), **FCA/PCA** (configuration audits), **TRR** (test readiness). Smaller mission classes (NPR 8705.4 A–D) may collapse to one review each for requirements, design, and acceptance (plus FRR for flight).

---

## EVM Arithmetic (measure "the system that produces the system")

- **BCWS** = planned cost of work scheduled · **BCWP (Earned Value)** = budgeted cost of work *performed* · **ACWP** = actual cost spent
- **Schedule variance** = BCWP − BCWS (negative ⇒ behind) · **Cost variance** = BCWP − ACWP (negative ⇒ overrun)
- **SPI** = BCWP / BCWS · **CPI** = BCWP / ACWP (<1 unfavourable, =1 on plan, >1 favourable)
- **VAC** = BAC − EAC · one-time-variance cross-check: **EAC = ACWP + (BAC − BCWP)**
- **Rule:** planned-vs-actual cost measures *spending only* — performance is always judged through earned value (BCWP).

---

## Technical-Measure Hierarchy (keep the viewpoints straight)

- **MOE** — customer viewpoint, operational, solution-independent; failing its critical value = stakeholder calls it a failure.
- **MOP** — supplier viewpoint, quantitative product attribute; an MOE is *validated* when its MOPs are met.
- **KPP** — must-not-fail subset; breaching a threshold → risk status, possible termination.
- **TPM** — build-time tracking of KPPs/MOEs/MOPs against the anticipated value; generic (mass, reliability) or unique.

**Three required leading indicators (NPR 7123.1, SRR→SAR):** **mass margin · power margin · RFA/RID/action-item burndown** — read for **maturity AND stability** (CDR-mature ≠ stable if requirements still churn).

---

## Interface Document Picker

| Document | Bilateral? | "Shall"? | Holds | Use when |
|---|---|---|---|---|
| **IRD** | Yes (all sign) | Yes | the boundary requirements | defining what the interface must do |
| **ICD** | Yes | No | the design solution | implementing the IRD |
| **IDD** | No (one-sided) | — | a fixed interface | one provider already set it; others conform |
| **ICP** | — | — | the control *process* | naming the forum + PIRN/IRN change mechanism |

Bilateral interfaces need **unanimous** approval; interface-control readiness sequences MCR (approach) → SDR (preliminary) → PDR (baselined).

---

## Decision-Analysis Method Menu

| Method | Best for | Watch out |
|---|---|---|
| **Trade study** | picking one option within constraints | trades yield *bounds*, not final values; escalate unresolved dissent |
| **Cost-benefit / cost-effectiveness / least-cost** | net benefit / benefit-per-fixed-cost / quality-as-cost-penalty | most cost-effective ≠ most effective |
| **Influence diagram** | formulation, clear communication | a *state* picture; convert to a tree to quantify |
| **Decision tree** | exhaustive consequence analysis | exponential branch growth |
| **AHP (Saaty)** | deriving criteria **weights** | biases alternative *selection* (assumes factor independence) |
| **Borda counting** | option best fitting *all* criteria | captures the consistent runner-up |
| **Utility / MAUT** | significant uncertainty, non-risk-neutral decider | utility curvature encodes risk attitude |

---

## Tells & Smells

- **"We already did stakeholder expectations"** at a lower tier → that's recursion; do them again for *this* product.
- **Verifying a design not yet detailed enough to build** → you jumped to the right side of the engine too early.
- **A real waiver labeled "customization"** → unapproved compliance gap; **customization labeled a waiver** → needless paperwork.
- **Over-tight performance spec** (3-hr recharge where 12 works; ±0.5 kg where ±2.5 works) → destroys solutions, inflates metrology cost.
- **"Minimize noise" requirement** → unverifiable; rewrite quantitatively or it isn't a requirement.
- **Safety/reliability/fault-management analysts engaged only after the design is formed** → bolt-on analysis that misses the real risk drivers.
- **Baselining before alternatives are understood** → kills inventive exploration; baseline *late* (but baseline).
- **Trusting a reused product's original pedigree** in a new system/environment → high ground heritage can be low space heritage; modification = new design.
- **A V&V Plan with only verification** → real validation happening informally and uncredited; preplan and record it.
- **Qualification levels cranked so high they induce unrealistic failures** → cost with no real-weakness insight.
- **WBS describing functions, not products** → only the PM is formally responsible for any deliverable.
- **Comparing planned to actual cost as "performance"** → that's spending; performance is earned value.
- **Overlapping decision-board scopes** → confusion, delay, decision paralysis, skill drain.
- **Extensively redlined, unpracticed procedures** (the NOAA N-Prime precondition) → CM red flag.
- **Treating the budget cycle as an SE process** → it's a planned *disturbance* (often a continuing resolution past Oct 1); plan around it.

---

## Governing Documents Map

**NPR 7123.1** (the 17 SE processes, engine, iterative/recursive definitions, Appendix G review criteria, Appendix H Compliance Matrices, three required leading indicators) · **NPR 7120.5/.7/.8** (program/project management — phase model, KDPs, JCL/EVM thresholds; space flight / IT & infrastructure / research & technology) · **NPR 7150.2** (software) · **NPR 8000.4 + NASA/SP-2011-3422** (Risk Management = RIDM + CRM) · **NPR 8705.4** (payload risk classification, tailoring anchor) · **SAE/EIA-649-2 + 649B** (CM: 5 functions, 37 principles) · **ANSI-EIA-748** (EVM system) · **ITAR/USML, NID 1600.55** (export control / SBU) · **AS9100** (quality-system crosswalk).
