---
name: sebok
description: "Knowledge base from the Guide to the Systems Engineering Body of Knowledge (SEBoK) v2.13 by the BKCASE Project. Use when referencing the established systems-engineering canon — lifecycle models, ISO/IEC/IEEE 15288 processes, system definition and architecture, V&V, MBSE, systems thinking, traceability, standards alignment, and SoS/enterprise/service SE. Good for grounding background and prior-art positions; thin on AI integration."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Guide to the Systems Engineering Body of Knowledge (SEBoK)
**Source**: BKCASE Project (Trustees of Stevens Institute of Technology) | **Version**: 2.13 (released 17 Nov 2025) | **Pages**: ~1,465 | **Chapters**: 41 | **Licence**: CC BY-NC-SA 3.0 | **Generated**: 2026-06-19

## When to use

Use this pack when you need the established systems-engineering canon: lifecycle models, ISO/IEC/IEEE 15288 processes, system definition and architecture, V&V, MBSE, systems thinking, traceability, standards alignment, or SoS/enterprise/service SE. Best for grounding background and prior-art positions; not for the AI-in-MBSE frontier (SEBoK is deliberately thin there).

**Prerequisites:** none — this pack is plain Markdown; no MCP server, API key, or licence tier is needed at runtime.

## How to Use This Skill

- **Without arguments** — load the core frameworks below for reference
- **With a topic** — ask about `lifecycle models`, `MBSE`, `traceability`, `tailoring`, `SoS`, or another indexed topic; I find and read the relevant chapter file
- **With a chapter** — ask for `ch18` to load System Architecture Design Definition
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I read the relevant `chapters/chNN-*.md` file before answering. Supporting files: `glossary.md` (105 terms), `patterns.md` (23 techniques), `cheatsheet.md` (decision rules and selection tables).

**Scope honesty:** SEBoK is the consensus SE reference — strong on fundamentals, lifecycle, processes, architecture, standards. It is *deliberately thin on AI/ML integration* (≈40 mentions across 1,465 pp). For the AI-in-MBSE frontier, use the `literature/` corpus, not this skill. SEBoK's best use here is establishing the textbook baseline you cite *before* introducing a contribution.

---

## Core Frameworks & Mental Models

**The Systems Approach (Ch 5, 7).** SEBoK's spine: tackle real-world problems with the concepts, principles and patterns of *systems thinking* before formal specification. When uncertainty is high, the opening question is "what's going on here?", not "what are the requirements?". Encapsulation and separation of concerns let you focus on one element while bounding the ripple of changes across related components.

**Emergence & the System-of-Interest (SoI) (Ch 2, 3).** A system is a set of elements with enough "togetherness" to form a bounded whole whose behaviour emerges from *interactions*, not parts alone. The **SoI** is the engineered system under a given lifecycle, distinguished from its **enabling systems** and its **system context** (everything across its boundary). Get the boundary and context right first; requirements cascade from it.

**ISO/IEC/IEEE 15288 as the gravitational centre (Ch 14, 20).** 15288 (System Life Cycle Processes) is the baseline all other SE standards orbit — 12207 (software), 24765/SEVocab (vocabulary), 24748 (lifecycle management guidance), 42010 (architecture description). Process groups: **Agreement, Organizational Project-Enabling, Technical Management, Technical**. Use SEVocab terms first to avoid cross-standard ambiguity. Distinguish **conformance** (voluntary) from **compliance** (mandated), and **full** vs **tailored** conformance — always declare which you claim.

**Life Cycle Model Selection (Ch 10, 13).** No universal model: select by uncertainty, change rate, and risk. **Vee** for well-understood, low-change systems; **incremental/iterative** for partial knowledge; **evolutionary/agile** for high uncertainty and fast feedback; **spiral (ICSM)** to risk-drive the choice. Tailor the chosen model — selection is a design decision, not a default.

**Architecture: logical before physical (Ch 18, 22).** Develop a **functional/logical architecture** (what the system must do) and allocate to a **physical architecture** (how) iteratively. Use **42010 viewpoints/views** to address stakeholder concerns. Maintain bidirectional **traceability** from needs → requirements → architecture → V&V.

**MBSE (Ch 6, 9).** Model-Based Systems Engineering replaces the document-centric approach with a single authoritative model (often SysML) as the source of truth, enabling consistency, query, and automated views. SEBoK frames MBSE as the trajectory of modern SE practice and the bridge to digital engineering.

