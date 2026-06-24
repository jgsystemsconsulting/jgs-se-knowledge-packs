# SD-22 DMSMS Cheatsheet

## Quick Decision Rules

**"Where do I start?"**
With **Prepare** — leadership sets the foundations and risk-based proactive/reactive split *before* the DMP is written, so scope matches funding.

**"Should I monitor this item proactively?"**
Run the **risk cube**: only items high on all three axes — item criticality, supply-chain vulnerability, and time to resolve — earn scarce proactive-monitoring dollars. Everything else can be reactive or unmonitored, with the decision revalidated periodically.

**"This item is flagged obsolete — do I open a case / resolve it?"**
Not automatically. **Obsolete is an input, not a conclusion.** No resolution is needed if on-hand stock, reclamation, low demand, or an imminent retirement/refresh covers projected demand. Software-license and information-assurance lapses are the exception — act immediately.

**"Which resolution do I pick?"**
Enumerate viable options top-to-bottom (existing material → substitutes → redesign), build each one's cost, compare on **net present value (AoA / BCA)**, then weight risk and discard dominated options. Check first whether an external organization is already resolving it.

**"How big should the life-of-need buy be?"**
Size to a known **end-of-need** date (retirement, a funded modification, or a longer-term resolution) with conservative assumptions and a safety level — under-buying almost always costs far more than excess inventory.

---

## The Five-Step Process (+ Strategize overlay)

| Step | Question it answers | Produces |
|---|---|---|
| **Prepare** | What infrastructure do we need? | foundations, DMT, DMP, operational processes |
| **Identify** | What is (or will be) obsolete? | monitored list of immediate / near-term / forecast issues |
| **Assess** | Resolve? When? At what level? | the need / timing / level decisions |
| **Analyze** | Which resolution is best? | a costed, risk-adjusted preferred option |
| **Implement** | How do we fund and execute it? | a budgeted, fielded resolution |

**Strategize** wraps all five: modification planning + using evaluation results to improve the program. Run as a continuous cadence — finish the list, then start again.

## Mechanisms

- **First-order obsolescence** — market/regulation loss of a source (buy/license/support).
- **Lower-order (derived) obsolescence** — *functional* obsolescence your own change created.
- Applies **symmetrically and simultaneously to hardware and software** — software is bound to license and support, so its loss is as serious as a part loss.

## The Five Obsolescence Causes (Ch 8)

**Technology · Function · Regulation · Supportability · Market demand.**
Obsolescence is situation-dependent (obsolete for *what use, under whose requirements?*). Planned vs. unplanned. Not all obsolescence is a DMSMS issue, and not all DMSMS comes from obsolescence — but most DMSMS issues do.

## Prepare essentials

- **DMT** chartered by PM/PSM; scales/evolves with the system. **ARCI chart**: exactly one Accountable per decision per level; PM ultimately accountable.
- **DMP** mandatory (DoDI 4245.15), living, tailored, aligned to the Appendix D capability matrix.
- **Operations funding ≠ resolution funding.** Expect a start-up spike over steady state.
- Run processes inside a **QMS** (quality plan, compliance metrics, Lean Six Sigma / DMAIC).
- Track cases **Open → Closed → Watch List** — stopping at funding (not fielding) is a bad practice.
- **The BOM is the keystone** — indentured beats flat.

## Identify essentials

- **Two filters** (subsystems, then items) → load predictive tools.
- Items sort into **definitely-monitor / do-not-monitor / uncategorized**; score uncategorized on the **risk cube**.
- **Four availability methods**: predictive tools · vendor surveys · critical-materials analysis · PDNs (GIDEP + DLA + tool alerts).
- Tools are imperfect (~71-72% recognition, disagree ~4%) — use more than one and **manually confirm**; "unknown" is never "available."

## Assess essentials

- Four impact types: **cost, schedule, availability, readiness**.
- Four data families: **programmatic, availability, criticality, logistics**.
- **Health assessment** + Appendix K = when the issue reaches the *system*, not just the part.
- **Days of supply is the clock**; four-step prioritization for which problem first; five factors for level of resolution.

## Analyze essentials

- **Total cost = sum of applicable cost elements** (~20 categories); add counterfeit testing when buying outside authorized sources.
- **Three categories**: existing material (logistics) → substitutes (engineering) → redesign (engineering).
- Compare on **NPV (BCA)** or light **AoA**; weight risk; discard dominated options; sometimes pay more to buy down risk.
- **Roadmaps + health assessments** set timing — fold fixes into planned refresh/insertion.

## Implement essentials

- Three processes: **program/budget → integrate with modification funding → execute**.
- Plan funding **in advance** — execution-year reliance is not a best practice.
- Three modification budgeting best practices: size LON to funded plans · avoid duplication · tap modification scope for surprises (financial-authority approval).
- Execute through the standard **ECP / configuration-change** process; a senior **champion** is critical.
- LON statutes: **31 U.S.C. 1502(a)** and **10 U.S.C. 2213**; a bona fide need statement and written determinations unlock exceptions.

---

## Tells & Smells

- **Monitoring everything** → prohibitively expensive; use the risk cube.
- **Accepting too much risk to save monitoring cost** → large surprise resolution costs.
- **Trusting one predictive tool / unverified output** → recognition gaps and inter-tool disagreement.
- **Reading "unknown availability" as safe** → false security.
- **Treating an "obsolete" flag as an automatic resolution trigger** → wastes money on unneeded fixes.
- **Delegating strategy to the DMT** → DMP scope exceeds funding.
- **Stopping case tracking at funding, not fielding** → no feedback on what was actually implemented.
- **Reading the PPP alone to judge security** → coordinate with SSE SMEs; the PPP may be stale or incomplete.
- **Cost as the sole criterion** → cheap option re-obsoletes; weight risk.
- **Sizing an LON buy without the roadmap** → over-procures past a modification that retires the item.
- **Relying on execution-year funding** → resources unavailable when the issue bites.
- **Leaving obsolete items in a design** → pushes buyers to risky distributors; counterfeit exposure.
