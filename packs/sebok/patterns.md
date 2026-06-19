# SEBoK Patterns & Techniques

## System Context Modelling
**When to use**: At project inception, before fixing requirements, to position the system-of-interest (SoI) within its socio-technical environment.
**How**: Define the SoI boundary by what you can change vs. what stays fixed; map external elements crossing the boundary (environment, enabling systems, organizational/meta-system layers, stakeholders); choose narrow- vs. wide-SoI deliberately.
**Trade-offs**: Fixing the boundary too early locks you into the wrong solution space; modelling context costs effort that product-only teams skip, but skipping it surfaces integration surprises at deployment.

## Mission–Goals–Objectives (MGO) + Measures of Effectiveness
**When to use**: To establish strategic intent and validatable success criteria during business/mission analysis.
**How**: State mission ("why"), decompose into goals (achievable pieces), then objectives (concrete "what"); attach Measures of Effectiveness (MOE) and measures of success; characterize green-field (blank-slate as-is/to-be) vs. brown-field (legacy-constrained).
**Trade-offs**: Weak or unmeasurable MOEs optimize the wrong thing; over-specifying intent under high uncertainty is premature when the right question is still "what's going on here?"

## Functional vs. Physical Architecture Decomposition
**When to use**: When deriving an implementation-independent design before allocating to hardware/software/people.
**How**: Build the logical architecture (functions as y=f(x,t), input-output flows, control-flow triggers, scenarios, operational modes) first; then a physical architecture; allocate functions to system elements (~5±2 per level) using affinity/partitioning criteria.
**Trade-offs**: Jumping straight to technology loses multidisciplinary comprehension and traceability; over-decomposing or static-only hierarchies obscure dynamic behaviour; skipping logical architecture for "known" products breaks when the domain set changes.

## Architecture Viewpoints & Frameworks
**When to use**: When stakeholders have distinct concerns and you need traceable, navigable model coverage.
**How**: Per ISO 42010 / IEEE 1471, define viewpoints (conventions) and generate views addressing each concern; organize via an architecture framework (Zachman, DoDAF, FEAF, TOGAF) so missing information and cross-links are visible.
**Trade-offs**: Frameworks add governance overhead and can become disconnected artifacts unless driven by business questions; static frameworks struggle with dynamically reconfiguring services.

## Model-Based Systems Engineering (MBSE)
**When to use**: For complex systems needing a single source of truth, live traceability, and integrated requirements-to-architecture flow.
**How**: Use a formal language (SysML) as the authoritative baseline; manage it under configuration management with a process framework; match formality/fidelity to system criticality; integrate descriptive, analytical, and executable models for semantic interoperability.
**Trade-offs**: Models decay without enforced updates; over-formalizing simple systems wastes effort; tools-without-organizational-change yields models-as-documentation, defeating the purpose.

## Black-Box / White-Box Modelling
**When to use**: To control abstraction level when specifying vs. designing.
**How**: Use black-box views to fix external behaviour and interfaces (solution-neutral); switch to white-box to reveal internal structure once decomposition is warranted. Set model scope by breadth, depth, fidelity.
**Trade-offs**: Over-modelling adds maintenance burden without value; isolated multi-domain models that lack semantic interoperability hide integration failures until late.

## Trade Studies (MODA / Value-Focused Thinking)
**When to use**: For multi-criteria decisions across performance, cost, schedule, risk.
**How**: Decompose into objectives, measures, alternatives, value functions; assign swing weights; map walk-away points to 0 and stretch goals to 100; use an additive value model. Generate alternatives from value criteria (value-focused), not just score pre-existing ones.
**Trade-offs**: Formal scoring is still vulnerable to confirmation/optimism bias and rankism; needs structural guard rails (independent review, premortem). Garbage-in data invalidates the result.

