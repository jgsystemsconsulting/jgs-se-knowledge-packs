# Chapter 8: Specialized Estimating Techniques and Internal Control

## Core Idea
Beyond the twelve-step process, reliable cost estimating draws on a body of specialized techniques tailored to particular cost behaviors and decision contexts: estimating software (where labor, not material, dominates and there is no production phase), modeling repetitive-production cost reductions through learning curves, comparing candidate solutions through a disciplined Analysis of Alternatives, and grounding the whole estimating enterprise in a recognized internal-control framework. Each technique exists because a generic analogy or build-up estimate would misrepresent the underlying cost dynamics. The unifying thread is that the cost estimating process itself is an internal control — a continuous, people-driven mechanism that gives an entity reasonable (not absolute) assurance its objectives will be met — so the integrity of these specialized methods is what makes program decisions defensible.

## Frameworks Introduced

- **Software cost estimation approach (Appendix V)**: A two-element method — first size the software deliverables, then convert size into development effort. The guide treats software separately because its life cycle differs from hardware: cost is mostly labor, software is trivial to copy so there is essentially no recurring production phase, yet the same families of methods (analogy, engineering build-up, parametric) still apply.
  - When to use: Major acquisitions where software is a growing share of system cost. The guide cites projections that software, under half of a typical defense system's cost in 1997, would reach roughly 80 percent or more by 2020.
  - Components: size estimation; conversion to development effort via a productivity factor (e.g., lines of code or function points per labor-month); schedule estimation; sustainment; IT infrastructure and services.

- **Software sizing methods (Appendix V)**: A menu of techniques for producing a numerical size estimate — among them **source lines of code (SLOC)**, **function point** and **object point** analysis, **use-case** sizing, and the **COSMIC Functional Sizing Method** (from the Common Software Measurement International Consortium). SLOC is named as the predominant method because many organizations hold historical SLOC databases.
  - When to use: Choice depends on the software type and on data availability for comparable efforts. Some methods estimate from requirements alone (useful early); others need the planned architecture; others address modifications to standard software.
  - Caution introduced here: many sizing methods lack a standards body controlling their counting rules, so different users modify the rules internally, producing inconsistent counts across organizations.

- **Code-origin classification for modification (Appendix V)**: A scheme distinguishing newly written code from **reused** (used verbatim, unmodified), **adapted** (redesigned, possibly converted, needing further modification), and **auto-generated** code. Used after a sizing method is chosen to judge whether modifying existing code beats writing fresh code.
  - Anchor: The Office of Management and Budget memorandum M-16-21 (Federal Source Code Policy) is named as the basis for making custom-developed source code available for government-wide reuse, with securing data rights and documenting source code highlighted as supporting requirements.

- **Parametric software estimation (Appendix V)**: Commercially available parametric tools that draw on broad cross-project datasets and cost estimating relationships to generate cost, schedule, effort, and risk estimates from user inputs (size, personnel capability, experience, development environment, reuse, language, labor rates), with default values where inputs are missing.
  - When to use: Early in the life cycle when requirements and design are still vague; they accept multiple sizing metrics so estimators can compare methods' effects.
  - Caution: These tools are often "black boxes" (closed systems), so the user cannot easily test the model; the source of the sizing data (initial estimate at award versus final size at completion) materially changes results.

- **Software sustainment taxonomy (Appendix V)**: A classification of maintenance into **corrective** (fixing defects missed in testing), **adaptive** (modifying software for changes or technology upgrades in its operating environment), and **perfective** (adding new functionality in response to user enhancement requests). Help-desk support and perfective maintenance are named as typically the bulk of operations-and-maintenance effort.

- **COTS and ERP considerations (Appendix V)**: Guidance for estimating commercial off-the-shelf software and Enterprise Resource Planning systems. ERP is singled out because it forces business-process reengineering and is unusually hard to estimate; the guide cites a 2010 GAO report finding six of nine examined DOD ERPs slipped 2 to 12 years and five incurred cost increases ranging from $530 million to $2.4 billion.

