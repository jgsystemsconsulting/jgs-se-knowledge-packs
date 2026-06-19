# NASA NPR 7123.1D Cheatsheet

## Quick Decision Rules

**"Do I need a waiver/deviation or can I just customise?"**
- Are you seeking relief from *what* the NPR requires you to do? → **Tailoring** (need waiver/deviation + ETA approval)
- Are you choosing *how* to implement what the NPR requires? → **Customising** (no waiver needed; document in SEMP)

**"Which Appendix G table do I use for my review?"**
- Program (not single-project) at SRR or SDR? → Tables G-1, G-2
- Project, single-project program, or any other review type? → Tables G-3 onwards

**"Is this product verification or validation?"**
- Checking against specifications/requirements? → **Verification** ("Did I build it right?")
- Checking against stakeholder expectations in the intended environment? → **Validation** ("Did I build the right thing?")

**"Is my review complete?"**
All must be true: (1) RIDs/RFAs dispositioned with TA concurrence; (2) board report distributed; (3) plans exist for all issues/actions; (4) chairperson reported to management; (5) Decision Authority signed decision memo.

**"Is a waiver or deviation needed?"**
- Relief needed *before* requirements go under configuration control? → **Deviation**
- Relief needed *after* configuration control? → **Waiver**

**"What TRL do I need before CDR?"**
- Critical technologies: TRL 6 minimum at PDR; TRL 7 at CDR for mission-critical elements

---

## The 17 Common Technical Processes at a Glance

| Group | Process | Req ID | Core output |
|---|---|---|---|
| **System Design** | Stakeholder Expectations Definition | SE-07 | Baselined ConOps + MOEs |
| | Technical Requirements Definition | SE-08 | Verified "shall" statements + MOPs/TPMs |
| | Logical Decomposition | SE-09 | Functional models + derived requirements |
| | Design Solution Definition | SE-10 | Preferred design alternative + specifications |
| **Product Realization** | Product Implementation | SE-11 | Made/bought/reused lowest-level product |
| | Product Integration | SE-12 | Assembled product from verified lower-level products |
| | Product Verification | SE-13 | Proof of specification conformance |
| | Product Validation | SE-14 | Proof of stakeholder expectation satisfaction |
| | Product Transition | SE-15 | Delivered verified/validated product to next customer |
| **Technical Management** | Technical Planning | SE-16 | SEMP |
| | Requirements Management | SE-17 | Bidirectional traceability + change control |
| | Interface Management | SE-18 | Interface definitions + compliance |
| | Technical Risk Management | SE-19 | Risk register + mitigation plans |
| | Configuration Management | SE-20 | Controlled configuration + change records |
| | Technical Data Management | SE-21 | Trade studies, analyses, reports captured |
| | Technical Assessment | SE-22 | Life-cycle review inputs + status reports |
| | Decision Analysis | SE-23 | Documented criteria, alternatives, selection |

---

## Mandatory Work Products by Review (SE "shall" requirements)

| Review | Required Products |
|---|---|
| **MCR** | Baselined stakeholder expectations (SE-35), concept definition (SE-36), approved MOEs (SE-37) |
| **SRR** | Baselined SEMP (SE-38), baselined requirements (SE-39), baselined HSI approach (SE-66) |
| **MDR/SDR** | Approved TPMs (SE-40), baselined architecture (SE-41), baselined requirements allocation (SE-42), initial TPM trends (SE-43), baselined SEMP for programs (SE-44) |
| **PDR** | Preliminary design solution (SE-45), baselined integration plans (SE-67), baselined V&V Plan (SE-68) |
| **CDR** | Baseline detailed design (SE-46) |
| **SIR** | Updated integration plan (SE-47), initial V&V results (SE-48) |
| **ORR** | Preliminary V&V results (SE-69), baselined decommissioning plans (SE-51), baselined disposal plans (SE-52) |
| **FRR** | Baseline V&V results (SE-53), final certification for flight/use (SE-54) |
| **DR** | Updated decommissioning plans (SE-55) |
| **DRR** | Updated disposal plans (SE-56) |

---

## TRL Quick Reference

| TRL | Label | Key Evidence |
|---|---|---|
| 1 | Basic principles observed | Peer-reviewed research documentation |
| 2 | Concept formulated | Documented application/concept description |
| 3 | Proof-of-concept | Documented analytical/experimental results |
| 4 | Component in lab | Lab test performance vs. analytical predictions |
| 5 | Component in relevant env | Test performance + scaling requirements defined |
| 6 | Prototype in relevant env | Full-scale prototype test in relevant environment |
| 7 | Prototype in operational env | Demonstration in actual operational environment/platform |
| 8 | Flight qualified | Test and analysis in final configuration for operational environment |
| 9 | Flight proven | Successful actual mission operations |

---

## Work Product Maturity Terminology

| Term | Meaning |
|---|---|
| **Initial** | Continually developed and updated; not yet stable |
| **Preliminary** | Stabilising but not yet under configuration control; development leading to a baseline |
| **Approve** | Approved but not under classic configuration control; changes documented at each update |
| **Baseline** | Under configuration control; at least a final draft going into the designated review; formally baselined coming out |
| **Update** | Expected evolution of a previously approved or baselined document |
| **Final** | Expected to exist in this form; e.g., meeting minutes, final reports |

---

## Tells and Smells — Things That Should Concern You

**Process tells (signs SE is working)**
- Reviews scheduled when entrance criteria are satisfied, not when the calendar says
- Compliance matrix (Appendix H) is current and in the SEMP
- TPMs (including mass and power margins) are tracked and reported on a defined interval
- ETA approval precedes any SEMP baseline or key technical document release
- All RIDs/RFAs from prior reviews are dispositioned before the next review begins

**Anti-pattern smells (warning signs)**
- Calendar-driven review scheduling — "We need to hold SRR before the budget cycle closes"
- No bidirectional traceability from requirements to design and up to stakeholder expectations
- SEMP written at programme start and never updated
- ETA reports to the programme manager in the same budget chain
- A technology below TRL 6 entering PDR without a documented mitigation plan
- V&V plan created after CDR
- HSI treated as a late-phase human factors review, not a continuous planning thread
- Compliance matrix absent from the SEMP
- "We'll tailor that later" with no ETA approval in progress
- Insight/oversight requirements defined after contract award, not in the solicitation

---

## Key NPR Requirement Numbers

| Requirement | Topic |
|---|---|
| SE-06 | ETA approval of SEMP and key technical documents |
| SE-07 to SE-10 | Four system design processes |
| SE-11 to SE-15 | Five product realization processes |
| SE-16 to SE-23 | Eight technical management processes |
| SE-24 to SE-31 | Contracted project SE activities |
| SE-32 to SE-57 | Life-cycle review requirements (planning, conduct, completion) |
| SE-58 to SE-64 | SEMP content and TPM requirements |
| SE-65 to SE-69 | HSI approach and additional life-cycle review products (new in 7123.1D) |
