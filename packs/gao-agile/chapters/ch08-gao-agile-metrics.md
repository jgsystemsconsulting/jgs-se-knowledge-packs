# Chapter 8 — Agile Metrics

## Core Idea

GAO's recurring position is that organizations have to collect and actually use performance data to understand how their operations and programs are doing. Performance information can be gathered at multiple stages of software development and at several layers of an organization, and it serves a range of purposes: surfacing problems so corrective action can follow, shaping strategy and resource allocation, recognizing and rewarding good work, and spreading approaches that work. Because of this, no matter which Agile development framework a program prefers, it should settle on a fitting set of metrics — and the processes that go with them — early in the development cycle, with the goals defined up front. Consistent with the Agile Manifesto, the chapter insists that Agile metrics be oriented toward measuring outcomes and satisfying customer needs rather than tracking activity for its own sake. Programs are unique and so are the organizations that run them, so each is best placed to set its own thresholds and guardrails around its metrics.

## Frameworks Introduced

The chapter is organized around **six best practices for developing meaningful metrics**, presented as Figure 18 (overview) and Table 16 (summary), both attributed to GAO under GAO-24-105506:

1. **Identify key metrics based on the program's Agile framework** — tailor metrics to the program's needs and its chosen framework.
2. **Keep metrics aligned with — and prioritized against — the goals and objectives of the whole organization** — different metrics matter for technical management, program management, and Agile methods, and strategic goals should trace down to Agile artifacts such as the road map and backlog.
3. **Establish and validate metrics early and align with incentives** — tailor metrics to the intended audience and tie them to team-based rewards.
4. **Establish management commitment** — managers ensure measurement processes are established, reflect an Agile approach, and are used consistently, balancing program-wide health assessments against monitoring deployed capabilities.
5. **Commit to data-driven decision-making** — design metrics to support specific decisions at each organizational level, assess goals at the Agile cadence, name the metrics in the contract, and capture them with automated tools where possible.
6. **Communicate performance information frequently and efficiently** — use Agile program management and software development tools to capture and display metrics in real time.

The chapter also introduces several specific analytical and reporting instruments by name:

- **Cumulative flow diagram (CFD)** — Figures 19 and 20. An analytical chart of colored bands, one per development stage, that visualizes effort and progress as tasks move through the workflow over time. The worked example uses six workflow phases — an estimated backlog, then work in progress, work under test, work that has been accepted, items staged and ready for deployment, and finally items deployed. A healthy CFD shows bands rising evenly while the deployed band grows; band widths reveal capacity problems and bottlenecks.
- **Lead time and cycle time** — defined as near-universal Agile metrics. Lead time spans from identifying a capability or feature to its release into production; cycle time spans from starting work on a story to getting it into production. Teams want both to be short.
- **Velocity** — the volume of work a given team finishes in a set period, reported in story points. Captured via burn up or burn down charts; usable for a team's own planning from historical data but explicitly not valid for comparing across teams.
- **Burn up and burn down charts** — Figure 21. Burn up charts plot time on the horizontal axis and cumulative story points completed on the vertical axis; burn down charts plot remaining work over time. Both track progress toward releases, iterations, or requirements, and support velocity-based projection of completion.
- **Health radar / team health assessment** — described in Agile in Action 7. A wheel-shaped maturity instrument that splits metrics into three nested levels (key areas → drivers → success metrics), typically run at a quarterly release retrospective and used to build a growth plan.
- **Combinations of metrics** — a sidebar framework (sourced to GAO analysis of DOD, Scrum.org, and Premiere Agile) giving three counterbalanced metric pairings that prevent gaming a single number.
- **Earned value management (EVM)** — referenced as an overall-program performance approach carried over from conventional development, with the detail deferred to chapter 7.
- **Best Practices Checklist: Agile Metrics** — a six-item verification checklist closing the chapter, mirroring the six best practices.

## Key Concepts

**Categories and levels of metrics.** Metrics fall into general categories — technical management (for example, testing and integration), program management (cost, schedule, performance), and Agile methods (collaboration or continuous improvement) — and they also exist at organization, program, and team levels. Each program selects and tailors its set; customizing commercial software, for instance, calls for a different approach than building custom software for specialized hardware.

