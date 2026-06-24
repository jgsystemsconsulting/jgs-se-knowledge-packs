# Chapter 15 — Technical Management Processes

> Synthesized reference notes from SEBoK v2.14, Knowledge Area **Technical Management Processes** (Part 3). Content is transformed for study use under CC BY-NC-SA 3.0; attribution to the BKCASE Project. No long verbatim passages are reproduced.

## Core Idea

This Knowledge Area concerns the management of resources and assets that are allocated to do systems engineering — usually inside a project or a service, sometimes inside a less well-defined activity such as enterprise-level R&D. SEBoK frames the whole area as **Systems Engineering Management (SEM)**, and draws a deliberate line: SEM is set apart from general project management by its concentration on the *technical or engineering* side of the work. The recurring image is a Venn diagram of **Systems Engineering Management Boundaries**: some functions are managed inside the SE function, others are managed collaboratively with systems-implementation management and with overall project/systems management. There is no one-size-fits-all split — an in-company SE group leans on the corporate organization for accounting, while a pure-SE company absorbs accounting into SEM. The constant is that SE managers must be actively involved in everything inside the SE system boundary, work out the collaborative arrangements that fit their situation, and stay aware of events *outside* the boundary that affect their ability to perform.

The KA decomposes SEM into a family of tightly coupled technical-management processes: **Project Planning**, **Project Assessment and Control**, **Decision Management**, **Requirements Management**, **Risk Management**, **Configuration Management** (with **Configuration Baselines** and **Configuration Management Implementation**), **Information Management**, **Quality Management**, and **Measurement**. None of these stands alone — the connective tissue between them (planning feeds assessment, measurement feeds risk, decisions consume both) is as important as any single process.

## Frameworks Introduced

(Exact SEBoK terms; what each is and when/how it is used.)

- **Systems Engineering Management (SEM)** — the umbrella for the entire KA. Use it to scope the *technical* management work, distinct from but collaborating with general project management. Spans planning, organizational structure, the collaborative environment, and program controls so stakeholder needs are met.

- **Systems Engineering Management Plan (SEMP)** / **Systems Engineering Plan (SEP)** — the highest-level technical plan, subordinate to the project plan, usually with subordinate technical plans beneath it. SEBoK flags a U.S.-defense distinction: SEP and SEMP are *not* interchangeable there — the SEP is a high-level plan written by the government customer before acquisition begins (and may include an acquisition plan); the SEMP is the development plan written by the developer/contractor.

- **Integrated Product (Development) Team — IPDT / IPT** — a cross-discipline team used during planning to keep communication open, integrate design considerations and testing early, and break down the knowledge "stovepipes" that otherwise form. Listed among the proven planning practices.

- **Decision Management Process / Trade Study** — the structured, analytical framework (per ISO/IEC/IEEE 15288) for identifying, characterizing, and evaluating alternatives at any life-cycle point and selecting the most beneficial course of action. The trade study is the most common decision method; the process decomposes a hard decision into logical segments so the decision maker stays inside human cognitive limits without oversimplifying.

- **Multiple Objective Decision Analysis (MODA)** and its tooling — used inside Decision Management: the **value function** (transforms measure space to value space, anchored by a **walk-away point** mapped to 0 and a **stretch goal** mapped to the top of the scale), the **swing weight matrix** (sets priority weights by importance × measure range, weights normalized to sum to one for the **additive value model**), the **alternative generation table / morphological box**, the **stakeholder value scatterplot**, **Monte Carlo simulation**, **tornado/waterfall/line diagrams**, **decision trees**, and **influence diagrams**. Use these to score alternatives deterministically, then layer probabilistic and sensitivity analysis on top.

- **Value-Focused Thinking** (Keeney) — a best practice woven through Decision Management: use objectives to *create better alternatives*, transitioning from "alternative-focused thinking" to "value-focused thinking," and use the **ideal alternative** as a value-focused anchor in scoring.

- **The five-activity Configuration Management process** — **CM Planning and Management**, **Configuration Identification**, **Configuration Change Management**, **Configuration Status Accounting**, and **Configuration Verification and Audit**. Benefits are maximized only when all five are planned and executed; they are interrelated and applied concurrently/iteratively, not strictly sequentially.

