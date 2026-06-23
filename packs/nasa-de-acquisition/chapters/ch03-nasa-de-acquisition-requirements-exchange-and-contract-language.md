# Chapter — Requirements Exchange Format, Master Records Index, and Contract Language for Data Acquisition

## Core Idea
NASA-HDBK-1004 turns the abstract goal of "deliver data that NASA can actually reuse" into three concrete, contract-ready artifacts: a **Requirements Exchange Format (REF)** that standardizes the minimum attribute set for every requirement object passed between requirements-management tools; a **Master Records Index (MRI)** that captures the complete as-delivered build standard of a system and all its configuration items; and a body of **recommended contract language** that forces interoperability, machine-readable formats, defined data rights, and standards-based transmittal into the RFP/SOW *before* award rather than discovering the gap at delivery. The unifying move is to specify deliverables digitally and explicitly — formats, attributes, metadata, naming, transmittal mechanism, and rights — in place of permissive "contractor format acceptable" language. Each artifact is presented as a Data Requirements Description (DRD) that a center tailors and cites in its data procurement documents.

> **Caveat — pairs with NASA-HDBK-1009A.** This handbook supplies the *acquisition* side: the exchange schema, the records index, and the contract clauses. The deeper metadata/data-architecture vocabulary it leans on (the framework that classifies requirement types, the data-interoperability practices, the common data dictionary concept) is governed alongside NASA-HDBK-1009A. Treat the attribute lists and standards citations here as the procurement instantiation; consult 1009A for the underlying data-architecture intent.

## Frameworks Introduced (exact source names)
- **Requirements Exchange Format (REF) — DRD No. STD-REF.** The DRD that defines what a deliverable "requirement object" must contain so requirements stay integrable as they move through the full life cycle and between disparate RM systems. Used when a program needs to build one integrated requirement set from data originating in many tools/suppliers. Initial submission is due within 30 days of award; submissions recur 30 days before each contract major milestone, with interim submittals available on request up to 60 days before a scheduled delivery. OPR is NASA Systems Engineering and Integration (SE&I).
- **RIF/ReqIF (Requirements Interchange Format).** The XML file format named as the carrier for exchanging requirements plus their metadata between vendor tools. The REF format is to be RIF/ReqIF-compatible, preferably delivered via the provided XML template.
- **NASA Data Architecture Framework (NDAF).** Named as the authority defining several of the requirement-type classifications (the source marks Constraint, Functional, Interface, Performance, Operational with a footnote attributing them to NDAF).
- **Digital Collaborative Environment (DCE).** Named as the assigner of the constant `System Id` string (with input from the system owner) and as the namespace owner in the sample CMIS-style XML type definition.
- **Master Records Index (MRI) — DRD No. STD-MRI.** The DRD defining the as-delivered build standard: a keyed index of approved models, drawings, and records plus all design changes from amendments and modifications. The contractor uses it to define the product as-delivered; the government uses it to confirm the product meets its build standard. Initial submission is 90 days after build start, with quarterly updates and ad-hoc updates on contract change. It is subordinate to the CDMP, SEMP, and ISP, and inter-relates with engineering models/drawings and the Master Equipment List (MEL).
- **Contract Language for Data Acquisition and Interoperability (A.14).** A library of tailorable RFP/SOW clauses organized by the *type* of data interoperability, plus clauses for metadata, transmittal, data rights, and incremental vocabulary/dictionary/namespace definition.
- **Recommended Configuration and Data Management (CDM) SOW sections (A.15, e.g., CDM001/CDM002).** Ready-to-cite SOW clauses covering CDM planning, identification, baselines, control, status accounting, audits, and interface control — each pointing at companion DRDs (STD-CDMP, STD-CR, STD-CSA, STD-AD, STD-CDMPA).

## Key Concepts

