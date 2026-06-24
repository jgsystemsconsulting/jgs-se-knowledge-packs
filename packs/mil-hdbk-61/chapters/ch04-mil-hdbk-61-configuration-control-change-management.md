# Chapter — Configuration Control & Change Management

> Source: MIL-HDBK-61B, Section 6 (Configuration Control). This chapter reflects the current 61B revision, not the superseded 2001 MIL-HDBK-61A(SE).

## Core Idea

Configuration control is the most outwardly visible piece of configuration management: it is the disciplined process by which both the supplier (typically a contractor) and the acquirer (typically the Government) prepare, justify, evaluate, coordinate, disposition, and implement proposed engineering changes and variances against configuration items (CIs) and the baselined documentation that defines them. Its central purpose is to install a systematic change-management process that keeps life-cycle costs in check while still allowing enough design and development freedom, and while guaranteeing that every alteration to a Government-controlled baseline — however trivial it may appear — is reviewed by the proper approval authority before it takes effect.

The handbook frames this as an *integrated* change process: change preparation, justification, evaluation, coordination, disposition, and implementation are shared responsibilities split between acquirer and supplier, with the downstream impacts of approved changes and variances explicitly identified and accounted for during implementation. Control is not a one-time gate; it is a discipline that runs across the entire program life cycle, tightening as the program matures.

## Frameworks Introduced (exact source names, when/how)

- **Configuration Control Board (CCB)** — Established for every acquisition program as the chartered command or agency body that acts on Class I ECPs and on requests for major or critical variances. The Program Manager (PM) owns disposition of changes at the CCB and may delegate that authority; when a decision is reached, the CCB chairperson issues a CCB directive (or an equivalent letter/memorandum) that directs the implementing actions. Contractors run a parallel internal board for their own control.
- **Engineering Change Proposal (ECP)** — The formal vehicle for a requested change. ECPs submitted to the Government are typed as Class I or Class II. The handbook points to the DD Form 1692 instruction sheet and GEIA-HB-649 for the detailed classification criteria.
- **Request for Variance (RFV)** — The mechanism for delivering or installing an item that does not (or will not) conform to baselined documentation. The handbook notes that an RFV requested during or after manufacture was previously termed a deviation or waiver, and that an RFV follows the same processing rules those older terms used. Classification criteria live in the DD Form 1694 instruction sheet and GEIA-HB-649.
- **Notice of Revision (NOR)** — An ancillary document to the ECP that conveys the specific edits to a specific affected document. It is required when the precise document changes must be spelled out; for documents the ECP originator controls, the NOR is optional, since the originator may instead describe each document's change inside the ECP body. NORs are prepared and submitted per the contract SOW and the CDRL / DD Form 1423.
- **Current Document Change Authority (CDCA)** — The single organization (Government or contractor) holding decision authority over a document's contents, reflecting proprietary or data rights. There is exactly one CDCA per document at a time, though that role can transfer.
- **Application Activity (AA)** — A configuration control authority whose reach is limited to *using* a product and its documentation rather than changing it; multiple AAs can exist when a product has more than one user. An AA cannot authorize a change but may participate in the change process when invited by the CDCA or the Government lead AA.
- **Baselines (FBL / ABL)** — Government configuration control always covers the Functional Baseline (FBL) and the Allocated Baselines (ABLs) for lower-level CIs whose specifications the Government issued or approved. The span of Government control begins once the first configuration document is approved and baselined, which normally happens when the functional configuration baseline is set.

## Key Concepts

**Span of configuration control.** Government control starts at the moment the first configuration document is baselined — typically the establishment of the functional baseline. From that point on, complementary Government and contractor procedures evaluate each proposed change or requested variance, assess the total impact (cost included) through coordination with affected functional activities, disposition it with a timely approve/disapprove decision, and assure prompt implementation by both parties.

**Why changes arise.** The handbook lists representative drivers: countering a new threat, inserting new technology, responding to technical and operational test and evaluation results, and correcting problems. The responsible Government activity confirms the need, sets performance/cost/schedule thresholds, judges whether the change is technically achievable and affordable, and prepares the change-action request — which, depending on life-cycle phase, the contractor or the Government may author.

**Who approves what.** The Government decides when the change touches a requirement of a Government-controlled baselined document, *or* when a change to a contractor-controlled document affects specified performance, supportability, or other contractually specified requirements tied to a Government-controlled CI. The contractor decides when the change is to items/documentation for which it is the approval authority and the change does not touch the Government's baselines. The contractual configuration approval authority governs the full set of baselined documents for a product under a specific contract; if it is not the CDCA for a particular document needing change, it cannot approve that change and must either solicit ECP approval from the applicable CDCA or pick an alternate design.

**Approval-authority residence and responsibility.** The contractual approval authority for implementing a product change may start with the contractor or the Government, may transfer from contractor to Government, or may stay with the contractor for the CI's whole life. Whoever holds it is both technically responsible for product performance and fiscally responsible for funding the changes.

**Change classification (ECPs).** A Class I ECP goes to the Government CCB for approval and is authorized through a contract modification. A Class II change, unless the contract says otherwise, is typically reviewed by the local Government representative for concurrence in its classification.