## Set-Based Design (SBD)
**When to use**: Early design under uncertainty with a large tradespace and competing disciplines.
**How**: Treat design factors as sets; explore multiple alternatives in parallel; progressively narrow the feasible tradespace using feasibility/performance/cost data (dominance, Pareto frontier, sensitivity). Protect set drivers; adapt set modifiers for new missions.
**Trade-offs**: Converging to a point solution too early throws away SBD's value; running parallel sets costs more upfront than committing to one design.

## Risk-Based Process Tailoring
**When to use**: On every project — standard process sets are never applied as-is.
**How**: Adjust 15288/24748 process rigor to context using scaling factors (size, safety level, novelty, mission criticality, certification, team distribution/skill, domain/solution complexity); document rationale; reassess continuously, not once.
**Trade-offs**: Over-engineering ("all processes to be safe") wastes cost; reusing another project's baseline blindly mismatches conditions; letting tool limits drive process inverts the dependency.

## Life Cycle Model Selection & Adaptation
**When to use**: When choosing/adapting sequential, incremental, evolutionary, or agile approaches per project and per element.
**How**: Drive selection by risk and requirements clarity (PMI Situation Context Framework); allow domain-specific models (hardware vs. software) with synchronization intervals; adapt entry/exit criteria; get acquirer–supplier agreement; review against KPIs over time.
**Trade-offs**: Synchronization too short adds overhead, too long invites incompatible interface assumptions; treating models as static or selecting in isolation from enabling systems increases risk.

## Agile SE Cadence
**When to use**: Dynamic environments with evolving knowledge, where increments yield early feedback.
**How**: Time-boxed iterations producing deliverable increments; modular loosely-coupled architecture; continuous integration; adaptive planning; learning iterations for exploration; commitment reviews (ICSM) gate each cycle on evidence.
**Trade-offs**: Not a silver bullet for safety-critical/hardware cycles; "agile = less documentation" loses traceability; ceremonies without decision-making speed, or monolithic architecture, give agility without effect.

## Decision Gates / Technical Reviews
**When to use**: At lifecycle transition points to assess progress and authorize proceed/pause/terminate.
**How**: Hold reviews (PDR/SRR/TRR etc.) against pre-agreed entry/exit criteria; choose timing strategy (schedule-, event-, or evidence-based per Boehm & Lane); balance reviewer mix between close-enough-for-insight and independent-enough-for-objectivity.
**Trade-offs**: Reviews under schedule pressure with unmet entry criteria miss defects; no clear criteria makes them subjective; wrong reviewer mix kills independence.

## Requirements Management & Bidirectional Traceability
**When to use**: Throughout the lifecycle to keep needs, design, and verification linked.
**How**: Elicit → allocate → baseline → control changes; maintain bidirectional links from stakeholder sources through requirements to verification artifacts (tests/inspections/analyses); baseline just-in-time.
**Trade-offs**: Too-early baselining guarantees high change volume and rework; skipping traceability in iterative work loses institutional memory and impact analysis.

## Configuration Management & Baselines
**When to use**: Whenever multiple versions, teams, or lifecycle changes must stay consistent.
**How**: Identify configuration items, baseline them, control changes via CCB/engineering change requests, status-account and audit; enforce form-fit-function-interface (F3I) compatibility on upgrades.
**Trade-offs**: Orphaned baselines across many changes lose features and break integration; CM is overhead small projects under-resource until a regression bites.

## Risk Management (Full Treatment Set)
**When to use**: Continuously, to reduce risks below acceptable thresholds before they occur.
**How**: Plan → identify → analyze → treat → monitor; evaluate all treatment options (assumption, avoidance, control/mitigation, transfer) rather than defaulting to mitigation; address root causes, not recurring instances. Include opportunity (positive uncertainty) management at portfolio level.
**Trade-offs**: Automatic mitigation wastes resources when transfer/avoidance is superior; band-aid treatment accumulates systemic risk; risk-only frameworks miss opportunities.