- **Work Breakdown Structure templates (Appendix VI)**: A library of example WBSs anchored to **MIL-STD-881D** (the 2018 update of the DOD standard practice for Work Breakdown Structures for Defense Materiel Items, mandatory for ACAT programs) for aircraft, missile/ordnance, sea, space, ground-vehicle, and information/defense-business-system types, plus non-defense templates from the **NASA WBS Handbook (NASA/SP-2010-3404)**, the **Department of Energy WBS Handbook**, and the **Project Management Institute Practice Standard for Work Breakdown Structures, second edition (2006)** for environmental, pharmaceutical, process-plant, and telecom programs.
  - When to use: As starting frameworks for structuring a program's scope; the guide advises checking the source for updates before reuse.

- **Learning curve analysis — unit and cumulative average formulations (Appendix VII)**: Two ways to model the empirical finding that production cost drops by a constant percentage each time cumulative quantity doubles. Both share the form Y = AX^b, where A is the first-unit cost and b is the slope coefficient (b = ln(slope)/ln 2).
  - **Unit formulation (unit theory)**: Each doubling of quantity reduces the *individual* unit's cost by the slope. The guide's worked example: an 80 percent curve on a $1,000 first unit yields about $800 for unit two and roughly $702 for unit three.
  - **Cumulative average formulation (cumulative average theory)**: Each doubling reduces the *cumulative average* cost by the slope; associated with T. P. Wright's 1936 work. The same functional form is interpreted on cumulative averages rather than individual units.
  - When to use: There are no firm rules; selection is guided by analogous systems, industry standards, historical/contractor practice, and the expected production environment. Cumulative average is presented as a better fit for immature production (prototype tooling, weak supplier base, early design changes, concurrency); unit theory fits a well-prepared production start.

- **Production rate and break adjustments (Appendix VII)**: Extensions to the unit curve. A rate term (Y = AX^b Q^r) captures economies of scale as production rate rises, and rate penalties when nominal capacity is exceeded. For interruptions, two named methods work in sequence:
  - **Anderlohr method**: Quantifies learning *lost* during a production break by dividing loss into five weighted categories — personnel learning, supervisory learning, production continuity, methods, and tooling — whose weights must total 100 percent, combined into a weighted-average "learning lost factor."
  - **Retrograde method**: Determines, after lost learning is quantified, which earlier unit on the original curve corresponds to the true cost of the first post-break unit, so production "restarts" at that retrograde unit rather than at the next sequential number.

- **Step-down functions and prototype-to-production theories (Appendix VII)**: Methods for placing the first production unit on the curve using development cost data. The estimator first computes **equivalent prototype units** (crediting partial articles), then chooses among the **continuous approach** (improvement carries straight through) and two displacement theories — **sequential** (improvement continues from last development unit plus one, with a step-down) and **disjoint** (curve displaced and learning restarts at unit one, typically yielding much lower estimates). The guide also names **toe-up** (higher recurring end-of-production cost) and **nonrecurring close-out costs** as end-of-program effects.

- **Technology Readiness Levels (Appendix VIII)**: The 1–9 maturity scale (and Technology Readiness Assessments that apply it) used across DOD, NASA, and other agencies to communicate technology maturity, from basic-concept research at level 1, through laboratory demonstration around level 4, to a proven technology operating in its intended environment at level 9. Cross-referenced to the GAO Technology Readiness Assessment Guide (GAO-20-48G).

- **Integrated Baseline Review (Appendix IX)**: A structured review whose objective is to gain insight into a program or contract's cost and schedule risk and build confidence in its acquisition plans by assessing the adequacy of the baseline plan. Five process components: **IBR Program Management** (scope, control accounts, scheduling), **IBR Team** (size, training, experience), **IBR Execution** (the review itself), **IBR Risks** (classification by severity, evaluation criteria), and **IBR Findings** (conveying and summarizing results).
  - When to use: As early as possible — before award where appropriate, and no later than six months after. Risk is categorized as cost, management process, resource, schedule, and technical.

