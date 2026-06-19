---
name: nasa-risk
description: "Knowledge base from NASA Risk Management Handbook (NASA/SP-2011-3422). Use for risk-informed decision making, continuous risk management, performance commitments, risk scenario diagrams, risk disposition types, risk burn-down schedules, objectives hierarchies, deliberation and alternative selection, risk driver identification, and RM planning for space and safety-critical programmes. Does not cover domain-specific PRA methods (fault trees, event trees) in procedural depth — see NASA PRA Procedures Guide for those."
---

<!-- argument-hint: [topic, process, or chapter number] -->

# NASA Risk Management Handbook (NASA/SP-2011-3422)
**Source**: NASA (US Government work, public domain) | **Chapters**: 10

## When to use
Use this skill when designing or evaluating a risk management process for a programme, project, or system with defined performance requirements across safety, technical, cost, and schedule domains. It is the authoritative NASA reference for both pre-decision risk-informed alternative selection (RIDM) and post-decision implementation risk management (CRM). Also use when writing or reviewing Risk Management Plans, Technical Basis for Deliberation documents, Risk-Informed Selection Reports, or any artefact that must comply with NPR 8000.4A.

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill
- **Without arguments** — load the core frameworks below.
- **With a topic** — ask about risk tolerances, performance commitments, risk scenario diagrams, CRM Plan step, burn-down schedules, individual risk statements, or any other topic; I read the relevant chapter.
- **With a chapter** — ask for `ch05` (RIDM Part 3) or `ch07` (CRM Identify and Analyze).

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

## Core Frameworks & Mental Models

### The Integrated RM Framework: RIDM + CRM

NASA Risk Management = RIDM + CRM operating together within every organisational unit throughout the full programme/project life cycle.

**RIDM** (Risk-Informed Decision Making) answers: *Which alternative should we implement?*
- Part 1: Identify alternatives (objectives hierarchy → performance measures → feasible alternatives)
- Part 2: Risk analysis (multidisciplinary probabilistic analysis → Technical Basis for Deliberation)
- Part 3: Risk-informed selection (performance commitments → deliberation → Risk-Informed Selection Report)

**CRM** (Continuous Risk Management) answers: *How do we manage risk during implementation?*
- Six steps: Identify → Analyze → Plan → Track → Control → Communicate & Document
- Seeded by RIDM's risk analysis of the selected alternative
- Feeds back into RIDM when conditions require requirements rebaselining

### The Four Mission Execution Domains
Every performance shortfall maps to one or more of: **Safety, Technical, Cost, Schedule**.

### RIDM: Performance Commitments
A performance commitment is a performance measure value at a defined risk tolerance percentile, so that the probability of failure to meet the commitment is equal across all alternatives. This enables *risk-normalised comparison* — comparing what each alternative can achieve at equal probability of success.

**Setting commitments:**
1. Set risk tolerances for each performance measure (before seeing results)
2. Order performance measures from lowest to highest risk tolerance
3. Sequentially condition commitments on prior measures being met
4. The resulting commitment chart is the primary input to deliberation

### CRM: Individual Risk Statement Format
```
Given that [CONDITION: current fact-based situation],
there is a possibility of [DEPARTURE: future change from baseline]
adversely impacting [ASSET: affected portfolio element],
thereby leading to [CONSEQUENCE: inability to meet performance requirement].
```
CONSEQUENCE must be written without regard to potential mitigations.

### CRM: Six Risk Disposition Types
- **Accept**: Performance risks all within tolerance; document assumptions
- **Mitigate**: Positive action — departure prevention or consequence reduction
- **Watch**: Monitoring plan for risk driver observables; no baseline change
- **Research**: Investigation plan to reduce epistemic uncertainty about a driver
- **Elevate**: Transfer management to next higher level; last resort
- **Close**: Risk drivers no longer significant; bookkeeping removal

### CRM: Burn-Down Schedule
The risk tolerance profile over time. Tolerable → Marginal → Intolerable zones defined at each milestone. If performance risk exceeds Marginal, the Plan step is triggered. The schedule must reflect the actual project plan's nominal success path.

### The Graded Approach
Calibrate analysis depth to decision stakes. Apply bounding analysis first; escalate to full probabilistic methods only where the decision is sensitive to uncertainties. Risk Scenario Diagrams (RSDs) are developed at the level of detail warranted by strategic criticality — from simple two-pathway diagrams to fully branched event trees.

### Risk Drivers
Risk drivers are uncertain elements (parameters, pivotal events, or departures) whose optimistic values would move performance risk across a tolerability threshold. Identified by sensitivity analysis. Characterise drivers at all three levels (parameter → pivotal event → departure) for maximum mitigation latitude.