**System classification drives method (Ch 21–25).** Classify the SoI as **product / service / enterprise / system-of-systems** — each has different stakeholders, value-delivery, and governance. Apply **Maier's independence test** (operational + managerial independence) to detect a true SoS, which needs federated governance and a wave-model evolution, not monolithic control.

---

## Chapter Index

| # | Knowledge Area | Key Frameworks |
|---|----------------|----------------|
| [ch01](chapters/ch01-foundations-of-systems-engineering.md) | Foundations of Systems Engineering | Systems Praxis Framework; Integrative Systems Science |
| [ch02](chapters/ch02-systems-engineering-fundamentals.md) | Systems Engineering Fundamentals | System Context Model; Engineered System Context |
| [ch03](chapters/ch03-the-nature-of-systems.md) | The Nature of Systems | Six Intertwined Concepts; Ten Systems Concerns |
| [ch04](chapters/ch04-systems-science.md) | Systems Science | General Systems Theory; Cybernetics |
| [ch05](chapters/ch05-systems-thinking.md) | Systems Thinking | The Systems Approach; System Dynamics |
| [ch06](chapters/ch06-representing-systems.md) | Representing Systems | MBSE; View and Viewpoint |
| [ch07](chapters/ch07-systems-approach-applied-to-engineered-systems.md) | Systems Approach Applied | Open System Relationships Model |
| [ch08](chapters/ch08-applications-of-systems-engineering.md) | Applying the Systems Approach | System Value Cycle; Concurrent Activities |
| [ch09](chapters/ch09-systems-engineering-and-management.md) | Model-Based Systems Engineering | MBSE; SysML; Architecture Frameworks |
| [ch10](chapters/ch10-life-cycle-terms-and-concepts.md) | Life Cycle Terms and Concepts | Technical Review; Audit; Review Timing |
| [ch11](chapters/ch11-development-approaches.md) | Development Approaches | ICSM; DevOps/CI-CD; Scrum |
| [ch12](chapters/ch12-agile-systems-engineering.md) | Agile Systems Engineering | Situation Context Framework |
| [ch13](chapters/ch13-life-cycle-model-selection-and-adaptation.md) | Life Cycle Model Selection & Adaptation | 24748-1; Hump Diagram |
| [ch14](chapters/ch14-process-concepts.md) | Process Concepts | ISO/IEC/IEEE 15288; 24748-2; Risk-based Tailoring |
| [ch15](chapters/ch15-process-selection-and-tailoring.md) | Process Selection and Tailoring | PMI Scaling Factors; Concurrency/Iteration/Recursion |
| [ch16](chapters/ch16-technical-management-processes.md) | Technical Management Processes | Decision Management; Trade Study; SEAC |
| [ch17](chapters/ch17-system-concept-definition.md) | System Concept Definition | Mission Analysis; Stakeholder Needs; MGOs |
| [ch18](chapters/ch18-system-architecture-design-definition.md) | System Architecture Design Definition | Logical & Physical Architecture; Functional Architecture |
| [ch19](chapters/ch19-system-maintenance.md) | System Maintenance | Service Life Extension; Life Cycle Cost |
| [ch20](chapters/ch20-systems-engineering-standards.md) | Systems Engineering Standards | 15288; 12207; 24765/SEVocab |
| [ch21](chapters/ch21-applications-of-systems-engineering.md) | Applications of Systems Engineering | Four application Knowledge Areas |
| [ch22](chapters/ch22-product-systems-engineering.md) | Product Systems Engineering | 42010 Architecture Definition; IPD/IPPD; CM |
| [ch23](chapters/ch23-service-systems-engineering.md) | Service Systems Engineering | SLA; Service Design Process |
| [ch24](chapters/ch24-enterprise-systems-engineering.md) | Enterprise Systems Engineering | Maier's SoS Definition; Federation of Systems |
| [ch25](chapters/ch25-systems-of-systems-sos.md) | Systems of Systems (SoS) | SoS Wave Model; Complexity Primer |
| [ch26](chapters/ch26-healthcare-systems-engineering.md) | Healthcare Systems Engineering | VA 4-Pillar Methodology; Lean Six Sigma |
| [ch27](chapters/ch27-enabling-systems-engineering.md) | Enabling Systems Engineering | CMM; INCOSE SE Competencies |
| [ch28](chapters/ch28-enabling-businesses-and-enterprises.md) | Enabling Businesses and Enterprises | SE Organizational Strategy |
| [ch29](chapters/ch29-enabling-teams.md) | Enabling Teams | Leadership Styles; Fiedler's Contingency Model |
| [ch30](chapters/ch30-enabling-individuals.md) | Enabling Individuals | INCOSE SE Competency Model |
| [ch31](chapters/ch31-related-disciplines.md) | Related Disciplines | (navigational — cross-discipline KAs) |
| [ch32](chapters/ch32-systems-engineering-and-environmental-engineering.md) | SE & Environmental Engineering | Environmental Impact Assessment; Green Engineering |
| [ch33](chapters/ch33-systems-engineering-and-geospatial-geodetic-engi.md) | SE & Geospatial/Geodetic Engineering | GIS; Positioning, Navigation & Timing |
| [ch34](chapters/ch34-systems-engineering-and-industrial-engineering.md) | SE & Industrial Engineering | Work Breakdown Structure; Cost Estimating Relationships |
| [ch35](chapters/ch35-systems-engineering-and-project-management.md) | SE & Project Management | Acquisition Process; Portfolio Management |
| [ch36](chapters/ch36-systems-engineering-and-software-engineering.md) | SE & Software Engineering | Phase-Specific Feature Tables; Software Metrics |
| [ch37](chapters/ch37-systems-engineering-and-mechanical-engineering.md) | Loss-Driven Systems Engineering | LDSE; Loss Control Design Principles |
| [ch38](chapters/ch38-systems-engineering-and-enterprise-it.md) | SE & Enterprise IT | Human Systems Integration; Seven HSI Domains |
| [ch39](chapters/ch39-systems-engineering-and-quality-attributes.md) | SE & Quality Attributes | RAM Engineering Lifecycle; Hardware Assurance |
| [ch40](chapters/ch40-se-implementation-examples.md) | SE Implementation Examples | ICSM; Complex Adaptive Systems scheduling |
| [ch41](chapters/ch41-emerging-knowledge.md) | Emerging Knowledge | MBSE; Model Driven Architecture |