## Interface Definition (ICD/IDD)
**When to use**: At every component boundary in product and SoS integration.
**How**: Baseline interfaces in an Interface Control Document / Interface Design Description capturing interactions (data, material, energy) AND relationships (spatial, temporal, social, organizational); verify components against it during integration.
**Trade-offs**: Treating interfaces as mere physical connections misses non-interactive relationships and organizational failure modes.

## Reliability/Safety Analysis (FMECA, FTA, RBD)
**When to use**: When quality attributes (reliability, availability, safety) must be designed in, not tested in.
**How**: FMECA tables identify failure modes, effects, and criticality (likelihood × severity) to prioritize; FTA decomposes top-level failure top-down via AND/OR/K-of-N gates; RBD models success paths and redundancy (series/parallel/k-of-n). Follow the RAM lifecycle; account for censored ("survival") data.
**Trade-offs**: Treating reliability as a testing problem can't prove absence of unintended functionality; ignoring censored data biases estimates upward; single-layer mitigations expose new attack surfaces (use mitigation-in-depth).

## Loss-Driven SE & Defense-in-Depth
**When to use**: When safety, security, resilience, and reliability concerns overlap and are otherwise siloed.
**How**: Unify loss-driven specialty areas via shared loss scenarios; apply hazard control, loss margins, protective failure, anomaly detection, and layered defense-in-depth; model loss scenarios explicitly in MBSE artifacts.
**Trade-offs**: Treating specialty areas in isolation yields redundant requirements and conflicting solutions; bolting loss concerns onto capability-focused 15288 late is expensive.

## SoS Governance via Trust & Contract Architectures
**When to use**: For systems of systems with operationally and managerially independent constituents.
**How**: Replace hierarchical control with governance through trust, influence, and contracts; make interface governance the primary control; use Mission Engineering threads to evaluate end-to-end effects; iterate via the SoS Wave Model; classify regimes with Cynefin.
**Trade-offs**: Expecting central control generates friction; ignoring constituent motivations breeds resistance; optimizing constituents in isolation degrades the whole; boundary ambiguity yields unpredictable emergence.

## Cost Estimating (Analogy / Parametric / Build-Up)
**When to use**: To translate requirements into defensible budgets across the lifecycle.
**How**: Follow the seven-step process (WBS → technical baseline → collect → analyze → apply CERs → roll-up/validate → report); pick analogy, parametric (calibrated CERs), or bottom-up build-up; refresh at major milestones; use a multidisciplinary team.
**Trade-offs**: Analogy without cost-driver adjustment, uncalibrated CERs, or expert opinion as the primary method all lack credibility; frozen estimates mask risk; finance-only teams miss technical/integration costs.

## Work Breakdown Structure (WBS)
**When to use**: To anchor scope, cost, schedule, and responsibility for any project.
**How**: Decompose deliverable-oriented work into a tree (per MIL-STD-881) with a WBS dictionary defining terms; map elements to components/capabilities; aggregate cost and assign accountability.
**Trade-offs**: A WBS organized by org chart rather than deliverables fragments scope; it captures structure but not dynamic behaviour or interfaces.

## Human Systems Integration (HSI)
**When to use**: When human performance materially affects mission outcome, suitability, and cost.
**How**: Coordinate the seven HSI domains (manpower, personnel, training, human factors engineering, safety & occupational health, force protection/survivability, habitability) with cross-domain trade-offs; decompose MOEs into human-specific MOPs/MOSs.
**Trade-offs**: Assigning HSI to a human-factors engineer without SE authority relegates it to a specialty; deferring human considerations to post-design training yields high manpower cost and poor usability.

## Soft-Systems / Critical-Systems Methods
**When to use**: For wicked, contested, ill-defined "problematic situations" with conflicting worldviews.
**How**: Apply Soft Systems Methodology (participatory, learning-oriented) when goals are contested; use Critical Systems Thinking to judge when to deploy hard vs. soft methods and combine them; engage politics/values rather than erasing them.
**Trade-offs**: Hard optimization on socio-political problems fails; soft methods trade quantitative rigor for stakeholder learning and may feel inconclusive to engineers expecting a single answer.
