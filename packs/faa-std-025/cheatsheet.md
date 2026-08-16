# Cheatsheet — FAA-STD-025f

## Decision rules
1. **Need requirements or as-built design?** IRD = shall requirements; ICD = is/are design characteristics.
2. **Facility interface?** IRD yes; ICD not required.
3. **Both IRD and ICD needed?** Approve IRD before ICD; start IRD before SOW finalization.
4. **Unknown data at baseline?** TBS in IRD only (limited future-use exception in ICD); revise promptly when known.
5. **Section not applicable?** Explicit N/A sentence—do not omit the heading.
6. **Every shall ready?** Must appear once in the VRTM with level + method.
7. **Changing a baseline?** Full revised document + new revision number under Order 1800.66.
8. **Power crossing the interface?** Specify electrical/electronic factors; pick one FAA-G-2100 revision.

## Document pair quick map
| Need | Artifact | Verb | Typical owner path |
|------|----------|------|--------------------|
| Bilateral requirements | IRD | shall | FAA program / author → CM baseline |
| Implemented design | ICD | is/are | Developer deliverable → approval subset |
| Site space/power prep | Facility IRD | shall | Iterative PM/SE path (no ICD) |

## Verification levels
| Level | Typical venue | Role |
|-------|---------------|------|
| Subsystem/Service (Development) | Contractor facility | End-item acceptance |
| Integration | Cross-system lab/event | Multi-party interface prove-out |
| Site | Key/operational site | Installed interface verification |

## Tells & smells
| Smell | Likely gap |
|-------|------------|
| ICD approved, IRD still draft | Ordering violation (ch01, ch06) |
| Shall count ≠ VRTM rows | Traceability break (ch05) |
| Blank outline sections | Missing N/A/TBS discipline (ch02) |
| Security only at one end | Incomplete risk assessment (ch03) |
| Mixed 2100g and 2100h citations | Power baseline conflict (ch03, ch04) |
| Facility data still "initial" at build | Iteration model stalled (ch06) |
| Informal email "interface agreements" | CM/revision bypass (ch06) |