## Chapter Index

| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-introduction-and-rm-overview.md) | Introduction and RM Overview | RM = RIDM + CRM; mission execution domains; graded approach; NPR 8000.4A |
| [ch02](chapters/ch02-ridm-crm-integration.md) | RIDM–CRM Integration | RIDM-to-CRM handoff; requirements rebaselining; RMP; parameter vs. scenario models |
| [ch03](chapters/ch03-ridm-part1-identification-of-alternatives.md) | RIDM Part 1 — Identification of Alternatives | Objectives hierarchy; fundamental vs. means objectives; performance measures; trade tree |
| [ch04](chapters/ch04-ridm-part2-risk-analysis-of-alternatives.md) | RIDM Part 2 — Risk Analysis of Alternatives | TBfD; performance parameters; model rigor vs. graded analysis; sensitivity studies; configuration control |
| [ch05](chapters/ch05-ridm-part3-risk-informed-selection.md) | RIDM Part 3 — Risk-Informed Alternative Selection | Performance commitments; risk tolerance; deliberation; RISR; decision robustness |
| [ch06](chapters/ch06-crm-initialisation-and-planning.md) | CRM Initialisation and Planning | RMP; burn-down schedule; risk taxonomies; performance margins; tolerability zones |
| [ch07](chapters/ch07-crm-identify-and-analyze.md) | CRM — Identify and Analyze Steps | Individual risk statements; 8-question validity test; RSDs; Quick Look; risk drivers |
| [ch08](chapters/ch08-crm-plan-step.md) | CRM — Plan Step | Six disposition types; tactical vs. strategic planning; risk response options and alternatives; Risk Response Matrix |
| [ch09](chapters/ch09-crm-track-control-communicate.md) | CRM — Track, Control, and Communicate & Document | Performance risk tracking chart; monitoring streams; risk database; communication protocols |
| [ch10](chapters/ch10-enterprise-risks-and-appendices.md) | Enterprise and Institutional Risks, and Appendices | Institutional/enterprise/strategic risk; TBfD and RISR content guides; JCL; NASA ESAS examples |

## Topic Index
- **Risk-informed decision making** → ch01, ch02, ch05
- **Objectives hierarchy** → ch03
- **Performance measures and imposed constraints** → ch03, ch05
- **Risk analysis framework / TBfD** → ch04
- **Performance commitments and risk tolerance** → ch05
- **Deliberation and alternative selection** → ch05
- **RISR structure** → ch05, ch10
- **Risk Management Plan (RMP)** → ch02, ch06
- **CRM initialisation** → ch06
- **Burn-down schedule** → ch06
- **Risk taxonomies** → ch06
- **Individual risk statements** → ch07
- **Risk Scenario Diagrams (RSDs)** → ch07
- **Risk drivers** → ch07
- **Quick Look vs. Graded Approach** → ch07
- **Plan step / disposition types** → ch08
- **Mitigate, Watch, Research, Elevate, Close, Accept** → ch08
- **Tactical vs. strategic planning** → ch08
- **Track and Control steps** → ch09
- **Risk database** → ch09
- **Communication protocols** → ch09
- **Enterprise and institutional risks** → ch10
- **TBfD content guide** → ch10
- **RISR content guide** → ch10
- **JCL (Joint Confidence Level)** → ch10

## Supporting Files
- [glossary.md](glossary.md) — ~55 terms with chapter references, from Accept to Watch
- [patterns.md](patterns.md) — 14 named patterns with When/How/Trade-offs, covering objectives hierarchy to defence-in-depth driver characterisation
- [cheatsheet.md](cheatsheet.md) — RIDM vs. CRM decision tables, individual risk template, 8 validity questions, tells and smells

---

## Scope & Limits
This skill covers the NASA Risk Management Handbook (NASA/SP-2011-3422), a US Government public-domain work covering the integrated RIDM and CRM processes, their interaction with NASA systems engineering and organisational hierarchy, and their extension to institutional and enterprise risk domains. It does not provide procedural depth on domain-specific analysis methods (fault trees, event trees, Monte Carlo simulation, Bayesian inference) — those are covered in the NASA PRA Procedures Guide (NASA/SP-2002) and NASA/SP-2009-569 (Bayesian Inference). It does not cover safety standards or programme-management requirements in detail (NPR 8715.3C, NPR 7120.5D). The handbook is applicable primarily to NASA space flight programmes and projects; adaptation is required for other industries or regulatory contexts.