### The REF requirement object — required vs. optional attributes
A requirement object is the agreed need expressed as a "shall" statement that is clear, correct, feasible, unambiguous, and validatable at its level; as a set, the requirements must be non-redundant, consistent in terminology, and free of conflict. The schema fixes data primitives and cardinality:
- **UUID** — a 16-octet (128-bit) identifier rendered as 36 characters in the 8-4-4-4-12 hyphenated hex form, per ISO/IEC 11578:1996.
- **Datetime** — ISO 8601 extended form with optional time-zone designator (Z for UTC or an explicit offset); unspecified zones are treated as undetermined.
- **Required attributes**: Requirement ID number (system-unique, ≤60 chars), Requirement UUID, Requirement Name, Requirement Text (the shall statement), Lifecycle Status/State, Previous Version UUID (self-reference if none), Last Modified Date, and System Id (the DCE-assigned constant source identifier).
- **Optional attributes**: Requirement Type, Rationale, Comment, Upstream UUID (multi), Downstream UUID (multi), and Verification Method.

### Lifecycle state machine
Both requirements and specifications share four legal states: **In-Work** (initial, un-reviewed), **Completed** (reviewed/approved but not yet baselined), **Accepted** (board-approved, ready to baseline), and **Obsolete** (overtaken by events, canceled, or deleted). This shared vocabulary lets status flow consistently between supplier-chain systems — the DRD explicitly defines a workflow for transmitting requirement status across that chain.

### Traceability as paired UUIDs
Traceability is carried structurally, not narratively: **Upstream UUID** points to the parent(s) a requirement was derived from, **Downstream UUID** points to its children. Because both are multi-cardinality UUID links, a receiving tool can validate the trace graph independent of any single vendor's internal identifiers. The same upstream/downstream pattern repeats at the Requirement Specification level, and the sample XML uses `FromUUID`/`ToUUID` list properties to model these relationships.

### Requirement types and verification methods (enumerated)
The type vocabulary includes Constraint, Functional, Interface, Performance, Physical, TPM (Technical Performance Measure), Verification, Operational, and Maintenance. The verification-method enumeration is the classic four: **Test, Demonstration, Inspection, Analysis** — each with a precise definition (e.g., Analysis uses models, calculations, and nondestructive results to predict typical or failure behavior). Verification Method is multi-cardinality, so a requirement can legitimately carry more than one method.

### The Requirement Specification object
A parallel object type wraps requirements into specifications, with its own UUID, name, number (≤60 chars), lifecycle state, description, and — distinctively — **Specification Effectivity**, which records *which specific hardware/software item instances* a given specification revision applies to. Optional fields mirror the requirement object's traceability (upstream/downstream/previous-version UUIDs), modification date, and System Id.

### MRI contents — the full as-built index
The MRI is a structured set of sub-indices, each sorted hierarchically (typically System → Subsystem → CI):
- **Index of CIs** — built from the Configuration Item List; lists every CI hierarchically with reference number, nomenclature, CI type (HWCI/CSCI), parent subsystem/system, and design organization.
- **Index of Components (IOC)** — the physical build structure down to piece parts, with indenture level, part number, variant number, part-number status (PROPOSED/CURRENT/OBSOLETE/HISTORICAL), quantity fitted, and drawing number.
- **Indentured Drawing List (IDL)** — every drawing (including subcontractor drawings) with indenture, number, latest revision letter, title, type, size, sheet count, and revision date.
- **Index of Configuration Documentation (IOCD)** — the functional/allocated/product-baseline documents (drawings excluded), spanning system/development/product specs, ICDs, software requirement/design/version descriptions, interface and database design descriptions, and materials/process specs.
- **Index of Technical Manuals (IOTM)**, **Index of Major (Class I) ECPs** and **Minor (Class II) ECPs**, **Index of Requests for Variance (RFVs)** (sectioned by Critical/Major/Minor), and **Index of Ancillary Equipment (IAE)** for support/test and training equipment.

The change indices capture decision provenance: ECP indices record justification codes (per MIL-HDBK-61A), CCB decisions, decision dates, impacted CIs, and old/new part numbers including re-identification relationships; the MRI ties as-built configuration to the change history that produced it.