## Topic Index

- **15288 / lifecycle processes** → ch14, ch20, ch10
- **Standards alignment, conformance, tailoring** → ch20, ch15
- **Lifecycle models (Vee, agile, incremental, spiral)** → ch13, ch11, ch12, ch10
- **MBSE / SysML / digital engineering** → ch09, ch06, ch41
- **Architecture (logical, physical, viewpoints, 42010)** → ch18, ch22, ch06
- **Requirements / stakeholder needs / mission analysis** → ch17, ch16
- **Traceability** → ch18, ch16, ch20
- **Verification & Validation** → ch16, ch10, ch39
- **Systems thinking / systems science / emergence** → ch05, ch04, ch03
- **System-of-Interest, boundary, context** → ch02, ch03
- **System classification (product/service/enterprise/SoS)** → ch21, ch22, ch23, ch24, ch25
- **Systems of Systems / Maier independence / federation** → ch25, ch24
- **Trade studies / decision management** → ch16
- **Process selection & tailoring** → ch15, ch14
- **Competency / teams / organizations** → ch27, ch28, ch29, ch30
- **Quality attributes / RAM / assurance** → ch39
- **Software engineering interface** → ch36
- **Project management interface** → ch35, ch34

## Supporting Files

- [glossary.md](glossary.md) — 105 key SE terms with definitions and chapter refs
- [patterns.md](patterns.md) — 23 concrete techniques (context modelling, integration matrices, tailoring, trade studies, V&V, SoS governance)
- [cheatsheet.md](cheatsheet.md) — decision rules, lifecycle-model selection table, system-classification matrix, tells & smells

---

## Scope & Limits

This skill covers SEBoK v2.13 content only. SEBoK is a consensus reference, deliberately conservative and citation-grounded — strong for the established SE position, weak on emerging AI/ML integration. For thesis work: cite SEBoK to ground background and prior art (e.g. "MBSE is established practice", baseline traceability, the 15288 process model); use the `literature/` corpus for the AI-in-MBSE frontier. SEBoK is CC BY-NC-SA — content is openly reusable with attribution and share-alike.