- **Common probability distributions for risk and uncertainty (Appendix X)**: The five distributions the guide names as most common for cost risk modeling — **triangular** (three points: most likely, pessimistic, optimistic), **lognormal** (positively skewed, known lower bound, limitless upper bound), **beta** (no negative cost/duration, symmetric or skewed), **uniform** (all values equally likely), and **normal** (symmetric, allows negative values, ~68 percent within one standard deviation).

- **Analysis of Alternatives (AOA) — 22 best practices in five phases (Appendix XI)**: A structured process to compare the operational effectiveness, cost, and risk of candidate alternatives against a mission need so the best alternative is chosen on documented selection criteria. The 22 practices are grouped into phases: **Initialize**, **Identify alternatives**, **Analyze alternatives**, **Document and review** (conducted throughout), and **Select a preferred alternative**.
  - Three roles: the **customer** (implements the decision), the **decision-maker** (signs off and selects), and the **AOA team** (does the day-to-day analysis).
  - Four characteristics of a reliable AOA — **well-documented, comprehensive, unbiased, credible** — each mapped to a subset of the 22 practices.
  - Decision basis: Net Present Value (discounted benefits minus discounted costs) where benefits can be monetized; otherwise the team must document why NPV is not used and justify its alternative method.

- **GAO Standards for Internal Control in the Federal Government — the "Green Book" (GAO-14-704G) (Appendix XII)**: The overarching framework for designing, implementing, and operating an effective internal control system, organized into **five components** and **seventeen principles**.
  - Components and principle ranges: **Control Environment** (principles 1–5), **Risk Assessment** (6–9), **Control Activities** (10–12), **Information and Communication** (13–15), and **Monitoring** (16–17). Each principle carries detailed attributes.
  - When to use: As the criteria against which an entity's cost estimating policy and process are judged to be internal controls; the 12 estimating steps are mapped to the components and principles.

## Key Concepts

- **Sizing consistency test**: A sizing method is reliable only if two analysts applying the same rules to an identical problem independently reach comparable results. The guide frames a checklist of questions — whether rules are rigorously and widely defined, governed and updated by a recognized independent body, supported by counter certification and statistical evidence of consistency, stable over time, and backed by available source artifacts.

- **Size growth before risk analysis**: A best practice is to estimate software size with two methods that converge, then adjust the size upward for expected growth from requirements creep or optimism *before* performing risk and uncertainty analysis, updating the estimate as data arrive so growth can be monitored.

- **Effort depends on application type**: Real-time embedded, safety-critical, and operating-system software typically demands more effort than an automated information system of the same size because of stringent quality and certification testing — so activities must be matched to the application type, not just to raw size.

- **Schedule pressure as a cost driver**: Compressing the schedule by cutting requirements analysis, skipping documentation, building in parallel, deferring functionality, postponing rework, or minimizing testing may save time initially but tends to add later effort, cost, and risk. Rework should be planned into every software schedule because defect-free first delivery is unlikely.

- **IT infrastructure is routinely undercounted**: For some IT systems, roughly 90 percent of cost lies in the infrastructure and services that support and run them, yet reporting commonly addresses only the software portion. A vendor quote alone is rarely sufficient — internal help-desk, facilities, ongoing maintenance/repair, and training costs persist even under "software as a service" or cloud arrangements.

- **Learning loss has structure**: A production break does not erase learning uniformly. The Anderlohr categories let an estimator reason about *which* learning is lost (people, supervision, continuity, methods, tooling) and weight each, rather than applying a single guess; methods are usually least affected when documented.

- **Equivalent units**: Partial development articles (e.g., a static article representing a fraction of a full aircraft) are converted into fractional equivalent units so that learning credited in development is placed correctly on the curve for the first production unit.

