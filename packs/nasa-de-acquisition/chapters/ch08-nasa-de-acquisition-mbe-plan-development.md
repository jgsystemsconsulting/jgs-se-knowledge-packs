# Chapter — Model-Based Engineering (MBE) Plan Development

> Source: NASA-HDBK-1004, Appendix J ("Model-Based Engineering (MBE) Plan"), including Table 9 (MBE Plan Development Guidelines) and Table 10 (MBE Plan Section Development).
> Caveat: This pack pairs with NASA-HDBK-1009A. Where 1009A goes deeper on digital-engineering and model/simulation credibility practice, this chapter stays within the acquisition-and-planning scope of 1004 and defers detailed M&S credibility treatment to its companion.

## Core Idea

The MBE Plan is the controlled document through which a program manager and the various providers of model-based engineering services reach and record a shared agreement on *how* a program's MBE capabilities will actually be delivered. Its job is not to invent the engineering itself but to pin down the delivery mechanism: which Center is responsible for what, which tools and IT services back each capability, what the implementation approach is, and the timing for standing up the MBE environment along with its associated processes, data, elements, attributes, and formats. Because so much of MBE rests on information-technology infrastructure, the Plan deliberately ties program documents, project data, and process requirements together with the provision of IT capabilities and services so they stay synchronized.

A defining feature is that the Plan is a *living, formally controlled* artifact rather than a one-time deliverable. Its content shifts with two independent forces: the program's own life-cycle phasing, and current or planned changes to the IT used to implement MBE — for example upgrades and new capabilities that the MBE tool vendors commit to. For a single-project or tightly coupled program (using the definitions in NPR 7120.5), one program-wide Plan is produced rather than scattered project-level versions. The Plan must be refreshed at least annually or at a major Key Decision Point (KDP), and for product life-cycle purposes it is maintained all the way through KDP F, the close-out and archival of data.

## Frameworks Introduced (exact source names, when/how)

- **MBE Plan Development Guidelines (Table 9)** — A recommended guideline that lays out, element by element and phase by phase, the MBE framework information to be captured in the Plan. It is used at the outset to decide what maturity each MBE element should reach as the program advances. Table 9 maps MBE elements against the NASA life-cycle phases (Pre-Phase A through Phase F, spanning Formulation and Implementation) and the KDP gates (KDP 0 through KDP VI), marking each cell as Preliminary, Baseline, or Update so the team can plan when each element firms up.

- **MBE Plan Section Development (Table 10)** — The structural template for the body of the Plan. It is used when drafting the document itself: it lists each numbered section, identifies the MBE contributor or competency responsible, states the agreement that must be reached for that MBE area, and then gives detailed guidance on the data to include. All sections of the Plan are required; where a section does not apply, the team must still mark it "Not applicable" and give the rationale rather than omit it.

- **NASA life-cycle phases and KDP gates** — Drawn from the broader NASA program/project framework, these phases (Pre-Phase A Concept Studies; Phase A Concept and Technology Development; Phase B Preliminary Design and Technology Completion; Phase C Final Design and Fabrication; Phase D System Assembly, Integration and Test, Launch and Checkout; Phase E Operations and Sustainment; Phase F Closeout) and their KDPs form the time axis along which Table 9 schedules MBE-element maturity.

- **Referenced standards and directives** — The Plan's sections invoke specific external authorities when describing how data is to be handled: NASA-STD-7009 (Standard for Models and Simulations) for modeling-and-simulation data handling; SAE EIA-649-2 (NASA Configuration Management Requirements for NASA Enterprises) for configuration management; and NPD 1440.6 (NASA Records Management) together with NPR 1441.1 (NASA Records Retention Schedules) for records content. These are named as the source authorities whose relevant content the Plan summarizes rather than restates.

## Key Concepts

**The Plan as a controlled, signed commitment.** Concurrence is recorded by signature. The program manager signs, as do the Mission Directorate Associate Administrator and the providers of MBE capability such as Center Directors and the Mission Directorates; project managers of tightly coupled programs are required to sign as well. A Center Director's concurrence is not a formality — it documents that Center's commitment to supply the resources the Plan calls for. This signature structure is what turns the Plan from a description into an enforceable agreement among the parties who must deliver.

**Maturity states across the life cycle.** Table 9 tracks each MBE element through three states — Preliminary, Baseline, and Update — as the program moves through its phases. Elements such as Security Architecture, Information Support System Architecture, Data Architecture, Process Architecture, Requirements Management, Configuration Management, Risk Management, Product Data Management, Parts Management, CAD Data Management, Product Structure (Bill of Material), Models-Based Design (including models and simulations), Digital Data Standards and Contract Language, and Interoperability and Sustainability each have a planned trajectory. Some elements are marked with an asterisk, meaning they are still expected to be addressed in the Plan but may legitimately sit in an in-work or to-be-determined state with a planned resolution. By the late phases most elements have baselined and are simply being updated.

**KDP C as the data-roadmap inflection point.** The source singles out KDP C as the moment when programs and projects begin to understand the data roadmap — that is, the Data Architecture — and the interdependencies between suppliers and NASA. This frames the early phases as the window for getting the architecture right before downstream commitments harden.

