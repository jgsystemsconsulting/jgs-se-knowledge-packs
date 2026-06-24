# GAO Schedule Assessment Guide Cheatsheet

Fast reference for GAO-16-89G: the ten best practices, the four characteristics, CPM arithmetic, and the tells of an unreliable schedule.

## The Ten Best Practices (no fixed order — a reliability checklist, not a build recipe)

| # | Best Practice | One-line test | Ch |
|---|---|---|---|
| 1 | Capturing all activities | Is every WBS element (all parties) in the schedule? | 2 |
| 2 | Sequencing all activities | Does every activity have justified predecessor/successor logic? | 2 |
| 3 | Assigning resources to all activities | Are labor/material/equipment loaded and feasible? | 3 |
| 4 | Establishing the duration of all activities | Are durations derived from effort, not from a target date? | 3 |
| 5 | Verifying horizontal and vertical traceability | Do hand-offs and roll-ups stay consistent across levels? | 4 |
| 6 | Confirming the critical path is valid | Does the path truly drive the finish, recomputed each cycle? | 4 |
| 7 | Ensuring reasonable total float | Is float plausible — not a symptom of broken logic? | 5 |
| 8 | Conducting a schedule risk analysis | Has duration uncertainty been simulated (Monte Carlo)? | 5 |
| 9 | Updating using actual progress and logic | Is the schedule statused to a real status date? | 6 |
| 10 | Maintaining a baseline schedule | Is there a CM-controlled baseline to measure against? | 6 |

## The Four Characteristics (the ten practices roll up into four)

| Characteristic | Question it answers | Best Practices |
|---|---|---|
| **Comprehensive** | Is everything in it? | BP1, BP3, BP4 |
| **Well-constructed** | Is the logic and critical path sound? | BP2, BP6, BP7 |
| **Credible** | Does it trace and is it risk-informed? | BP5, BP8 |
| **Controlled** | Is it kept current and measured against a controlled baseline? | BP9, BP10 |

## Schedule levels (one IMS, three views)

- **Summary** — strategic milestones to start/finish the program.
- **Intermediate** — key activities/milestones showing how high-level milestones are met.
- **Detailed** — day-to-day sequenced effort; rolls up into the higher levels.

## CPM arithmetic (forward/backward pass)

- **Forward pass** (start → finish): `EF = ES + duration − 1`; multi-predecessor early start = latest predecessor EF.
- **Backward pass** (finish → start): `LS = LF − duration + 1`; multi-successor late finish = earliest successor LS.
- **Total float**: `TF = LS − ES = LF − EF`. Zero/least float ≈ critical path.
- **Critical path** = longest continuous chain from status date to finish milestone.
- Prefer the **driving (longest) path** over the float-flagged critical path when constraints, multiple calendars, out-of-sequence progress, or leveled resources are present.

## Logic & constraints (Best Practice 2)

- Default link type: **finish-to-start (F–S)**. Let it dominate.
- Forbidden: circular, redundant, dangling, start-to-finish logic; logic on summary activities.
- Minimize and justify every **date constraint, lag, and lead** — a customer-mandated date is *not* a valid justification.
- Enter only the program start date; let the passes compute everything else.

## Statusing (Best Practice 9)

- Set the **status date** (data date) = actuals/forecast boundary. Not the file-open or save date.
- Update by **remaining duration** (or work), not typed-in percent complete.
- Out-of-sequence progress → prefer **retained logic** (conservative) over progress override; fix the underlying logic.
- Never delete activities from a baselined schedule — zero out, mark complete, note.

## Schedule risk analysis (Best Practice 8)

- Deterministic schedules run **optimistic** because of **merge bias** (converging paths multiply, not average).
- Monte Carlo → **S-curve** of completion dates → pick a confidence-priced date → size **contingency**.
- Inputs: **three-point durations** + **risk drivers** (combine both).
- Prioritize risks by **remove-one-and-rerun** (days saved at target percentile), not sensitivity alone.
- **Contingency ≠ total float**: contingency is PM-owned reserve, explicit activities, under change control.

## Tells & smells (signs of an unreliable schedule)

- Activities that don't trace to a WBS element, or WBS elements with no activity.
- Dangling logic, missing predecessors/successors, logic on summaries.
- Many date constraints / lags / leads — a symptom of a poorly planned, possibly infeasible schedule.
- Unreasonably large positive float (broken/missing logic) or any negative float (an unjustified constraint).
- LOE or summary activities sitting on the critical path; "critical" used to mean "important" or "long."
- Percent-complete typed in rather than remaining-duration forecast; no status date discipline.
- No schedule risk analysis → an un-simulated, optimistic finish date.
- No controlled baseline, or frequent rebaselining (weak scope understanding).
- Schedule delivered as PDF/slides — those are not schedule files; demand the **native IMS**.

## Auditor's move (Appendix II triad — applied per best practice)

**Key Questions** → **Key Documentation** (WBS dictionary, BOEs, SRA file & risk register, change log, schedule basis document) → **Likely Effects If Criteria Are Not Fully Met** (pre-written consequence). The practices are coupled — a defect in capture/sequencing invalidates downstream judgments.

## Quantitative health & comparisons (Appendices VI–VII)

- Schedule health = per-best-practice **data measures**, deliberately **no pass/fail tripwires**; severity of an error outranks its count.
- GAO's practices substantially agree with DCMA 14PA, NAVAIR 11-point Toolkit, the DHS Handbook, NASA's Handbook, and NDIA PASEG/GASP — the recurring divergence: most do **not** require resource loading or government/contractor integration.
