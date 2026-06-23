# NASA-HDBK-1004 Patterns & Techniques

Reusable patterns drawn from NASA-HDBK-1004 (the Digital Engineering Acquisition Framework Handbook). Each has When / How / Trade-offs. Ground every application in the source slice and tailor to the program/project.

## Pattern 1: Buy the Data While the Bidders Still Compete

**When to use**: during RFP/RFQ development, before award — the only window where competitive leverage exists.

**How**: write achievable data requirements into the front end and put the same data approach in three places — the SOW (functional/technical requirements, typically Section C), the DRD (a template demanding the details, submitted with the proposal), and the Cost Volume (data as a separate priced line item). Force offerors to assert all restrictions on deliverable technical data and software up front, then evaluate and negotiate special licenses only where standard categories fail.

**Trade-offs**: front-loading data requirements adds drafting effort and proposal scope at a busy moment — but every requirement deferred to closeout becomes a sole-source negotiation with no competitive lever left, and historically cost millions to recover.

---

## Pattern 2: Treat Each DRD as a Data Contract with an Interface Spec Attached

**When to use**: whenever a deliverable data item must drop into the receiver's tools without rework.

**How**: in each DRD nail down the schema (Contents), the encoding (Format plus named neutral standards), the SLA (submission timing and maintenance), and the access policy (Data Type 1–5 and distribution). Express submission as milestones ("30 days after contract award"), never calendar dates, so the schedule survives slips. Assemble the DRDs into a DPD that rides alongside the SOW/PWS and is invoked by SOW/PWS language. Acceptance criterion: the item integrates after verification alone.

**Trade-offs**: precise DRDs take more effort than "contractor format acceptable," and over-specified contents add review burden — but permissive language at RFP time produces a non-reusable data dump at delivery time.

---

## Pattern 3: Set the Data Type as a Control-and-Trust Dial

**When to use**: when deciding how much Government oversight each deliverable needs.

**How**: turn the dial up to Type 1 when data will enter the Center baseline under CDM control and demands written approval before use; leave it mid-range (Type 2 with its tailorable 45-day disapproval window, or Type 3 deliver-on-time) for review or routine items; turn it down to Types 4/5 for contractor-retained data NASA can pull or inspect — adding FAR 48 CFR §52.227-16 when delivery must be compellable. Pick the lowest level that still protects the baseline.

**Trade-offs**: Type 1 on everything maximizes control but slows the contractor and floods the approval queue; under-controlling baseline-bound data risks unapproved configurations entering sustainment.

---

## Pattern 4: Mature the TDP with the Life Cycle

**When to use**: when scheduling technical-data-package deliveries against NPR 7120.5 reviews.

**How**: deliver the TDP as a sharpening photograph of the design — a Conceptual level around SRR/SDR (feasibility sketches and low-fidelity CAD), a Developmental level before PDR (a documented design approach, explicitly not adequate for competitive parts procurement), and a Product level before CDR (full documentation enabling competitive procurement), with a Commercial level for proprietary/off-the-shelf items. Ground the structure and levels in MIL-STD-31000, and ingest the TDP into the Government environment to seed the as-sustained Product Baseline.

**Trade-offs**: maturing levels mean repeated submissions and review cycles rather than one drop — but a single end-of-program dump cannot support the early decisions or seed a controlled baseline.

---

## Pattern 5: Standardize Identity and Traceability with Paired UUIDs (REF)

**When to use**: when one integrated requirement set must be built from data originating in many vendor RM tools.

**How**: adopt the REF minimum attribute set — give every requirement object a UUID, a system-unique ID, shall-text, a lifecycle state (In-Work → Completed → Accepted → Obsolete), and version/source identity, with Previous Version UUID self-referencing when there is no prior version so the identity graph never dangles. Carry traceability structurally as multi-cardinality Upstream/Downstream UUID links, and exchange via RIF/ReqIF-compatible XML. Agree the schema, not the tool.

**Trade-offs**: enforcing a UUID schema and shared lifecycle states constrains every supplier's tooling — but it dissolves vendor lock-in, because any receiving tool can validate the trace graph independent of internal identifiers.

---

## Pattern 6: Reconstruct the Build Standard from the MRI

**When to use**: when the Government must confirm a delivered product meets its build standard and trace every change that produced it.

**How**: require the MRI as the indexed as-delivered record — CIs, components down to piece-part level, drawings, configuration documentation, technical manuals, Class I/II ECPs (with justification codes, CCB decisions, dates, and old/new part numbers), RFVs, and ancillary equipment — subordinate to the CDMP, SEMP, and ISP. Test: if you cannot rebuild the as-delivered build standard from the MRI, the configuration record has failed.

