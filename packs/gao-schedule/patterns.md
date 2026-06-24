# GAO Schedule Assessment Guide Patterns & Techniques

Reusable patterns from the GAO Schedule Assessment Guide (GAO-16-89G). Each has When / How / Trade-offs. Ground all schedule work in the ten best practices and the four characteristics.

## Pattern 1: Capture All Activities from the WBS

**When to use**: at the very start of building or auditing an IMS, before any sequencing, resourcing, or risk work.

**How**: walk the product-oriented work breakdown structure and its dictionary. Every WBS element gets at least one activity; every activity traces back to a WBS element. Include *all* effort — government, contractor, subcontractor, vendor, and external interfaces — not just the prime contractor's slice. Use milestones sparingly (major events/deliverables), let detail activities carry the work, keep level-of-effort off the critical path, and give the schedule exactly one start and one finish milestone.

**Trade-offs**: a complete capture is laborious and exposes uncomfortable scope — but a schedule with missing activities fails every downstream best practice: you cannot confirm correct sequencing, a valid critical path, or a complete risk analysis on work that isn't there.

---

## Pattern 2: Sequence the Network with Sound Logic

**When to use**: immediately after capture, turning a static activity list into a predictive network.

**How**: link every activity (except the start/finish milestones) with a justified predecessor and successor; let finish-to-start logic dominate; enter only the program start date and let the forward/backward passes compute the rest. Forbid circular, redundant, dangling, and start-to-finish logic, and never put logic on summary activities. Minimize and justify every date constraint, lag, and lead — prefer dynamic logic, model external supply as reference/visibility activities, and split activities rather than force dates. Watch path convergence: heavy merges are a warning sign.

**Trade-offs**: clean logic takes discipline and resists the temptation to hard-code known dates — but constraints and lags silently freeze the network so it stops forecasting, and a customer-mandated date is never a valid justification for a constraint.

---

## Pattern 3: Resource-Load and Set Durations from Effort

**When to use**: once the network exists and you need the schedule to model *what work takes*, not just *when it happens*.

**How**: load labor, material, equipment, facilities, and travel onto the activities that consume them (never onto milestones or summary activities); store resources in the schedule itself and have owners justify each estimate. Crosscheck the loaded total against budget and inspect resource peaks for feasibility — don't trust the tool to prevent over-allocation. Derive each duration from effort, resources, and productivity under most-likely (unpadded) conditions — not from a desired finish date — and keep risk margin in separate contingency. Size durations to the reporting period; use inch-stones (quantifiable backup data) to progress long activities. Level only within float, on detailed schedules; build calendars deliberately rather than defaulting them.

**Trade-offs**: bottom-up, effort-based durations are slower than back-solving from a target date and often yield an unwelcome longer schedule — but date-driven durations and an unloaded schedule silently assume infinite resources and produce a plan that cannot be executed.

---

## Pattern 4: Validate the Critical Path (and the Driving Path)

**When to use**: before baselining, and after every status update — the path is dynamic.

**How**: recompute the critical path each cycle and confirm it runs continuously from the status date to the finish milestone with no gaps. Keep it clean: no LOE, no summary activities, no unexplained long durations, no lags/leads, no constraints making unimportant activities appear to drive a milestone. When date constraints, multiple calendars, out-of-sequence progress, or leveled resources are present, trace the *driving (longest) path* back from the finish milestone instead of trusting the software's float-based flag. Manage near-critical and risk-critical paths too.

**Trade-offs**: re-validating every cycle is overhead — but "critical" means *drives the finish date*, not "important" or "long," and a stale or float-distorted critical path sends management to defend the wrong activities.

---

## Pattern 5: Run a Schedule Risk Analysis and Size Contingency

**When to use**: after a sound CPM schedule exists, to price confidence in the completion date and at decision points/budget cycles thereafter.

**How**: feed quantified duration uncertainty and risks into a Monte Carlo simulation to produce an S-curve of completion dates; pick a date at a chosen confidence level and size schedule contingency to defend it. Use both three-point durations and risk drivers — risk drivers trace contingency to mitigable root-cause risks and induce correlation automatically; three-point ranges capture residual spread. Prioritize risks with the remove-one-and-rerun method (days saved at the target percentile), not sensitivity charts alone. Hold contingency as explicit activities under change control, owned by the program manager — never as total float.

**Trade-offs**: an SRA needs a risk register, distributions, and simulation effort — but simply summing deterministic durations understates the real schedule because of merge bias, so an un-simulated finish date is optimistic by construction.

---

## Pattern 6: Status the Schedule and Hold a Controlled Baseline

**When to use**: every reporting cycle once a baseline is set, to keep the schedule honest over time.

**How**: set the status date as the actuals/forecast boundary; load real start/finish dates and progress, and update by *remaining duration* (or work), not typed-in percent complete. Handle out-of-sequence progress with retained logic (conservative) over progress override, and repair the underlying logic either way. Never delete activities from a baselined schedule — zero out, mark complete, and note. Version, archive, and narrate every approved update. Keep both baseline and current schedules under configuration management, backed by a living schedule basis document; limit baseline changes to scope change or formal replanning, and treat frequent rebaselining as a red flag. Performance is the variance between baseline and current — and is only as valid as the schedule is reliable.

**Trade-offs**: disciplined statusing and change control cost time each cycle — but without updating, the current schedule drifts into fiction, and without a controlled baseline there is nothing legitimate to measure it against.

---

## Pattern 7: Audit a Schedule with the Appendix II Triad

**When to use**: when assessing a schedule someone else produced, or judging reliability for a decision.

**How**: for each of the ten best practices, apply GAO's three-part instrument — **Key Questions** (e.g., does every activity trace to a WBS element?), **Key Documentation** (demand the WBS dictionary, BOEs, SRA file, change log, basis document that would prove it), and **Likely Effects If Criteria Are Not Fully Met** (the pre-written consequence). Roll the ten findings up into the four characteristics — comprehensive, well-constructed, credible, controlled — and remember the practices are coupled: a defect in capture or sequencing invalidates downstream judgments. Request schedules in native file format; PDFs and slides are not schedule files.

**Trade-offs**: a full audit demands evidence and expertise — but admiring a schedule's surface tells you nothing; reliability is demonstrated by inspecting the calculations, the logic, the constraints, and the documentation behind them.
