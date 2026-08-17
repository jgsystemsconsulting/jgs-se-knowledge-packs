# Chapter 5: Postmission Disposal of Space Structures

## Core Idea
Do not abandon the vehicle. Pick a disposal family, prove the orbit stays out of protected bands for the required horizon, and show the disposal *system* will work (reliability ≥ 0.90 at EOM). Immediate removal — controlled reentry or Earth escape — is the preferred 2019 ODMSP option. This chapter is the Ops/Maint/Disposal gold slice.

## Frameworks Introduced
- **Six methods**: natural atmospheric reentry; direct (controlled) reentry; maneuver to a storage orbit; direct retrieval; long-term reentry; Earth escape.
- **Requirement 4.6-1**: natural reentry (lifetime as short as practicable, ≤25 years after mission, conservative/low solar activity); *or* direct reentry as soon as practical; *or* retrieve within 5 years (shorter than 25 because a waiting target at higher altitude is a worse collision source).
- **Requirement 4.6-2 storage / escape**:
  - Between LEO and GEO: eccentric storage with perigee ≥2000 km and apogee ≤35,586 km for ≥100 years, and ≤25 years spent in 20,182±300 km over 200 years; *or* near-circular storage that avoids LEO, GEO, and 20,182±300 km for ≥100 years and avoids known ≥10-spacecraft constellation altitudes.
  - Above GEO: minimum perigee 35,986 km for ≥100 years (GEO + 200 km protected; IADC/FCC/ITU formula adds a solar-radiation margin that grows with area-to-mass).
  - Earth escape: heliocentric trajectory.
- **Requirement 4.6-3 long-term reentry** (MEO, Tundra, highly inclined GEO, similar): use resonances to grow eccentricity; lifetime ≤200 years and as short as practicable; ≤25 years per protected zone (LEO, GEO, 20,182±300 km); P(>10 cm collision) < 0.001 over life.
- **Requirement 4.6-4 reliability**: disposal success probability ≥ 0.90 at EOM. For controlled reentry, success at the deorbit burn must also keep 4.7-1 casualty risk legal (see ch06). The 0.01 MMOD term in 4.5-2 is *not* folded into the 0.90 inherent reliability.

## Key Concepts
- **Why dispose**: abandoned mass (historically >8 million kg) becomes the feedstock for future catastrophic collisions.
- **25 years is a ceiling**: spend residual propellant to go shorter. Staging LEO payloads above ~700 km from a lower parking orbit lets dead stages decay faster.
- **Drag sails / balloons**: they cut lifetime but raise collision area. ODAR must show net risk drop *or* that a hit will not fragment spacecraft/large debris.
- **GEO gauging**: small Δv, large consequence of running dry. Hold reserve, execute the EOMP burn sequence, then passivate leftovers without kicking the disposal orbit. If a GEO kick-stage must separate, *it* independently meets 4.6-2b.
- **Protected neighbors**: avoid GNSS / other constellation altitudes; 25-year decay orbits may *transit* those altitudes briefly each rev, but should not loiter.
- **Beyond Earth**: lunar/Mars disposal is coordinated with the Planetary Protection Officer (NPD 8020.7 / NPR 8020.12). Lagrange missions should not leave junk that blocks future users.
- **Maneuver hygiene**: large, low-thrust, and gravity-assist burns that cross Earth orbit go through CARA (robotic) or TOPO (crewed) with 18 SPCS support. Controlled reentry effective perigee ≤50 km so the vehicle does not skip.

## Mental Models
- Disposal is a *protected-band exit*, not “park it somewhere quiet.”
- Preference order: leave Earth now → decay out of LEO quickly → carefully justified storage or resonant long-term reentry.
- 0.90 is the *disposal system* number; 0.01 is the *MMOD killed my thruster* number; both are required.
- Retrieval gets only 5 years because you left a large target in a busier band.

## Anti-patterns
- **Treating 25 years as a design target**: the shall is “as short as practicable.”
- **Graveyard by default**: storage is allowed only if the 100-year (or 200-year) perturbation case stays out of LEO/GEO/MEO slots.
- **Drag device without a collision-consequence paragraph**.
- **GEO dispose-and-hope on the last kilograms of fuel**.
- **Folding 4.5-2 into 4.6-4** or ignoring 4.6-4 because DAS does not compute it (it does not — use FMEA).

## Key Takeaways
1. Choose 4.6-1, 4.6-2, or 4.6-3 explicitly and run the matching long-term perturbation case.
2. Prefer immediate removal; otherwise LEO ≤25 years with conservative solar flux.
3. Prove disposal reliability ≥ 0.90; keep controlled-reentry failure inside the 4.7-1 product.
4. Coordinate EOM burns; do not create a new debris concentration.
5. Document drag-augmentation collision risk if used.
6. Keep the EOMP current so operations cannot spend the disposal margin.

## Connects To
- **ch04**: Passivation sequence and MMOD threat to disposal hardware.
- **ch06**: Reentry casualty when disposal is atmospheric.
- **ch07**: ODAR Sections 6 / 13 and the living EOMP.
- **ch01**: Current-edition judgment for mission-extension disposal decisions.
