# Chapter — Obsolescence and Its Relationship to DMSMS

## Core Idea

Obsolescence and DMSMS (Diminishing Manufacturing Sources and Material Shortages) are run with the same management process, yet the two terms are not interchangeable. From a process standpoint there is no daylight between managing obsolescence and managing DMSMS; from a definitional standpoint, obsolescence is the looser, more context-bound concept. An item that one program treats as obsolete may still be perfectly serviceable from another program's vantage point. The chapter's central move is to separate the *state* of being obsolete from the *event* of a supply-chain failure, then map the overlap between them: most DMSMS problems trace back to some flavor of obsolescence, but the two sets are not identical — obsolescence does not automatically create a DMSMS problem, and a DMSMS problem can arise with no obsolescence at all.

The practical payoff for a sustainment engineer is restraint in opening cases. Recognizing that an obsolete item with adequate production or inventory is *not yet* a DMSMS issue keeps effort focused where supply actually cannot meet demand.

## Frameworks Introduced (exact source names, when/how)

- **Five underlying causes of an item being "out-of-date."** Introduced as the dimensions along which obsolescence is judged in a DMSMS context — an item counts as obsolete once it has fallen out of currency and something newer has taken over the role it filled. The source names them explicitly: **Technology**, **Function**, **Regulation**, **Supportability**, and **Market demand**. Each is given a worked example (see Key Concepts).

- **Planned vs. unplanned obsolescence.** Introduced as a two-way split in *how* an item becomes obsolete. The source illustrates planned obsolescence with a manufacturer deliberately halting production of proprietary consumable parts to push customers onto a newer model.

- **Figure 26 — Notional Relationship between DMSMS and Obsolescence.** Cited by the source as the diagram that depicts, in notional (not quantitative) terms, the overlap between the set of obsolete items and the set of DMSMS problems. The narrative around it establishes that the overlap is high but partial.

## Key Concepts

**Obsolescence is situationally dependent.** An item can be obsolete from one perspective and current from another. The Intel 8086 — an early 16-bit microprocessor from 1978 — is gone from modern computers but still serves in some industrial and embedded roles. Vacuum tubes, once foundational to radio, television, and radar, are obsolete for those uses yet still prized in certain high-end audio amplifiers for the sound they produce. Obsolescence is therefore a judgment relative to a use case, not an absolute property of the part.

**The five underlying causes, with the source's examples:**

- **Technology** — a newer technology becomes the broadly preferred choice even though the older one still works and can still be made or bought for niche needs. DVD recorders and players superseding videocassette recorders is the cited case.
- **Function** — the item no longer performs as intended because of hardware, software, or requirements changes, even if it remains commercially available. A videocassette tape (a Betamax tape especially) is functionally obsolete because the players needed to read it are no longer sold.
- **Regulation** — a ban on an item or substance forces its obsolescence. The source cites the prohibition on Freon for its ozone-depleting properties, and a ban on purchasing rare-earth elements such as neodymium or ytterbium from China.
- **Supportability** — the item can no longer be supported. Commercial software is the lead example: it needs ongoing support to fix defects, patch vulnerabilities, and in some cases keep licenses valid; unsupportable software is obsolete. The principle extends beyond software — if the test capability an item depends on disappears, the item may no longer function reliably and can be treated as obsolete.
- **Market demand** — demand evaporates. The item may still be for sale but is no longer wanted (leisure suits), or it has become unprofitable to produce because demand is too low.

**Obsolescence does not equal a DMSMS issue.** An obsolete item that is still in production is not a DMSMS problem as long as production can meet demand — hand pumps for water, still made for off-grid locations, are the example. An obsolete, out-of-production item is likewise not a DMSMS problem if inventory on hand covers all future demand. In the first situation no DMSMS case is opened (the item is still produced); in the second a case is opened but needs no resolution.

