# Chapter 12: eSTAR Submissions

Sources: S11 Electronic Submission Template for Medical Device 510(k) Submissions (2023-10-02), §§ I–VI (eSTAR structure, technical screening, waivers/exemptions, mandatory date 2023-10-01); S12 Electronic Submission Template for Medical Device De Novo Requests (2024-08-23), §§ I–VI (De Novo eSTAR structure, technical screening, waivers/exemptions, mandatory date 2025-10-01).

## Core Idea

eSTAR (electronic Submission Template And Resource) is FDA's guided PDF template for building complete 510(k) and De Novo electronic submissions. It replaces free-form assemblage with a fixed section map, embedded logic, prompts for attachments, links to related guidances, and a status flag that reads "eSTAR Complete" only when required sections are done. Section 745A(b) of the FD&C Act authorizes FDA to require electronic format by guidance; S11 and S12 are the device-specific guidances that set the template structure and the dates. For authors, the job changes from "write a narrative 510(k)" to "answer the template, put software and cybersecurity evidence in their designated sections, and clear technical screening before substantive review starts."

## Frameworks Introduced

- **Electronic submission template model**: a guided preparation tool that walks the submitter through required contents, collects structured answers, and accepts unstructured attachments (documents, PDFs, images, videos) under the relevant bookmarks.
- **eSTAR as the sole current template**: for both 510(k) and De Novo, eSTAR is the only electronic submission template FDA currently offers to produce a valid electronic submission package (eSubmission).
- **Technical screening before review**: after user-fee payment, FDA runs virus scan and technical screening to check that eSTAR responses are consistent and complete enough to describe the device. An incomplete eSTAR does not proceed; a replacement is expected within the hold window described in the guidances (S12 states 180 days for De Novo holds of this kind).
- **Mandatory electronic dates**: 510(k) electronic submission requirements take effect 2023-10-01; De Novo electronic submission requirements take effect 2025-10-01. After the applicable date, non-electronic originals (unless exempt) are not received.
- **Section maps (Table 1 in each guidance)**: parallel high-level structures for 510(k) and De Novo, with pathway-specific blocks (predicates and substantial equivalence for 510(k); benefits, risks, mitigation measures and proposed classification for De Novo).

## Key Concepts

- **Legal hook.** Section 745A(b), as amended, directs further standards, a timetable, and waiver/exemption criteria for medical device electronic submissions. The "745A(b) device parent guidance" sets the program pattern; S11 and S12 are the 510(k) and De Novo instantiations.
- **What eSTAR is.** A collection of questions, text, logic, and prompts inside a template that constructs a complete request. It is highly automated relative to older free-form or eSubmitter pilots, surfaces relevant regulation and guidance links, and structures content so reviewers see a consistent skeleton.
- **What eSTAR is not.** The guidances establish structure, format, use, timing, and waiver/exemption rules. They do not freeze every pixel of the user interface forever; FDA intends to ship new eSTAR versions as policy changes.
- **510(k) scope of the electronic requirement.** After 2023-10-01, original Traditional, Special, and Abbreviated 510(k)s, plus subsequent supplements and amendments (unless exempt), must arrive as electronic submissions built as described in S11. A non-electronic 510(k) is not received unless an exemption or waiver applies.
- **De Novo scope of the electronic requirement.** After 2025-10-01, De Novo originals plus subsequent supplements and amendments (unless exempt) must arrive as electronic submissions under S12. Until that date, voluntary eSTAR De Novo use is allowed; S12 notes eSTAR has been available for De Novo content since the January 2022 expansion.
- **Exemptions (both pathways, same pattern).** Interactive review responses; certain amendments (appeals/supervisory review requests, substantive summary requests, change-in-correspondent amendments, add-to-files after final decision); and withdrawal requests. Interactive replies can stay on email when the reviewer used phone or email; other additional-information responses belong in eSTAR under the Amendment/AI response category, with the actual updated artifacts placed in their home sections (for example revised labeling in Labeling).
- **Waivers.** Neither guidance identifies circumstances for a waiver; FDA does not intend to grant 510(k) or De Novo eSTAR waiver requests given widespread availability of the PDF tools.
- **Transmission.** Completed eSTARs go through FDA's electronic portal for CDRH, or the Electronic Submission Gateway for CBER, per the program instructions cited in the guidances. Known technical portal limits may still force mail for some packages; the guidances flag that operational detail without undoing the electronic-content requirement.
- **Table 1 structure shared across 510(k) and De Novo (author-facing map).**
  - Submission Type
  - Cover Letter / Letters of Reference
  - Applicant Information
  - Pre-Submission Correspondence and Previous Regulator Interaction
  - Consensus Standards
  - Device Description
  - Proposed Indications for Use
  - Classification
  - Labeling
  - Reprocessing, Sterility, Shelf Life, Biocompatibility (as applicable)
  - Software/Firmware
  - Cybersecurity/Interoperability
  - EMC, Electrical, Mechanical, Wireless, and Thermal Safety
  - Performance Testing
  - References
  - Administrative Documentation
  - Amendment/Additional Information (AI) response
