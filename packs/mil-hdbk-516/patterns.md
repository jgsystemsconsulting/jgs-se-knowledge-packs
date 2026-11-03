# Patterns  -  MIL-HDBK-516D

Reusable patterns for applying MIL-HDBK-516D, 29 May 2026. Method only. No criterion cells.

## Pattern: Build a certification basis

**When:** Starting or major-modifying an air system AW basis.

**How:**

1. Frame usage, configuration, and environment (ch02).
2. Tailor applicable sections from the frozen chapter set (ch01 method).
3. For each selected standard, name MoCs and evidence owners.
4. Integrate system safety hazards and residual risk.
5. Place the basis under CM with manuals and software loads.

**Trade-offs:** Full-catalogue adoption looks complete but hides non-applicable noise. Aggressive cuts without authority agreement reopen late.

## Pattern: Standard plus MoC argument

**When:** Closing any single criterion.

**How:**

1. State the design attribute in own words.
2. Point to analysis, test, demonstration, or examination MoCs that actually apply.
3. Record limitations and residual risk.
4. Link related domain chapters (structure/flight, power/control, software/host).

**Trade-offs:** Analysis-only MoCs are fast and weak for high-criticality claims. Test-heavy MoCs are strong and expensive.

## Pattern: Degraded-state first

**When:** Flight technology, subsystems, electrical, or VCF claims.

**How:**

1. List credible single failures (hydraulic loss, power channel loss, control path loss).
2. Show flying qualities or SCF retention after each.
3. Only then close the healthy-aircraft case.

**Trade-offs:** Healthy-only evidence fails review. Enumerating every remote failure without tailoring wastes effort.

## Pattern: Modification reopener

**When:** DMS, form-fit-function, software load, store set, or outer mold line change.

**How:**

1. Diff the change against structures, electrical/E3, avionics/CS&S, and mass properties.
2. Re-enter only the affected criteria and MoCs.
3. Update manuals and configuration identity.

**Trade-offs:** "Same form-fit-function" claims without E3/software check are a common miss.

## Pattern: Maintenance products as MoC

**When:** Section 16 criteria or damage-tolerance / corrosion assumptions.

**How:**

1. Drive cautions, warnings, and tests from FMECA-quality analysis.
2. Align inspections with NDI and durability plans.
3. CM the publications with the approved design.

**Trade-offs:** Orphan manuals drift from the flying configuration and quietly invalidate prior approvals.

## Pattern: Named references only

**When:** Section 2 publications and any cited MIL, JSSG, FAA, SAE, or statute.

**How:**

1. Name the document and the role it plays.
2. Do not paste long requirements text into the pack or into informal notes derived from this pack.
3. Pull the authoritative text from the program's controlled source when implementing.

**Trade-offs:** Quoting feels faster and creates stale, possibly wrong copies.