- **Internal control gives reasonable, not absolute, assurance**: An internal control system is a continuous built-in component of operations, effected by people, providing reasonable assurance objectives will be met. In a mature system, internal control can be indistinguishable from day-to-day work.

- **The estimating process IS an internal control**: A realistic cost estimate supports funding decisions, budget requests, resource evaluation at decision points, and performance measurement baselines — so the estimating process helps an entity operate efficiently, report reliable information, and comply with laws, qualifying it as an internal control.

- **Mapping steps to principles**: The guide maps individual estimating steps to control components — e.g., the multidisciplinary estimating team relates to the Control Environment (structure/responsibility/authority, competence, accountability — principles 3–5); the WBS relates to Information and Communication (principles 13–15); risk and uncertainty analysis relates to Risk Assessment (principles 6–7); and documentation relates to Information and Communication (principles 13–14). (Table 50 in the source provides a fuller step-to-principle matrix; redraw rather than reproduce.)

- **Three levels of control deficiency**: Auditors assess internal control at the level of **design** (a needed control is missing or wrongly designed — e.g., no documented estimating process), **implementation** (a well-designed control not placed into operation — e.g., a policy never communicated), or **operating effectiveness** (a designed-and-implemented control that does not operate as intended — e.g., a policy exists but untrained staff cannot perform robust risk analysis). A control cannot operate effectively if it was not effectively designed and implemented.

## Mental Models

- **Size first, then effort, then schedule**: Software estimating is a pipeline — a numerical size estimate feeds a productivity factor to yield effort, which then drives schedule. Errors compound downstream, so the size estimate is the foundation and deserves two-method cross-checking and explicit growth adjustment.

- **Doubling, not adding**: Learning curves are governed by *doublings* of cumulative quantity, not linear unit counts. The cost difference between unit theory and cumulative-average theory is largest in the first few units and shrinks as quantity grows — so the choice matters most for short or early production runs.

- **A break runs the clock backward**: A production interruption effectively moves the program back up its learning curve. The retrograde method makes this literal: you restart not at the next number but at the earlier, more expensive unit that the lost learning corresponds to.

- **Bias is the enemy of an AOA**: Nearly every AOA best-practice "effect" the guide states traces back to bias — defining the mission need in solution-specific terms, setting functional requirements off-mission, weighting criteria without justification, or skipping the independent review all let a predetermined answer masquerade as analysis. The phases run in sequence precisely to keep bias out, with documentation and independent review as the cross-cutting safeguards.

- **Design → implement → operate is a one-way dependency**: Internal control maturity is layered. You cannot implement what was never designed, and you cannot operate effectively what was never properly designed and implemented — so a deficiency at a lower layer guarantees deficiency above it.

- **The estimate is a control, not just a number**: Reframing the estimating process as an internal control changes the audit question from "is this number right?" to "does the entity have a designed, implemented, and operating process that reliably produces good numbers?" A reliable estimate is impossible if the underlying policy does not address all twelve steps.

## Anti-patterns

- **Inconsistent SLOC counting (Appendix V)**: Because many sizing methods lack a controlling standards body, users modify counting rules internally, producing dissimilar counts across organizations and undermining accuracy and reproducibility — the failure the consistency test is designed to catch.

- **Underestimating COTS/off-the-shelf integration (Appendix V)**: Estimators tend to underestimate the effort to integrate and implement off-the-shelf software; requirements, design, and system-level testing still must be done, poorly defined requirements force new custom code, and commercial software may ship with minimal testing, causing defects and incompatibilities that consume unplanned time.

- **Ignoring toe-up and close-out costs (Appendix VII)**: No broadly accepted technique exists for projecting recurring end-of-production toe-up costs, and "in truth, such costs are often ignored" — the guide recommends developing and applying a factor from contractor-specific historical data instead.