**A DMSMS problem can evolve over time.** Change the facts of the inventory example and a problem materializes. If stock cannot cover future demand, DoD might repair the obsolete computer rather than replace it — and if repair is viable, there is still no DMSMS problem. A genuine DMSMS issue appears only when repair itself is blocked: the repair parts are also obsolete, the know-how (e.g., the skills) to do the repair is gone, or the test equipment needed to verify the system after repair is unavailable.

**A non-obsolete item can have a DMSMS issue.** Supply can fail for reasons unrelated to the part being out-of-date: market forces driving a supplier out of a product line, a supplier's bankruptcy, a natural disaster halting production, or a buyout of a sole-source provider that ends production temporarily or permanently. Some DMSMS issues are temporary and stem from allocation of a scarce item — in which case some systems hit a shortage while others do not.

## Mental Models

**Two overlapping circles, not one.** Picture obsolescence and DMSMS as two sets with a large but incomplete intersection (the source's Figure 26 is exactly this). Not all obsolescence lands in the DMSMS circle, and not all DMSMS lands in the obsolescence circle — yet most DMSMS problems sit inside the overlap, because most of them spring from some form of obsolescence.

**Supply-vs-demand as the DMSMS trigger.** Obsolescence is a status; the DMSMS trigger is whether remaining production capacity *or* inventory can satisfy future demand. An item can be obsolete for years without ever becoming a DMSMS problem, right up until the supply line — production, stock, repair, or test — can no longer keep pace.

**The repair chain as a failure ladder.** When replacement is off the table, repair becomes the fallback, but repair depends on three rungs: parts, skills, and test capability. A DMSMS problem emerges the moment any one rung is missing. Use this ladder to diagnose *why* an aging item has become a true shortage rather than merely an old part.

**Obsolescence as a lens, not a label.** Because an item can be obsolete from one perspective and current from another, treat "obsolete" as a question — obsolete *for what use, under whose requirements?* — rather than a fixed tag stamped on a part number.

## Key Takeaways

- DMSMS management and obsolescence management share one process, but the words are not synonyms — obsolescence is the looser, situation-dependent concept.
- An item is obsolete in the DMSMS sense once it has fallen out of currency and a newer thing has taken over the role it filled; the source organizes the causes into five buckets — Technology, Function, Regulation, Supportability, and Market demand.
- Obsolescence may be planned (e.g., deliberately discontinuing proprietary consumables to force an upgrade) or unplanned.
- Being obsolete is necessary-ish but not sufficient for a DMSMS issue: if production or inventory still meets demand, there is no DMSMS problem to resolve.
- A DMSMS issue can develop later, when repair becomes the only option and the parts, skills, or test capability for that repair are missing.
- A perfectly current item can still hit a DMSMS issue — supplier exit, bankruptcy, disaster, sole-source buyout, or scarce-item allocation.
- The bottom line the source draws: not all obsolescence causes DMSMS, and not all DMSMS comes from obsolescence, but most DMSMS issues do arise from some form of obsolescence.

## Connects To

- **Case management and triage** — the obsolete-but-still-supplied examples (hand pumps, in-inventory computer) explain *when not* to open a DMSMS case and *when* to open one that needs no immediate resolution, feeding directly into case-prioritization practice.
- **Repair-vs-replace sustainment decisions** — the parts/skills/test ladder ties this chapter to repair-source analysis and to test-equipment and workforce-skill sustainment.
- **Supply-chain risk and supplier monitoring** — the non-obsolescence DMSMS causes (bankruptcy, sole-source buyout, disaster, allocation) link to supplier health surveillance and sole-source risk mitigation.
- **Regulatory and environmental compliance** — the Regulation cause connects to substance bans and counterfeit/material-restriction controls in the broader sustainment program.
- **Proactive obsolescence forecasting** — the situational, perspective-dependent nature of obsolescence motivates forward-looking technology and end-of-life monitoring rather than reactive part-by-part labeling.
