---
name: sd-22-dmsms
description: "Knowledge base from the SD-22 DMSMS Guidebook (DSPO, FY24 working draft). Use for managing Diminished Manufacturing Sources and Material Shortages (DMSMS) and obsolescence across a long-lived system's life cycle: the five-step process (Prepare, Identify, Assess, Analyze, Implement) plus the Strategize overlay; standing up a DMSMS Management Team (DMT) and Management Plan (DMP); risk-based monitoring and surveillance (the risk cube, predictive tools, vendor surveys, GIDEP/DLA PDNs, critical-materials analysis); health assessments and resolution timing; costing and selecting resolutions (life-of-need buys, substitutes, redesign, technology refreshment) by AoA/BCA; and budgeting/executing resolutions through modification funding and the ECP process. Defense-sustainment / DoD-acquisition framing throughout. Does NOT teach general systems engineering, parts-management standards, or contracting law in depth, and does not reproduce DoD policy text or the source's tables and figures."
---

<!-- argument-hint: [DMSMS step, DMT/DMP, monitoring/risk cube, predictive tools/PDN, health assessment, resolution option/LON buy, obsolescence cause, chapter number] -->

# SD-22 DMSMS Guidebook
**Source**: DSPO (Defense Standardization Program Office), US Government work, public domain | **Chapters**: 8

## When to use
Use this skill to manage obsolescence and supply loss on a system that must stay supportable for decades while the technology inside it ages in years. It covers the full SD-22 discipline: setting up a DMSMS program, deciding what to watch, judging when an obsolescence issue actually threatens cost/schedule/readiness, choosing the cheapest durable resolution, and funding and fielding it. This is the sustainment-engineering complement to the broader life-cycle SE packs (`dau-se-guidebook`, `nasa-npr-7123`) and to system security engineering (`nist-sse`), into which DMSMS plugs at the resolution-decision point.

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill
- **Without arguments** — load the core frameworks below: the five-step process, the DMT/DMP infrastructure, the risk-based monitoring model, and the cost-and-risk resolution logic.
- **With a topic** — ask about a step (Prepare/Identify/Assess/Analyze/Implement), a monitoring concept (risk cube, predictive tools, PDN, vendor survey, critical materials), a resolution option (life-of-need buy, substitute, redesign, technology refreshment), or an artifact (DMT, DMP, health assessment, ARCI chart).
- **With a chapter** — `ch03` (Prepare/DMT/DMP), `ch04` (Identify/monitoring), `ch05` (Assess/health assessment), `ch06` (Analyze/resolution selection), `ch07` (Implement/funding).

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

> **One discipline, two words.** SD-22 uses *DMSMS* and *obsolescence* almost interchangeably and runs both with the same process — but they are not synonyms. Obsolescence is a situation-dependent *state*; a DMSMS issue is the *event* of supply failing to meet demand. Most DMSMS problems arise from obsolescence, but not all (a current item can still hit a supplier loss), and not all obsolescence is a DMSMS problem (an obsolete item with adequate stock is fine).

## Core Frameworks & Mental Models

### What DMSMS is, and why it is inevitable

DMSMS — **Diminished Manufacturing Sources and Material Shortages** — is the loss, or coming loss, of the manufacturers and suppliers of the items, raw materials, and software a system depends on. Because technology life cycles are short while defense systems are long-lived, these losses are not anomalies to eliminate but an inevitability to manage. SD-22 frames DMSMS management as **risk-based, multidisciplinary, and life-cycle-long**: proactive management is the cheapest way to blunt the cost, schedule, performance, and readiness impacts of obsolescence. Every system is susceptible — across all domains, all levels of assembly, and all item types, including software and **MaSME** (materials and structural, mechanical, electrical) items, not just electronics.

**Two mechanisms.** *First-order* obsolescence is driven directly by market forces or regulation (loss of the ability to buy, license, or support an item). *Lower-order (derived)* obsolescence is *functional* obsolescence your own change created. They apply symmetrically and simultaneously to hardware and software.

### The Five-Step Process (+ Strategize)

The spine of the guidebook. Run it as a continuous cadence, not a one-pass project:

