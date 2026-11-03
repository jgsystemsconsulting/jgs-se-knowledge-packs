# Chapter: Avionics, electrical system, and E3

## Core Idea

This chapter groups section 11 (avionics), section 12 (electrical system), and section 13 (electromagnetic environmental effects). Avionics covers communication, navigation, and identification (CNI); architecture; safety-critical displays and controls; diagnostics; and technical-manual engineering data. The foreword records that prior-edition diagnostics content folds into section 11.

Electrical criteria address power generation and wiring for airborne and shipboard use, including modifications and diminishing-manufacturing-sources changes. Stores with electrical power or wiring that affect safety-critical systems are treated as extensions of the air vehicle.

E3 criteria establish electromagnetic compatibility (EMC) in the intended electromagnetic environment (EME), including lightning and precipitation-static concerns when outer mold line or equipment changes matter. MIL-STD-464 is named as a related E3 requirements source that programs may tailor with engineering justification.

## Frameworks Introduced

### Avionics buildup

Demonstrate CNI, architecture, safety-critical human-machine interfaces, and diagnostics with design, analysis, and test data at subsystem then system level.

### Diagnostics fold

Diagnostic capability is part of avionics under D, not a separate chapter. MoCs show detection and isolation performance that supports safe operation and maintenance decisions.

### Electrical as generation plus wiring

Separate power-generation claims from wiring-system claims, then integrate for safety-critical loads and fault behavior.

### E3 at component and system level

Qualify equipment and the installed system against the operational EME. Tailor early using operational requirements and analysis.

## Key Concepts

- **CNI and CNS/ATM.** Communication, navigation, identification, and air-traffic management interfaces as design attributes.
- **Avionics architecture.** Integration, partitioning, and integrity of the avionics suite.
- **Safety-critical displays and controls.** Human-machine interfaces that affect SOF.
- **Diagnostics.** Onboard detection and isolation supporting AW and maintenance.
- **Electrical power generation.** Sources, quality, and distribution under normal and failure conditions.
- **Wiring system.** Installation, protection, and integrity of wiring, including legacy wiring touched by mods.
- **EMC / EME / E3.** Compatibility inside the air system and with the external environment.
- **Lightning and p-static.** Outer mold line and equipment changes can reopen these claims.

## Mental Models

- **Installed performance beats bench-only.** Box qualification is not the full E3 or avionics story.
- **Stores extend the vehicle.** Electrical stores ride the same safety-critical assessment when they couple to vehicle systems.
- **Named standards, not quotes.** Cite MIL-STD-464 and peer documents by name; do not paste their text.

## Key Takeaways

- Sections 11-13 cover avionics (with diagnostics), electrical power/wiring, and E3.
- Diagnostics folds into avionics per the foreword.
- Treat wiring and generation as distinct then integrated claims.
- Reopen E3 when equipment or outer mold line changes.

## Connects To

- ch04 and ch07 for safety-critical displays and VCF interfaces
- ch06 for power consumers and bonding-related subsystems
- ch09 for software hosted on avionics processors
- ch11 for armament electronics interfaces
