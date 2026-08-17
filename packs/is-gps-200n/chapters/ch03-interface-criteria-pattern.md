# Chapter 3: Interface Criteria as ICD Shalls

## Core Idea
Section 3.3.1 is the pattern to steal when writing any RF (or similar physical) ICD: name the occupied band, the coherent source, the loss/noise/spurious budgets, the relative phasing, the user-received levels (including special volumes), group delay, coherence, and polarization. Quote the *kinds* of shalls, not the numeric RF dumps.

## Frameworks Introduced
- **Criteria block**: “the requisite characteristics of the SS/US interface for L1 and L2.” Everything here should be measurable by a user-segment or space-segment test.
- **Frequency-plan pattern**: state the analysis bandwidth (here, 20.46 MHz about L1/L2 for IIR–IIF; 30.69 MHz for GPS III/IIIF+), the coherent common source (nominal 10.23 MHz as seen on the ground), and the two carrier centers (L1 1575.42 MHz, L2 1227.6 MHz). Relativistic clock offset is an explicit ICD line, not a footnote for theorists.
- **Quality budgets as shalls**: correlation loss (code- and block-dependent dB caps), carrier phase noise (trackable to 0.1 rad rms in a stated loop bandwidth), in-band spurious (≤ −40 dBc, with “in-band” defined as energy in the 3.3.1.1 bands that is *not* an L1/L2 component).
- **Phasing pattern**: L1 C/A lags P by 90° within a milliradian tolerance; bit-state to phase-reversal rules are written so a user can reconstruct the composite constellation. Later L2 civil/P components may be quadrature *or* co-phased — the ICD must say which degrees of freedom exist.
- **Level / delay / polarization pattern**: minimum received power tables exist per block and bandwidth (including Space Service Volume for GEO-based antennas); equipment group delay and its uncertainty/differential are specified; polarization is a shall, not an assumption.

## Key Concepts
- **Correlation loss definition** is itself ICD craft: difference between power in the specified band and power recovered by an ideal correlator with a linear-phase brick-wall replica. Caps differ by code family and SV block (tighter C/A & L2C on III/IIIF).
- **“In-phase” / “quadrature” are relative labels** — Table 3-III says so. Do not over-read them as an absolute ECEF frame.
- **SSV is a second user**: Space Service Volume levels are a separate criteria row, not a terrestrial afterthought. An ICD that forgets the second user community will be revised by PIRN.
- **Coherence** (3.3.1.8) ties back to 3.2.3: carriers, codes, and data on one SV come from one source. Criteria make the identification claim testable.
- **Skip list for this pack**: exact dB-min tables, milliradian-by-state phase tables, and chip-generator diagrams. They illustrate the pattern; they are not synthesized here.

## Mental Models
- A good physical ICD reads like a *test procedure waiting for numbers*.
- Bandwidth, coherence, budgets, geometry (phase/polarization), and delivered level are the five recurring slots.
- Block-conditional numbers are still one requirement family — tag the applicability; do not fork the document.

## Anti-patterns
- **Pasting every received-power table into notes** — implementers open the IS; agents need the slots.
- **Omitting the definition of correlation loss or “in-band spurious.”** Without the definition, the dB number is ambiguous.
- **Forgetting SSV or group-delay differential** because terrestrial users seemed sufficient.
- **Writing phase rules in prose only** with no tolerance.

## Key Takeaways
1. Steal the 3.3.1 slot list when authoring RF interface criteria.
2. Always bind numbers to a bandwidth, a block, and a user community (terrestrial vs SSV).
3. Define loss, noise, and spurious in testable words before stating limits.
4. Phasing and polarization are shalls with tolerances.
5. Coherence is how identification becomes verifiable.
6. Leave the numeric RF dumps in the official IS.

## Connects To
- **ch02**: Combinations that these criteria constrain.
- **ch04**: Data modulation sits on top of this physical layer.
- **ch05**: Time/Z-count is another criteria family (3.3.4).
- **faa-std-025**: Where those shalls would be outlined in an IRD and verified in a VRTM.