- **Configuration Item (CI)** / **configuration information** / **baseline** — a CI is a system element under CM; its functional and physical characteristics are its configuration information; a baseline is a formally approved, fixed-in-time snapshot of the approved configuration, changeable only through formal change procedures.

- **Configuration Control Board (CCB)** (also Configuration Steering Board / Change Control Board) and **Technical Review Board (TRB)** — the boards that decide on changes and variances. CCBs can split into change-review and change-implementation boards; a TRB can be inserted before the CCB to ensure thoroughness of the supporting information. Larger/more complex programs use a *hierarchy* of CCBs; small organizations may run a single organizational-level CCB.

- **The three formal configuration baselines** — the **Functional Configuration Baseline (FBL)**; the **Allocated Configuration Baseline (ABL)**; and the **Product Configuration Baseline (PBL)**, each with paired documentation (**FCD / ACD / PCD**). FBL captures the approved originating performance requirements and verification; ABL allocates requirements to the major lower-level CIs; PBL captures the approved definition/description from system-definition activities. SEBoK notes other baselines may exist (e.g., a **Mission Objective Baseline** per ECSS-M-ST-40C).

- **Information Management (IM) process** — generate, obtain, confirm, transform, retain, retrieve, disseminate, and dispose of information for designated stakeholders (per ISO/IEC/IEEE 15288, 6.3.6.1). Distinguished from CM (CM cares about the *significance/applicability* of information to system elements; IM manages the information's own lifecycle) and from **Knowledge Management (KM)**, which sits at the organization level and aims to re-apply existing knowledge.

- **The Quality movement's four stages** — **Acceptance Sampling**, **Statistical Process Control (SPC)**, **Design for Quality**, and **Six Sigma** — SEBoK's narrative arc of how quality management matured over ~80 years. Each is also a named strategy (e.g., the **Shewhart 3-sigma control chart** under SPC; **DMAIC**/**DMADV** and **lean six sigma** under Six Sigma; **Taguchi**-style response-surface design under Design for Quality).

- **The four-activity Measurement process** (from PSM / ISO/IEC/IEEE 15939) — **Establish and Sustain Commitment**, **Plan Measurement**, **Perform Measurement**, **Evaluate Measurement**. Adopted by CMMI's measurement-and-analysis process area and across ISO/IEC/IEEE 15288/12207/15939.

- **Measurement-need approaches** — the **PSM** approach (information categories → measurable concepts → prospective measures) and the **Goal-Question-Metric (GQM)** approach (goals decomposed into questions that select measures). Use these to derive the *right* measures from genuine information needs.

- **Technical measurement family** — **Measures of Performance (MOPs)**; **Measures of Effectiveness (MOEs)**; and **Technical Performance Measures (TPMs)** — planned early, performed throughout the life cycle with rising fidelity, to predict whether the technical solution will meet requirements and mission needs.

- **Systems Engineering Leading Indicators** — measures (or collections of measures) composed of *characteristics + a condition + a predicted behavior*, giving predictive, forward-looking insight into likely future SE performance.

- **Newer measurement frameworks** — the **PSM Digital Engineering (DE) Measurement Framework** (data and models are the core products under measurement) and the **Continuous Iterative Development (CID) Measurement Framework** (for agile-style software development), both supplementing the ISO/IEC/IEEE 15939 foundation.

- **Risk treatment options** — **assumption, avoidance, control (mitigation), and transfer** — all four are evaluated for each risk before one is chosen; hybrid strategies combining options under a single implementation approach are allowed.

## Key Concepts

- **SE planning is concurrent with project planning, not a subset of it.** SE planning develops and integrates the technical plans needed to hit technical objectives within resource constraints and risk thresholds, involving the success-critical stakeholders so tasks land with the right timing in the life cycle. It covers the full technical scope — development, risk, quality, configuration, measurement, information, production, V&V, integration, validation, deployment — and integrates SE functions so plans, requirements, operational concepts, and architectures stay consistent and feasible.

- **Assessment and control buys visibility.** The purpose of **Systems Engineering Assessment and Control (SEAC)** is adequate visibility into actual technical progress and risk against the SEMP/SEP, so the team can act *preventively* on disruptive trends and *correctively* when performance breaches thresholds. It runs reviews and audits, escalates significant technical risk to the project risk register, manages actions to closure, and holds a **post-delivery assessment** (post-project review) to capture knowledge. SEBoK lists a catalog of DAU technical-review examples (SRR, SFR, PDR, CDR, TRR, SVR, PRR, FCA/PCA, ISR, OTRR, plus the Technology Readiness Assessment).

- **Decisions are hard because objectives compete under uncertainty with real consequences.** A formal Decision Management process lets experts assess alternatives within their expertise while the whole decision is decomposed and re-synthesized. A defining feature of MODA is the transformation from measure space to value space via value functions, then weighting by importance *and* measure range.

- **Cognitive bias can distort any decision maker.** SEBoK gives unusual weight to behavioral research (Kahneman; Thaler & Sunstein — both Nobel laureates), naming specific biases (**confirmation, rankism, complacency, optimism**) tied to real catastrophes (Challenger, Columbia, Tenerife, Three Mile Island, Bhopal). Self-mitigation is generally not feasible; the literature instead points to organizational "nudges" and named mitigations.

- **Requirements Management is cross-cutting, not a one-time baselining.** RM keeps needs and requirements aligned with other artifacts across the life cycle — baselining, communicating, managing flow-down (allocation and budgeting), managing interfaces, maintaining bidirectional traceability, and managing change. It leans on CM, Interface Management, Systems Analysis, and Information Management, and aims to establish an **Authoritative Source of Truth (ASoT)** within a digital engineering ecosystem.

- **Two definitions of "risk" coexist.** SEBoK (per INCOSE Handbook 5th ed. / ISO 15288:2023) holds two: "the effect of uncertainty on objectives" (effects may be negative *or* positive — the positive side becomes **opportunity**) and "how the likelihood of harm occurring combines with how severe that harm would be" (negative only, used heavily in safety). The classic decomposition is probability × consequence; catastrophic-risk analysis adds a third trio — **threat, vulnerability, consequence**.

- **The SE risk process has five activities.** Planning, identification, analysis, treatment, monitoring — continuous and forward-looking. Use structured **if-then** risk descriptions; pick top-level and lower-level identification approaches (no single accepted method); ISO 31010 catalogs **41** assessment techniques, including the risk matrix/cube. Emerging methods like **STPA** target complex, unpredictable system behaviors.

- **CM keeps the built system matching the planned system.** Its three fundamental objectives are consistency between system and configuration information, integrity/traceability of that information and its changes, and reproducibility — together enabling define/realize/transition/operate/maintain/dispose. CM applies to any system (hardware, software, services, SoS) and across the whole life cycle, with tailoring.

- **IM treats information as a strategic asset.** It ensures information is relevant, complete, verified, protected, distributed, and disposed of when no longer relevant. **Data** = raw, unstructured values; **information** = structured data in context that has been analyzed and interpreted; **metadata** = "data about data." IM also owns **Information Security Management** (broader than cybersecurity — covers physical formats and knowledge in stakeholders' minds), with a five-step approach inspired by NIST SP 800-160v1r1.

- **Quality means fit for use / conformance to requirements.** SEBoK cites Juran ("fitness for use") and Crosby ("conformance to requirements"). Quality attributes (a.k.a. quality factors / characteristics / non-functional requirements) cannot all be optimized at once, so trade-off analysis is required; attributes differ in prominence for products vs. services vs. enterprises. Quality is unreachable when it cannot be measured — hence the **Measurement System Analysis (MSA)** spans tools, processes, procedures, people, and environment.

- **Measurement exists to inform decisions, not for its own sake.** Three fundamental concepts: measurement is a consistent-but-flexible *tailored* process; decision makers must understand and connect what is measured to what they need to decide (closed-loop feedback control); and measurement must actually be *used* to be effective.

## Mental Models

**SEM is the part of management with the engineering in it.** When deciding where a function "lives," ask whether it is fundamentally technical (it belongs inside the SE boundary) or fundamentally enterprise/corporate (managed collaboratively from outside). The boundary is situational — design the collaborative arrangement deliberately rather than assuming a default.

**The technical-management processes are one tightly coupled mesh, not a list.** SEBoK keeps repeating the linkages: planning feeds milestones to assessment; measurement supplies indicators to assessment, risk, and decisions; assessment and risk feed *back* into re-planning; decision management consumes monitoring results as decision criteria. Treat any single process as broken if you cannot name what feeds it and what it feeds.

**Baseline just in time, not too early.** A baseline is leverage — once set, you can trace the impact of any change. But baselining requirements or designs before they are understood guarantees rework. The proven move is "just-in-time baselining": fix a requirement/design only when other work commits to its stability; if work must start while it is still uncertain, build robustness in to absorb change with minimum rework.

**Make review gates have "teeth."** A technical review that a schedule-driven manager can override on appeal is theater. Treat uncertainty as normal — don't penalize a team for admitting it; ask for the risk-mitigation plan instead. The dark mirror of a toothless gate is "it can't afford the time to do it right, but finds the time to do it again."

**Map measures to value, then weight by importance *and* range.** In a trade study, don't score on raw measures — transform each measure through a value function anchored at a walk-away point (0) and a stretch goal (top). Then set weights with the swing-weight matrix so that both how-much-it-matters and how-much-it-can-swing drive priority.

**Run a premortem before the big decision.** To fight optimism and confirmation bias, surround the decision with trusted experts whose job is to argue the negative case in advance ("perhaps launch later, not now"). Pair with independent review (organizationally and financially independent technical authority) and, in operational crews, crew-resource-management-style communication.

**Opportunity is the dual of risk, but the math is asymmetric.** Manage opportunities with the same two-component structure (probability × impact), but remember that a positive opportunity does not offset an equal-magnitude risk in utility terms — losses loom larger than gains (prospect theory), and pursued opportunities carry their own side-effect risks.

**Watch the "Sea of Green."** Green status on budget, staffing, and data-gathering for a risk-treatment plan can hide a plan that never actually reduces the risk. Track whether the *risk itself* is moving, not whether the activities around it are on schedule.

## Anti-patterns

(Named pitfalls drawn directly from the KA's pitfall tables.)

- **Incomplete and Rushed Planning** — saving time by skimping on SE planning creates downstream cost and schedule damage through omissions, missing detail, un-integrated effort, and infeasible cost/schedule.
- **Inexperienced Staff** — assigning SE planning to engineers without relevant, similar-project judgment yields unrealistic plans.
- **No Measurement** (assessment) — running assessment and control without insightful measurement: "what you get is what you measure."
- **"Something in Time" Culture** — measuring only what's easy (cost, schedule) and letting schedule trump fitness-for-purpose, forcing rework.
- **No Teeth** — review gates a project manager can override, especially dangerous in schedule-driven organizations.
- **Too Early Baselining** — baselining requirements/designs before they're understood, guaranteeing high rework.
- **Process Over-Reliance** / **Tool and Technique Over-Reliance** (risk) — leaning on process or tooling while neglecting human/organizational behavior and day-to-day execution.
- **Lack of Continuity** (risk) — doing risk management only to satisfy reviews instead of continuously.
- **Automatic Mitigation Selection** (risk) — defaulting to "control/mitigate" instead of weighing all four treatment options.
- **Sea of Green** / **Band-Aid Risk Treatment** (risk) — green indicators masking an ineffective plan; patching each instance instead of the root cause.
- **Shallow Visibility / Poor Tailoring / Limited CM Perspective / Insufficient CM Awareness / Lack of CM Plan / Insufficient CM Checks** (configuration management) — and for baselines: **Shallow Baselines Visibility**, baselines **not tailored adequately**, **lack of baselines planning and management**, **baselines not used by stakeholders**, **missing baselines checks**.
- **CM Boards organization not clarified / Insufficient CM training / Insufficient CM tooling** (CM implementation).
- **No Information/Data Dictionary, No Information identification strategy, No Metadata, No predefined Information/data lifecycle, No security rules, No clear information communication rules, Missing content-/access-/repositories-obsolescence management, Inadequate back-up policy** (information management).
- **Golden Measures, Single-Pass Perspective, Unknown Information Need, Inappropriate Usage** (measurement) — chasing a universal measure set, treating measurement as one-pass, measuring without knowing why, or misusing measures (e.g., to rate individuals) without context.

## Key Takeaways

1. **SEM is technical management.** Frame the whole KA as Systems Engineering Management — distinguished from general project management by its engineering focus — and design the boundary between what SE manages directly and what it manages collaboratively.
2. **Plan the SEMP/SEP first; everything else hangs off it.** It is the highest-level technical plan, subordinate to the project plan, with subordinate technical plans below. In U.S. defense work, keep SEP (customer, pre-acquisition) and SEMP (developer) separate.
3. **Wire the processes together.** Planning, assessment/control, decision, risk, and measurement are mutually feeding; treat missing linkages as defects. Run assessment, risk, and measurement concurrently.
4. **Decide formally when stakes and uncertainty are high.** Use the decision-management/trade-study process with value functions, swing weights, and an additive value model — then stress it with probabilistic and sensitivity analysis, and actively counter cognitive bias.
5. **Manage requirements as a living, traceable set toward an ASoT.** Baseline, allocate/budget, maintain bidirectional traceability, and manage change in a digital ecosystem — expect change, especially early.
6. **Run risk as a continuous five-step process and evaluate all four treatment options.** Use structured if-then descriptions; don't auto-mitigate; watch the Sea of Green; manage opportunity as risk's asymmetric dual.
7. **Hold five CM activities and three formal baselines.** Plan/identify/change-manage/status-account/verify-and-audit; FBL → ABL → PBL with paired documentation; control changes through CCB/TRB hierarchies sized to the program.
8. **Separate IM from CM and KM, and treat information as an asset.** IM owns the information lifecycle and security; CM owns configuration information's significance; KM (organization-level) aims to reuse knowledge.
9. **Measure quality and measure for decisions.** Apply the right quality strategy (acceptance sampling / SPC / design for quality / six sigma); run the four-activity measurement process; derive measures from real information needs (PSM/GQM); use MOEs/MOPs/TPMs and leading indicators for predictive insight.
10. **Capture knowledge at the end.** Hold post-delivery assessments / post-mortems to feed estimation models, lessons-learned databases, and gate checklists.

## Connects To

- **ISO/IEC/IEEE 15288** (System Life Cycle Processes) — the backbone standard cited throughout: defines the Decision Management purpose, the CM process purpose (6.3.5.1), and the IM process purpose (6.3.6.1). The 2023 edition anchors the risk discussion.
- **ISO/IEC/IEEE 16085** (Risk Management) and **ISO 31000 / ISO 31010 / ISO 31073** — the risk-process detail, integrated-risk-management guidance, and the 41-technique assessment catalog; ISO Guide 51 / ISO 14971 / ISO 22367 anchor the safety ("harm") definition of risk.
- **ISO 10007** and **SAE EIA-649C** (with EIA-649-1A, GEIA-859B) — the CM and configuration-baseline standards alignment; **ISO/IEC/IEEE 15289** for content of life-cycle information items.
- **ISO/IEC/IEEE 15939** (Measurement Process) and **PSM** — the four-activity measurement process, supplemented by the **DE** and **CID** measurement frameworks; **CMMI** measurement-and-analysis process area.
- **ISO 9000 series**, the **Malcolm Baldrige** criteria, and **TL 9000** — quality-management standards and assessment criteria referenced in Quality Management.
- **INCOSE Systems Engineering Handbook** (4th/5th eds.), the **INCOSE Needs and Requirements Manual (NRM)** / **Guide to Needs and Requirements (GtNR)** — primary references for the management processes, especially Requirements Management.
- **NIST SP 800-160v1r1** (Engineering Trustworthy Secure Systems) — inspiration for the IM information-security approach.
- **SEBoK Part 6 collaborative-management KAs** — Systems Engineering and Software Engineering, and Project Management, and Industrial Engineering, and Procurement/Acquisition, and Quality Attributes — the explicit out-of-boundary collaborations for SEM. The KA also cross-references SEBoK's **System Requirements Definition**, **Concept Definition**, **Service Systems Engineering**, and **Systems Engineering and Quality Attributes** articles.
- **Rebentisch (2017), Integrating Program Management and Systems Engineering** (PMI–INCOSE–MIT collaboration) — the documented bridge between SE and project management used across planning, risk, and assessment.