- **510(k)-specific blocks.** Predicates and Substantial Equivalence (predicate identity, comparison, why differences do not defeat SE; reference device if used). Design/Special Controls, Risks to Health, and Mitigation Measures appear for Special 510(k) submissions (change identification, risk analysis methods and results, risk control measures). Administrative forms include the Truthful and Accuracy Statement and a 510(k) Summary or 510(k) Statement.
- **De Novo-specific blocks.** Benefits, Risks, and Mitigation Measures (probable risks, proposed general and special controls, benefit-risk discussion with valid scientific evidence). Classification content includes proposed Class I or II, classification summary information, and related 21 CFR 860.220 elements. Device Description also expects alternative practices or procedures (or a statement that none are known) and any Request for Designation number.
- **Software/Firmware section.** Both templates call for applicable software documentation when the device includes software, pointing authors at the device software functions documentation guidance (S1 in this pack). That is the designated home for the Basic/Enhanced software package from ch02, not a free-floating appendix.
- **Cybersecurity/Interoperability section.** Both templates call for applicable cybersecurity assessment information and point at the cybersecurity premarket guidance and the interoperable devices guidance. That is the designated home for the artifacts owned by ch07 and ch09.
- **Prompts and attachments.** Answering "yes" to clinical testing (and similar gates) triggers prompts for the matching attachments and financial disclosure artifacts. Attachments sit under the relevant bookmark for both submitter and FDA viewers.
- **Completeness signal.** After required sections are correctly completed, the PDF status message shows "eSTAR Complete." That status is the author's local gate before paying the fee and transmitting.
- **Review mechanics after pass.** Once technical screening passes and the submission is accepted, FDA review proceeds on the structured content. The older Refuse-to-Accept manual checklist work is largely automated inside eSTAR, with technical screening carrying the early quality gate.

## Mental Models

- **Template is the outline of record.** If content has no section, it is in the wrong place. Software evidence goes to Software/Firmware; cyber evidence goes to Cybersecurity/Interoperability; performance studies go to Performance Testing.
- **Logic before literature dump.** eSTAR asks questions and unlocks prompts. Authors should answer truthfully so the attachment requests match the actual testing story.
- **Complete beats clever.** A polished narrative PDF that is not an eSTAR does not get received after the mandatory date. An eSTAR that is not "Complete" stalls in technical screening.
- **AI responses are surgical.** Put the cover response in the AI section, and put each updated artifact back in its native section so the review copy stays coherent.
- **Dates are hard.** 2023-10-01 (510(k)) and 2025-10-01 (De Novo) are requirement-effective dates, not soft goals.

## Anti-patterns

- **Building a legacy paper-style 510(k) and hoping eCopy alone satisfies 745A(b).** After the mandatory date, the submission must be an electronic submission as defined through eSTAR.
- **Parking all software and cyber PDFs under Administrative Documentation or a single catch-all attachment.** Use the dedicated sections so technical screening and reviewers land on the right bookmarks.
- **Treating "eSTAR Complete" as optional polish.** It is the completeness signal the process expects before filing.
- **Updating labeling only inside an AI cover letter.** S11/S12 both say put the actual revised artifacts in their sections.
- **Assuming a waiver will cover tool or process unreadiness.** Both guidances state FDA does not intend to grant waivers for these templates.
- **Ignoring Special 510(k) or De Novo-only blocks.** Special 510(k) risk-analysis content and De Novo benefit-risk/special-controls content are first-class sections, not footnotes.

## Key Takeaways

1. eSTAR is the only current FDA electronic submission template for 510(k) and De Novo device submissions.
2. 510(k) electronic submissions are required as of 2023-10-01; De Novo electronic submissions as of 2025-10-01.
3. Authors work inside fixed sections with logic-driven prompts; software and cybersecurity have named homes.
4. Technical screening follows fee payment; incomplete eSTARs do not enter normal review until replaced.
5. Narrow exemptions exist (interactive review replies and listed amendment/withdrawal types); waivers are not offered as a planning assumption.
6. 510(k) templates add predicate/SE (and Special 510(k) change/risk blocks); De Novo templates add classification, benefits/risks/mitigations, and related 860.220 content.
7. "eSTAR Complete" is the local readiness flag before transmit.
8. Put AI-driven content updates in the sections they change, not only in the AI response bucket.

## Connects To

- **ch01**: which pathway (510(k) vs De Novo vs other) the eSTAR file is serving.
- **ch02**: software documentation package that lands in the Software/Firmware section.
- **ch07 / ch09**: cybersecurity and interoperability artifacts that land in the Cybersecurity/Interoperability section.
- **ch10**: when a software change forces a new 510(k) that must then be authored in eSTAR.