**Contributor-and-agreement structure.** Every section in Table 10 names a responsible competency and the agreement to be reached, not just the content. Responsibilities are distributed across Program/Project Management, Center management and CIOs, the MBE Program/Project Manager and Delegated Technical Authorities, the MBE Process Lead, and the MBE Tool Implementation Lead. The NASA Chief Engineer supplies the program/project its MBE architecture document(s) to assure MBE needs will be met. This makes the Plan a coordination instrument: each section is also a record of who agreed to what.

**Section walkthrough.** The body moves from a Program/Project Overview (introduction, objectives, solution summary, assumptions/limitations/constraints, and responsible organizations with plan-update timing), through Requirements Traceability (a matrix showing the MBE system meets the contract Data Requirements Description, plus explicit "do-not-apply" justifications and a future-work discussion), into MBE Strategy and then the detailed Implementation sections. The implementation sections cover processes, user communities, MBE tools, process mapping, Data Architecture, Product Breakdown Structure, specialized data types, specialized libraries and part data, engineering release and configuration management and change control, data management, and information security — closing with appendices for supporting material such as concepts of operation, user scenarios, and glossaries.

**Gap analysis as a recurring decision.** Several sections direct the team to review existing Center processes, tools, and architectures and decide whether a gap analysis is needed before reusing them — for strategy, for processes, for tools, and for the product breakdown structure. The Plan treats reuse of existing Center capability as the default but forces an explicit determination of whether that capability actually meets program/project needs.

**Authoritative data and product definition data (PDD).** The Plan repeatedly centers on keeping authoritative data properly and efficiently managed, on defining the stages a product passes through (as designed, as built, as delivered, as maintained), and on controlling data exchange between design and downstream activities such as assembly. Where standard processes are not yet in place or exceptions have been made, the Plan requires the reasoning to be explained rather than left implicit.

## Mental Models

**The Plan is a treaty, not a textbook.** Its value is the recorded agreement among signatories about who delivers which capability and with what resources. The engineering content can be referenced out to stand-alone documents; what the Plan itself secures is the commitment.

**Maturity is a schedule, not a switch.** Each MBE element has a planned glide path from Preliminary to Baseline to Update across phases and KDPs. Planning MBE means deciding *when* each element firms up, accepting that some begin as to-be-determined with a named resolution date.

**Two clocks drive revision.** The Plan changes because the program advances (phasing) and because the IT changes underneath it (vendor upgrades and committed capabilities). Either clock can trigger an update; the annual-or-major-KDP cadence is the floor.

**Reuse-then-verify.** For processes, tools, and architectures the model is: start from what the Center already has, then run a deliberate check (gap analysis when warranted) to confirm it fits — never assume inherited capability is sufficient.

**Every requirement is traceable or justified.** Each Table 9 guideline is either mapped to an implementation paragraph in the Plan's Section 4, declared not-applicable with rationale, or assigned to future work. There is no silent gap; a future-work entry raises awareness but does not substitute for a later Plan update.

## Key Takeaways

- The MBE Plan documents a signed, controlled agreement on how MBE capabilities will be delivered; for single-project or tightly coupled programs (per NPR 7120.5) one program-wide Plan is produced.
- Table 9 schedules the maturity (Preliminary / Baseline / Update) of each MBE element against NASA life-cycle phases and KDP gates; asterisked items may remain in-work or to-be-determined with a planned resolution.
- Table 10 is the required section template: each section names a responsible competency, the agreement to reach, and the data to include. Non-applicable sections are marked as such with rationale, not deleted.
- Signatures — program manager, Mission Directorate Associate Administrator, Center Directors, Mission Directorates, and tightly coupled project managers — convert the Plan into a resource commitment, especially the Center Directors' pledge of resources.
- The Plan is updated annually or at a major KDP, and maintained through KDP F for data close-out and archival; KDP C is when the data roadmap and supplier/NASA interdependencies start to come into focus.
- Requirements traceability is mandatory: every Data Architecture and Process Architecture guideline is mapped, justified as not-applicable, or pushed to a tracked future-work item.
- Implementation detail draws on named authorities — NASA-STD-7009 for models and simulations, SAE EIA-649-2 for configuration management, and NPD 1440.6 / NPR 1441.1 for records.

## Connects To

- **NASA-HDBK-1009A** (companion pack): for the deeper digital-engineering and model/simulation credibility practice that this acquisition-and-planning chapter deliberately defers; the MBE Plan's modeling-and-simulation and PDD handling sections are where the two handbooks meet.
- **NPR 7120.5** (NASA program/project management): supplies the single-project and tightly coupled program definitions that decide whether one program-wide Plan is required.
- **Earlier chapters of this pack** on the NASA life cycle, KDP gates, and architectures (Security, Information Support System, Data, Process): Table 9 is essentially the MBE overlay on that same phase/KDP backbone.
- **Configuration-management and records standards** referenced in-text — SAE EIA-649-2, NPD 1440.6, NPR 1441.1 — and the modeling-and-simulation standard NASA-STD-7009, each of which the Plan summarizes rather than reproduces.
- **Requirements-traceability practice** elsewhere in the SE standards landscape: the Plan's Requirement Traceability Matrix mirrors the broader systems-engineering discipline of mapping every requirement to an implementation or an explicit justification.