**RFV mechanics.** RFVs most commonly attach to production CIs under a production contract — items that do not or will not match the Government-baselined documentation. A contractor submits one when some legitimate constraint — long lead time is the example given — means a few units will ship without a Government-required performance attribute having been achieved or confirmed, or when parts have to go out in an off-baseline configuration ahead of final assembly of the first affected serial-numbered unit. RFVs are classified by their originators as minor, major, or critical, unless the contract assigns that call to a Government technical representative.

**RFV approval and consideration.** RFVs are usually processed to benefit the contractor, since the Government actually wants the configuration it contracted for. Per FAR 46.407, the Government should accept non-conforming material only when doing so serves its best interests and there is appropriate consideration; if approved, the contracting officer must negotiate equitable consideration sized to the quantity of affected CIs and/or the degree of non-conformance. The CCB review feeds an estimate of that consideration to the contracting office. Minor RFVs are normally approved by the Government CO or designated representative — but FAR 7.503 makes approval of *all* RFVs (minor, major, critical) an inherently Governmental function that may not be delegated to support or defense contractors. Items tendered with an approved RFV must still be suitable for intended use without later repair or restoration at Government expense.

## Mental Models

- **Control tightens as the program matures.** The process evolves from informal early on to highly disciplined and formal later. In the TMRR phase, definition documents are still being shaped, so control is lighter — several informal requirements baselines may be set just to keep all participants synchronized, with an informal change procedure helping review changes to the evolving system-level specs. By EMD, Production and Deployment, and Operation and Support, a formal process is essential and the earlier informal document control becomes insufficient.
- **Macro view is simple; micro view is not.** At a top level, configuration control just guards the documentation defining performance, physical, and functional characteristics. Drill into the actual flow and it becomes considerably more complex — the simplicity is only at altitude.
- **One CDCA per document, always.** Authority over a document's contents is singular and unambiguous. AAs orbit that authority — they consume and may comment, but they never authorize the change.
- **An ECP carries the change; the NOR pins down the words; the variance buys an exception.** The ECP is the change itself, the NOR is the precise documentary edit, and the RFV is a bounded permission to ship something off-baseline.
- **Talk before you file.** One of the largest contributors to control efficiency and effectiveness is clear, concise communication among the Government, the CDCA, and the contractor *before* the formal ECP request — ideally inside an IPT environment.

## Anti-patterns

- **Change proliferation.** A stated control objective is to eliminate unnecessary change proliferation; uncontrolled change volume is treated as a defect the process exists to suppress.
- **Recurring RFVs masking a real problem.** The Government should ensure approved RFVs are rarely recurring. Repeated RFVs against the same item characteristic or issue should raise concern that either the contractor needs corrective manufacturing action or the CI's technical requirements are too stringent — in the latter case the Government should request a Class I (major) ECP to revise the CI's documentation. A variance is an exception, not a substitute for fixing the underlying cause or the requirement.
- **Operating without an effective control process.** Without one, the program office risks delivering CIs that are technically inadequate and fail performance requirements, are not logistically supportable, may be unsafe, waste resources, and leave no accurate historical record to base future changes on.

## Key Takeaways

- Configuration control is the visible heart of CM: a shared acquirer/supplier process for preparing, justifying, evaluating, coordinating, dispositioning, and implementing changes and variances against CIs and their baselines.
- The objective is a systematic change process that regulates life-cycle cost while preserving design latitude and ensuring complete, accurate, timely documentation under the proper approval authority.
- Government control begins when the first document is baselined (normally the functional baseline) and always covers the FBL and ABLs.
- Approval routing turns on baseline ownership: Government baselines and contractually specified impacts pull the decision to the Government; everything else may rest with the contractor.
- ECPs are Class I (CCB + contract modification) or Class II (local representative concurrence); RFVs are minor/major/critical and require negotiated consideration, with approval an inherently Governmental, non-delegable function.
- The NOR is the precise documentary instrument tied to an ECP; the CDCA is the single document-content authority; AAs may participate but never authorize.
- Process formality scales with phase — informal in TMRR, formal and essential from EMD onward — and recurring variances are a warning sign, not a workaround.

## Connects To

- **Configuration identification & baselines** — Control presupposes identified CIs and established baselines (FBL/ABL); the span of control begins exactly when the first document is baselined.
- **Configuration status accounting** — The handbook's insistence on accurate documentation of initial and changed configurations, plus change effectivity in both records and actual units, feeds directly into status accounting.
- **GEIA-HB-649 and DD Forms 1692 / 1694 / 1423** — The detailed classification criteria and activity templates live outside the handbook; this section repeatedly defers to GEIA-HB-649, the DD Form 1692 (ECP) and DD Form 1694 (RFV) instruction sheets, and the CDRL / DD Form 1423 for NOR submission.
- **FAR (7.503, 46.407)** — Variance approval as an inherently Governmental function and the non-conforming-material consideration rule are anchored in the FAR, tying CM practice to acquisition regulation.
- **Program management / IPT structures** — The PM owns CCB disposition, and the handbook locates the most effective pre-ECP coordination inside an IPT, binding configuration control to the broader program-management apparatus.
