# Chapter 5: Commodity WBS Templates — Ground, Unmanned Maritime, Launch, and IS/DBS

## Core Idea
Appendices G–J cover ground vehicles, unmanned maritime systems, launch vehicles, and Information Systems/Defense Business Systems—the templates most often mishandled when teams force every program into an aircraft-shaped WBS.

## Frameworks Introduced
- **Appendix G Ground Vehicle Systems** — combat/tactical vehicle product breakouts, turrets/mission equipment, mobility, and ground-unique support.
- **Appendix H Unmanned Maritime Systems** — USV/UUV and maritime unmanned product structures with vehicle, payload, and C2 considerations.
- **Appendix I Launch Vehicle Systems** — launch vehicle stages, propulsion, avionics, and ground launch support unique to launchers.
- **Appendix J Information Systems / Defense Business Systems** — IT/DBS product and service structures; apply electronics patterns where hardware exists but keep IS/DBS parents for business/warfighter IT.

## Key Concepts
- **Ground mission equipment vs chassis** — keep mission systems identifiable for cost and readiness drivers.
- **Unmanned maritime payloads and C2** — payload and control segments often dominate cost; give them honest parents.
- **Launch vs space vehicle** — launch vehicle (I) is not the on-orbit space vehicle (F); interface elements must be explicit.
- **DBS/IS software releases** — release-oriented children are valid when they are the managed products; still map to system parents.
- **Generic electronics crossover** — Appendix B remains available when the 'system' is essentially an electronic product hosted on varied platforms.
- **Training/data/support** — still pulled from Common Elements rather than reinvented per appendix.

## Mental Models
- **Do not aircraft-ify ground or IT programs** — wrong appendix choice is a structural defect, not a cosmetic one.
- **Launch and space are different products** — conflating them breaks both communities' CERs.
- **IS/DBS deserves its own spine** — embedded avionics software rules are the wrong default for enterprise IT.

## Anti-patterns
- Using Appendix A for a ground combat vehicle 'because we always have'.
- Hiding DBS development under a weapon-system avionics element.
- Merging launch vehicle and satellite WBS into one untraceable tree.
- Omitting C2/payload parents on unmanned maritime efforts.

## Key Takeaways
1. G–J supply non-aircraft commodity spines that must be chosen deliberately.
2. Unmanned maritime and launch programs need payload/C2 or stage-level honesty.
3. IS/DBS follows Appendix J, not embedded-weapon software defaults.
4. Common Elements still finish the structure for training, data, and support.

## Connects To
- **ch04** — air/missile/sea/space counterparts.
- **ch06** — Common Elements definitions.
- **ch03** — software dual-path rationale.
