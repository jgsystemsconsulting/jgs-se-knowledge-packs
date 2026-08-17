# Chapter 4: Explosions, Intentional Breakups, and On-Orbit Collisions

## Core Idea
Most long-lived hazardous fragments historically came from explosions (residual propellant, pressurants, batteries) and from collisions that shatter an intact vehicle. Limit *probability* of accidental explosion and catastrophic collision, *passivate* stored energy at EOM, and treat intentional breakups as planned debris-deposition events with both long-term and short-term risk caps.

## Frameworks Introduced
- **Requirement 4.4-1**: integrated probability of accidental explosion for all credible failure modes of each free-flying object < 0.001 (small-particle impacts excluded — those live in 4.5-2).
- **Requirement 4.4-2**: design and plan either to deplete/disconnect all stored and generated energy when no longer needed for mission or disposal, *or* to control energy so it cannot explode/deflagrate into debris. Depletion burns/vents should minimize collision with tracked objects.
- **Requirement 4.4-3 (intentional, long-term)**: fragments >10 cm: object-time product < 100 object-years; no >1 mm fragment stays in Earth orbit > 1 year.
- **Requirement 4.4-4 (intentional, short-term)**: immediately before the event, P(collision of >1 mm debris with any operating spacecraft within 24 h) < 10⁻⁶. Coordinate with 18 SPCS no later than 30 days prior.
- **Requirement 4.5-1**: P(accidental collision with >10 cm objects) over orbital lifetime < 0.001 (cap analysis lifetime at 100 years for storage-orbit cases).
- **Requirement 4.5-2**: during the mission, P(MMOD damage sufficient to prevent the required disposal maneuver) < 0.01.

## Key Concepts
- **Passivation catalog**: burn residuals; vent tanks/lines; vent pressurants; stop battery recharge (prefer disconnecting the array from the bus; else disconnect charge circuits); safe range-safety; de-energize CMGs. Sealed heat pipes, individual battery cells, and passive nutation dampers are called out as not requiring EOM depressurization. Leak-before-burst is helpful, not sufficient — still depressurize unless a relief device covers every plausible case.
- **Do not fire unused pyros** just to “safe” them if they are not part of pressure passivation — MMOD-damaged hardware plus a pyro is a fragmentation risk. Disarm firing circuits instead.
- **Intentional-breakup cloud physics**: early debris is spatially clumpy (high local flux); after days it becomes a pseudo-torus then a shell, at which random-encounter math applies. Near-term risk can only be computed days before the event.
- **Large vs small collision**: >10 cm is assumed catastrophic (direct debris source). Millimeter-to-centimeter MMOD can disable disposal (indirect future debris source). Approximate large-object probability as P ≈ F·A·T when the product is < 0.1.
- **Critical surfaces (4.5-2)**: only hardware needed for controlled reentry or transfer to a disposal orbit. DAS estimates failure probability; it is *not* a shielding-design tool — escalate to Bumper / ODPO if DAS shows a problem.
- **Uniform probability, not tailored consequence**: 4.4-1 and 4.5-1 are the same number on every NASA object so programs cannot bargain a looser explosion/collision budget.

## Mental Models
- Explosion risk is a *design reliability* number; collision risk is a *geometry × flux × time* number; passivation is the *after-mission energy* story.
- 0.001 explosion and 0.001 large-object collision are siblings: both target a very small chance that *someone else* later hits your fragments.
- 0.01 small-MMOD is about *keeping disposal alive*, not about payload survival (though the same method can be reused for instruments).
- Intentional breakup is two plans: development-time environment budget (4.4-3) and week-of 18 SPCS cloud (4.4-4).

## Anti-patterns
- **Leaving residuals “because leak-before-burst”**: still passivate.
- **Counting MMOD in the 0.001 explosion budget**: 4.4-1 excludes them; they belong in 4.5-2.
- **Using DAS to size Whipple shields**: DAS flags vulnerability; Bumper designs protection.
- **Planning an ASAT-like test without a 30-day 18 SPCS loop**: 4.4-4 is operational, not paperwork.
- **Passivating so late that leftover propellant cannot also shorten lifetime**: LEO depletion burns should also pull lifetime down.

## Key Takeaways
1. Show P(explosion) < 0.001 per free flyer via FMEA/PRA or equivalent.
2. Design passivation (or equivalent energy control) and put the timeline in the ODAR/EOMP.
3. Intentional breakups owe both a 1-year / 100 object-year long-term cap and a 10⁻⁶ 24-hour short-term cap.
4. P(>10 cm collision) < 0.001 over life; P(MMOD kills disposal) < 0.01 during the mission.
5. Mitigate large-object risk with orbit, area, or lifetime; mitigate small-object risk with shielding, layout, redundancy, compartmentalization.
6. Coordinate disposal and breakup burns with CARA/TOPO and 18 SPCS.

## Connects To
- **ch03**: Operational debris is planned release, not fragmentation.
- **ch05**: Passivation is usually sequenced with disposal; 4.6-4 reliability is separate from 4.5-2.
- **ch06**: Controlled-reentry failure probability multiplies casualty risk.
- **ch07**: ODAR Sections 4–5 and 11–12.
