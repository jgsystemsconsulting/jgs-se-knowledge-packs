# Chapter 11: T&E / V&V Integration Checklist

## Core Idea
When a simulation is embedded in or is the system under test, verification/validation and developmental/operational T&E must share one requirements-to-assessment plan — otherwise the same critical behaviors are tested twice, missed, or scheduled against incompatible resources.

## Frameworks Introduced
- **Five integration cases**: Sans (M&S used, not supporting a system); Separate (M&S precedes and stays apart from the system); Supporting (partially embedded); Subset (wholly embedded); Same (simulation and system are identical). Only Supporting / Subset / Same require T&E–V&V integration.
- **Ten-step coordination process**: pick the case → gather simulation/system requirements → bin shared requirements by criticality → partition each bin into Verification / Validation / DT&E / OT&E → repeat remaining bins → specify techniques, schedule, and resources per requirement → combine compatible assessments → number combined assessments → draw per-bin timelines → present tables and timelines to the User for authorization.
- **Criticality bins × assessment partitions**: each shared requirement lives in exactly one criticality bin (critical / important / less important) and is then assigned to one primary partition (verification, validation, DT&E, OT&E).

## Key Concepts
- **Shared-requirement filter**: Cases 1–2 stay on ordinary RPG VV&A. Cases 3–5 first isolate requirements that belong to both the simulation and the system.
- **Partition ranking**: when a requirement could sit in two partitions, put it in the higher-ranking one; if still unclear, default to Verification.
- **Assessment matrix**: for each bin, record requirement, partition flags, technique(s), when the work occurs, and explicit resources (skill, software, platforms — not “trained personnel”).
- **Combination rule**: merge assessments only when techniques, schedules, and resources actually match and no requirement is shortchanged. Combined less-critical items ride in the more-critical bin’s table.
- **User authorization**: bin tables plus timelines are the decision artifact — who assesses what, in which phase, when, with what resources.

## Mental Models
- **Integration is a case, not a slogan**: embedding depth decides whether T&E and V&V even share a plan.
- **Criticality first, method second**: rank what matters to the decision, then choose verification vs validation vs live test.
- **Time and people are the credibility budget**: extra technique depth must buy residual-risk reduction the User will fund.

## Anti-patterns
- Running full T&E–V&V integration for a standalone analysis model that never touches the system (Case 1/2).
- Double-counting the same requirement in two criticality bins or two partitions.
- Combining fleet test and code analysis because both are “assessments,” not because they share technique, schedule, and resources.
- Presenting a matrix the User never authorized — then treating unfunded validation as residual-risk silence.

## Key Takeaways
1. Integrate T&E and V&V only when the simulation supports, is embedded in, or is the system.
2. Bin shared requirements by criticality, then partition into verification, validation, DT&E, and OT&E.
3. Specify technique, schedule, and named resources before combining events.
4. The User signs the tables and timelines; that authorization is part of the validation/T&E plan, not a briefing courtesy.

## Connects To
- **ch01**: intended-use frame that makes “critical” vs “less important” meaningful.
- **ch05**: V&V Agent techniques and independence when verification/validation partitions execute.
- **ch08**: validation partition is accuracy-vs-referent work, not a synonym for DT&E.
- **ch10**: resource/schedule trade-offs are residual-risk choices.
- **ch12**: validation-partition items still need an adequate referent.