1. **Prepare** — stand up the infrastructure: leadership foundations, a chartered DMT, an approved DMP, and the operational processes.
2. **Identify** — monitoring and surveillance: turn bills of materials into a list of immediate, near-term, and forecast obsolescence issues.
3. **Assess** — weigh an issue's cost/schedule/availability/readiness effect to decide *whether*, *when*, and *at what level* to resolve.
4. **Analyze** — enumerate viable resolution options, cost each, and pick the best risk-adjusted return.
5. **Implement** — program/budget the resolution, integrate it with modification funding, and execute it.

**Strategize** is the continuous sixth activity wrapping all five (modification planning + using evaluation results to improve the program). Steps are tailorable and enterable at any point — but starting early widens every later option.

### Prepare — the program engine

- **DMT** (DMSMS Management Team): chartered by the PM/PSM, multidisciplinary (DMT lead, program office, DMSMS SME, engineering, **System Security Engineer**, logistics/PSM, sustainment, software SME, plus ad-hoc). Roles assigned via an **ARCI chart** — Accountable/Responsible/Consulted/Informed/Not-Informed, with exactly one Accountable per decision per level. The PM is ultimately accountable.
- **DMP** (DMSMS Management Plan): mandatory under DoDI 4245.15, developed by the DMT, approved by the PM. Living, tailored, a reference not a tutorial; aligned to the Appendix D four-level **process-capability matrix**.
- **Operations funding ≠ resolution funding.** Budget operations without fiscal constraint first, then accept and document risk if funding falls short. Expect a **start-up spike** over steady-state effort.
- Run everything inside a **QMS** (quality plan, compliance metrics, Lean Six Sigma / DMAIC). Track cases **Open → Closed → Watch List** — stopping at funding rather than fielding is a bad practice.
- **The BOM is the keystone** — without knowing what is on the system, even reactive management is crippled.

### Identify — risk-based monitoring

Monitoring everything is prohibitively expensive, so Identify is governed by a risk-based scoping decision:

- **Two filters**: screen *subsystems* first (safety, mission criticality, cost history, problem areas, life-cycle phase, sustainment strategy, data availability, supply-chain vulnerability), then *items* within them. Sort items into **definitely-monitor / do-not-monitor / uncategorized**.
- **The risk cube**: score uncategorized items on **item criticality × supply-chain vulnerability × time to resolve**; proactively monitor only items high on all three axes.
- **Four availability methods**: predictive tools, vendor surveys, critical-materials analysis, and product discontinuance notices (**PDNs** — pull GIDEP + DLA + tool alerts, since each carries unique data, and always validate before acting).
- Predictive tools are imperfect: they recognize only ~71-72% of items and disagree on status, so use more than one and **manually confirm**; never read "unknown availability" as "available."
- **Indentured BOMs beat flat ones** — seeing obsolescence in the assembly hierarchy reveals when one redesign beats several life-of-need buys.

### Assess — is it an issue, and when does it bite?

"Obsolete" is an input; "issue worth resolving" is a conclusion. Assess answers three questions — **need, timing, level** — by weighing **cost, schedule, availability, readiness** against four data families (programmatic, availability, criticality, logistics):

- A resolution may be **unneeded** (no demand, enough stock to retirement/refresh, reclamation covers it, or the design phase) — but software-license and information-assurance lapses flip the default toward acting immediately.
- A **health assessment** (by-year balances per item) plus the **Appendix K** method translate component-level stock into a *system-level* timeline of when the issue actually bites. **Days of supply is the clock.**
- A **four-step prioritization** ranks competing problems; **five factors** plus cost arithmetic decide the level of resolution (fix the item vs. redesign the next-higher assembly).

### Analyze — cost it, compare on cost, adjust for risk

- Build a resolution's **total cost = sum of applicable cost elements** (~20 categories); add counterfeit-testing cost when buying outside authorized sources.
- Walk the **three resolution categories** top-to-bottom — existing material (logistics) → substitutes (engineering) → redesign (engineering) — keeping only options that meet *all* requirements and second-order effects.
- Because every viable option buys the same outcome (sustained availability), compare on **net present value** via **BCA** (formal) or **AoA** (light). Then weight technical/supply-chain/financial/schedule risk, discard dominated options, and sometimes pay more to buy down risk.
- **Roadmaps and health assessments set timing** — fold fixes into a planned technology refresh/insertion; check whether an external organization is already resolving it; let a resolution **trigger a System Security Engineering re-look** (assurance, SCRM, program protection, cybersecurity), coordinated with SSE SMEs, not the PPP alone.

