# Chapter 4 — Opportunity Management and Cross-Program Risks

## Core Idea
Risk management protects a program's cost, schedule, and performance baseline; **opportunity management** is its mirror image — a proactive, resourced search for future *benefits* to that baseline. The DoD RIO Guide frames opportunities as the engine for hitting **should-cost** objectives (versus merely staying inside the **will-cost** estimate), and it treats opportunity management as a sibling discipline to risk and issue management rather than a separate program. The second half of this chapter shifts from the single program to the boundaries between programs: when a system depends on hardware, software, or schedules controlled by *other* programs, the interfaces themselves become a major risk source that no one program fully owns. Both topics are about reaching beyond the comfortable middle of the baseline — opportunities reach for upside, cross-program management reaches across organizational seams to contain downside.

This is the DoD acquisition-program complement to `nasa-risk` (NASA's CRM/RIDM treatment) and `dau-se-guidebook` (the broader SE process view). Where those cover risk theory and the SE process frame, this chapter carries the defense-acquisition mechanics: registers, boards, MOAs, tripwires, and the artifacts (SEP, Acquisition Strategy, IMS) that bind interdependent programs.

## Frameworks Introduced
- **Opportunity Management Process** (RIO Guide Figure 3-2) — a closed loop of six linked activities: Opportunity Process Planning, Opportunity Identification, Opportunity Analysis (the business-case step), the management-options decision (pursue / reevaluate / reject), Opportunity Monitoring, and Communication and Feedback that ties them together.
  - When/how: stood up continuously across the life cycle so candidate enhancements can be found before execution and at every later phase. Programs document the process and may fold it into the **PRMP** (Program Risk Management Plan).
- **Should-cost vs. will-cost framing** (Figure 3-1) — risk management keeps the program inside the will-cost/should-cost band; opportunity management is what actively *drives toward* the should-cost target.
  - When/how: used as the screening criterion for whether a candidate is a genuine opportunity; should-cost objectives set the likelihood and benefit thresholds.
- **Four management options for an approved opportunity** — Pursue now, Defer, Reevaluate, Reject. Each is chosen on a cost/schedule/performance benefit-versus-risk basis (or a hybrid of options).
  - When/how: applied at the decision point after the business-case analysis; the selected option drives the implementation approach.
- **Opportunity Register** (RIO Guide Table 3-1) — the opportunity analogue of the risk register: likelihood, cost to implement, monetary/schedule/performance return, program priority, strategy, owner, and expected closure date.
  - When/how: populated once an opportunity is approved and an owner assigned; reviewed at Program Management Reviews; pursue-option activities are also inserted into the **IMS**.
- **Risk Management Board (RMB) as opportunity authority** — the Guide assumes the existing RMB also adjudicates opportunities, though a separate **Opportunity Management Board** is permitted.
  - When/how: the RMB examines each candidate, approves or rejects, assigns owners, and oversees the register.
- **Cross-program / interdependency management toolkit** (RIO Guide Section 4) — a designated technical authority over interfaces, **MOAs** with cost/schedule/performance **tripwires**, an **Interface Control Working Group (ICWG)**, **ICDs/IRSs**, **Associate Contractor Agreements**, a synchronized schedule, an integration plan, and the interdependency-tracking chart (Figure 4-2).
  - When/how: invoked whenever a system depends on programs outside the PM's or PEO's portfolio, on another Service, or on joint/international partners.

## Key Concepts
- **Opportunity defined**: a potential future improvement to cost, schedule, or performance, realized by deliberately spending effort and resources — the likelihood of capture rises with the effort invested, which inverts the usual risk relationship where you spend to *reduce* likelihood.
- **Sources of opportunity**: changes that cut total ownership cost, e.g., a modular open systems approach or securing Government rights to a technical data package (which open up sparing and competition for modifications); design or manufacturing changes during R&D and production (often via **Value Engineering Change Proposals** that cut production/support cost without changing performance); and O&S-phase observations of actual in-service performance that surface reliability, fuel-efficiency, or maintenance gains.
- **The should-cost discipline**: a candidate that buys a short-term gain at the price of long-term harm is not a real opportunity. Genuine opportunities can also offset cost or schedule damage from *realized* risks.
- **Aggregation of small wins**: many minor, low-disruption improvements are encouraged because their benefits accumulate into a meaningful program-level gain — so incentives should reward vendors for spotting and recommending even small ones.
- **Incentivizing capture**: value management and contracting incentives (Value Engineering Change Proposals, benefit-split arrangements) are used to motivate both Government and contractor to pursue opportunities.
- **Cross-program risk origin**: integrating mature, stable, non-developmental government-furnished equipment goes relatively smoothly; new development that hosts or incorporates other programs' products generates technical, programmatic, and business risk because the interfaces are immature.
- **Interdependency reconciliation surface**: interdependent programs must reconcile funding levels, hardware/software schedules, **SWAP-C** (size, weight, power, and cooling) allocations, immature technologies, test results, and other factors such as spectrum, bandwidth, threats, mission area, and support concept.
- **Technical authority and adjudication**: the acquisition chain of command acts as (or appoints) a technical authority to control interfaces and settle disputes among participating programs; requirements disputes are referred to the **Configuration Steering Board (CSB)**.
- **MOAs and tripwires**: Memorandums of Agreement between interdependent programs fix roles, responsibilities, and cost/schedule/performance objectives, and are documented in the Acquisition Strategy and **SEP**; they carry tripwires that force a program to warn its family-of-systems partners of any significant variance — including variances driven by the program's own risk, issue, or opportunity activity.
- **Giver-receiver relationships**: dependencies are framed as giver/receiver pairs with documented deliverables tracked in the IMS, and the provider agrees to give the dependent program early warning.

## Mental Models
- **Risk and opportunity are two pumps on the same baseline**: risk management pushes the baseline back up when threats erode it; opportunity management pulls it down toward should-cost. Run only the risk pump and you defend will-cost but never reach should-cost.
- **Effort buys likelihood (the inverted lever)**: for a risk you spend resources to *lower* likelihood of a bad event; for an opportunity you spend resources to *raise* likelihood of a good one. Same lever, opposite direction — which is why the pursue decision is fundamentally a return-on-investment question.
- **The opportunity register is a portfolio, not a list**: opportunities carry priority numbers and strategies so the program ranks them and decides where scarce resources earn the most should-cost return — the register exists to be triaged at PMRs, not merely logged.
- **Deeper analysis can flip the sign of a business case**: a candidate that looks like a net loss on first pass can become a large net win once second-order effects (reliability, spares, maintenance, life-cycle cost) are modeled — so the first-order number is a screen, not a verdict.
- **Interfaces are owned by no one and therefore everyone**: the seam between two programs has no single program manager by default, so the model assigns an explicit technical authority and binds the parties with MOAs — otherwise the risk falls through the gap between portfolios.
- **Tripwires make a program's internal RIO activity an external obligation**: because one program's risk/issue/opportunity decisions can ripple into dependent programs, the tripwire converts an internal management action into a mandatory notification to partners.
- **Elevate early, never let it languish**: cross-program risks ride a time-phased escalation ladder (PM → PEO → Service Acquisition Executive → Defense Acquisition Executive) and should be raised to the right level as early as possible to align priorities and resources.

## Anti-patterns
- **Short-term gain, long-term loss masquerading as an opportunity**: the Guide explicitly warns that improvements yielding near-term benefit but long-term negative consequences are usually neither opportunities nor appropriate should-cost initiatives.
- **Letting cross-program risks and issues languish**: the Guide names this directly — interdependency risks and issues must be elevated progressively and early, not allowed to sit unaddressed at a low level.

## Key Takeaways
1. **Opportunity management is the proactive twin of risk management** — it spends resources to capture future cost/schedule/performance benefits and is the mechanism for reaching should-cost, not just staying within will-cost.
2. The **six-activity opportunity loop** (plan → identify → analyze → decide → monitor → feedback) mirrors the risk process and can live inside the **PRMP**.
3. Approved opportunities get a **business-case analysis**, an owner, an entry in the **opportunity register**, and one of four options — **pursue / defer / reevaluate / reject** — chosen on a benefit-versus-risk basis; pursued ones go into the **IMS** and their residual risks into the risk register.
4. The existing **RMB** normally governs opportunities (a separate Opportunity Management Board is optional); **small, low-disruption wins aggregate** and should be incentivized for both Government and contractor.
5. **Interfaces between interdependent programs are a primary risk source** — new development hosting other programs' products is where technical, programmatic, and business risk concentrates.
6. Cross-program risk is contained with a **designated technical authority**, **MOAs carrying cost/schedule/performance tripwires**, an **ICWG**, **ICDs/IRSs**, **synchronized schedules**, an **integration plan**, and giver-receiver deliverables tracked in the IMS — bound to the **SEP** and **Acquisition Strategy**.
7. **Escalate cross-program risks early** up the PM → PEO → SAE → DAE chain; refer requirements disputes to the **CSB**.

## Connects To
- **ch on Risk Management (this pack)**: opportunity uses the same board, register concept, and process shape as risk; tripwires link the two when an opportunity decision ripples to dependent programs.
- **ch on Issue Management (this pack)**: opportunities can offset cost/schedule impacts from realized risks (issues), so opportunity management is a relief valve for issue burn-down.
- **`dau-se-guidebook` pack**: the broader SE-process frame for RIO, Interface Management, Configuration Management, and the SEP — this chapter supplies the defense-acquisition program-execution detail beneath that frame.
- **`nasa-risk` pack**: NASA's CRM/RIDM risk model — complementary risk theory; this chapter is the DoD-side program-mechanics counterpart (registers, boards, MOAs, AAF-era artifacts).
- **`dod-mosa` pack**: the modular open systems approach is named here as a direct *source* of cost-reduction opportunities (sparing, competition for modifications, technical-data-package rights).
- **Acquisition Strategy / SEP**: the binding documents for required MOAs, SWAP-C allocations, synchronization schedules, and interface control across the family of systems / system of systems.
