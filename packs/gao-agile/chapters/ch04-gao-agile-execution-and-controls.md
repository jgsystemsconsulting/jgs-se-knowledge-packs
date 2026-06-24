# Chapter — Overview of Agile Execution and Controls

## Core Idea

Adopting an Agile framework for building software is only the starting point; a program still has to apply disciplined execution and control practices once development is underway. The GAO Agile Assessment Guide (GAO-24-105506) frames effective program management as the thing that raises a program's odds of delivering the promised capabilities on schedule and within budget. The guide groups the disciplined practices a program needs into three areas — first, the development and management of requirements; second, the shaping of an acquisition strategy; and third, monitoring and control of the program — and treats this chapter as the high-level background for all three. Chapters 5, 6, and 7 then carry each area into the specific best practices that apply on an Agile program.

The chapter's central tension, which it raises and then resolves, is whether classic program-management discipline clashes with Agile values. The guide's answer is no: artifacts the Agile team already produces — feature lead and cycle time, defect counts, and velocity trends — can be repurposed to oversee an Agile program in near-real time, letting management surface risks early and decide faster rather than waiting for end-of-phase reporting.

## Frameworks Introduced (exact source names, when/how)

The slice does not introduce a software-process framework (it explicitly notes there are no standard Agile terms from an acquisition viewpoint); instead it introduces a planning structure, a constraint model, and two companion GAO guides that the Agile guide draws on.

- **Agile Planning Levels (five levels of planning).** Presented in Figure 5 ("Agile Planning Levels") as an inverted-triangle model used to progressively define work. The five levels, top to bottom, are vision, epic, release, iteration, and user story. The inverted triangle is meant to show traceability from the planning documents at the top (vision and epics) down to the working documents (releases, iterations, and user stories).

- **Rolling wave planning.** Introduced as the planning style Agile teams typically embrace, where near-term work is planned in detail while later work is held at a high level. The guide ties this concept back to its own *Schedule Assessment Guide* (GAO-16-89G).

- **Waterfall-versus-Agile constraint model.** Shown in Figure 6, which compares the program-management constraints of the two approaches side by side. It contrasts which variables are fixed and which float: Waterfall fixes requirements while letting cost and schedule vary; Agile fixes cost and schedule while letting the requirements for each iteration vary.

- **Cost Estimating and Assessment Guide (GAO-20-195G).** Named as the GAO "Cost Guide," first released in 2009 and revised/re-released in 2020. It establishes a best-practice methodology federal agencies can use to develop, manage, and evaluate program cost estimates, and it covers monitoring processes such as Earned Value Management.

- **Schedule Assessment Guide (GAO-16-89G).** Named as the GAO "Schedule Guide," first released in 2016 as a companion to the Cost Guide. It supplies a methodology for developing, managing, and evaluating schedules, presented as ten detailed best practices for a reliable, high-quality schedule, plus guiding principles for auditors.

- **OMB Memorandum M-15-14.** Cited as the source of the "adequate incremental development" expectation — delivery of new or modified technical functionality to users at least every six months — that acquisition strategies are expected to satisfy.

## Key Concepts

- **The three program-management areas.** First, developing and managing the program's requirements; second, developing its acquisition strategy; and third, monitoring and controlling the program — the area the guide associates with cost and schedule estimating. The chapter gives background; the deep treatment lives in chapters 5–7.

- **Requirements as a continuous process.** Because Agile integrates planning with design, development, and testing to ship small amounts of working software on a short cycle, requirements management becomes an ongoing activity rather than a single up-front phase. A documented strategy helps ensure each requirement traces backward to the business need and forward to its design and test.

- **Bounded refinement.** Rolling wave planning lets requirements be refined as the program learns, but the guide stresses that the magnitude of that refinement must stay within the capabilities scoped in the program road map — Agile is not a license for boundless, open-ended development.

- **Epic decomposition.** Remaining work is captured in an epic; as the future becomes clearer, epics break down into features for release planning and into user stories for iteration planning. This rolling wave cycle repeats until all work has been converted into user stories, which are then broken into the team's daily tasks.

- **Release versus deployment.** A release is typically an internal hand-off of working code; a deployment is what actually makes functionality available to external users and stakeholders. The guide notes that, in a government setting, the recipient of a release is often a certifier or an independent test organization — not the end user directly — which is unlike some commercial programs that release daily or more often.