**Trade-offs**: a complete MRI is heavy to produce and maintain at quarterly cadence — but without it, as-built configuration is untraceable to the changes that created it, and sustainment loses its provenance.

---

## Pattern 7: Mandate Neutral Formats and Standards-Based Transmittal

**When to use**: whenever delivered data must be reused or exchanged across organizations using different tools.

**How**: replace "contractor format acceptable" with named electronic formats — sort obligations by data type (proprietary: native file plus a common rendering; structured: schema, DB type/version, W3C XML or OMG XMI; document: text-searchable PDF/A; metadata: machine-readable, standards-based, defined more than 90 days before first use, grounded in ISO 10303-233/-239). Define data formats independently of the access method, and select transmittal — view-in-place, direct entry, repository upload, or REST/SOAP system-to-system with NIST 800-series / FIPS 140-2 encryption for sensitive data.

**Trade-offs**: neutral formats can lag a vendor's newest native features and add conversion steps — but proprietary formats lock the Government into one toolchain and force costly extraction later.

---

## Pattern 8: Acquire the Minimum Essential Data with Sufficient Rights

**When to use**: when specifying license rights for technical data (TD) and computer software (CS).

**How**: use Table 3 to match each TD/CS deliverable to a license category (Unlimited, Government Purpose, Limited (TD), Restricted (CS), Specifically Negotiated, SBIR, Commercial) by who funded development and whether the item is commercial. Pick the lowest category that still meets the mission, never accepting less than Limited Rights in noncommercial TD or Restricted Rights in noncommercial CS. Mark less-than-unlimited-rights data with the FAR 52.227-14 Alternates II/III legend. Use priced options and the deferred delivery/ordering clauses (DFARS 252.227-7026/-7027) plus a Data Accession List to postpone delivery while locking the option at award. Acquire enough rights for the full life cycle, including downstream re-bid and support contractors.

**Trade-offs**: acquiring broad rights costs more up front and can deter offerors with proprietary IP — but under-scoping rights quietly forecloses future competition and sustainment options.

---

## Pattern 9: Make Models Authoritative and Map Release States

**When to use**: when multiple parties exchange model-based data using different release vocabularies.

**How**: treat each deliverable as {object + metadata + state + effectivity + authorized usage}, not a static file, since the same CAD model can be released for manufacturing or for outer-mold-line work depending on intended use. Rather than forcing one vocabulary, map each supplier source state to a program-defined destination state (Notional State Compatibility Map) using the MBE Plan, the SOW/PWS, and standards like MIL-STD-31000. Keep authority in the electronic model; treat documents as generated views, and when the two disagree, the model wins.

**Trade-offs**: building and maintaining a state-translation table is ongoing coordination work — but mandating one uniform release vocabulary across primes and Centers is usually infeasible and breaks at the first supplier boundary.

---

## Pattern 10: Run the Four Use Cases Before Fixing Interoperability Requirements

**When to use**: during acquisition planning, before selecting tools, formats, and access levels.

**How**: reason through the four MBE use cases as a ladder of increasing demand — Viewing (show geometry, maybe metadata/PMI), Data Exchange (round-trip exact geometry and post-exchange PMI processing), Data Integrity (correctness against an authoritative source and model), and Data Interoperability Formats (standards-governed bi-directional cross-organization exchange) — correlated with Table 6. Let the heaviest case you genuinely need set the format bar (judged against the Table 8 maturity levels, where higher is fitness not prestige), and attack the manual-copy problem with automated data integration and daily/weekly automated data audits.

**Trade-offs**: the heaviest use case demands the most capable (and costly) formats and tools — but specifying to a use case lighter than you actually need forces rework when the real demand surfaces downstream.

---

## Pattern 11: Make the MBE Plan a Signed Treaty with a Maturity Schedule

**When to use**: when standing up a program's MBE capabilities and committing Center resources.

**How**: produce one program-wide MBE Plan (for single-project or tightly coupled programs per NPR 7120.5) as a living, formally controlled artifact. Use Table 9 to schedule each MBE element (architectures, requirements/configuration/risk management, product data, parts, CAD, product structure, design, standards/contract language, interoperability) through Preliminary → Baseline → Update across phases and KDPs. Use Table 10 as the required section template — each section names a responsible competency, the agreement to reach, and the data to include; mark non-applicable sections with rationale rather than deleting them. Capture every requirement as mapped, justified not-applicable, or tracked future-work. Record concurrence by signature (PM, Mission Directorate AA, Center Directors, tightly coupled project managers); refresh at least annually or at a major KDP, through KDP F.

**Trade-offs**: the signature structure and full-section discipline make the Plan slow to assemble and revise — but signatures convert description into an enforceable resource commitment, and the maturity schedule prevents elements from firming up too late to influence downstream commitments.
