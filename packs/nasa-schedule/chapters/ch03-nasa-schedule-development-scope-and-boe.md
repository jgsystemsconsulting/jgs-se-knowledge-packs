# Chapter — Schedule Development I: Scope, WBS/IMP/OBS/CBS, and Basis of Estimate

> Source basis: NASA Schedule Management Handbook (2024 edition), Chapter 5 "Schedule Development," Sections 5.1–5.4. This chapter is grounded in that edition; the superseded 2010 SP-2010-3403 should not be used as the reference.

## Core Idea

Before any network of activities can be laid down, the scheduler must first know — completely and unambiguously — what work the program or project (abbreviated P/p in the handbook) has been authorized to do. Schedule Development therefore opens not with dates but with scope. The handbook frames the whole effort as the act of defining, building, and deploying a scheduling capability whose end product is a Schedule Database, held inside a scheduling tool, from which an Integrated Master Schedule (IMS) and the other schedule outputs can be generated. That capability is meant to feed the downstream Schedule Management sub-functions (the reporting, assessment, and analysis covered in the handbook's later chapters), and the sub-function does not finish until the IMS exists and can be baselined.

Two ideas anchor the chapter. First, the four breakdown structures answer four complementary questions about scope: the Work Breakdown Structure (WBS) is the "what," the Organizational Breakdown Structure (OBS) is the "who," the Cost Breakdown Structure (CBS) is the "how much," and the IMS itself is the "when." A schedule is credible only when all four are consistent and traceable to one another. Second, the rationale behind every scheduling decision must be written down as it is made, in a Schedule Basis of Estimate (BoE) — the documented ground rules, assumptions, and drivers that would let an independent reader reconstruct the IMS and judge whether it can be trusted.

The whole effort is governed by the Schedule Management Plan (SMP); the Schedule Development Plan is the first of the SMP's four sub-plans and specifies which tools and techniques suit the type and level of scheduling the P/p actually needs.

## Frameworks Introduced (exact source names, when/how)

- **Schedule Management Plan (SMP) and the Schedule Development Plan.** The handbook treats Schedule Development as work performed in accordance with the SMP. The Schedule Development Plan — named as the first of four SMP sub-plans — defines the tools and techniques matched to the P/p's scheduling needs and sets the requirements, approach, and timeline for building the IMS. It is named as a prerequisite that must be available before development begins.

- **Work Breakdown Structure (WBS) and WBS Dictionary.** Introduced in Section 5.3.1 as the "what" of P/p scope: a product-oriented, hierarchical decomposition of hardware, software, services, facilities, and other activities making up the total scope. The accompanying WBS Dictionary is a narrative definition of each WBS element in product-oriented terms, tying each element to the progressively higher levels above it. The handbook directs the reader to NPR 7120.5 (space flight programs) and NPR 7120.8 (research and technology, "R&T," programs) for the standard level-two templates, and to the NASA WBS Handbook for tailorable examples.

- **Integrated Master Plan (IMP).** Introduced in Section 5.3.2. The handbook is explicit that the IMP is not a NASA-required product and is usually contractor-developed, but a contractor may pair it with the WBS to help build the IMS. It is an event-based, top-level plan: a hierarchy in which each key P/p event decomposes into accomplishments, and each accomplishment into criteria. Events carry no calendar dates — an event is complete only when its accomplishments are done and their supporting criteria are satisfied.

- **Organizational Breakdown Structure (OBS).** Introduced in Section 5.3.3 as the "who": the hierarchical division of the organization showing who performs the work, valid whether the organization is functional, organized into Integrated Product Teams (IPT), or matrixed.

- **Responsibility Assignment Matrix (RAM).** Introduced alongside the OBS: combining the WBS and OBS produces a RAM that names the responsible organization for each scheduled task, and is typically used to identify control accounts for earned value purposes.

- **Cost Breakdown Structure (CBS), also called Resource Breakdown Structure (RBS).** Introduced in Section 5.3.4 as the "how much": the hierarchical structure that sorts resources into control accounts — at the top level, labor, travel, materials, equipment, and other direct and indirect costs.

- **Control Account and Control Account Manager (CAM).** Defined within Section 5.3.4. A control account sits at the intersection of one WBS element and one responsible organization on the RAM; it is the natural point where budgets and actual costs accumulate and are compared to earned value. The CAM is the person accountable for that account and is usually responsible for creating, statusing, and maintaining its schedule activities.

- **Integrated Master Schedule (IMS).** Introduced in Section 5.3.5 as the "when": the time-phased plan for executing the total approved scope, containing tasks, milestones, and logically sequenced interdependencies that model the implementation plan from start to completion, detailed enough to expose the longest path through the entire P/p.

- **Schedule Basis of Estimate (BoE).** Introduced in Section 5.4. Using the NPR 7120.5 definition, a BoE documents the ground rules, assumptions, and drivers behind the cost and schedule estimate, including model inputs and the rationale for analogies. The handbook describes the Schedule BoE as a "dossier" — a structured collection of technical and programmatic information sufficient to develop, assess, and in principle reproduce the IMS — and deliberately gives no fixed template or format.

- **Performance Measurement Baseline (PMB), Management Reserve (MR), and Unallocated Future Expense (UFE).** Named in Section 5.3.4 as the cost-side constructs the schedule must stay aligned with: the PMB is the time-phased cost plan for all authorized work; MR and UFE are amounts deliberately held outside the baseline (no scope is assigned to MR).

## Key Concepts

**Scope first, schedule second.** The opening move of building a new IMS is to understand the complete work content — through the WBS, OBS, the funding dynamics and CBS, and the governing agreements and authorization documents. The handbook is firm that a valid schedule cannot be built until the work content is clearly understood, and that scope may have to be assembled from many documents: the P/p Plan, acquisition and verification plans, the Request for Proposal, the Statement of Work and contracts, and external or international agreements such as MOUs and MOAs.

**The WBS is the spine of traceability.** Work that has not been approved into the WBS or WBS Dictionary by P/p management should not appear in the IMS. Conversely, the schedule's structure should track the approved WBS closely, accomplished by carrying the correct WBS code on every applicable schedule task — hardware, software, test facilities, subcontracts, international contributions, and support systems. Task definition begins from the product-oriented WBS and is extended down to discrete, measurable tasks. The handbook notes a practical limit: the Agency Core Financial System captures actual costs only to seven WBS levels, but a P/p's technical and schedule WBS may go lower to preserve management insight.

**IMP-to-IMS relationship.** Where an IMP exists, it is the relatively top-level, event-and-accomplishment view, while the IMS shows the detailed, time-based network of activities that accomplishes the IMP's content. Each IMP outline code should trace cleanly up to the WBS and down into the IMS, and individual tasks should carry an IMP assignment wherever one applies. Both the IMP and IMS underpin an Earned Value Management System (EVMS) and both serve proposal preparation, source selection, and execution.

**The control account is where scope, organization, and cost meet.** Because a control account binds one WBS element to one responsible organization, establishing control accounts prevents duplicated responsibility and lays the foundation for integrating scope, schedule, budget, work authorization, and cost accumulation under the EVMS. For NASA P/ps the WBS is typically the primary source for the CBS, with each control account aligned to a work package or detailed task.

**Cost loading and the integration problem.** A resource- or cost-loaded schedule yields a time-phased spending estimate that can be checked against funding availability over time. Because the cost-estimating tool and the IMS often differ in WBS depth at lower levels, the cost estimate may need to be rolled up or otherwise reconciled so the levels line up across both tools; whenever the WBS itself is revised, that revision has to be coordinated with the P/p so the estimate is not misread or miscommunicated. The CBS should trace to the P/p budget, and the baseline IMS should agree with all segments of the integrated cost and schedule baseline.

**Funding versus budget.** The handbook draws a sharp line: NASA funding is incremental — almost always authorized fiscal year by fiscal year — and is the money authorized for expenditure in that year; the P/p budget plan is the value assigned to the time-phased resources needed to do the scheduled work. The scheduler must phase the work so that estimated cost plus Management Reserve never exceeds the authorized budget plan in any fiscal year. When funding phasing constrains the work, the P/p must replan or, if severely limited, descope.

**The BoE matures with the program.** Under NPR 7120.5 the BoE is a documented, retrievable record, and its required maturity is keyed to life cycle reviews. The general pattern in the handbook: for Uncoupled and Loosely-Coupled Programs, a preliminary BoE at SRR, baseline at SDR, updates thereafter; for Tightly-Coupled Programs, preliminary BoEs at SRR and SDR, baseline at PDR, updates thereafter; for projects, preliminary BoEs at MCR, SRR, and SRR/MDR, baseline at PDR, with updates tied to schedule maturity at each review. For a project, the Phase E/F portion of the BoE first comes due at SIR, not before. R&T P/ps under NPR 7120.8 carry no explicit BoE requirement, yet a BoE is still expected at a maturity that tracks the IMS — and in practice any R&T effort whose outcome bears directly on a space-flight mission's success or its schedule is run under NPR 7120.5 regardless.

**Early estimating relies on analogy.** Early in Formulation — Pre-Phase A and Phase A — the P/p often leans on historical data and analogies drawn from tools and databases the handbook names: SMART, the Schedule Repository, CADRe, and NICM. By PDR, when the schedule is detailed enough to define all the work, the BoE should capture the rationale for selected durations, the duration uncertainties, and the activity attributes (owners; workflow logic; WBS/OBS/CBS and work-package identifiers; shifts; and assumptions or constraints).

**Source documents for the BoE.** The handbook lists the typical products the scheduler should know intimately before starting: P/p Plans; agreements and authorization documents (including Formulation Agreement and Decision Memorandums); the scope-definition set (WBS and WBS Dictionary, IMP if available, OBS, CBS); cost estimates and BoEs (PPBE data, the RFP or contract, Task Agreements, Data Requirements Documents, Bill of Materials, Core Financial reports); and risk information (the Risk Management Plan, risk statements, the risk matrix with likelihood and consequence distributions, and risk impact and mitigation descriptions).

## Mental Models

- **Four questions, one schedule.** Treat WBS / OBS / CBS / IMS as the "what / who / how much / when" of the same scope. A claim made in any one of them should be answerable, consistently, in the other three. When the four disagree, the schedule is not yet credible.

- **The grid: where the WBS meets the OBS.** Picture the WBS as columns and the OBS as rows; each filled cell where one product element crosses one responsible organization is a control account — the cost-and-schedule accounting atom of the program, owned by a single CAM.

- **Events ripen, they don't arrive.** In the IMP an event has no date; it ripens. It is "done" the moment its accomplishments are complete and their criteria are met — a maturity gate, not a calendar tick. The IMS is then the dated machinery that makes those events ripen on time.

- **The BoE as reproducibility ledger.** Imagine handing the IMS to an independent assessor with no other context. If the BoE is complete, that assessor can trace every duration, assumption, and constraint back to a primary source and rebuild the schedule. If they cannot, the BoE is incomplete — and the schedule's reliability is unproven.

- **Funding is a per-year ceiling, not a pool.** Because NASA money is authorized fiscal year by fiscal year, the planned spend (cost plus Management Reserve) is a wall the time-phased work cannot push through in any single year — phasing, not just totals, has to fit.

## Anti-patterns

The source frames these as cautions and prohibitions rather than a labeled "anti-pattern" list, but it states each one explicitly:

- **Scheduling unapproved work.** If work is not in the management-approved WBS or WBS Dictionary, it must not be placed in the IMS. (Section 5.3.1)

- **Committing beyond authorized funding.** The handbook flags as a "Caution" that P/p commitments must never exceed the authorized funding for a fiscal year, and that estimated cost with Management Reserve must not exceed the authorized budget plan in any fiscal year. (Section 5.3.4)

- **Misusing Management Reserve.** MR carries no scope and should not be used to cover past performance variances — it is reserved for in-scope budgeting, replanning on improved knowledge, and known/unknown risk realization. (Section 5.3.4)

- **Leaning on analogies that don't apply.** For new technologies where genuinely analogous historical data does not exist, the handbook warns against treating a weak analogy as sound; the scheduler should instead increase the uncertainty (and possibly the point estimate), document the reasoning in the BoE and IMS, and ensure adequate float and margin. (Section 5.4.1)

- **Letting scope interpretations diverge silently.** The handbook cautions that P/p personnel may not share the same reading of approved scope; leaving those differences unresolved yields an inaccurate schedule. The scheduler is expected to surface the conflicts — by asking which WBS element work belongs in, what deliverables and testing are required — so responsible managers can reconcile them. (Section 5.4.2)

## Key Takeaways

- Schedule Development is governed by the SMP and its Schedule Development Plan; its end product is a baselined IMS generated from a Schedule Database.
- Scope must be fully understood before a valid schedule exists, and the WBS (with its Dictionary) is the product-oriented backbone that every IMS task must trace to via WBS codes.
- The four breakdown structures map to four questions — WBS = what, OBS = who, CBS/RBS = how much, IMS = when — and must remain mutually consistent and traceable.
- The control account, set at the WBS-by-OBS intersection on the RAM and owned by a CAM, is the integration point for scope, schedule, budget, and cost under an EVMS.
- The IMP, when present, is an event/accomplishment/criteria plan whose events ripen on maturity rather than dates; it is contractor-oriented and not a NASA-required product.
- Funding (incremental, per fiscal year) and budget (time-phased resource value) are distinct; the schedule must phase work so cost plus MR never breaches the authorized annual budget, replanning or descoping otherwise.
- The Schedule BoE is the documented ground rules, assumptions, and drivers — a reproducibility dossier with no fixed template — whose required maturity is keyed to life cycle reviews under NPR 7120.5 and developed in conjunction with the IMS.

## Connects To

- **NASA NPR 7120.5 and NPR 7120.8** — the authority for WBS level-two templates, the BoE-maturity requirements by life cycle review, and the distinction in how space flight versus R&T P/ps are managed.
- **NASA WBS Handbook** — tailorable, product-oriented WBS examples referenced as the source for building project WBSs.
- **NASA Cost Estimating Handbook** — referenced for CBS detail (Appendix B) and for the JCL and UFE treatment used when probabilistic techniques set future expense.
- **Earned Value Management System (EVMS)** — the control-account, RAM, and PMB constructs in this chapter are the scheduling-side foundation for EVM, linking to NASA EVM implementation guidance and the IPMR/CPR reporting formats.
- **Later Schedule Management chapters** — this chapter (5.1–5.4) sets up the IMS construction detail in Section 5.5/5.6, the Schedule Assessment activities (Requirements Check, Basis Check) that consume the BoE, the SRA/ICSRA analysis schedule, and the change-control process that keeps the BoE current.
- **Schedule Management Plan (SMP)** — the upstream governing artifact whose Schedule Development Plan sub-plan scopes the tools, approach, and timeline for everything in this chapter.
