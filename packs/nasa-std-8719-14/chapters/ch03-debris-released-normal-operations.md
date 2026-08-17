# Chapter 3: Debris Released During Normal Operations

## Core Idea
Design not to release debris. If release is unavoidable, limit count, size, and orbital lifetime so the leftover objects do not become a long-lived collision source. Intact spacecraft and spent stages are *not* mission-related debris (they belong to collision and disposal chapters). Sub-1U CubeSats *are* treated as mission-related debris from LEO to GEO.

## Frameworks Introduced
- **Requirement 4.3-1a (LEO passers, ≥1 mm)**: each released object’s orbital lifetime ≤ 25 years from release.
- **Requirement 4.3-1b**: total LEO object-time product < 100 object-years per upper stage or per spacecraft.
- **Requirement 4.3-2 (near-GEO, ≥5 mm)**: within 25 years, apogee must fall below GEO−200 km *or* perigee rise above GEO+200 km, and the object must stay out of the GEO ±200 km / ±15° zone for at least 100 years after that.
- **Object-time product**: sum of each object’s LEO dwell time (time spent below 2000 km). If apogee is already below 2000 km, dwell time equals lifetime.

## Key Concepts
- **What counts**: sensor covers, tie-downs, bolt fragments, attitude devices, dual-payload fittings, staging hardware, deployment hardware, objects released at passivation/disposal. Thresholds: 1 mm (LEO concern), 5 mm (GEO concern).
- **What does not**: solid-rocket slag and dispersed liquids (explicitly out of §4.3). Intact buses and stages (see ch04–ch05).
- **Why 25 years / 100 object-years**: 25-year LEO removal is the researched U.S./agency consensus for limiting 100-year growth at acceptable program cost. 100 object-years was chosen so typical released debris sits near 10⁻⁶ collision probability with an average operating spacecraft.
- **Altitude tell**: perigees below ~600 km usually decay inside 25 years; the requirement bites hardest above ~700 km, where natural lifetime can be centuries.
- **Compliance method**: for each planned release, record average cross-section, area-to-mass, and initial orbit (parent orbit unless Δv ≳ 10 m/s), then run DAS. Solar-cycle phase matters — identical objects starting decay at solar min vs max have very different lifetimes. Update the EOMP if EOM timing slips.
- **Mitigations**: lower perigee at release; raise area-to-mass; use lunar/solar perturbations; retain covers/bolts instead of ejecting them; change ops so release never happens.

## Mental Models
- Count × time is the currency, not “we only released a few covers.”
- Four 25-year objects already consume the 100 object-year budget.
- GEO debris is a *band-exit* problem, not a 25-year decay problem — GEO lifetimes without removal are millennia.
- Sub-1U satellites inherit the MRD rules even though they look like “spacecraft.”

## Anti-patterns
- **Calling the bus itself MRD**: stages and spacecraft are disposal/collision objects.
- **Ignoring solar-cycle timing**: a DAS run at the wrong F10.7 epoch can fake a 25-year pass.
- **Releasing at GEO without a 100-year perturbation case**: 25-year exit is necessary but not sufficient.
- **Assuming slag/liquids are in §4.3**: they are carved out; do not hide other debris behind that carve-out.

## Key Takeaways
1. Prefer zero planned releases; if not, meet 4.3-1 / 4.3-2 and write the rationale.
2. LEO: ≤25 years each and <100 object-years total per stage or spacecraft.
3. GEO-crossing ≥5 mm debris must leave and stay out of the protected GEO zone.
4. Use DAS with honest area-to-mass and solar conditions; refresh at EOM.
5. Treat sub-1U CubeSats as MRD.
6. Document every >1 mm (LEO) / >5 mm (GEO) planned release in the ODAR and EOMP.

## Connects To
- **ch02**: Where this issue sits in the six-issue spine and DAS role.
- **ch04**: Intact objects that explode or collide are a different debris source.
- **ch05**: Disposal of the parent structure after the mission.
- **ch07**: ODAR Section 3 / 10 content checklist.
