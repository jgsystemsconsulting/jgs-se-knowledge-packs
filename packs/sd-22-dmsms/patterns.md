# SD-22 DMSMS Patterns & Techniques

Reusable patterns from the SD-22 DMSMS Guidebook. Each has When / How / Trade-offs. All are synthesized in original wording.

## Pattern 1: Run the Five Steps as a Continuous Cadence, Not a One-Pass Project

**When to use**: across the whole life cycle, from early technology development through sustainment.

**How**: cycle Prepare → Identify → Assess → Analyze → Implement, then begin again, because the market keeps shifting. Wrap the cycle in the Strategize overlay (modification planning plus self-evaluation). Tailor the entry point — you can enter at any step — but starting early widens every later option.

**Trade-offs**: continuous proactive management costs operations funding up front, and the start-up effort spikes above steady state. The payoff is hundreds of millions in documented cost avoidance versus escalating cost and readiness loss for reactive programs.

---

## Pattern 2: Set the Foundations Before You Write the Plan

**When to use**: at program initiation, before the DMP is finalized.

**How**: have program leadership define objectives, DMT roles, operating guidelines, meeting cadence, and the risk-based proactive/reactive split *first*; then the DMT writes the DMP to match the funding actually available. Charter the DMT with an ARCI chart (exactly one Accountable per decision per level; the PM is ultimately accountable). Keep the DMP a living, tailored, reference-not-tutorial document aligned to the Appendix D capability matrix.

**Trade-offs**: leadership engagement early costs senior attention, but delegating strategy to the DMT routinely produces a plan whose scope exceeds the budget or diverges from leadership's expectations.

---

## Pattern 3: Prioritize Monitoring with Two Filters and the Risk Cube

**When to use**: in the Identify step, before loading anything into predictive tools.

**How**: apply a first filter to screen *subsystems* (safety, mission criticality, cost history, problem areas, life-cycle phase, sustainment strategy, data availability, supply-chain vulnerability), then a second filter to screen *items* within them. Sort items into definitely-monitor, do-not-monitor, and uncategorized. Score the uncategorized on the risk cube — criticality, supply-chain vulnerability, time to resolve — and proactively monitor only the items that are high on all three axes.

**Trade-offs**: monitoring everything is prohibitively expensive; under-monitoring has produced large surprise resolution costs. The risk cube is the explicit bet about where to accept reactive risk — revalidate every do-not-monitor decision periodically.

---

## Pattern 4: Refresh Availability from Four Sources, and Confirm Everything

**When to use**: continuously through Identify, on a cadence matched to commodity volatility.

**How**: combine predictive tools, vendor surveys, critical-materials analysis, and product discontinuance notices (PDNs from GIDEP + DLA + tool alerts — pull all three since each carries unique data). Use more than one predictive tool, manually confirm findings, and never read "unknown availability" as "available." Survey electronics roughly twice yearly, software quarterly-to-annually by risk, and surface lower-tier critical materials by standing DMT engagement rather than exhaustive vendor surveys.

**Trade-offs**: multiple tools and manual confirmation cost labor, but tools recognize only ~71-72% of items and disagree on status, so single-tool, unverified output is a documented risk.

---

## Pattern 5: Treat "Assess" as a Gate That Decides Whether, When, and at What Level

**When to use**: when an issue surfaces (tool/vendor flag, PDN, or a health-assessment change), before committing resources.

**How**: gather programmatic, availability, criticality, and logistics data. Test the four "may-not-need-a-resolution" situations (no demand, enough stock to retirement/refresh, reclamation covers it, or the design phase). Run a health assessment (and the Appendix K system-level method) to find *when* the issue reaches the system. Prioritize competing problems with the four-step ranking, and decide level of resolution by the five factors plus cost arithmetic.

**Trade-offs**: assessment delays action and depends on data that is often incomplete (filled with assumptions that raise uncertainty). But "obsolete" is only an input — spending on a resolution that days-of-supply or an imminent refresh makes unnecessary wastes money, and software-license / IA lapses flip the default toward acting immediately.

---

## Pattern 6: Build Resolution Cost, Compare on Life-Cycle Cost, Then Adjust for Risk

**When to use**: in the Analyze step, once a resolution is judged necessary.

**How**: enumerate viable options by walking the three categories top-to-bottom (existing material → substitutes → redesign), keeping only options that meet *all* requirements and second-order effects. Build each option's total cost from the applicable cost elements (actuals first, program averages next, survey averages only as a sanity check). Compare on net present value via AoA or BCA — the benefit is identical, so the decision collapses to cost. Then weight technical, supply-chain, financial, and schedule risk, discard dominated options, and sometimes pay more to buy down risk. Check whether an external organization is already resolving it.

**Trade-offs**: rigorous costing and BCA take effort; for genuinely low-cost, low-risk choices a light AoA suffices. The cheapest option can re-obsolete quickly — risk weighting is what keeps the choice durable.

---

## Pattern 7: Resolve Security and Funding Together with the Resolution

**When to use**: from option selection through implementation.

**How**: because any resolution changes configuration, BOM, suppliers, or items, trigger a System Security Engineering re-look (assurance, SCRM, program protection, cybersecurity) coordinated with SSE SMEs — never the Program Protection Plan alone. Program and budget resolution funding in advance (DMSMS recurs yearly), and leverage funded modifications three ways: size LON buys against modification plans, account for modifications to avoid duplication, and rescope/slow a modification (with financial-authority approval) to absorb execution-year surprises. Execute through the standard ECP / configuration-change process with active DMT involvement, and size LON buys to a known end-of-need with conservative assumptions and a safety level.

**Trade-offs**: coordinating security and finance adds process and relationships to maintain; skipping the SSE re-look can field a new supply-chain vulnerability, and relying on execution-year funding risks unavailable resources. Under-buying an LON almost always costs far more than some excess inventory.