**Attributes of a good metric.** A well-designed metric should be quantifiable, meaningful (with targets, a clear definition, and a link to organizational priorities), repeatable and consistent, and actionable enough to drive decisions. Metrics should also be transparent: a clearly stated goal tells the Agile team what data to collect and tells the customer what the number means. Without metrics that are meaningful, clear, and actionable, management lacks the information to evaluate performance.

**Audience tailoring.** Developers and managers should match metrics to the audience. Some measures help a team gauge itself but hold no interest for users and need not be shared; others answer specific user questions. A program that fails to align metrics with user questions may lack the data to evaluate its own performance.

**Traceability to organizational goals.** Aligning metrics to organization-wide goals connects long-term strategy to daily work. In an Agile context these connections should trace from the road map through releases and into the prioritized backlog — epics and user stories. Lose that traceability and the organization may lack what it needs to make prioritization and re-planning calls. An organized structure that assigns goals and performance information to the right managerial level raises the usefulness of the data collected at each level.

**Product vs. team performance.** The chapter draws a deliberate line between the two. Development team performance measures the team's ability to deliver — taking on a set number of contract actions, deploying an agreed count of capabilities, or transitioning a number of capabilities within a span. Product performance measures effectiveness and security parameters such as code quality or user satisfaction. Both together drive overall program success.

**Effort-to-value test for metrics.** A metric's informative value should exceed the cost of collecting its data; if gathering the data is too burdensome, the metric may not earn its keep.

**Value tracking.** Value in Agile programs is reflected through a mix of process and product metrics, and because value depends on perspective — context, time, technology — the metrics used can evolve. Process metrics measure how planning, execution, and delivery are performing and expose flow problems like bottlenecks; product metrics measure user acceptance and alignment to desired outcomes, often blending automated data, survey responses, and direct communication with business users.

**Automation and its limits.** Metrics should, as far as possible, be captured by tools a program already runs — Agile management suites, version control, testing, and continuous integration pipelines — which also opens the door to advanced analytics. Collected data must be checked for completeness, comprehensiveness, and correctness, or it can mislead. Crucially, automated tools cannot capture everything: team dynamics and other organizational behaviors need other instruments such as periodic surveys or questionnaires to complete the picture.

**Communication mechanisms.** Short Agile delivery windows demand daily progress tracking visible to all stakeholders. Tools facilitate dissemination, but co-located teams can also use whiteboards and other visible, accessible physical or electronic displays — termed **information radiators** — to improve how performance information circulates. Frequent reporting (for example, defects found versus defects addressed) lets decision makers act in time, but the information must stay reliable and traceable back to requirements.

**Case studies and exhibits.** Three real-program examples anchor the chapter (images and figures themselves are excluded here as copyrighted content):

- *Case study 20 (USCIS ELIS, GAO-16-467)* — the program collected reliable code-quality metrics (production defect/incident counts, automated code scanning, code-issue counts) that surfaced a real problem: issues were being found faster than they could be closed. But it did not measure internal user satisfaction, so it could not gauge how adjudicators viewed the system or fully understand the value each release delivered.
- *Case study 21 (TSA TIM, GAO-18-46)* — the program ran frequent, regular performance reviews (weekly status meetings, periodic Agile reviews at each release end, an automated corrective-action tracker) covering velocity, progress, and product quality, yet had built three releases without establishing performance thresholds or targets, leaving oversight bodies short of information.
- *Case study 22 (USCIS ELIS again, GAO-16-467)* — reporting and planning metrics lacked traceability between user stories and sub-features, so scope was miscommunicated to management; across releases 6.1, 6.2, and 7.1, large fractions of sub-features were not developed or not clearly traceable to the backlog.

## Mental Models

**Outcome over output.** The Agile Manifesto framing reorients measurement toward results delivered to the customer, not volume of activity. Velocity counts story points, but the chapter repeatedly subordinates such throughput numbers to whether value reached the user.

**Bands rising, bands breathing.** The CFD turns workflow into a visual: even, rising bands mean healthy flow; a narrowing band means more work leaves a stage than enters it; a widening band means the reverse — work is piling up, signaling a bottleneck or capacity limit at that stage.

