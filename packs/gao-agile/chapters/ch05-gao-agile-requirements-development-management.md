# Chapter — Requirements Development and Management in Agile

## Core Idea

Sound requirements practice is decisive for any program, and iterative,
incremental approaches such as Agile do not relax that need — they relocate
it. Where Waterfall front-loads a fixed, fully specified requirement set,
Agile commits to a much shorter up-front planning window and then sustains
an ongoing discipline of eliciting, refining, and managing requirements as
understanding grows. This chapter (GAO-24-105506, Chapter 5) translates the
traditional requirements-development and requirements-management activities
GAO has documented across its prior body of work into the Agile setting, and
shows an auditor where the techniques, work products, and cadence change so
that compliance with existing best practices can still be assessed. The
central premise is that requirements in Agile are least understood at the
outset; programs are expected to learn as they go, and the practices exist to
make that learning visible, traceable, and tied back to the commitments a
program made to its oversight bodies.

A vocabulary caution frames everything: the guide uses "requirements" as an
umbrella term because it is widely understood from Waterfall, but Agile teams
rarely use the word at all. They substitute terms like *epic* or *user
story*, which may stand for a capability, a feature, a sub-feature, or a more
granular expectation. Because terminology varies by organization, GAO stresses
that each team must define its terms explicitly and apply them consistently —
otherwise traceability and assessment break down. The terms also map to
planning horizons: an epic or feature tends to be discussed and committed for
a release, while an iteration concentrates on the individual user stories that
compose that feature or epic.

## Frameworks Introduced (exact source names, when/how)

- **GAO Agile Assessment Guide (GAO-24-105506)** — the document this chapter
  belongs to. It enumerates eight requirements best practices (listed under
  Key Concepts) and provides a summary table (Table 6) and an overview figure
  (Figure 7). The practices are attributed to *GAO analysis of CMMI v. 1.3,
  PMI, and SEI documentation*.
- **CMMI v. 1.3, PMI (Project Management Institute), and SEI (Software
  Engineering Institute) documentation** — named as the analytical basis from
  which the Agile requirements best practices were derived.
- **Minimum viable product (MVP)** — introduced as a concept popularized in
  Eric Ries' 2011 book *The Lean Startup* (Crown Publishing Group). Presented
  as a working version of the product built with the least effort needed to
  learn from and interact with customers, surface their real needs, and refine
  direction early when changes are still cheap. The guide explicitly warns that
  an MVP is only useful if it is developed enough to allow real customer
  interaction and feedback — it is not merely the smallest slice of
  functionality.
- **Spike** — introduced as a technique derived from eXtreme Programming (XP).
  A spike is a placeholder user story representing research a team must do —
  to resolve a design question or an unfamiliar technical challenge — before it
  can size a story it cannot yet estimate.
- **Scrum** (product backlog of ordered items on a task board, with per-
  iteration commitments) and **Kanban** (continuous flow on a Kanban board
  that is not reset, deemphasizing time-boxed iterations) — named as two
  alternative methods a team may choose, since Agile values and principles
  guide *what* to do but do not prescribe a single requirements method.
- **Five levels of Agile planning** (referenced from Chapter 4) — vision at the
  top through daily work at the bottom — used here to position where epics,
  features, user stories, and tasks live.
- **Requirements traceability matrix (RTM)** — named as the Waterfall mechanism
  for demonstrating traceability; in Agile it is replaced by traceability
  through artifacts such as the road map and the backlog.

Several real programs are introduced as illustrative cases:

- **Agile in Action 2 — NNSA G2** (National Nuclear Security Administration,
  Program Management Information System Generation 2): a four-level
  requirements hierarchy (road map → feature → user story → task) observed
  during July 2016 release planning, with WBS numbering for traceability.
- **Case study 12 — Space C2** (GAO-23-105920, June 2023): absence of a
  program-level backlog.
- **Case study 13 — TSA TIM** (Technology Infrastructure Modernization,
  GAO-18-46, Oct. 2017): backlogs lacking prioritization levels.
