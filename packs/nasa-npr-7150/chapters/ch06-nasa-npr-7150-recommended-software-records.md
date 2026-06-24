# Chapter — Recommended Software Records Content

> Source caveat: This chapter synthesizes a slice of NPR 7150.2D, a NASA Procedural Requirement published through the NASA Online Directives Information System (NODIS) and rendered for this pack from the NODIS HTML. NPR 7150.2D states the software-engineering requirements that complement the broader software-for-systems area; it places no obligation on members of the public other than where law allows or where its terms have been written into a contract, and printed copies are uncontrolled — the NODIS Library is the authoritative version of record.

## Core Idea

This slice draws a deliberate line between *which* software records a project is expected to produce and *what those records should contain*. NPR 7150.2D lists the typical engineering products a software life cycle may generate, but it does not embed the content definitions inside the requirement itself. Instead it points to a companion handbook for the substance of each record. The governing principle stated up front is that record content decisions should begin with the people who will use the information: before drafting any plan, procedure, report, or specification, a project should understand the requirements, needs, and background of the users and stakeholders who will rely on it. Records exist to serve readers, not to satisfy a checklist.

## Frameworks Introduced (exact source names, when/how)

- **NASA-HDBK-2203 (the Software Engineering handbook)** — named as the authority where the recommendations for the content of software records are defined. The slice invokes it twice: once when introducing the product list (content recommendations live in NASA-HDBK-2203) and again in the product-content section, where it adds that the handbook also gives guidance on *when* each record should be drafted, baselined, and updated. So the requirement supplies the list of products; the handbook supplies the content and the timing.
- **Software Process Across NASA (SPAN) Web site** — named as the location for examples and templates of these records and datasets. The slice gives its access point as the NEN software wiki URL, positioning SPAN as the practical companion to the handbook's content guidance.
- **NODIS (NASA Online Directives Information System) Library** — referenced through the page-footer caveat as the verification source for the correct version of the document before use, reachable at the nodis3.gsfc.nasa.gov address.

## Key Concepts

- **Products versus content.** The slice separates the enumeration of software engineering products (section 6.1) from the content of those products (section 6.2). The requirement enumerates; the handbook defines content.
- **The typical product set.** The list of typical software engineering products or electronic data spans planning, configuration, testing, design, and operational artifacts. It includes the Software Development Plan / Software Management Plan; Software Schedule; Software Cost Estimate; Software Configuration Management Plan; Software Change Reports; Software Test Plans, Procedures, and Reports; Software Version Description Reports; Software Maintenance Plan; Software Assurance Plan(s); Software Safety Plan; Software Requirements Specification; Software Data Dictionary; the Software and Interface Design Description (architectural design) and the Software Design Description; the Software User's Manual; records of Continuous Risk Management for software; and Software Measurement Analysis Results. The list continues with the record of software engineering trade-off criteria and assessments (the make/buy decision); Software Acceptance Criteria and Conditions; Software Status Reports; the Programmer's / Developer's Manual; the Software Reuse Report; and software model and simulation data and documentation, which is paired with a Verification, Validation, and Credibility Plan for software models and simulations.
- **Tailoring is expected.** Specific content within these records may not apply to every project. The list is a menu of typical artifacts, not a mandate that every project produce all of them with all content.
- **Format flexibility.** NASA Center and contractor document formats are acceptable for deliverables, provided the content the project requires is actually addressed. The requirement cares about content coverage, not about conformance to a single house template.
- **Records are living.** Product records should be reviewed and updated as the work proceeds, rather than written once and shelved.
- **Timing belongs to the handbook.** The drafting, baselining, and updating cadence for each record is guided by NASA-HDBK-2203, not fixed in this requirement slice.
- **Version control of the requirement itself.** The recurring footer caveat reminds readers that a printed copy is uncontrolled and that the NODIS Library holds the verified current version.

## Mental Models

- **Menu, not mandate.** Treat the product list as a catalog of typical artifacts to select from and tailor, choosing what a given project actually needs rather than generating the full set by reflex.
- **Pointer architecture.** Picture the requirement as a thin index that points outward: 7150.2D names *what*, NASA-HDBK-2203 supplies *content* and *timing*, and SPAN supplies *examples and templates*. The records live where the guidance is richest, not all in one document.
- **Reader-first authoring.** Before writing a record, picture its downstream users and stakeholders and write to their needs and background; content is justified by who consumes it.
- **Content over container.** A Center or contractor format is just a container; what matters is whether the required content sits inside it.

## Key Takeaways

- The requirement enumerates a broad set of typical software engineering products but defers their content definitions to NASA-HDBK-2203.
- Begin record decisions with the users and stakeholders — their needs and background determine what content belongs in a record.
- Tailor the list: not every record, and not every element within a record, applies to every project.
- Center and contractor formats are acceptable as long as the project's required content is addressed.
- Records are reviewed and updated as living artifacts, with drafting / baselining / updating timing guided by the handbook.
- Use SPAN for examples and templates, and verify the requirement's current version through the NODIS Library before relying on a printed copy.

## Connects To

- **NASA-HDBK-2203 (Software Engineering handbook)** — the content-and-timing companion this chapter repeatedly defers to; the natural next read for the substance of any listed record.
- **SPAN (Software Process Across NASA)** — the template-and-example library that operationalizes the handbook's content guidance.
- **Configuration management and version control** — the Software Configuration Management Plan, Software Change Reports, and Software Version Description Reports in the product list, plus the "review and update" expectation, tie directly to a records-under-control discipline.
- **Verification and validation** — the Software Test Plans / Procedures / Reports and the Verification, Validation, and Credibility Plan for models and simulations connect this records chapter to the V&V activities of the wider software-for-systems area.
- **Risk and trade studies** — Continuous Risk Management records and the make/buy trade-off criteria record link record-keeping to the project's risk and engineering-decision processes.
