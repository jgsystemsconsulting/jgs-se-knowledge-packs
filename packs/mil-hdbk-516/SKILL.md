---
name: mil-hdbk-516
description: "Knowledge base from MIL-HDBK-516C (Airworthiness Certification Criteria). Use for DoD air-system airworthiness planning: tailoring a certification basis, systems engineering criteria, and domain clusters for structures, flight technology, propulsion/installation, avionics/electrical/E3/diagnostics, computer systems/software, and crew systems (including applicable UAS control-station elements). Qualitative guidance handbook — not raw contractual requirements. Does not replace service airworthiness authority policy, civil FAA certification rules as authorities, or detailed JSSG/MIL performance specs."
---

<!-- argument-hint: [airworthiness topic, certification basis, domain criteria, or chapter number] -->

# MIL-HDBK-516C — Airworthiness Certification Criteria
**Source**: DoD MIL-HDBK-516C (US Government work, public domain; Distribution Statement A) | **Chapters**: 8

## When to use
Use this pack when building or reviewing a DoD air system airworthiness certification basis from MIL-HDBK-516C — tailoring qualitative criteria, assigning methods of compliance, and navigating domain criteria clusters (SE, structures, flight, propulsion, avionics/E3, software, crew systems). Helpful for airworthiness engineers, SE leads, and domain SMEs aligning evidence to criteria.

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill
- **Without arguments** — load the core frameworks below.
- **With a topic** — ask about certification basis tailoring, SE criteria, structures, flight, propulsion, avionics/E3, software, or crew systems.
- **With a chapter** — ask for `ch01` through `ch08`.

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

> **Guidance only.** 516C says it is not to be cited as a requirement. Criteria are qualitative; define acceptable in the implementing context.

## Core Frameworks & Mental Models

### Certification basis via tailoring
Select a necessary and sufficient subset of 516C criteria for the specific air system; document methods of compliance; maintain under configuration control.

### Qualitative criteria plus evidence
Each section states criteria and often lists typical certification source data (analyses, tests, inspections). Closure is a reasoned evidence argument, not a single signature.

### SE backbone then domains
Systems engineering criteria (design criteria, tools, materials, manufacturing/quality, tech data, CM) underpin domain sections.

### Domain clusters in this pack
Structures; flight technology; propulsion plus installation; diagnostics/avionics/electrical/E3; computer systems/software; crew systems (including UAS/ROA control-station elements when applicable).

### UAS applicability
Avionics and crew-systems material explicitly contemplates unmanned/remotely operated control segments where they affect airworthiness.

## Chapter Index
| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-scope-applicability-and-tailoring.md) | Scope, Applicability, Tailoring | Handbook role, certification basis, tailoring rules |
| [ch02](chapters/ch02-systems-engineering-criteria.md) | Systems Engineering | Design criteria, tools, materials, quality, tech data, CM |
| [ch03](chapters/ch03-structures-criteria.md) | Structures | Structural airworthiness criteria and evidence patterns |
| [ch04](chapters/ch04-flight-technology-criteria.md) | Flight Technology | Flying qualities/performance/control evidence thinking |
| [ch05](chapters/ch05-propulsion-criteria.md) | Propulsion & Installation | Propulsion unit plus air-vehicle installation criteria |
| [ch06](chapters/ch06-avionics-e3-and-diagnostics.md) | Avionics / Electrical / E3 / Diagnostics | Electronics-heavy airworthiness cluster |
| [ch07](chapters/ch07-computer-systems-and-software.md) | Computers & Software | Software/computer system airworthiness criteria |
| [ch08](chapters/ch08-crew-systems-criteria.md) | Crew Systems | HMI, life support, escape, UAS control stations |

## Topic Index
- **Airworthiness authority / implementing office** → ch01
- **Avionics** → ch06
- **Certification basis** → ch01
- **Certification source data lists** → ch02–ch08
- **Configuration management (airworthiness)** → ch02
- **Crew station / HMI** → ch08
- **Diagnostics** → ch06
- **E3 / EMI/EMC airworthiness** → ch06
- **Electrical power system** → ch06
- **Escape / life support / crash survivability** → ch08
- **Flight technology / flying qualities** → ch04
- **Materials selection (SE)** → ch02
- **Methods of compliance** → ch01
- **Propulsion installation** → ch05
- **Software airworthiness** → ch07
- **Structures / damage tolerance framing** → ch03
- **Tailoring rules** → ch01
- **UAS/ROA control station** → ch06, ch08

## Supporting Files
- [glossary.md](glossary.md) — airworthiness terms used in 516C packing
- [patterns.md](patterns.md) — implementation patterns with When/How/Trade-offs
- [cheatsheet.md](cheatsheet.md) — decision rules, maps, tells & smells

---

## Scope & Limits
This pack covers **selected** MIL-HDBK-516C (12 Dec 2014) material: scope/tailoring, systems engineering, and major functional-area clusters (structures, flight, propulsion, avionics/electrical/E3/diagnostics, software, crew systems). Extraction metadata reports **527 PDF pages** for the everyspec mirror copy used at build (build-sheet estimate ~320; PDF page objects differ — body text and DIST-A verified; chars/page floor passed). Not every handbook subsection is chaptered (for example armaments, passenger safety, materials-as-own-chapter, air transportability). Does **not** reproduce full criterion text catalogs or third-party FAA/SAE standards. Guidance only. US Government public domain work (Distribution Statement A). No source-material download link is published.