- **Case study 14 — DHS / ICE SEVIS** (GAO-20-213, June 2020): a worked
  definition of done.
- **Case study 15 — DHS/TSA TIM descope** (GAO-20-170SP, Dec. 2019):
  re-scoping full operational capability.
- **Case study 16 — ICE SEVIS traceability** (GAO-20-213, June 2020):
  user-story-to-capability traceability in a backlog.

## Key Concepts

**The eight requirements best practices.** The chapter is organized around
eight named practices, each summarized in Table 6 and re-stated in a closing
checklist:

1. **Elicit and prioritize requirements.**
2. **Refine requirements.**
3. **Ensure requirements are complete, feasible, and verifiable** (stated more
   fully as sufficiently complete, feasible, and verifiable for the program's
   current state).
4. **Balance customer and user needs and constraints.**
5. **Test and validate the system as it is being developed.**
6. **Manage and refine requirements.**
7. **Maintain traceability in requirements decomposition.**
8. **Ensure work is contributing to the completion of requirements.**

**Progressive decomposition across governance layers.** After a vision is set,
a program elicits a preliminary, deliberately general set of operating
requirements from users — possibly informed by early discovery-level user
research — using surveys, face-to-face discussion, or mixed user-research
techniques. At this stage requirements are still vague and are called *epics*,
grouped into themes. As work for a theme or epic approaches in the near term,
the program decomposes it into smaller, more granular efforts so teams can
plan and execute, with the end goal of a set of user stories the team and
product owner can routinely discuss. Different governance bodies may receive
different levels of specificity. For instance, operating requirements might be
committed at a departmental investment review board; capabilities then get
refined at the component review board; features are worked out in detail with
an integrated program team; and the user stories are settled with a product
owner — each of these commitments reflected in a matching artifact (road map,
release plan, backlog).

**Product owner autonomy.** Once a governance body has agreed to a vision and
its epics, the product owner should be free to rank requirements without
returning to that body for approval. Constraining this autonomy is treated as
a program risk that can delay delivery of functionality.

**Strategic vs. tactical requirements.** A footnote frames requirements as
both strategic (the higher-level set that justifies a program, to which a work
breakdown structure and a form of earned value measurement can be assigned)
and tactical (the lower-level features that customers and stakeholders want).

**Functional vs. non-functional requirements.** Agile's emphasis on user-
facing functionality (e.g., search, data aggregation) can cause underlying
non-functional requirements to be overlooked — the example given is failing to
account for privacy when building a search feature. Non-functional
requirements can be derived from regulations or elicited by coordinating with
other organizational groups such as security or privacy. Two capture options
are offered: define each non-functional requirement as a discrete user story
tracing to a non-functional feature (e.g., architecture), or fold them into
the definition of done / acceptance criteria for functional requirements (for
example, requiring a demonstrated load or stress test before acceptance). Some
non-functional testing (performance, customer satisfaction) may be done
outside the iteration, just before release, with the noted risk that deferring
such tests lets hidden problems propagate until they are very hard to find.

**Definition of done, acceptance criteria, and definition of ready.** Before
development, a team defines what "done" means; multiple teams on one system or
release should agree on a mutual definition of done, and definitions mature
over time. Acceptance criteria are specific to a single user story and capture
the product owner's requirements for that story; the definition of done
applies to all user stories and bundles acceptance plus extra activities such
as testing or compliance checks (the chapter cites Section 508 accessibility
compliance as an example criterion). A definition of ready sets the level of
detail required before work may begin on a story — for instance, that its
relative complexity is estimated and its acceptance criteria are written.
Without clear definitions of ready, acceptance, and done, teams risk working
inefficiently on lower-ranked requirements.