### Contract language organized by data type
A.14 sorts deliverable obligations by *what kind of data* is being moved:
- **Proprietary formatted data** — deliver the native file, a definition of the producing application/version, a commonly readable rendering (JPEG/GIF/PNG or machine-readable PDF/A), and, where no common rendering exists, the reading application itself (source + executable) with COR concurrence.
- **Structured digital data from a source repository** — computer-readable extraction that preserves referential integrity; where XML is used, comply with W3C XML / Namespaces / Schema and OMG XMI for models, and reference a common data dictionary (NASA-defined, or contractor-defined including DB output format, DB type/version, and computer-readable schema for both XML and database output).
- **Document-formatted data** — text-searchable PDF (not scanned), Office formats, or other NASA-approved common formats (.txt, .rtf).
- **Metadata** — descriptive, structural, and administrative categories, defined in computer-readable form (CSV, XML, or approved standards-based formats such as embedded PDF/A); delivered with the file it describes; grounded in ISO 10303-233 (AP233, systems engineering) and ISO 10303-239 (AP239, product life cycle support); and defined more than 90 days before first use.
- **Transmittal** — view-in-place, direct entry into a NASA system, upload to a NASA repository, or **system-to-system** automated exchange via REST or SOAP APIs (or another documented standards-based API), with sensitive data encrypted per the NIST 800 series and FIPS PUB 140-2.

### Data interoperability and data rights
The interoperability clause set restates a make-data-visible/accessible/understandable philosophy — tag assets with discovery metadata, conform to consensus metadata standards, expose data in shared spaces except where law/policy/classification limits it, attach information-assurance metadata, and identify an authoritative source. On rights, the contract should specify delivered transaction scope, formats, metadata, and naming/interoperability standards independent of the access method; data with less than unlimited rights must be marked per FAR 52.227-14 Alternates II and III; deviations from existing standards need center approval; and PMs/Technical Authorities must acquire data with sufficient rights for the full range of needs (including external use by support contractors and future bidders), consulting the Contracting Officer and legal office to mitigate restricted-rights impacts. Common vocabulary, data dictionary, and namespace standards are to be defined **incrementally as life-cycle phase exit criteria**, reusing any existing NASA/center-level common elements.

### CDM SOW backbone
The A.15 clauses bind the data deliverables to configuration management: develop/deliver/update a CDMP (STD-CDMP); identify CIs and uniquely identify the documents disclosing their performance/functional/physical attributes; maintain functional, allocated, and product baselines; control changes via CRs and ECPs (functional-baseline changes are always Major; product-baseline changes are Major or Minor per SAE EIA-649-2); run Configuration Status Accounting (STD-CSA); conduct FCA/PCA audits (STD-AD) with NASA witnessing; and manage interfaces through an Interface Control Working Group (ICWG).

## Mental Models
- **Schema before tools.** Interoperability is achieved by agreeing on a minimum attribute set and primitive types (UUID, datetime, cardinality), not by mandating a single RM tool. If two systems agree on the REF schema, the vendor lock-in problem dissolves — RIF/ReqIF is just the wire format that carries that agreed schema.
- **Identity is the keystone.** Every object owns a UUID, and every relationship (version history, derivation, source system) is expressed as a UUID link. Where there is "no previous version," the object points the Previous Version UUID at itself — the graph is never allowed to have a dangling identity reference.
- **The MRI is the system's "as-built" twin on paper.** The functional/allocated/product baselines say what the system *should* be; the MRI is the indexed record of what was actually delivered, traced back through every ECP and RFV that changed it. If you cannot reconstruct the build standard from the MRI, the configuration record has failed.
- **Specify the deliverable, not the convenience.** The strongest lever in the whole handbook is replacing "contractor format acceptable" with explicit digital format, metadata, naming, and rights requirements. Permissiveness at RFP time becomes a non-reusable data dump at delivery time.
- **Rights are a design parameter, not a legal afterthought.** Acquire only the minimum essential contractor-originated data, but acquire it with enough rights for the *full* life cycle — including downstream competition. Under-scoping rights quietly forecloses future procurement options.
- **Interoperability is earned at phase boundaries.** Common vocabulary, data dictionary, and namespace are defined incrementally as exit criteria, so each life-cycle phase hands the next a usable semantic foundation rather than deferring integration to the end.

