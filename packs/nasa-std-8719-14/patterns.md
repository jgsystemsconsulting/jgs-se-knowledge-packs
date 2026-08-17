# Patterns — Limiting Orbital Debris (NASA-STD-8719.14C)

## Pattern: Six-issue ODAR spine
- **When**: Any NASA or NASA-sponsored object that will orbit.
- **How**: Walk normal-release, explosion/breakup, collision, disposal, reentry casualty, and special class. Mark N/A with rationale; never drop a slot. Split spacecraft vs launch-vehicle evidence.
- **Trade-offs**: Longer report; cheaper than discovering a missing shall at Final ODAR.

## Pattern: DAS first, escalate fidelity
- **When**: Earth-orbit lifetime, object-time, large-object collision, first-look reentry risk.
- **How**: Run current DAS with honest area-to-mass and epoch. If reentry DAS exceeds 1:10,000, schedule ORSAT. If small-MMOD DAS flags disposal-critical hardware, escalate to Bumper/ODPO. Record the tool version in ODAR front matter.
- **Trade-offs**: DAS is conservative; ORSAT/Bumper cost more but can recover a false fail.

## Pattern: Passivate, then dispose
- **When**: EOM of any free flyer with stored energy.
- **How**: Sequence depletion/vent/disconnect so leftover Δv also shortens LEO life when possible. Disarm unused pyros; do not fire them “to be safe.” Put the timeline in both ODAR and EOMP.
- **Trade-offs**: Early passivation can cut residual mission options; late passivation raises explosion and collision risk.

## Pattern: Ceiling, not target (25 years / 0.90)
- **When**: Choosing a LEO decay orbit or quoting disposal reliability.
- **How**: Use residual propellant and staging strategy to go well under 25 years. Design disposal reliability to beat 0.90, and analyze whether a large constellation needs ~0.99.
- **Trade-offs**: Extra propellant reserve vs leftover mass that becomes future fragments.

## Pattern: Controlled reentry as a product
- **When**: Uncontrolled casualty will not close, or policy prefers immediate removal.
- **How**: Design corridor (≤50 km effective perigee, land/ice keep-outs) *and* burn reliability so P(fail)×uncontrolled risk < 1:10,000.
- **Trade-offs**: Needs working propulsion and tracking at EOM; failure mode must still be a legal uncontrolled case.

## Pattern: Living EOMP
- **When**: After launch, especially after anomalies, extensions, or single-string transitions.
- **How**: Re-evaluate disposal-critical items and solar-cycle timing; do not treat the launch-approval EOMP as frozen.
- **Trade-offs**: Ops overhead; prevents a design-compliant vehicle from becoming an un-disposable one.
