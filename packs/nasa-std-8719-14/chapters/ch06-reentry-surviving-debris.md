# Chapter 6: Debris Surviving Atmospheric Reentry

## Core Idea
Using the atmosphere to clear orbit moves risk from space to the ground. Any remnant that hits with more than 15 J is treated as capable of injuring an unsheltered person. Uncontrolled reentry must stay under 1:10,000 world-wide casualty expectation. Controlled reentry must put that energy outside stated keep-out distances *and* keep (failure probability × uncontrolled casualty risk) under the same 1:10,000.

## Frameworks Introduced
- **15-joule threshold**: RCC 321-20 Supplement basis. Below 15 J, injury is treated as highly improbable; above, the object counts in debris casualty area (DCA).
- **Requirement 4.7-1a**: uncontrolled reentry casualty risk < 0.0001 (1:10,000).
- **Requirement 4.7-1b**: controlled reentry — no >15 J impact closer than 370 km to foreign landmasses, or within 50 km of the continental U.S., U.S. territories, or the permanent Antarctic ice pack.
- **Requirement 4.7-1c**: P(fail reentry burn) × (uncontrolled casualty risk) < 0.0001.
- **Requirement 4.7-1d**: long-term reentry (MEO/Tundra/inclined GEO family) — surviving debris either < 7 m² total DCA *or* 1:10,000 casualty risk.
- **DCA model**: total casualty area sums, for each surviving >15 J piece, a human-interaction term (0.6 m characteristic radius in the standard’s simple formula) plus the piece’s mean radius. Either that formula or the Opiela–Matney interaction model is acceptable. E = DA × population density for the inclination and year.

## Key Concepts
- **Scope**: all spacecraft and launch vehicles returning from above 130 km, including jettisoned parts. Applies whenever §4.6 chose atmospheric disposal.
- **Why 1:10,000**: NASA policy since 1995; later written into 2001/2019 ODMSP; aligned with RCC 321-20 public-risk language and adopted by ESA and IADC.
- **Conservative sheltering stance**: the calculation treats people between the orbit’s latitude extremes as unsheltered. NASA does *not* take credit for buildings, and also does not add bounce/ejecta/collapse terms — the two corrections fight and are not universally formulated.
- **Tool ladder**: DAS reentry module is simplified and conservative. If DAS ≤ 0.0001, you pass. If DAS exceeds, run ORSAT (ODPO-operated, compared to recovered debris and to ESA SCARAB). Do not shop for a friendlier unofficial code.
- **Controlled-reentry arithmetic**: example — 10% burn-failure probability means the equivalent uncontrolled risk must be < 0.001 so the product stays at 0.0001.
- **Mitigations**: controlled reentry (effective perigee ≤50 km); design-for-demise (low melt-temperature materials and exposed configuration); package many survivors into one surviving box (fewer objects); pre-reentry breakup below ~120 km (often ~80 km structural breakup) so pieces heat longer; or abandon reentry and use a §4.6 storage/escape option instead.

## Mental Models
- Casualty risk is **count × energy × who lives under the ground track**, not “did anything come back.”
- DAS fail is not an automatic waiver — it is a ticket to ORSAT.
- Controlled reentry is a *geometry plus reliability* pair; missing either fails 4.7-1.
- Design-for-demise is a materials *and* packaging problem: one surviving battery box beats ten surviving cells.

## Anti-patterns
- **Taking building-shelter credit** to squeeze under 1:10,000.
- **Declaring DAS conservatism as non-compliance** without an ORSAT run.
- **Controlled reentry aimed at land** or with a sloppy skip-prone perigee.
- **Ignoring 4.7-1c**: a beautiful corridor with a flaky deorbit motor still fails.
- **Spreading non-demising parts** across the vehicle when they could share one surviving enclosure.

## Key Takeaways
1. Count every >15 J survivor in DCA; target 1:10,000 uncontrolled risk.
2. Use DAS first; escalate to ORSAT if DAS is over the line.
3. Controlled reentry must meet keep-out distances *and* the failure-product test.
4. Long-term reentry paths use either 7 m² DCA or the same casualty cap.
5. Prefer demise, consolidation, or a non-reentry disposal if the number will not close.
6. Record assemblies, materials, and >15 J survivors in the ODAR.

## Connects To
- **ch05**: Atmospheric disposal is a 4.6-1 choice; 4.6-4b feeds 4.7-1c.
- **ch04**: Intentional pre-reentry breakup is a 4.4 event with its own debris rules.
- **ch07**: ODAR Sections 7 and 14.