### Implement — fund and field it

- Three processes: **program/budget → integrate with modification funding → execute**. Plan funding **in advance** (DMSMS recurs yearly); execution-year reliance is not a best practice.
- Leverage funded modifications three ways: size **life-of-need (LON) buys** against modification plans, account for modifications to avoid duplication, and rescope/slow a modification (with financial-authority approval) to absorb execution-year surprises.
- Execute through the standard **ECP / configuration-change** process with active DMT involvement; a senior **champion** is critical. Size LON buys to a known **end-of-need** with conservative assumptions and a safety level — under-buying almost always costs far more than excess. LON statutes: **31 U.S.C. 1502(a)** and **10 U.S.C. 2213**, with bona-fide-need and written-determination exception paths.

### How it connects to policy and the wider life cycle

DMSMS management is mandatory and layered — high-level supply-chain/product-support policy (DoDI 4140.01, DoDI 5000.91/.85/.88) plus a stand-alone instruction and manual (DoDI/DoDM 4245.15, Nov 2020). It is embedded in existing artifacts and reviews (the SEP, the SETR sequence, the LCSP's obsolescence-risk section, ILAs, and the statutory Sustainment Review under 10 U.S.C. 4323), and tailored across five of the six Adaptive Acquisition Framework pathways (all but Acquisition of Services), with MCA as the baseline.

---

## Chapter Index

| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-sd-22-dmsms-introduction-fundamentals.md) | Introduction & Fundamentals | What DMSMS is; first-order vs. lower-order mechanisms; hardware/software/MaSME symmetry; the five-step process + Strategize; why proactive management pays |
| [ch02](chapters/ch02-sd-22-dmsms-policy-lifecycle-guidance.md) | Policy & Life-Cycle Guidance | The DoD policy stack (DoDI 4140.01 / 5000.x / 4245.15); SE & sustainment artifacts (SEP, SETR, LCSP, ILA, Sustainment Review); tailoring across the six acquisition pathways |
| [ch03](chapters/ch03-sd-22-dmsms-prepare-program-infrastructure.md) | Prepare: Program Infrastructure | Foundations; the DMT and ARCI chart; the DMP and capability matrix; operations funding; resilient-design advocacy; record keeping; QMS; case tracking; supporting contracts |
| [ch04](chapters/ch04-sd-22-dmsms-identify-monitoring-surveillance.md) | Identify: Monitoring & Surveillance | The six Identify processes; two prioritization filters; the risk cube; predictive tools, vendor surveys, critical-materials analysis, PDNs (GIDEP/DLA); software monitoring; roadmap forecasting |
| [ch05](chapters/ch05-sd-22-dmsms-assess-resolution-need-timing-level.md) | Assess: Need, Timing & Level | The three Assess questions; four data families; the four "may-not-need" situations; the health assessment and Appendix K; four-step prioritization; five level-of-resolution factors |
| [ch06](chapters/ch06-sd-22-dmsms-analyze-resolution-determination.md) | Analyze: Resolution Determination | Cost elements and total cost; three resolution categories; AoA vs. BCA on NPV; risk weighting and dominated options; roadmaps and refresh timing; the SSE re-look; cost avoidance |
| [ch07](chapters/ch07-sd-22-dmsms-implement-resolutions.md) | Implement: Resolutions | Program/budget, integrate with modification funding, execute; the three modification budgeting best practices; LON-buy sizing and statutes; the ECP process; the champion |
| [ch08](chapters/ch08-sd-22-dmsms-obsolescence-relationship.md) | Obsolescence & its Relationship to DMSMS | The five obsolescence causes (technology/function/regulation/supportability/market demand); planned vs. unplanned; why obsolescence and DMSMS overlap but are not identical |

## Topic Index