**Counterbalanced pairs beat a single number.** Because optimizing one metric (velocity is the example) can quietly degrade another (quality), the chapter pairs metrics so each checks the other. Its three illustrations: carry-over stories alongside post-deployment defects (is the team rushing or over-reviewing?); automated unit-test count alongside build execution time (do new tests slow the build unduly?); and velocity alongside rejected, defect-heavy, unfinished, or never-started stories (is velocity being inflated by cherry-picking easy work?).

**Short feedback loop.** Metric reviews should match the development cadence so feedback and corrective action arrive in time. Involving staff from different organizational levels in frequent review meetings keeps decisions efficient and oriented toward course correction — which only works if the feedback loop stays short.

**Team-based incentives.** In Agile, recognition is built around team accomplishment rather than individual performance, and metrics should motivate desired behaviors with that team focus. Metrics decoupled from incentives leave teams feeling unrewarded for hitting program goals.

**Target values as a yardstick.** Management should set target values for critical metrics — for example, expected time from program launch to deploying a minimum viable product, time to deploy high-priority functionality, and time to fix production bugs — so reviews have something to measure against.

## Anti-patterns

The source names these failure modes explicitly:

- **Optimizing a single metric at the expense of others.** Teams are warned against maximizing one number, such as velocity, while sacrificing concerns like quality.
- **Inflating velocity by cherry-picking.** Raising velocity by grabbing easy user stories and leaving many stories abandoned or unfinished is called out as a behavior the counterbalanced-metrics combinations are designed to discourage.
- **Chronic failure to deliver value each iteration.** Occasionally missing some user stories is natural, but consistent, chronic failure to finish an iteration's backlog signals a problem — over-estimating work betrays a lack of insight into the team's real capacity.
- **Forcing Waterfall metrics onto Agile programs.** Requiring Waterfall-style reporting both impedes Agile adoption and execution and fails to give accurate insight into the software development process.
- **Operating without thresholds or targets.** As Case study 21 shows, using metrics while never setting acceptable performance levels leaves oversight bodies unable to judge whether the program is performing acceptably.
- **Reporting untraceable, unreliable metrics.** Case study 22 frames the absence of traceability between reported scope and the actual backlog as miscommunication that masks unreliable reporting and hides forecasting problems.

## Key Takeaways

- Pick metrics early, tailor them to the program's framework, needs, and audience, and make sure each is quantifiable, meaningful, repeatable, and actionable.
- Trace strategic goals down through the road map, releases, and prioritized backlog so metrics actually inform prioritization and re-planning.
- Keep product performance and development-team performance as distinct lenses; both matter to overall success.
- Use a balanced combination of counterbalancing metrics instead of optimizing any single one — velocity in particular is a team-internal planning aid, never a cross-team comparison.
- Lead time, cycle time, the cumulative flow diagram, and burn up/burn down charts are the recurring instruments for visualizing flow and progress.
- Automate metric capture where you can, but augment it with surveys and other sources for team dynamics and behaviors that tools cannot see; validate data for completeness and correctness.
- Tie metrics to team-based incentives, set target values and thresholds for critical metrics, and demand management commitment to act on what the data shows.
- Communicate performance information frequently, reliably, and visibly — through tools or information radiators — at a cadence that matches development, so corrective action stays timely.
- Confirm the metrics program against the closing Best Practices Checklist, which restates the six best practices as verifiable items.

## Connects To

- **Chapter 3 (Adopting Agile / organizational change)** — the source draws on chapter 3 for management commitment to performance information, the relevance-reliability-timeliness criteria for metrics, government-versus-contractor incentive differences, and the warning that weak or absent automated testing signals an organization still maturing in Agile.
- **Chapter 6 (Contractual obligations and execution)** — performance standards that set the government's expected accomplishment level, naming performance-monitoring metrics in the contract, and metrics for a team's adherence to Agile best practices are tied back to chapter 6.
- **Chapter 7 (Program management, EVM, and value)** — earned value management applied to Agile, the work breakdown structure tied to the Agile structure, cost/schedule variance tracking, technical-debt cost estimation, and determining a feature's added value all reference chapter 7.
- **External SE practice** — lead time, cycle time, cumulative flow diagrams, velocity, and burn up/burn down charts are common Lean/Agile flow and forecasting tools, making this chapter a bridge between GAO oversight expectations and standard Agile delivery measurement; the value sidebar itself synthesizes material from DOD, Scrum.org, and Premiere Agile.