## Anti-patterns (named or directly implied by the source)
- **"Contractor format acceptable" language.** The handbook explicitly directs PMs and Technical Authorities to specify delivered data in defined digital formats *in lieu of* "Contractor format acceptable" or similar wording — naming this permissive phrasing as the thing to eliminate.
- **Acquiring more data than the life cycle needs.** The guidance is to acquire the *minimum essential* contractor-originated data required to meet life-cycle requirements; over-acquisition is implicitly the failure mode.
- **Unmarked restricted-rights data.** Delivering data with less than unlimited rights without the FAR 52.227-14 Alternates II/III legend is called out as a marking obligation, i.e., its omission is the defect.
- **Late metadata.** Metadata used in a phase is to be defined more than 90 days before first use; defining it at or after the point of use is the implied anti-pattern.

## Key Takeaways
1. **REF (STD-REF)** standardizes a minimum requirement-object attribute set — UUID, name, shall-text, lifecycle state, version/source identity, and optional traceability — carried as RIF/ReqIF-compatible XML, so requirements stay integrable across vendor RM tools.
2. **Lifecycle state** (In-Work → Completed → Accepted → Obsolete) and **paired upstream/downstream UUIDs** make status and traceability tool-independent and machine-validatable across the supplier chain.
3. The REF type vocabulary (several classifications attributed to **NDAF**) and the four verification methods (Test/Demonstration/Inspection/Analysis) are enumerated, with Verification Method allowed to be multi-valued.
4. **MRI (STD-MRI)** is the indexed as-delivered build standard — CIs, components to piece-part level, drawings, configuration documentation, technical manuals, Class I/II ECPs, RFVs, and ancillary equipment — subordinate to the CDMP/SEMP/ISP.
5. **A.14 contract language** sorts obligations by data type (proprietary / structured / document / metadata) and mandates standards-based, machine-readable delivery plus defined transmittal (view-in-place, direct entry, upload, or REST/SOAP system-to-system with NIST/FIPS encryption).
6. **Replace permissive format language**, acquire the **minimum essential** data with **sufficient rights** (FAR 52.227-14 marking for less-than-unlimited rights), and define common vocabulary/dictionary/namespace **incrementally as phase exit criteria**.
7. **A.15 CDM SOW clauses** bind these deliverables to baseline discipline, change control (Major/Minor per SAE EIA-649-2), status accounting, FCA/PCA audits, and ICWG-managed interfaces.

## Connects To
- **NASA-HDBK-1009A** (pairing caveat): the data-architecture/metadata intent and requirement-type framework that this acquisition-side handbook instantiates — read together for the underlying vocabulary.
- **SAE EIA-649 / EIA-649-2 (Configuration Management Requirements for NASA Enterprises)** and **GEIA-859 (Data Management)**: the CM/DM standards the MRI and CDM SOW clauses are required to be consistent with.
- **ISO 10303 AP233 / AP239, ISO/IEC 11578, ISO 8601, W3C XML/Namespaces/Schema, OMG XMI**: the external standards underpinning the REF primitives, metadata foundation, and structured-data exchange.
- **FAR 52.227-14 (Rights in Data — General), NIST 800 series, FIPS PUB 140-2**: the data-rights and transmittal-security obligations carried in the contract language.
- **MIL-HDBK-61A** and **SAE GEIA-HB-649**: referenced for ECP justification codes and FCA/PCA audit criteria respectively.
- **Companion DRDs (STD-CDMP, STD-CR, STD-CSA, STD-AD, STD-CDMPA)**: the change, status-accounting, and audit DRDs cited by the CDM SOW clauses that complete the data-acquisition framework.