- **Analysis of Alternatives / Business Case Analysis (AoA / BCA)** → ch06
- **ARCI chart / accountability** → ch03
- **Assess step (need, timing, level)** → ch05
- **Availability methods (the four)** → ch04
- **Bill of materials (BOM) / indentured BOM** → ch04, ch03
- **Bona fide need statement** → ch07
- **Case monitoring and tracking** → ch03
- **Champion (implementation)** → ch07
- **Cost avoidance** → ch06
- **Cost elements (resolution)** → ch06
- **Critical materials analysis** → ch04
- **DMSMS Management Plan (DMP)** → ch03
- **DMSMS Management Team (DMT)** → ch03
- **DMSMS mechanisms (first-order / lower-order)** → ch01
- **Five-step process (Prepare/Identify/Assess/Analyze/Implement)** → ch01
- **Functional obsolescence** → ch08, ch01
- **GIDEP / DLA discontinuance sources** → ch04
- **Health assessment** → ch05
- **Identify step (monitoring and surveillance)** → ch04
- **Implement step (program, budget, execute)** → ch07
- **Level of resolution** → ch05, ch06
- **Life-of-need (LON) buy** → ch07, ch03
- **MaSME items** → ch01, ch03
- **Modification funding (integrating resolutions)** → ch07
- **Obsolescence causes (technology, function, regulation, supportability, market)** → ch08
- **Obsolescence vs. DMSMS relationship** → ch08
- **Policy stack (DoDI 4140.01 / 5000.x / 4245.15)** → ch02
- **Predictive tools** → ch04
- **Prepare step (program infrastructure)** → ch03
- **Process capability matrix** → ch03
- **Product Discontinuance Notice (PDN)** → ch04
- **Quality Management System (QMS) / DMAIC** → ch03
- **Resolution categories (existing material / substitute / redesign)** → ch06
- **Risk cube (criticality, supply chain, time to resolve)** → ch04
- **Roadmaps and forecasting** → ch04, ch06
- **Strategize overlay** → ch01
- **Supportability (obsolescence cause)** → ch08
- **Sustainment Review (10 U.S.C. 4323)** → ch02
- **System Security Engineering (SSE) re-look** → ch06
- **Tailoring across acquisition pathways** → ch02
- **Technology refreshment** → ch06, ch01
- **Vendor surveys** → ch04
- **Watch list (case status)** → ch03
- **Window of opportunity** → ch04, ch03

## Supporting Files

- [glossary.md](glossary.md) — key DMSMS and obsolescence terms, alphabetical, with chapter references
- [patterns.md](patterns.md) — reusable patterns (running the five steps, setting foundations first, two-filter prioritization, four-source availability, the assess gate, costing-then-risk, security+funding with the resolution) with When/How/Trade-offs
- [cheatsheet.md](cheatsheet.md) — quick decision rules, the five-step table, per-step essentials, the five obsolescence causes, tells & smells

---

## Scope & Limits

**Covers**: DMSMS and obsolescence management for long-lived (chiefly DoD) systems per the SD-22 Guidebook — the five-step process and Strategize overlay; the DMSMS program infrastructure (DMT, DMP, ARCI, QMS, case tracking, supporting contracts); risk-based monitoring and surveillance (two filters, the risk cube, predictive tools, vendor surveys, critical-materials analysis, GIDEP/DLA PDNs, software monitoring, roadmap forecasting); assessment of resolution need/timing/level (health assessments, days-of-supply, prioritization); resolution determination (cost elements, three categories, AoA/BCA, risk weighting, the SSE re-look, cost avoidance); and implementation (programming/budgeting, modification funding, life-of-need buys, the ECP process, statutory LON limits). The policy and life-cycle scaffolding (DoD issuances, SE/sustainment artifacts, acquisition-pathway tailoring) is summarized, not reproduced.

**Does not cover in depth**: general systems-engineering process and architecture (see `dau-se-guidebook`, `nasa-npr-7123`, `sebok`); parts-management standards such as SD-19 / MIL-STD-11991B (named, not taught); the full text of DoD policy issuances, appropriations law, or contracting regulation (cited as constraints only); detailed system-security-engineering method (see `nist-sse`); counterfeit-avoidance standards (named — the SAE AS55xx/AS61xx family — not reproduced); and the source's own tables, figures, and appendix worksheets (referenced by name and synthesized, never reproduced).

**Source version**: SD-22 DMSMS Guidebook, **FY24 Working Draft (April 2024)**, published by DSPO and obtained via ASSIST (assist.dla.mil). As a *working draft*, section/figure/table numbers and some guidance may shift in the final FY24 release; this pack synthesizes the draft's stable content and names artifacts so they remain locatable across revisions. The guidance is DoD-internal sustainment doctrine; non-DoD readers should treat the process model as transferable but the policy citations as DoD-specific.

**Jurisdiction**: US Government work — public domain (Distribution A, approved for public release; distribution unlimited). Free to reproduce, transform, and redistribute, including commercially.
