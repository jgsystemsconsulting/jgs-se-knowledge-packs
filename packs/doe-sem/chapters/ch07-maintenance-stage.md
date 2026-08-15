# Chapter 7: Maintenance Stage

## Core Idea
Maintenance is a full SEM stage after acceptance, not an informal forever-after. SEM defines a nested maintenance process model — from problem/modification identification through analysis, design, construction, test, acceptance, and delivery of changes — tailored by size and measured with process metrics.

## Frameworks Introduced
- **Maintenance process model**: Problem/Modification Identification → Analysis → Design → Construction → System Test → Acceptance → Delivery.
- **Tailoring for size**: Maintenance efforts scale process depth like development projects.
- **Operational CM**: End products remain under configuration management for the remainder of life.

## Key Concepts
- **Entry**: Accepted system, operational baseline, CM procedures, support organization, known owners/users.
- **Problem/Modification Identification**: Capture defects, enhancements, mandatory changes (policy, security, EA); prioritize against mission and resources.
- **Analysis**: Impact analysis across requirements, design, data, interfaces, and operations; decide proceed/defer/reject.
- **Design / Construction / Test**: Apply appropriately scaled design and build practices; regression test to protect baseline behavior.
- **Acceptance and Delivery**: Owner/operations acceptance of the change; deliver updated system and documentation; restore clean operational baseline.
- **Metrics**: SEM includes process model metrics concepts for maintenance (throughput, quality, backlog) to manage the steady state.
- **Relationship to earlier stages**: Maintenance re-enters micro-cycles of the same engineering disciplines rather than inventing an ad hoc path.
- **COTS/maintenance caution**: Proprietary interfaces accepted earlier can dominate maintenance cost — a planning/design debt realized here.

## Mental Models
- Every production change is a tiny SEM project with proportional reviews.
- Backlog management is lifecycle governance, not only ticket hygiene.
- Regression discipline is how maintenance avoids un-accepting the system.
- If CM was weak in construction, maintenance becomes archaeology.

## Anti-patterns
- **Hotfix culture without impact analysis**: Silent requirement drift and fragile ops.
- **Enhancements bypassing acceptance**: Shadow systems inside production.
- **No regression suite tied to critical requirements**: Slow-motion breakage of mission functions.
- **Undocumented emergency changes**: Breaks auditability and future maintenance.

## Key Takeaways
1. Maintenance is stage 10 of SEM with an explicit nested process model.
2. Changes flow through identification, analysis, design, build, test, acceptance, and delivery.
3. Size tailoring still applies; small fixes are lighter, not uncontrolled.
4. CM and baselines make operational change safe and reversible.
5. Metrics help manage maintenance as a system, not a hero queue.
6. Design-time COTS and quality choices determine maintenance cost.

## Connects To
- **ch02**: Lifecycle continues after acceptance under CM.
- **ch03**: CM/QA plans still govern operational change.
- **ch05–ch06**: Technical practices reused at smaller scale.
- **ch01**: Systems (not only software) maintenance scope.