- **Defining mission need or functional requirements in solution-specific terms (Appendix XI)**: Stating the need around a predetermined solution introduces bias that can exclude viable alternatives and invalidate the analysis; setting functional requirements to anything other than the mission need lets arbitrary measures drive the study.

- **Skipping the independent review (Appendix XI)**: Without an independent review by an entity outside the program's chain of command, results are more likely to carry organizational bias or lack thoroughness, so a favored solution can be chosen rather than the best one.

- **No documented estimating policy (Appendix XII)**: The guide presents the absence of a documented cost estimating process — or a process that omits an essential best practice, cost risk and uncertainty analysis being the example given — as a deficiency in the *design* of internal control, illustrated by the 2020 Census case where little planning and policy documentation supported the Bureau's estimate.

## Key Takeaways

- Software estimating is a distinct discipline because cost is labor-dominated and there is no production phase; the approach is to size the software, then convert size to effort, then to schedule — sizing first and cross-checked.
- Sizing methods (COSMIC, function points, object points, SLOC, use case) vary in rigor and governance; reliability hinges on whether two independent analysts reach comparable counts, and SLOC dominates mainly because of historical databases.
- Code reuse is rarely free: reused, adapted, and auto-generated code each carry integration effort, and OMB's M-16-21 source-code policy frames reuse expectations, data rights, and documentation.
- Learning curves come in unit and cumulative-average forms sharing Y = AX^b; the choice is judgment-driven by analogous systems, industry/contractor practice, and production maturity, with the two diverging most for early units.
- Production breaks destroy learning in structured ways; the Anderlohr method weights five loss categories and the retrograde method repositions the restart point further up the curve.
- The 22 AOA best practices in five phases exist chiefly to keep bias out and ensure the result is well-documented, comprehensive, unbiased, and credible — with NPV as the default comparison basis and independent review as a key safeguard.
- The Green Book's five components and seventeen principles supply the criteria that make the cost estimating process itself an internal control; estimating steps map to components, and deficiencies are diagnosed at the design, implementation, or operating-effectiveness level.

## Connects To

- **The 12-step cost estimating process (earlier chapters of this guide)**: Appendix XII explicitly maps each step to internal-control components — step 2 team composition to Control Environment, step 4 WBS to Information and Communication, step 9 risk/uncertainty to Risk Assessment, step 10 documentation to Information and Communication — making the specialized techniques here downstream applications of the core process.
- **Work Breakdown Structure development**: The Appendix VI WBS templates (MIL-STD-881D, NASA, DOE, PMI) feed the WBS step that the internal-control mapping ties to quality information and communication (principles 13–15).
- **Risk and uncertainty analysis**: Appendix X's five distributions (triangular, lognormal, beta, uniform, normal) supply the modeling tools for the risk step, and AOA best practice 16 requires presenting each alternative's life cycle cost estimate with a confidence level or range rather than a point estimate.
- **Schedule assessment**: Appendix V defers detailed scheduling and rework treatment to the GAO Schedule Assessment Guide (GAO-16-89G), and the IBR (Appendix IX) ties cost and schedule baselines together through EVM and the integrated master schedule.
- **Technology maturity**: Appendix VIII's TRL 1–9 scale connects to the GAO Technology Readiness Assessment Guide (GAO-20-48G) and informs the technical-risk judgments embedded in AOA viability screening and IBR technical risk.
- **Earned Value Management**: The Integrated Baseline Review (Appendix IX) operationalizes the performance measurement baseline that the estimating process produces, classifying program risk across cost, management process, resource, schedule, and technical categories and feeding EVM monitoring.
- **Agile software development**: Appendix V flags Agile's relative-estimation and capacity concepts as a different effort-estimation path and defers detail to a separate GAO Agile guide, linking software estimating to lifecycle-model selection.
- **Government Auditing Standards (GAO-18-568G)**: Appendix XII draws its definitions of internal control and its three deficiency levels (design, implementation, operating effectiveness) from the auditing standards, connecting estimating quality to audit practice.
