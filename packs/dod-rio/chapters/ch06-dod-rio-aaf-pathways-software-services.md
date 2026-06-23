# Chapter — Managing Risk by AAF Pathway: Software, Defense Business Systems, and Services

> **Scope note.** This chapter is the DoD-side, acquisition-policy complement to the more general,
> process-agnostic risk treatments in the `nasa-risk` and `dau-se-guidebook` packs. Where those
> packs teach risk *method*, this chapter shows how the DoD RIO guide tailors that method to three
> specific Adaptive Acquisition Framework (AAF) pathways — Software Acquisition, Defense Business
> Systems (DBS), and Acquisition of Services — each governed by its own DoD Instruction. Treat the
> activity lists here as suggested, tailorable practice, not mandatory checklists; the guide
> repeatedly stresses that programs adapt them to their Acquisition Strategy objectives.

## Core Idea

Risk management is not pathway-neutral. The same RIO discipline produces very different working
activities depending on *which* AAF pathway a program runs on, because each pathway has a
different cadence, a different decision structure, and a different governing instruction. This
chapter walks three of those pathways. The Software Acquisition pathway, governed by DoDI
5000.87, treats risk reduction as something baked into an iterative engineering pipeline —
automation, continuous test, and cybersecurity are persistent requirements rather than gates. The
DBS pathway, governed by DoDI 5000.75, frames risk around fitting commercial business systems to
re-engineered business processes through a sequence of Authorizations to Proceed (ATPs). The
Acquisition of Services pathway, governed by DoDI 5000.74, manages risk through a seven-step
team-and-requirements process where the hardest risk is writing a good requirement and then
verifying performance against it. The unifying move across all three: identify where the pathway's
mechanics create exposure, then attach risk-reducing activities to the phase where that exposure
actually lives.

## Frameworks Introduced (exact source names, when/how)

The slice names a number of concrete, citable artifacts and instruments. These are not invented for
the guide — they are external policy, tooling, or method references the guide directs programs to:

- **DoDI 5000.87, "Operation of the Software Acquisition Pathway"** — the instruction governing the
  Software Acquisition pathway; cited as the basis for the Capability Needs Statement (CNS) and the
  pathway's planning/execution structure.
- **Software Initial Capabilities Document (SW ICD), per JCIDS** — the alternative requirements
  basis to the CNS that can guide the Software Planning phase.
- **DoD Agile Metrics Guide (2020)** — recommended source for the agile metrics a software program
  should plan, so it can manage day-to-day Agile work (root-cause analysis, constraint
  identification, rapid learning).
- **"Test and evaluation as a continuum" (Collins 2023)** — a referenced concept used to argue for
  iterative methodologies with continuous, automated testing built in from the start.
- **Common Weakness Enumeration (CWE)** and **Common Attack Pattern Enumeration and Classification
  (CAPEC)** — named catalogs used to review a baseline architecture for weaknesses and attack
  susceptibility, so the architecture can be refined to shrink attack surface and mission impact.
- **Mission-Based Cyber Risk Assessments (MBCRAs)** — the analysis used to focus design and testing
  on the highest mission-consequence cyber risks.
- **Software Bill of Materials (sBOM)** — produced and maintained per release, with production
  automated.
- **Minimum Viable Product (MVP)** and **Minimum Viable Capability Release (MVCR)** — the two
  iterative-delivery milestones the pathway revolves around; the MVP is explicitly framed as a
  risk-reduction measure and can become the MVCR if fielded for operational use.
- **GAO Agile Assessment Guide (2020)** — GAO's guide on best practices for adopting and
  implementing Agile, cited as a source of best practices for the software pathway.
- **DoDI 5000.75, "Business Systems Requirements and Acquisition"** — the instruction governing the
  DBS pathway and its phase descriptions.
- **DoDI 7041.03, "Economic Analysis for Decision-Making"** — the basis for the economic analysis
  the cost agency uses to compare DBS solution alternatives.
- **Authorization to Proceed (ATP)** gates — Solution Analysis ATP, Functional Requirements ATP,
  Acquisition ATP, Limited Deployment ATP, and Full Deployment ATP — the decision structure of the
  Business Capability Acquisition Life Cycle.
- **Chief Management Office (CMO) certification** — the initial certification a CMO decision
  authority approves before the Acquisition ATP.
- **DOT&E Oversight List / IOT&E** — for business systems on that list, DOT&E approves operational
  test plans and an IOT&E runs before Full Deployment.
- **DoDI 5000.74** and the **"Seven Steps to the Service Acquisition Process"** — the instruction
  and process the Acquisition of Services pathway incorporates, organized into Plan, Develop, and
  Execute phases.
- **DAU Service Acquisition Mall (SAM)** and the Version 2.0 (2017) **Engineering Technical
  Services (ETS) acquisition guidebook** — named additional guidance for the services pathway.