- **Cadence and time-boxing.** Iterations should be a fixed length, commonly 2–4 weeks, so a stable cadence can emerge; releases also occur at fixed intervals. Because both are time-boxed, counting iterations per release becomes simple arithmetic (the guide's example: a 12-week release with 2-week iterations yields six iterations).

- **Estimating unlocks commitment.** Reliable estimating is described as critical because it lets the team predict and commit to near-term deliverables. Effort serves as a proxy for cost, so estimating effort predicts both cost and how long deliverables will take. Understanding team capacity — how much work fits in one iteration — supports prioritization and quantifying the cost of delay when "must have" features slip.

- **Estimate updated, baseline preserved.** Agile's repeating iterations and releases create many chances to refine the cost estimate as the team learns what the customer wants. But the original baseline is developed once: the estimate at completion may be revised while the original cost estimate is rarely changed, so variances stay observable.

- **Scope flexibility in government context.** A commercial Agile vendor may run fixed cost and schedule with flexible scope, but government programs usually lack fully flexible scope. The guide's remedy is to separate "must have" from "nice to have" requirements early, deliver the "must haves" first, and where possible acquire a minimum viable product (MVP) on a fixed budget or schedule — while acknowledging overruns can still occur to reach full program scope.

- **Risk and uncertainty analysis.** Because not enough is known at the start about exact requirements, low-level requirements should stay flexible. Whenever assumptions shift, the cost and schedule estimates ought to quantify that effect — done through risk and uncertainty analysis, backed by a defined strategy for identifying, communicating, and controlling risks.

## Mental Models

- **Inverted triangle of planning.** Stable, high-level intent (vision) sits at the wide top and changes rarely; detail increases as you descend toward user stories and tasks. Traceability runs the full length, linking strategic documents to the working documents that get coded.

- **Fixed-versus-variable dials.** A clean way to hold the Waterfall/Agile distinction: Waterfall pins requirements and lets cost and schedule move; Agile pins cost and schedule and lets requirements move per iteration. Same dials, opposite settings.

- **Start-and-end inversion.** Waterfall begins with a plan covering all requirements and ends when those requirements are complete. Agile begins with a high-level goal plus priority requirements and ends when the goal is met, with everyone accepting that requirements get refined as small software increments are demonstrated for feedback.

- **Effort as a proxy for cost.** Treating effort as the cost surrogate lets a team translate estimated work into both budget and delivery timing for near- and long-term deliverables.

- **Existing Agile artifacts as control instruments.** Rather than bolting on separate oversight machinery, map data the team already generates (lead/cycle time, defect counts, velocity) to traditional management tools to get the same oversight results in real time.

## Anti-patterns

The source frames these as failure modes through its case studies and cautions rather than labeling them as named "anti-patterns," but the following are explicitly called out as problems:

- **Treating Agile as boundless development.** Letting requirements refinement exceed the road map's scope is explicitly warned against.

- **Standing up programs before defining the unifying concept and its goals.** In Case Study 10 (Joint Cyber Warfighting Architecture, GAO-21-68), USCYBERCOM established requirements and launched several acquisition programs before developing the JCWA concept, never defined interoperability goals for the constituent systems, and had not moved past diagramming the concept or set up a governance structure to prioritize requirements across programs. GAO concluded the missing goals and governance left the portfolio at risk of failing to deliver the joint cyber capability — though DOD later closed the gaps by finalizing a Concept of Operations and documenting integration and capabilities-management office roles.

- **Lacking a reliable schedule and cost estimate.** In Case Study 11 (National Background Investigation Services, GAO-23-105670), DCSA used Agile methods but persistently lacked a reliable schedule and a reliable cost estimate, did not implement a prior GAO recommendation to fix schedule weaknesses, and managed work by funding-available rather than against a credible estimate — which GAO tied to ongoing delays and an inability to project costs accurately.

## Key Takeaways

- Adopting Agile does not remove the need for program-management discipline; it changes how that discipline is applied across requirements, acquisition strategy, and monitoring and control.
- The five planning levels (vision, epic, release, iteration, user story) plus rolling wave planning provide the progressive-definition structure that keeps refinement traceable and bounded by the road map.
- The fixed/variable contrast is the crisp distinction between Waterfall and Agile: requirements fixed versus cost and schedule fixed.
- Reliable estimating is the lever for prediction and commitment; estimates should be refreshed on the program's cadence while the original baseline stays put so variances remain visible.
- Government scope is rarely fully flexible, so prioritizing "must have" over "nice to have" and pursuing an MVP first is how a program delivers maximum value early within constraints.
- Traditional cost, EVM, and schedule best practices (the Cost Guide and Schedule Guide) still apply, because Agile artifacts often already hold the metrics that map onto traditional management tools.

## Connects To

- **Chapter 1** — for the foundational Waterfall-versus-Agile contrast that this chapter extends into program-management tradeoffs.
- **Chapter 5** — requirements development and management in Agile, including the MVP concept introduced here.
- **Chapter 6** — contracting in an Agile environment, expanding the acquisition-strategy background into three best practices (tailor acquisition planning and contract structure to Agile; incorporate Agile metrics, tools, and retrospective lessons into contract management; integrate the program office with the developers).
- **Chapter 7** — how program monitoring and control best practices pair with an Agile work breakdown structure and Agile principles.
- **Chapter 8** — the lead-time and cycle-time metrics referenced here as real-time oversight signals.
- **GAO Cost Estimating and Assessment Guide (GAO-20-195G)** and **GAO Schedule Assessment Guide (GAO-16-89G)** — the companion methodologies this chapter leans on for cost, EVM, and schedule discipline.
- **OMB Memorandum M-15-14** — the federal IT guidance behind the "adequate incremental development" (delivery at least every six months) expectation for acquisition strategies.