**Value-based prioritization and the prioritized backlog.** Requirement value
is subjective and is generally left to the product owner, who should have a
consistent process for valuing work so that stories are developed by relative
value. A clarifying footnote distinguishes "priority" (relative value to an
iteration or project at a point in time, as judged by the product owner) from
importance — a product owner might prioritize higher-risk but lower-importance
work to retire risk early. Higher-priority stories are usually clearer and more
detailed, enabling more precise estimates; lower-order stories carry less
detail. Stories not completed in a release stay in the backlog and can be
reprioritized.

**Continuous integration and automated testing.** Teams routinely build and
test through continuous integration — repeatedly merging all developers'
working copies many times a day via an automated process. Its strength depends
entirely on the automated testing in the build; a failed build should be fixed
and resubmitted. Good-quality code can still miss the original user story's
requirements, which is why acceptance criteria and definition of done create a
shared understanding of completeness.

**Validation beyond product owner acceptance.** Validation occurs through story
demonstrations or end-of-iteration reviews, where users and customers can
observe functionality and judge fit. The chapter is explicit that product owner
acceptance does not by itself mean a story was adequately tested to traditional
standards or that it meets user intent — assurance often requires usability
testing with real users at regular intervals to supplement demonstrations.

**Backlog as a living record and traceability.** Requirements live in the
prioritized backlog, which is never complete and is never empty while the
program exists (even if a development contract ends, the system and backlog
persist). It holds user stories for new functionality plus bugs/defects
representing revisions, spanning functional and non-functional requirements.
Well-managed requirements trace from a source requirement down to lower-level
requirements and back again, so a program can confirm all sources are
addressed and all lower-level items trace to a valid source. In place of a
Waterfall RTM, Agile traces through artifacts like the road map and backlog,
and the product owner uses that trace to justify each iteration's value to
oversight groups.

