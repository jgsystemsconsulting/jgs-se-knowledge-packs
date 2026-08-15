# Cheatsheet — DOE SEM Version 3

## Decision rules
1. **DOE IT investment lifecycle needed?** Start with SEM stages + exits, not only coding standards.
2. **No Project/QA/CM plans?** You are still in (or failed) Planning.
3. **Ready for next stage?** Only after Stage Exit with owner/stakeholder approval.
4. **Work product complete?** Run Structured Walkthrough before treating it as done.
5. **Need independent view?** In-Stage Assessment (QA), not only peer walkthrough.
6. **Requirements changing mid-build?** CM change against baseline — update RTM.
7. **Small project?** Tailor depth; do not delete gates.
8. **In production?** Use Maintenance nested model, not hallway hotfixes only.
9. **Source is 2002?** Keep intents; replace obsolete tool guidance with current practice.

## Stage map
| Stage | Primary question | Chapter |
|-------|------------------|---------|
| Planning | Should we, and how will we manage it? | ch03 |
| Requirements Definition | What exactly must it do? | ch04 |
| Functional Design | Logical solution shape? | ch04 |
| System Design | Physical/technical how? | ch05 |
| Construction | Built per design with unit proof? | ch05 |
| Integration & Testing | Works end-to-end? | ch06 |
| Installation & Acceptance | Owner accepts in operations? | ch06 |
| Maintenance | Controlled change over life? | ch07 |

## Quality triad
| Gate | Who | Question |
|------|-----|----------|
| Structured Walkthrough | Peers | Is the technical work product sound? |
| In-Stage Assessment | Independent QA | Are deliverables complete and process-healthy? |
| Stage Exit | Owner/stakeholders | Authorize next stage, stay, or stop? |

## Tells & smells
| Smell | Likely gap |
|-------|------------|
| Coding started, no CM plan | Planning incomplete |
| “We’ll baseline requirements later” | Requirements stage skipped |
| Design docs only in slides | Missing inspectable work products |
| No RTM at test time | Traceability never lived |
| Acceptance is email “LGTM” | Hollow Stage Exit |
| Prod hotfixes undocumented | Maintenance model absent |
| One process for 2-week and 2-year projects | Size tailoring ignored |

## What this pack is not
- Not DOE O 413.3B full capital asset guidance
- Not a modern DevSecOps toolchain standard
- Not current CIO policy if superseded after 2002
- Not facility/nuclear SE methods beyond IT SEM scope
