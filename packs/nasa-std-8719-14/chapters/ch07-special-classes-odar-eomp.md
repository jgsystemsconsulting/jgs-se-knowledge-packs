# Chapter 7: Special Mission Classes, ODAR, and EOMP

## Core Idea
Special mission types inherit every §4.3–4.7 shall *plus* 2019 ODMSP Objective 5. Tethers and sub-1U smallsats get extra numeric limits in this standard. The assessment is not finished until it is written as an ODAR (design-time, versioned) and kept alive as an EOMP (operations-time). This is the governance secondary.

## Frameworks Introduced
- **Requirement 4.8-1**: large constellations; small satellites including CubeSats; rendezvous / proximity / servicing; active debris removal safety; and tethers shall meet (1) §§4.3–4.7, (2) ODMSP Objective 5, and (3) the extra bullets below.
- **Tethers** (defined in §3.2 as flexible structures >300 m): intact *and* severed remnants must limit collision debris. Do not leave them deployed after the experiment. Disposal (full retract/stow and/or removal) reliability > 0.9, including the chance the tether is cut before disposal. Yo-yo despin masses with cables <10 m are MRD, not tethers.
- **Smallsats smaller than 10 cm on a side when deployed**: LEO lifetime as short as practicable, ≤25 years after mission; mission object-time product in LEO < 100 object-years. Trackability by the Space Surveillance Network is strongly encouraged.
- **Large constellations** (≥100 operational spacecraft cumulative, per 2019 ODMSP): disposal reliability above 0.9 with a *goal* of 0.99, threshold set from mass, collision probability, orbit — not one number for every constellation. Call ODPO for the threshold analysis.
- **ODAR versions**: Initial (MCR, App A.4) → PDR detailed (resolve issues by KDP B) → CDR update (remaining non-compliances before launch approval; resolve by KDP C) → Final (launch approval). Electronic delivery to OSMA; ODPO assists the review.
- **EOMP**: living decommissioning/disposal plan (App B). Identifies disposal-critical items and “single-string” watch points. Updated after operational milestones. Attach the ODAR rather than rewriting it.

## Key Concepts
- **ODAR split**: spacecraft assessments occupy Sections 2–8; launch-vehicle orbital stages occupy Sections 9–14. Same technical areas, separate evidence.
- **Front matter that is easy to skip and fatal to omit**: version/date, signatures, App A.2 self-assessment, proprietary/ITAR/export statement (or an explicit “none”), history plus prior OSMA reviews, DAS version or a full alternate-model description.
- **Section map (spacecraft / LV twin)**: management & mission overview; vehicle description (mass, fluids, propulsion, ACS, pyros, power, other stored energy, radioactive materials, proximity ops); normal-release debris; explosions/passivation; collisions (plus any avoidance/trackability aids); disposal option and reliability; reentry survivors and casualty; special-class addendum.
- **Joint / export programs**: if partners or ITAR/proprietary limits strip the copy that leaves NASA, still deliver a *full* ODAR to ODPO.
- **Beyond-GEO destinations**: still assess the near-Earth / up-to-GEO legs *and* destination-specific applicability.
- **Review artifact**: OSMA/ODPO returns the Figure A.2 check sheet (compliant / not / incomplete per requirement, launch vehicle vs spacecraft columns). Incomplete rows carry risk rating and project risk number.
- **Tether mitigations**: detach from end masses, retract, thicken/cover/ribbon-or-mesh so it will not sever before EOM, or fly lower.

## Mental Models
- Special class ≠ alternate standard. It is *additive*.
- ODAR is the design compliance case; EOMP is the operations constraint list.
- Separate spacecraft and launch-vehicle sections so a green bus cannot hide a dirty stage.
- Large-constellation 0.99 is a *goal whose necessity is analyzed*, not a slogan and not automatic.

## Anti-patterns
- **Leaving a tether extended “because the experiment is over.”**
- **Treating every CubeSat as if 4.8 smallsat numeric limits apply** — the extra 4.8-1b numbers are for vehicles smaller than 10 cm on a side; larger CubeSats still owe §§4.3–4.7 (and sub-1U vehicles already follow MRD rules in ch03).
- **One 0.90 disposal number for a 1,000-sat LEO mega-constellation** without the Objective 5 threshold analysis.
- **Final ODAR as the first serious debris look.**
- **EOMP that never updates after a safe-mode or propellant anomaly.**
- **Shipping a redacted partner ODAR to ODPO as if it were complete.**

## Key Takeaways
1. Special classes add ODMSP Objective 5 on top of ch03–ch06.
2. Tethers need a >0.9 retract/remove story that survives a cut.
3. Tiny smallsats reuse the 25-year / 100 object-year MRD-like caps.
4. Build ODAR in four versions with the App A.1 outline; keep an App B EOMP alive.
5. Split spacecraft vs launch-vehicle evidence; declare DAS version and data restrictions.
6. Use ODPO for constellation reliability thresholds and tether analyses.

## Connects To
- **ch01**: NPR 8715.6 deliveries and relief (NPR 8715.3).
- **ch02**: Cadence, exemptions, living-document idea.
- **ch03–ch06**: Every ODAR section traces to a numbered requirement.
