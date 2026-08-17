# Chapter 2: Assessment Overview and Technical-Area Organization

## Core Idea
Orbital-debris work is a structured assessment, not a single calculation. Section 4.1–4.2 states the policy objective, names the NASA offices and tools, splits the problem into six issues, and defines two living artifacts: the Orbital Debris Assessment / Report (ODA / ODAR) and the End of Mission Plan (EOMP).

## Frameworks Introduced
- **Seven limiting actions** (4.2.2): normal-operations debris; impact probability; impact consequences; tether hazard; energy depletion after mission; lifetime in protected orbits or move to a disposal orbit; human casualty from surviving reentry.
- **Six ODAR issues** (4.2.5.3): (a) normal-release debris, (b) explosions and intentional breakups, (c) collisions during operations, (d) reliable disposal after mission, (e) Earth-impacting remnants after reentry disposal, (f) tethers and other special classes.
- **Technical-area template** (Table 4.2-1): every §4.x is Definition → Requirements → Rationale → Methods → NASA mitigation summary.
- **Approved tool stack**: DAS (or higher-fidelity ORSAT for reentry), Bumper for hypervelocity impact, ORDEM for debris environment, MEM for meteoroids. Alternate models need OSMA approval *before* the assessment.

## Key Concepts
- **ODPO + Center SMA**: ODPO at JSC supports assessments; Center and HQ SMA help prepare ODARs and EOMPs.
- **Earth and Moon first; recommend beyond**: generation limits apply in Earth and lunar orbit; NPR 8715.6 *recommends* limiting debris at Mars and near Sun-Earth / Earth-Moon Lagrange points. This standard tailors process for each environment.
- **ODAR cadence**: Initial ODAR at Mission Concept Review (cost-risk early). First detailed ODAR at PDR; CDR update; Final with launch approval. NPR 8715.6 owns delivery timing. Attach existing analyses rather than rewriting them.
- **Abbreviated vs full**: component- or portion-level ODAs use the Abbreviated ODAR (App A.3). Phase A space-system ODAs use the Initial ODAR (App A.4).
- **ISS / exploration exemptions**: encapsulated or permanently mounted payloads, and temporarily installed items later returned as cargo, skip debris assessments. Anything expected to be released, jettisoned, or deployed does *not*.
- **EOMP is living**: maintained through operations so use does not preclude safe decommissioning. It flags capability/consumable “single-string” threats to disposal — planning cues, not automatic trigger points to terminate.
- **Deviations**: any ODAR/EOMP non-compliance needs a waiver per NPR 8715.6.

## Mental Models
- Six issues, one report spine — if an issue is N/A, say so; do not omit the slot.
- Tools are part of the requirement set: DAS/ORSAT/ORDEM/MEM unless OSMA pre-approves a substitute.
- Initial ODAR is a *cost-avoidance* artifact: find disposal/passivation drivers before design hardens.
- EOMP is the operations twin of the design-time ODAR.

## Anti-patterns
- **Waiting until PDR to think about debris**: Initial ODAR exists specifically for MCR.
- **Swapping in an unapproved environment model**: OSMA first, then assess.
- **Regenerating every prior analysis inside the ODAR**: attach and point.
- **Treating EOMP as a pre-launch binder**: it must track in-flight health of disposal-critical items.
- **Assuming ISS/exploration payloads are always exempt**: only if they stay encapsulated/mounted or return as cargo.

## Key Takeaways
1. Organize work by the six issues; map each to a §4.x chapter in this pack.
2. Use ODPO-agreed tools (DAS/ORSAT, ORDEM, MEM, Bumper as needed).
3. Deliver Initial / PDR / CDR / Final ODARs on the NPR 8715.6 schedule.
4. Keep an EOMP alive through operations, including single-string disposal threats.
5. Waive explicitly; do not silently skip a technical area.
6. Released ISS/exploration items are in scope.

## Connects To
- **ch01**: Applicability and NPR frame that put you in this overview.
- **ch03–ch06**: The six issues in requirement depth.
- **ch07**: ODAR/EOMP section-by-section content and special classes.