- **Acquisition Requirements Roadmap Tool (ARRT)** — used to define and refine service requirements
  and draft the Performance Work Statement (PWS) and Quality Assurance Surveillance Plan (QASP).
- **Multi-Functional Team (MFT)** led by a **PM or Functional Services Manager (FSM)** — the team
  construct that drives the seven steps.
- **QASP, PWS, SOW, SOO, Service Delivery Summary (SDS), Contracting Officer's Representative
  (COR)/Contractor's Representative**, and the **Contractor Performance Assessment Reporting System
  (CPARS)** — the service-acquisition documents and roles used to specify, measure, and record
  contractor performance.
- The **simplified acquisition threshold (SAT)** — the dollar trigger that scopes which service
  acquisitions use this pathway.

## Key Concepts

**The Software pathway makes automation a precondition, not an afterthought.** The guide is blunt
that software development infrastructure — a software factory, continuous integration, automated
unit tests, automated static analysis, automated deployment — should exist at the program's start.
Standing it up late is treated as a velocity-killer that undermines the program's agility. Test and
evaluation as a continuum depends on that automation being present early.

**Two interlocking timelines: the planning/execution split and the MVP→MVCR delivery loop.** The
software pathway has a Planning phase (understand needs, develop strategies, build the roadmap,
engage users, design architecture, stand up infrastructure, set cybersecurity and enterprise-service
approaches) and an Execution phase that iterates: plan iteration, code, build, test, iterate,
release, refine the MVP, monitor, reach an MVCR, and operate. The MVP is a deliberate risk-reduction
artifact whose definition is allowed to evolve; insights from MVP feedback shape the MVCR. There is
an explicit one-year time constraint tied to achieving the MVCR, and the program must keep
re-identifying what sits on the critical path to it as iterations close.

**Cybersecurity is woven through every software activity, not isolated to one phase.** The slice
threads secure design and coding standards, threat modeling, static analysis, software composition
analysis (SCA), dynamic analysis, vulnerability detection and remediation, chain-of-custody review
from development through sustainment, penetration testing, recurring assessments of the development
environment, and MBCRAs across planning, coding, testing, releasing, and monitoring. The recurring
pattern is detect → prioritize → remediate, with automation maintained as a standing capability.

**The User Agreement (UA) is the risk-bearing commitment device for software.** Because the pathway
depends on continuous user involvement, the guide makes the UA the instrument that locks in
resourcing of operational users and assigns decision authority over capability prioritization,
feature/cadence trade-offs, user acceptance, and readiness for deployment. Without that committed
involvement, the iterative feedback loop the pathway relies on degrades.

**DBS risk is governed by ATP gates over a business-process re-engineering arc.** The DBS pathway
moves through Capability Need Identification, Solution Analysis, Functional Requirements and
Acquisition Planning, Acquisition/Testing/Deployment, and Capability Support. The central technical
act is re-engineering high-level future business processes and selecting/tailoring commercial best
practices to fit them — captured in "to-be" capability process maps. A **fit-gap analysis** against
the known capabilities of the chosen COTS/GOTS solution then drives design specs and lets the
program trade cost and schedule within scope. Funding availability must be validated before the
Functional Requirements ATP, and deployment is staged: a Limited Deployment (a subset of
functionality to a subset of users, approved at a Limited Deployment ATP) precedes Full Deployment.

**Services risk lives in the requirement and in performance management.** The slice states plainly
that defining the requirement is both the single most important step and the hardest one in a
services acquisition, because a well-written requirements document is what makes the service
procurable and manageable. The pathway uses
the seven steps — form the team, review current strategy, perform market research, define
requirements, develop the acquisition strategy, execute the strategy, manage performance — and
leans on the QASP and incentive arrangements to make contractor performance measurable. Step Seven
splits into contract administration mechanics and relationship management among customers,
stakeholders, and the contractor, with performance documented annually in CPARS.

## Mental Models

**Pathway as risk-shaping force.** Don't ask "what is my risk process?" first; ask "what pathway am
I on, and what does that pathway's mechanics expose me to?" The software pathway exposes you to
velocity loss from missing automation and to accumulating technical debt across iterations. The DBS
pathway exposes you to misfit between a commercial product and your business processes (which is why
fit-gap analysis is central) and to funding gaps at ATP boundaries. The services pathway exposes you
to vague requirements and to unmeasured contractor performance.

**Technical debt as a tracked, recurring liability.** In the software Execution phase the guide
treats technical debt almost like a risk register entry: review last iteration's debt for resolution
this iteration, actively manage it against life-cycle objectives, track its accumulation when
re-prioritizing the backlog, and use prior-iteration knowledge to keep developing without piling on
more debt. Debt is something you carry forward and pay down deliberately, not a one-time cleanup.

