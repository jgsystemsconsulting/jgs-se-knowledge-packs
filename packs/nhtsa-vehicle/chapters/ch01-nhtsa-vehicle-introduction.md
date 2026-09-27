# Chapter 1: Introduction: Scope of the NHTSA Vehicle Safety Pack

> Source: pack scope across NHTSA Cybersecurity Best Practices for the Safety of Modern Vehicles (Updated 2022, final), NHTSA Automated Driving Systems 2.0: A Vision for Safety (2017), and the 16 selected 49 CFR Part 571 sections pinned at eCFR versioner date 2025-01-01.

## Core Idea

This pack is a synthesized reference for three US Government vehicle-safety sources that systems engineers meet when work touches modern road vehicles in the United States: NHTSA's 2022 cybersecurity best-practices guidance, NHTSA's 2017 Automated Driving Systems (ADS) voluntary guidance known as ADS 2.0, and a fixed selection of Federal Motor Vehicle Safety Standards (FMVSS) from 49 CFR Part 571. The chapters restate what those sources organize and cover. They do not reprint regulation text, do not invent process frameworks the sources lack, and do not stand in for excluded industry standards the sources only name.

The three sources play different roles. The cybersecurity document is non-binding voluntary guidance for product cybersecurity across motor vehicles and motor vehicle equipment, including software. ADS 2.0 is voluntary guidance and a vision document for automated driving systems on public roads; it is not a final federal ADS statute or a complete ADS rulebook. The FMVSS slice is a set of vehicle-level minimum performance standards, not a process standard and not the whole of Part 571.

## What the Pack Contains

**Document 1 , Cybersecurity Best Practices for the Safety of Modern Vehicles (Updated 2022, final).** NHTSA's updated voluntary guidance on organizational and technical practices that reduce safety risk from vehicle cybersecurity. Chapter 2 synthesizes the practice areas the 2022 document itself uses. Four PDF pages that carried verbatim third-party standard requirement text in footnotes were screened out of the source base; the pack does not draw prose from those pages.

**Document 2 , Automated Driving Systems 2.0: A Vision for Safety (2017).** NHTSA's voluntary guidance organized around twelve priority safety design elements, a Voluntary Safety Self-Assessment path, and technical assistance material aimed at States. Chapter 3 synthesizes that structure. Currency is fixed by the pack's SOURCE-VETTING row rather than by restating later draft policy as if it had already replaced ADS 2.0.

**Document 3 , Sixteen FMVSS sections at eCFR 2025-01-01.** The pinned snapshot includes all sixteen section identifiers below. Chapters 4 through 6 cover them by theme (occupant protection; brakes, stability, and lighting; fuel and electric-vehicle integrity including minimum sound). Official short titles come from the section headings in that snapshot.

| Section id | Official short title (heading) |
|---|---|
| 571.102 | Standard No. 102; Transmission shift position sequence, starter interlock, and transmission braking effect |
| 571.103 | Standard No. 103; Windshield defrosting and defogging systems |
| 571.105 | Standard No. 105; Hydraulic and electric brake systems |
| 571.108 | Standard No. 108; Lamps, reflective devices, and associated equipment |
| 571.126 | Standard No. 126; Electronic stability control systems for light vehicles |
| 571.127 | Standard No. 127; Automatic emergency braking systems for light vehicles |
| 571.135 | Standard No. 135; Light vehicle brake systems |
| 571.141 | Standard No. 141; Minimum Sound Requirements for Hybrid and Electric Vehicles |
| 571.201 | Standard No. 201; Occupant protection in interior impact |
| 571.208 | Standard No. 208; Occupant crash protection |
| 571.209 | Standard No. 209; Seat belt assemblies |
| 571.210 | Standard No. 210; Seat belt assembly anchorages |
| 571.214 | Standard No. 214; Side impact protection |
| 571.226 | Standard No. 226; Ejection Mitigation |
| 571.301 | Standard No. 301; Fuel system integrity |
| 571.305 | Standard No. 305; Electric-powered vehicles: electrolyte spillage and electrical shock protection |

Pinned date for the FMVSS text: **2025-01-01** (eCFR versioner). Section 571.141 is present in that snapshot; the pack therefore includes minimum-sound coverage rather than the absent-section fallback.

## What the Pack Refuses

- **Not ISO 26262, not ASPICE, not ISO/SAE 21434, not UNECE R155 or R156, not SAE J3016.** Those instruments are outside this pack's body text. Where a reader needs the industry landscape that names them, use the signpost packs by slug only: `automotive-signpost` and `functional-safety-signpost`. This pack may name those standards when the NHTSA sources name them; it never quotes their requirements.
- **Not the whole of Part 571.** The FMVSS chapters are a deliberate 16-section selection. Adjacent bands and heavy-vehicle brake or stability standards that sit outside the list are out of scope even when a reader might expect them next door.
- **Not final federal ADS policy.** ADS 2.0 is voluntary guidance and a vision document. A successor exists in draft; do not treat this pack's ADS chapter as the last word of US federal ADS regulation.
- **Not a cybersecurity regulation or mandate.** The 2022 cybersecurity document is guidance. Manufacturers decide whether and how to apply it to their systems.
- **Not a process standard for how to engineer a vehicle.** FMVSS entries state vehicle-level minimum performance expectations under defined tests and applications. They do not replace systems-engineering life-cycle process models.

## How to Read the Later Chapters

- Chapter 2 follows the 2022 cybersecurity document's own headings: purpose and scope, general best practices (leadership, development process, information sharing, vulnerability reporting, incident response, self-auditing), audience and serviceability notes, and technical best practices.
- Chapter 3 follows ADS 2.0's voluntary-guidance spine (twelve safety elements and the self-assessment) and the States technical-assistance section, with the currency caveat required by SOURCE-VETTING.
- Chapters 4–6 give, for each selected FMVSS section, the official short title, the vehicle classes the section applies to, and a synthesized note on the performance area it governs. No tables are copied from the XML; no clause text is reproduced.

## Key Takeaways

1. The pack combines three US Government sources: Cyber 2022 guidance, ADS 2.0 voluntary vision guidance, and sixteen FMVSS sections pinned at eCFR **2025-01-01**.
2. All sixteen section ids, including **571.141**, are present in the pinned snapshot and are in scope.
3. Cyber 2022 is **guidance**, not a regulation; ADS 2.0 is **not** final federal ADS policy; the FMVSS slice is **not** the whole of Part 571.
4. Excluded industry standards (ISO 26262, ASPICE, ISO/SAE 21434, UNECE R155/R156, SAE J3016) are named only by reference; detail lives in `automotive-signpost` and `functional-safety-signpost`.
5. Chapters synthesize original reference notes. They do not reprint requirement language even though the underlying US Government works are public domain.

## Connects To

- **ch02 (cyber practices):** organizational and technical practices from the 2022 cybersecurity guidance.
- **ch03 (ADS vision):** twelve safety design elements, self-assessment, and State roles from ADS 2.0.
- **ch04, ch06 (FMVSS selection):** occupant, chassis/lighting, and fuel/EV performance standards in the 16-section list.
- **`automotive-signpost` / `functional-safety-signpost`:** industry standards this pack deliberately does not reproduce.
- **Open SE process models:** life-cycle and risk process packs that sit beside vehicle performance standards rather than inside them.
