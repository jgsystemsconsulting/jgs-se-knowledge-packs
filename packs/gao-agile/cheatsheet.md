# GAO Agile Assessment Guide Cheatsheet

Fast-reference decision rules, tables, and tells from GAO-24-105506. Synthesized.

## The three adoption perspectives (where to look)

| Perspective | What it governs | Watch for |
|---|---|---|
| Team dynamics & activities | Self-organizing, cross-functional, stable teams; product owner; user stories; estimation; prioritization | Stretched product owner; unestimated stories; people churned between teams |
| Program operations | CI/automation; code quality & technical debt; standups, demos, retrospectives; technical environment; sustainable pace | Standup used as status report; emergent-only architecture; skipped ceremonies |
| Organization environment | Goal alignment; cascading sponsorship & champions; trained sponsors; culture of trust; Agile-aligned incentives; acquisition policy | Agile forced by mandate; rewards for individuals/process not working software |

Rule: adopt incrementally, prioritizing practices **across** all three — not one ring at a time.

## Five Agile planning levels (inverted triangle)

Vision → Epic → Release → Iteration → User story.
Detail and volatility increase top to bottom; traceability runs the full length.

## Fixed vs. variable dials

| | Waterfall | Agile |
|---|---|---|
| Fixed | Requirements | Cost & schedule |
| Variable | Cost & schedule | Requirements (per iteration) |
| Starts with | Plan covering all requirements | High-level goal + priority requirements |
| Ends when | Requirements complete | Goal met |

Government caveat: scope is rarely fully flexible — split "must have" from "nice to have," deliver must-haves first, pursue an MVP on a fixed budget/schedule.

## The eight requirements best practices (ch05)

1. Elicit and prioritize requirements
2. Refine requirements
3. Make requirements sufficiently complete, feasible, and verifiable
4. Balance customer and user needs against constraints
5. Test and validate the system as it is built
6. Manage and refine requirements (change control)
7. Maintain traceability through decomposition
8. Ensure work contributes to completing requirements

## "Done" gates

- **Definition of ready** → may we start? (estimated, criteria written)
- **Acceptance criteria** → per-story conditions from the product owner
- **Definition of done** → universal gate: acceptance + testing + compliance (e.g., Section 508)

## Contracting document selection (ch06)

| Certainty about end state | Use | Notes |
|---|---|---|
| High | SOW | Part of contract; change is disruptive |
| Medium (results measurable) | PWS | Part of contract; change expected |
| Low / evolving | SOO | Most flexible; can carry vision, themes, road map, initial backlog |

Other rules: encourage **modular contracting**; the goods-vs-services decision drives contract type, vehicle, and oversight data; keep the product owner **and** COR as empowered government employees; avoid permanent fixed vendor pools.

## Monitoring & control — keep it at the right level (ch07)

| Agile level | Stability | Role in oversight |
|---|---|---|
| Epic | Broad, low detail | Baseline & roll-up; total float / critical path |
| Feature | Stable through 1–2 reporting periods | **The control level** — cost estimate, schedule, EVM, control accounts |
| User story | Volatile | Quantifiable backup data only; 0/100 credit |

- Earn value at feature level via **percent complete**; credit stories **0/100**.
- EVM not forced on **small** programs; tailor it in for medium/large.
- Report EVM on the Agile cadence (e.g., a retrospective view of total-backlog overrun).

## Metrics that matter (ch08)

- Universal: **lead time**, **cycle time**, **velocity** (team-internal only), **CFD**, **burn up/burn down**.
- Make each metric quantifiable, meaningful, repeatable, actionable.
- Use **counterbalanced pairs** to prevent gaming:
  - carry-over stories ↔ post-deployment defects
  - automated unit-test count ↔ build execution time
  - velocity ↔ rejected/unfinished/never-started stories

## Tells & smells (anti-patterns to flag)

- One product owner spread across many teams (USCIS ELIS: up to twelve).
- Daily standup turned into a management status meeting.
- Architecture built only as code is written (no up-front runway).
- Agile imposed by policy mandate before transition mechanisms exist.
- Velocity inflated by cherry-picking easy stories; velocity compared across teams.
- EVM/schedule tracked at story or task level → volatile, masks real problems.
- Hard date constraints used to model iterations → breaks critical path.
- Program baseline that moves with new scope every cycle → EVM stops measuring (F-35 Block 4).
- Backlog left empty while the program is still active.
- Non-functional testing deferred carelessly to just before release.
- Waterfall-style reporting/artifacts forced onto an Agile program.

## The ten Agile myths (ch09) — and the tempered truth

Agile does **not** mean: no documentation · no planning · no oversight · co-located only ·
small single-team only · any framework guarantees success · no architecture · no risk
analysis · no reliable schedule baseline · incompatible with EVM. Each has a tempered,
correct version (appropriate-level docs at time-boxed milestones; planning spread across the
life cycle; governance guard rails; tailored EVM; baseline built alongside rolling-wave
planning; and so on).

## Auditor quick-start (ch09)

1. Agree shared terminology across the audit team first.
2. Collect organization-, program-, and team-level documentation.
3. Learn the local Agile method.
4. For each best practice: ask the key questions → compare condition vs. criteria → reason to the likely effect.
5. Probe product-owner authority and availability hardest.
