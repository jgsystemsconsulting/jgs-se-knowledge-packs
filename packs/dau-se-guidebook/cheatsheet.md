# DoD Systems Engineering Guidebook Cheatsheet

## Quick Decision Rules

**"Is this a risk, an issue, or an opportunity?"**
- Future event, negative → **Risk** (likelihood × consequence matrix; accept/avoid/transfer/control)
- Already happened / present problem → **Issue** (consequence matrix; corrective-action burn-down)
- Future event, beneficial → **Opportunity** (opportunity matrix; pursue/reject)

**"Verification or validation?"**
- Conformance to requirements/specification, developmental test → **Verification** ("built it right") → SVR/FCA
- Meets the operational need in the intended environment, operational test → **Validation** ("built the right thing")

**"Which baseline does this review establish/verify?"**
- SFR → **functional** baseline · PDR → **allocated** baseline · CDR → initial **product** baseline · PCA → verifies **product** baseline (as-built)

**"Should I hold this review now?"**
- Only if the system meets the **entrance criteria** in the SEP. Reviews are event-driven, not calendar-driven. If criteria aren't met → delay, don't paper over.

**"Do I need a SEP?"**
- MDAP or ACAT II/III → **required** (unless waived by the SEP approval authority). Everything else → recommended best practice.

**"Policy or guidance?"**
- This Guidebook = **guidance** (how). Binding requirements = **DoDI 5000.88** (Engineering of Defense Systems) and related issuances (what).

---

## The 16 SE Processes (8 + 8)

| Technical Management (8) | Technical (8) |
|---|---|
| Technical Planning | Stakeholder Requirements Definition |
| Decision Analysis | Requirements Analysis |
| Technical Assessment | Architecture Design |
| Requirements Management | Implementation |
| Risk Management (RIO) | Integration |
| Configuration Management | Verification |
| Technical Data Management | Validation |
| Interface Management | Transition |

All 16 map to ISO/IEC/IEEE 15288 and are **scaled** to the program. Technical processes flow along the V (design down, realization up); technical management runs continuously.

---

## Technical Reviews & Audits — Major Capability Acquisition sequence

| Order | Review/Audit | Gates |
|---|---|---|
| 1 | **ASR** (Alternative Systems Review) | Feasible materiel solution; requirements understood |
| 2 | **SRR** (System Requirements Review) | Requirements baselined & traceable |
| 3 | **SFR** (System Functional Review) | **Functional baseline** |
| 4 | **PDR** (Preliminary Design Review) | **Allocated baseline**; preliminary design at acceptable risk |
| 5 | **CDR** (Critical Design Review) | Initial **product baseline**; ready to fabricate/code |
| 6 | **SVR/FCA** (System Verification Review / Functional Configuration Audit) | System **verified** vs. functional baseline |
| 7 | **PRR** (Production Readiness Review) | Ready for production at acceptable risk |
| 8 | **PCA** (Physical Configuration Audit) | Product baseline = as-built |

Each has defined products and entrance/success criteria; all **RFAs** dispositioned before completion.

---

## RIO Matrices at a Glance

- **Risk** → 5×5 **likelihood × consequence**; handling = Accept / Avoid / Transfer / Control (mitigate).
- **Issue** → consequence-based; handling = corrective-action **burn-down**.
- **Opportunity** → opportunity matrix; handling = **pursue / reject** (cost-benefit).

## TPM vs. Leading Indicator

- **TPM** — quantitative measure tracked against a **planned profile**; tells you if the design will meet a requirement.
- **Leading indicator** — **forward-looking** measure/trend; warns *before* a threshold is breached so mitigation can start early.

---

## The 24 Design Considerations (reference list)

Accessibility (Section 508) · Affordability (SE trade-off analyses) · Anti-Counterfeiting · COTS · Corrosion Prevention & Control · Critical Safety Item · Demilitarization & Disposal · DMSMS · Human Systems Integration (HSI) · Insensitive Munitions · Intelligence (Life Cycle Mission Data Plan) · Interoperability & Dependencies · Item Unique Identification (IUID) · Manufacturing & Quality (incl. manufacturing readiness / MRLs) · Modular Design · Operational Energy · Packaging, Handling, Storage & Transportation (PHS&T) · Reliability & Maintainability (R&M) · Spectrum Management · Standardization · Supportability · Survivability · System Safety (incl. software system safety, ESOH, hazard tracking) · System Security Engineering.

**Rule:** engineer them **in**, don't bolt them on; plan their treatment in the SEP; assess MRLs alongside TRLs.

---

## Tells & Smells

- **Calendar-driven review** ("PDR is next month regardless") → should be event-driven on entrance criteria.
- **"Mitigating" something that already happened** → that's an **issue**, not a risk; burn it down.
- **TPM with no planned profile / no leading indicator** → you'll only see the shortfall after a breach.
- **Requirement with no parent or no allocation** → Requirements Management has failed; CM can't control its change.
- **Safety/security/HSI deferred to late phases** → bolt-on; expensive or infeasible to retrofit.
- **Reviews/data/MOSA missing from the RFP** → can't be reliably obtained after award.
- **Treating the Guidebook as mandatory** → it's guidance; the "shall" lives in DoDI 5000.88.

---

## Key Documents the SEP Must Stay Consistent With

APB · AS · TEMP (Test & Evaluation Master Plan) · PPP (Program Protection Plan) · LCSP (Life Cycle Sustainment Plan) · IMP / IMS · WBS · Risk Management Plan.