**The MVP as an experiment you can field.** Frame the MVP as a hypothesis about user value that is
cheap to test and explicitly counts as risk reduction. Deploying it to real user environments yields
feedback that defines the MVCR — and if it proves sufficient for operational use, the MVP *becomes*
the MVCR. The model is "learn by fielding small," not "perfect then release."

**"Rainy day" coverage as a resilience contract.** For software testing, the guide expects the
stressing and degraded conditions — reduced or disrupted communications, failover, bad data from
upstream systems — to be mandatory test coverage, alongside the operationally relevant and
scalability cases. The mental model: every resilient mode you designed in must be a mode you test.

**Fit-gap before design.** For DBS, the model is to select the solution, then measure the gap
between what the COTS/GOTS product already does and what the re-engineered process needs, and let
that gap — prioritized — drive design specs and cost/schedule trades. You design to the gap, not
from scratch.

**Trust-and-measurement as the services control loop.** For services, the model pairs an environment
of trust and fair dealing among the three parties with hard measurement through the QASP and CPARS.
The relationship keeps everyone aimed at the mission outcome; the documentation keeps performance
honest and on the record.

## Key Takeaways

- The RIO discipline is constant, but its concrete activities are pathway-specific; the governing
  DoD Instruction (5000.87 / 5000.75 / 5000.74) sets the structure within which risk gets managed.
- For software, build the automated pipeline and continuous-test/cyber capability up front — treating
  them as persistent requirements is itself the primary risk-reduction strategy, and deferring them
  costs velocity.
- The MVP→MVCR loop, the one-year MVCR critical-path constraint, the User Agreement, and disciplined
  technical-debt tracking are the software pathway's core risk levers.
- Cybersecurity for software is end-to-end: standards, threat modeling, SCA/static/dynamic analysis,
  chain-of-custody, penetration testing, MBCRAs, and automated, maintained vulnerability scanning —
  applied continuously, not at a single checkpoint.
- For DBS, risk turns on re-engineering business processes, fitting a commercial solution to them via
  fit-gap analysis, validating funding before the Functional Requirements ATP, and staging Limited
  before Full Deployment with appropriate (and for oversight-list systems, DOT&E-approved) testing.
- For services, the requirement is the risk: use ARRT to build the PWS and QASP, get the acquisition
  strategy reviewed for sound business sense and competition, and manage performance against the QASP
  with annual CPARS documentation.
- All three pathways close the loop with a self-check: the software section literally instructs
  programs to ask, for each suggested practice they skip, whether skipping it introduces risk to
  software development and delivery — a built-in tailoring-with-justification habit.

## Anti-patterns

The source does not present a labeled anti-pattern list. It does, however, name specific
consequences of omission that function as cautions, and these can be read as practices-to-avoid:

- **Deferring automation.** The guide states that not embedding automation at the program's start
  causes inefficiency and constrains the program's velocity and agile efficacy.
- **Leaving constraints unidentified.** It notes that unidentified and unaddressed constraints on the
  development effort will limit velocity.
- **Skipping a suggested practice without examining the risk.** The software risk-reduction section
  frames an explicit self-interrogation: if the program is not following a suggested practice, it
  should ask whether ignoring it creates risk to software development and delivery — implying that
  unexamined omission is the failure mode to avoid.

Beyond these source-named cautions, no further anti-patterns are asserted here.

## Connects To

- **`nasa-risk`** — the general continuous risk-management process (identify, analyze, plan, track,
  control, communicate) that this chapter specializes to DoD acquisition pathways. NASA's
  process-level treatment is the method; the RIO pathway activities are the DoD-acquisition
  application. Use NASA's risk-matrix and likelihood/consequence machinery underneath these pathway
  activity lists.
- **`dau-se-guidebook`** — the DoD systems-engineering process companion. The SE technical reviews,
  architecture, and T&E concepts in that pack underlie the software pathway's design-architecture,
  build, and test activities; "test and evaluation as a continuum" and MOSA appear in both.
- **Other chapters of this pack** — the foundational RIO definitions (risk vs. issue vs.
  opportunity), the assessment and handling steps, and the program-level risk register all feed the
  pathway-specific activities here; this chapter assumes that core RIO vocabulary and applies it by
  pathway.
- **MOSA / modular-open-systems material** — the modular open systems approach the software pathway
  calls for (and the DBS interoperability concerns) connects to any modularity or open-architecture
  pack in the broader SE library.
- **Cybersecurity and software-assurance references** — CWE, CAPEC, SCA, sBOM, and MBCRA tie this
  chapter to dedicated software-assurance and cyber-survivability material; the guide treats these as
  named external instruments rather than re-deriving them.
