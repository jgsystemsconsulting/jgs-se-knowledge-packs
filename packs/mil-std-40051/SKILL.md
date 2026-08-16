---
name: mil-std-40051
description: "Knowledge base from MIL-STD-40051-2C (15 Dec 2015), Preparation of Digital Technical Information for Page-Based Technical Manuals. Use for TM/TDP structure, work packages, front/back matter, style/format, warnings/HAZMAT, change packages, content selection matrices, and plate exemplars. Primary Training & Documentation pack (cluster 25) with Ops & Maintenance procedure use—page-based (-2C) only, not IETM 40051-1."
---

<!-- argument-hint: [TM, work package, front matter, warning, HAZMAT, change package, content matrix, DMWR, RPSTL, page-based, training documentation, or chapter number] -->

# MIL-STD-40051-2C — Page-Based Technical Manuals
**Source**: MIL-STD-40051-2C, 15 December 2015 (US DoD/DLA family; public domain; cover DISTRIBUTION STATEMENT A) | **Chapters**: 8 | **Basis**: selected main body ~151 pp of 584 extracted pages (plates skipped)

## When to use
Use this pack when **authoring, tailoring, reviewing, or training on page-based military technical manuals** under MIL-STD-40051-2C: scoping TM families, building work-package structures, completing front/back matter (including distribution/export notices), applying style/format and warning/HAZMAT rules, issuing change packages with revision bars, filling content selection matrices, and checking drafts against standard plate exemplars. Primary home is **Training & Documentation** production; also use for **Ops & Maintenance** procedure quality.

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime. Pair with acquiring-activity TM style guides and, if interactive manuals are in scope, a separate 40051-1/IETM source (not this pack).

## How to Use This Skill
- **Without arguments** — load the core frameworks below.
- **With a topic** — ask about work packages, front matter, warnings, changes, matrices, DMWR/NMWR, or training documentation delivery.
- **With a chapter** — ask for `ch01` through `ch08`.

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

## Core Frameworks & Mental Models

### Page-based TM spine
**Matrix → WP structure → front matter/release markings → formatted procedures with warnings → change control → exemplar QA.**

### 40051 family split
| Part | Product |
|------|---------|
| 40051-1 | IETM (interactive) — out of scope here |
| **40051-2C** | **Page-based TM / ETM synonym in this standard** |

### Work package module
Initial setup → warned steps → figures/tables → end-of-WP → stable ID for training and field citation.

### Dual-layer hazards
Warning summary (front) + step-adjacent WARNING/CAUTION/NOTE (+ HAZMAT icons).

### Change effectivity
Change package + revision bars + title-page dates + TOC; same state for ops and training fleets.

### Content selection
Appendix/matrix-driven include lists per maintenance level and TM type (operator, maintainer, DMWR/NMWR, PM products, BDAR, software, etc.).

## Chapter Index
| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-scope-tm-family-and-applicability.md) | Scope, TM Family, Applicability | -2C slice, TM types, DIST-A on standard |
| [ch02](chapters/ch02-tm-structure-and-work-packages.md) | TM Structure and Work Packages | Chapters, WP anatomy, numbering |
| [ch03](chapters/ch03-front-matter-and-back-matter.md) | Front and Back Matter | Cover, warning summary, title, TOC, reporting |
| [ch04](chapters/ch04-style-format-and-layout-rules.md) | Style, Format, Layout | Trim, headers, tables, figures, xrefs |
| [ch05](chapters/ch05-warnings-cautions-notes-and-hazmat.md) | Warnings, Cautions, HAZMAT | Signal words, icons, placement |
| [ch06](chapters/ch06-change-packages-and-revision-marking.md) | Change Packages and Revision Marking | Bars, renumber, effectivity |
| [ch07](chapters/ch07-content-selection-matrix-and-tailoring.md) | Content Selection and Tailoring | Matrices, levels, appendix roles |
| [ch08](chapters/ch08-plate-exemplars-and-production-patterns.md) | Plate Exemplars | Sample plates as production patterns |

## Topic Index
- **Battle damage / BDAR documentation** → ch01, ch07
- **Change package / revision bars / effectivity** → ch06
- **Comprehensibility / reading grade** → ch01, ch04
- **Content selection matrix / tailoring** → ch07
- **Distribution statement / export / destruction notices** → ch03
- **DMWR / NMWR** → ch01, ch03, ch08
- **Documentation production / authoring line** → ch04, ch07, ch08
- **Front matter / title page / TOC** → ch03
- **HAZMAT warnings and icons** → ch05
- **Initial setup information** → ch02
- **Maintenance levels (operator through depot)** → ch01, ch07
- **Ops & Maintenance procedure use** → ch02, ch05
- **Page-based TM / ETM synonym** → ch01
- **Phased maintenance / PMC / PMS / PMD / PMI** → ch01, ch07
- **Plate exemplars / sample covers and WPs** → ch08
- **RPSTL** → ch02, ch07
- **Style / trim size / figures / tables** → ch04
- **Technical manual training materials** → ch01, ch07, ch08
- **Training & Documentation** → ch01, ch07, ch08, Topic Index
- **Warning / caution / note signal words** → ch05
- **Warning summary** → ch03, ch05
- **Work package (WP) structure and numbering** → ch02, ch06

## Supporting Files
- [glossary.md](glossary.md) — TM/40051 terms with chapter refs
- [patterns.md](patterns.md) — eight production/review patterns
- [cheatsheet.md](cheatsheet.md) — stacks, checklists, cluster hooks

---

## Scope & Limits
- Covers **MIL-STD-40051-2C** page-based TM requirements from a **selected main-body extraction** (plates largely skipped; see PACK.yaml notes).
- Does **not** cover MIL-STD-40051-1 IETM interactive behavior.
- Synthesized reference notes for Training & Documentation and Ops & Maintenance practice—not a substitute for the official ASSIST/everyspec publication on contract.
- No source PDF or full-text redistribution in this pack.
