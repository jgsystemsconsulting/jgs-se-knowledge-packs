# FAA System Safety Handbook — Patterns & Techniques

Reusable patterns synthesized from the FAA System Safety Handbook (Dec 30, 2000). Each has
When / How / Trade-offs. These are paraphrased techniques, not source reproductions.

## Pattern 1: Run the Five-Step Risk Management Process Around Stated Acceptance Criteria

**When to use**: at the launch of any safety effort, before any analysis begins.

**How**: follow Order 8040.4's five steps — plan (and fix the risk-acceptability criteria up
front), identify hazards, analyze them by severity and likelihood, assess them comparatively
against the plan's criteria, and decide with management owning the residual risk. State what
counts as acceptable and unacceptable as early as you state cost and performance targets.

**Trade-offs**: defining acceptance criteria before you know the design feels premature, but a
program with no stated criteria cannot tell an acceptable hazard from an unacceptable one, and
ends up litigating each decision from scratch.

---

## Pattern 2: Describe the System with 5M / SHEL(L) Before Assessing It

**When to use**: as the first analytical act, before identifying a single hazard.

**How**: decompose the system with the 5M model (Mission, Man, Machine, Management, Media) or the
SHEL(L) model (Software, Hardware, Environment, Liveware). Examine every element *and every
interface* on an individual, interface, and system level. Trade breadth against depth: a wide
system (the NAS) gets a general description; a narrow component gets a detailed one.

**Trade-offs**: this front-loads work that does not yet name any hazard. But interfaces are where
mismatches hide, and an analysis that never bounded the system tends to miss the interactions
that actually cause accidents.

---

## Pattern 3: Couple Severity to Allowable Probability via the Risk Matrix

**When to use**: whenever assessing a hazard or allocating a safety requirement.

**How**: fix worst-credible severity first (independent of likelihood), then read across to the
probability the design must achieve — the more catastrophic the outcome, the lower its allowable
probability. Combine the two in the severity-by-likelihood matrix to land in a High / Medium / Low
band, which is management's acceptance criterion (High tracked until reduced; Medium needs review;
Low needs no further tracking). ASOR formalizes this as paired objective/requirement against a
Target Level of Safety.

**Trade-offs**: severity and likelihood feel like independent knobs, but coupling them is what
justifies spending more to drive down the probability of severe hazards while tolerating minor ones
at higher rates.

---

## Pattern 4: Work the Safety Order of Precedence Top-Down

**When to use**: every time a control must be chosen.

**How**: descend the fixed hierarchy — (1) design for minimum risk (eliminate by design), (2)
incorporate safety devices, (3) provide warning devices, (4) develop procedures and training.
Falling back to procedures/training for catastrophic, hazardous, major, or critical severity
normally requires concurrence of authority. For a *fielded* system, redesign is often not
cost-effective, so revising procedures becomes the fastest route even though it only cuts
likelihood or severity rather than removing the hazard.

**Trade-offs**: design-out is the most durable control but the most expensive to retrofit late;
procedures are cheap and fast but the weakest and most fragile control.

---

## Pattern 5: Build the Integrated Hazard Picture, Then Close the Loop

**When to use**: for any complex system where an accident is a chain of contributors, not a point.

**How**: logically combine the separate hazard analyses (PHL → PHA → RHA → SSHA → SHA → O&SHA → HHA)
around human–machine–environment interactions — reasoned integration, not stapled reports.
Hypothesize the accident scenario, identify initiating and contributory hazards along it, estimate
worst-credible harm and its likelihood, design controls, and carry every medium/high-risk hazard
into a Hazard Tracking and Risk Resolution system through verified closure via the Safety Action
Record.

**Trade-offs**: integration is reasoning work that resists templating, and closure discipline adds
overhead — but a hazard that gets lost between two analyses, or a "combined" report that never
reasoned about interactions, is exactly how complex-system accidents slip through.

---

## Pattern 6: Choose Analysis Techniques to Cover Each Other's Blind Spots

**When to use**: when selecting analytical methods for a program.

**How**: combine event-driven (top-down/deductive) and consequence-driven (bottom-up/inductive)
framings. Use **FTA** to map failure paths down from a defined undesired event; use **FMEA/FMECA**
to walk component failures up to their effects; use **CCFA** to test whether redundancy is real;
use **Sneak Circuit Analysis** for latent conditions that misbehave with no component failing;
use **Energy Trace** to inventory energy and seed fault-tree top events. Do qualitative work first;
quantify only when the value justifies the cost and the limits of the numbers are stated.

**Trade-offs**: a single top-down view can miss a non-obvious top event; a single bottom-up view
drowns you in failures that never cause accidents — neither is complete alone. Quantification adds
precision but also false-precision risk when the data feeding it is inexact.

---

## Pattern 7: Treat Software Safety as a Systems Problem and Rank by Control Capability

**When to use**: whenever software performs or influences a safety-significant function.

**How**: run the five-step software safety process (plan/manage → assign criticality → derive
requirements → design & analyze → test) with a multi-discipline team and a Software Safety Working
Group. Rank each software contributor by its *control capability over the hazard* (MIL-STD-882C
categories or DO-178B levels) crossed with severity in the Software Hazard Criticality Matrix — not
by a software-failure probability, which cannot yet be reliably quantified. Trace each hazard
control down to the code modules and verify by test where practical, knowing 100% coverage is
usually unattainable.

**Trade-offs**: control-capability ranking demands engineering judgment rather than a tidy number,
and tracing controls to code is laborious — but treating software as a programming specialty rather
than a systems problem is how specification-omission hazards (the largest cause) survive into the
field.

---

## Pattern 8: Manage Operational Risk in the Field with ORM

**When to use**: during operational use, run pre-emptively (e.g., before each flight), not after an
accident.

**How**: run the six-step ORM loop — identify hazards, assess risks, analyze control measures, make
control decisions, implement controls, supervise and review. Govern it with the four ORM principles
(accept no unnecessary risk; decide at the level that controls the resources; accept risk only when
benefits outweigh costs; integrate into planning at every level). Match rigor to the situation
(time-critical / deliberate / strategic). Drive controls up the user-involvement ladder toward user
ownership, and judge controls by directly measuring behavior, conditions, attitudes, and knowledge
rather than by waiting on accident statistics.

**Trade-offs**: ORM adds a deliberate decision step to routine operations, and user ownership is
slower than issuing a directive — but most control failures are people failures, and controls
imposed without involving the people exposed to the risk tend not to stick.
