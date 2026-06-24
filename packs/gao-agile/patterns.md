# GAO Agile Assessment Guide Patterns & Techniques

Reusable patterns drawn from GAO-24-105506 — each with when to reach for it, how to
apply it, and the trade-offs the guide flags. Wording is synthesized from the source.

## 1. Adopt Agile incrementally across the three perspectives

- **When**: an organization is moving off Waterfall and is tempted to flip every practice
  at once.
- **How**: treat the best practices as one interlocking system spanning team dynamics,
  program operations, and the organization environment. Prioritize the highest-value
  practices and pick them *across* all three rings rather than finishing one ring first.
  Where a practice is dropped, have officials record the risk they are accepting.
- **Trade-offs**: changing everything simultaneously creates unmanageable disruption;
  going too slowly leaves a half-Waterfall, half-Agile mix that confuses staff. (ch03)

## 2. Decompose requirements progressively and keep them traceable

- **When**: defining what to build without front-loading a fixed, complete spec.
- **How**: start from a vision, elicit deliberately general operating requirements (epics)
  grouped into themes, then decompose just-in-time as work approaches: capabilities →
  features → user stories → tasks. Map each altitude to a governance touchpoint and a
  matching artifact (road map, release plan, backlog). Trace every story back to a source
  requirement so the product owner can justify each iteration's value to oversight.
- **Trade-offs**: too rigid a refinement process becomes change-*prevention* and starves
  user needs; too loose invites boundless development that never delivers required value. (ch05)

## 3. Make work "done" with a two-tier gate

- **When**: teams disagree on whether a story is complete, or compliance keeps slipping.
- **How**: write per-story **acceptance criteria** (the product owner's conditions for that
  one story) and a universal **definition of done** layered on top (acceptance plus testing,
  Section 508 accessibility, security, and other bundled activities). Add a **definition of
  ready** so work starts only on stories that are estimated and have criteria written.
  Multiple teams on one release should agree a shared definition of done.
- **Trade-offs**: vague or missing definitions leave teams working inefficiently on
  lower-ranked items; product owner acceptance alone is not full validation — supplement it
  with real-user usability testing. (ch05)

## 4. Capture non-functional requirements deliberately

- **When**: a functionality focus (search, aggregation) risks hiding underlying needs.
- **How**: derive non-functional needs from regulations or by coordinating with security
  and privacy groups, then either define each as a discrete story tracing to a
  non-functional feature, or fold them into the definition of done (e.g., require a passing
  load or stress test before acceptance).
- **Trade-offs**: deferring non-functional testing to just before release lets hidden
  problems propagate until they are very hard to locate. (ch05)

## 5. Size with relative estimation, but reconcile to consistent sizing for cost

- **When**: planning iterations *and* building a defensible program cost estimate.
- **How**: developers size stories relatively (points, t-shirt sizes) to set a sustainable
  pace; lock the estimate once an iteration begins so estimated-vs-actual can be studied.
  Cost estimators work at a higher level in **consistent** units (function points, SLOC) for
  cross-program comparison, then after each release relate delivered features back to that
  metric — building an Agile program database over time.
- **Trade-offs**: relative estimates vary team-to-team and cannot be normalized into a cost
  estimate; velocity is a refinement input, never a target or a cross-team yardstick. (ch03, ch07)

## 6. Keep monitoring high; let the bottom churn

- **When**: applying WBS, schedule, cost, and EVM discipline to volatile Agile work.
- **How**: build one product-oriented WBS from Agile artifacts (epics → features → stories),
  and baseline, schedule, and earn value at the **epic/feature** level. Treat story- and
  task-level data as quantifiable backup, not as the thing you baseline. Take earned value at
  the feature level by percent complete, crediting stories 0/100 (full credit only when a
  story is done).
- **Trade-offs**: tracking at the user-story or task level yields volatile, low-value data
  that can mask serious performance problems. (ch07)

## 7. Protect the baseline without freezing the backlog

- **When**: reconciling Agile reprioritization with credible EVM.
- **How**: run a disciplined baseline-change process. Reprioritizing the backlog between
  iterations is *not* a baseline change; carrying unfinished stories forward usually is not
  (though it creates a schedule variance). Moving an unstarted feature to a later release
  re-plans it (apply freeze-period controls if its baseline start is inside the freeze
  window); a product owner removing scope from a feature *is* a baseline change.
- **Trade-offs**: an unstable *program* baseline — not iteration flexibility — is what
  destroys EVM's value (see the F-35 Block 4 case, where the baseline grew 56% and the
  metrics distorted). (ch07)

## 8. Tailor the contract to the Agile cadence

- **When**: procuring Agile development under the FAR.
- **How**: encourage modular contracting (41 U.S.C. § 2308 / FAR 39.103); prefer a PWS or
  SOO over a SOW when the end state will evolve; let the goods-vs-services decision drive
  contract type and oversight data; build oversight on real release/feature data and a CDRL
  tailored to Agile metrics; replace heavyweight design-review gates with incremental reviews
  tied to the cadence. Keep the product owner and COR as empowered government employees.
- **Trade-offs**: too rigid stalls the cadence under long timelines and costly change
  requests; too loose misses mission outcomes. Beware self-reported metrics like velocity,
  which are easy to inflate. (ch06)

## 9. Build a balanced, early metrics set

- **When**: standing up measurement for an Agile program.
- **How**: pick metrics early, tailored to the framework and audience, each quantifiable,
  meaningful, repeatable, and actionable. Trace strategic goals down through road map →
  releases → backlog. Use **counterbalanced pairs** so one number can't be gamed (e.g.,
  velocity alongside carry-over and post-deployment defects). Automate capture where possible
  but add surveys for team dynamics tools can't see; set targets and thresholds.
- **Trade-offs**: optimizing a single metric degrades another; forcing Waterfall-style
  reporting impedes adoption and misrepresents progress; metrics without thresholds leave
  oversight unable to judge performance. (ch08)

## 10. Audit with paired questions and consequences

- **When**: evaluating whether a program's Agile practice is real, not nominal.
- **How**: before interviewing, agree shared terminology across the audit team; gather
  organizational, program, and team documentation; learn the local Agile method. For each
  best practice, ask the "key considerations" and reason from any gap to its "likely effect."
  Probe the product owner's authority and availability hardest — its absence cascades into
  wrong priorities, developer assumptions, and rework.
- **Trade-offs**: the question bank is a starting point, not a complete checklist; bring the
  ten Agile myths (no documentation, no planning, no oversight, EVM-incompatible, etc.) as
  ready counters to common objections. (ch09)