**Work-to-commitment alignment.** Agile measures progress by working software
delivered against an iteration goal. Teams should work only on tasks that
contribute to the user stories committed for that iteration; unrelated work
(the example given is a tiger team pulled off to fix another team's issue) is a
misalignment and a program risk. Kanban teams, which do not time-box, still pull
stories on a flow basis and keep all work contributing to a story on the board.
At the planning level, a management plan — in Agile, a program or release road
map laying capabilities/features across a timeline — should keep developed
stories aligned with the scope committed to oversight bodies.

## Mental Models

- **Requirements as a deferral curve, not a fixed contract.** Detail is
  intentionally lowest at the start and increases just-in-time as work
  approaches. The further down the backlog, the vaguer the item and the
  coarser the estimate; clarity and estimate precision rise together as a
  story is pulled toward the top.
- **The governance ladder mirrors the requirements ladder.** Each altitude of
  requirement (operating requirement → capability → feature/sub-feature → user
  story) maps to a governance touchpoint and a corresponding artifact (road
  map → release plan → backlog). Assessing a program means checking that these
  layers line up.
- **Done as a two-tier gate.** Acceptance criteria are the per-story gate;
  the definition of done is the universal gate layered on top. A story is only
  truly complete when it clears both, plus any bundled compliance and testing
  activities.
- **Priority is value at a moment, not permanent worth.** Ranking expresses
  relative value to the current iteration, reassessed continually; a lower rank
  does not diminish a stakeholder's underlying need.
- **The backlog is a ledger of intent.** It is the historical record of every
  proposed requirement and modification. If feedback from reviews is not
  captured there, the program loses its memory of what was asked for and why,
  and decision makers lose insight into delivered value.
- **Optionality as a benefit of continuous discovery.** Because functionality
  is built to match continuously refined requirements, the organization
  retains the option to stop the program at any point if the system no longer
  serves the vision — value to date is preserved if highest-value work was done
  first.
- **MVP as a learning instrument.** The MVP's purpose is to elicit feedback and
  learning, not to ship the minimum; an MVP too thin for real interaction
  fails its only job.

## Anti-patterns

The chapter names several failure modes tied to specific practices:

- **No strong commitment to ongoing elicitation/refinement** — delivered
  software may not meet the changing needs of the organization, users, and
  technical landscape.
- **No process to capture review feedback** — no historical record of proposed
  requirements or modifications, and a missing/undocumented change-control
  process that obscures the true value of delivered features for decision
  makers.
- **Functionality focus that crowds out non-functional requirements** —
  underlying system needs (e.g., privacy on a search feature) go unnoticed.
- **Deferring non-functional testing carelessly** — performance and similar
  problems can propagate to the point of being nearly impossible to locate.
- **Missing or unclear definitions of ready/acceptance/done** — uncertainty in
  development; teams work inefficiently on lower-ranked requirements.
- **Ignoring relative value when sequencing** — critical user stories slip to
  just before deployment; if funding is cut mid-iteration, mid-release, or
  mid-program, users are left without necessary functionality. (Case study 12,
  Space C2: no program-level backlog, raising the risk of delivering apps that
  miss users' most critical needs; Case study 13, TSA TIM: backlogs without
  prioritization levels, risking misaligned functionality.)
- **Refinement process too inflexible** — it becomes a change-prevention
  process and user needs are not incorporated.
- **Refinement process too flexible** — boundless development; the organization
  may not get the value it requires.
- **An empty backlog while a program is still active** — the backlog should
  never be empty unless the program is formally ended.
- **Treating product owner acceptance as full validation** — without real
  user/customer involvement and usability testing, software may not meet its
  intended purpose.
- **Working off-commitment** — any work not tied to the iteration's committed
  user stories is a misalignment between requirements and work and a program
  risk.

## Key Takeaways

- Agile compresses up-front requirements planning but replaces it with a
  sustained discipline of elicitation, refinement, and management; the eight
  best practices (and the closing checklist) are how GAO assesses whether that
  discipline is in place.
- "Requirements" is a Waterfall-rooted umbrella term; Agile programs must
  define and consistently apply their own terms (epic, feature, user story,
  task) for traceability and assessment to work.
- Requirements decompose progressively across governance layers, each with a
  matching artifact; the product owner must retain autonomy to rank
  requirements once vision and epics are agreed.
- Non-functional requirements need deliberate capture — as discrete stories or
  folded into the definition of done — because a functionality focus tends to
  hide them.
- Definition of ready, acceptance criteria, and definition of done together
  define when work may start and when it is complete; acceptance criteria are
  per-story, the definition of done is universal.
- Prioritization is value-based and continual; highest-value work goes first so
  the customer still benefits if funding ends, and the backlog is a never-empty
  living ledger.
- Continuous integration plus automated testing build and test routinely, but
  product owner acceptance is not full validation — usability testing with real
  users supplements it.
- Traceability replaces the Waterfall RTM with road map and backlog artifacts,
  letting the product owner justify each iteration's value to oversight bodies
  and keep work aligned to committed scope.

## Connects To

- **Chapter 3 (this guide)** — risks of not modifying acquisition and software
  life-cycle processes for Agile; "Organizational processes support Agile
  methods"; "Technical environment enables Agile development" (non-functional
  requirements and the automated-testing environment).
- **Chapter 4 (this guide)** — the five levels of Agile planning that position
  vision, epics, features, user stories, and tasks.
- **Chapter 6 (this guide)** — structuring a contract to allow requirements
  flexibility during development, and balancing too-flexible vs. too-inflexible
  refinement from a contracting perspective.
- **Chapter 7 (this guide)** — estimating cost and schedule, building on how
  requirements are defined and decomposed into a program plan.
- **CMMI v. 1.3, PMI, and SEI documentation** — the source frameworks GAO
  analyzed to derive the Agile requirements best practices.
- **The Lean Startup (Eric Ries, 2011)** — origin of the MVP concept.
- **eXtreme Programming (XP)** — origin of the spike technique.
- **Scrum and Kanban** — the two named method choices for organizing
  requirements work (committed product backlogs vs. continuous flow).
- **Prior GAO requirements work** — the broader body GAO cites for traditional
  requirements development and management activities, adapted here for Agile.
