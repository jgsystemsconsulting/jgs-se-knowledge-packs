# MIL-STD-882E Cheatsheet

## Risk Assessment Matrix (Table III)

```
               SEVERITY CATEGORY
               I             II            III           IV
PROBABILITY    Catastrophic  Critical      Marginal      Negligible
               (death/total  (partial      (lost work    (no lost
               disability/   disability/   day/moderate  work day/
               >=10M USD)    hosp 3+/      env/$100K-    minimal
                             >=1M USD)     $1M USD)      <$100K USD)

A  Frequent    HIGH          HIGH          SERIOUS       MEDIUM
B  Probable    HIGH          SERIOUS       MEDIUM        LOW
C  Occasional  SERIOUS       MEDIUM        MEDIUM        LOW
D  Remote      MEDIUM        MEDIUM        LOW           LOW
E  Improbable  LOW           LOW           LOW           LOW
F  Eliminated  ---           ---           ---           ---
```

**RAC format:** [Severity number][Probability letter] — e.g., 1A = Catastrophic/Frequent = HIGH risk.

**Quantitative probability thresholds (Appendix A):**
- A (Frequent): >= 10^-1
- B (Probable): >= 10^-2, < 10^-1
- C (Occasional): >= 10^-3, < 10^-2
- D (Remote): >= 10^-6, < 10^-3
- E (Improbable): < 10^-6
- F (Eliminated): physically incapable of occurrence — cannot be achieved by procedures/PPE

---

## Software Safety Criticality Matrix (Table V)

```
               SEVERITY CATEGORY
SCC Level      I (Cat)   II (Crit)  III (Marg)  IV (Neg)
1 Autonomous   SwCI 1    SwCI 1     SwCI 3      SwCI 4
2 Semi-Auto    SwCI 1    SwCI 2     SwCI 3      SwCI 4
3 Redund. FT   SwCI 2    SwCI 3     SwCI 4      SwCI 4
4 Influential  SwCI 3    SwCI 4     SwCI 4      SwCI 4
5 NSI          SwCI 5    SwCI 5     SwCI 5      SwCI 5
```

**LOR Tasks by SwCI:**
| SwCI | Required LOR Tasks | Default Risk if Incomplete |
|------|-------------------|---------------------------|
| 1 | Req + Arch + Design + Code analysis; in-depth safety-specific testing | HIGH |
| 2 | Req + Arch + Design analysis; in-depth safety-specific testing | SERIOUS |
| 3 | Req + Arch analysis; in-depth safety-specific testing | MEDIUM |
| 4 | Safety-specific testing only | LOW |
| 5 | No safety analysis or verification required | N/A |

Note: SSCM assigns rigor (criticality), not risk. Risk from software uses Appendix B Table B-I criteria.

---

## Risk Acceptance Levels

| Risk Level | Acceptance Authority | User Representative? |
|------------|---------------------|---------------------|
| HIGH       | Defined in DoDI 5000 series (senior authority) | Formal concurrence required |
| SERIOUS    | Defined in DoDI 5000 series | Formal concurrence required |
| MEDIUM     | Defined in DoDI 5000 series (programme level) | Not required |
| LOW        | Defined in DoDI 5000 series (lowest level) | Not required |

The specific authority levels are defined in the applicable DoDI 5000 series acquisition policy document, not in MIL-STD-882E itself.

---

## Design Order of Precedence (4.3.4)

| Priority | Mitigation Type | Notes |
|----------|----------------|-------|
| 1 | Eliminate via design selection | Remove the hazard; most effective |
| 2 | Reduce via design alteration | Lower severity or probability |
| 3 | Engineered features or devices | Active interrupt or passive protection |
| 4 | Warning devices | Alert personnel to hazard |
| 5 | Signage/procedures/training/PPE | Least effective; cannot be sole mitigation for Cat I/II |

---

## Task-by-Phase Application (Appendix A Table A-I Summary)

| Task | Type | MSA | TD | EMD | P&D | O&S |
|------|------|-----|----|-----|-----|-----|
| 101 Hazard ID & Mitigation | MGT | G | G | G | G | G |
| 102 SSPP | MGT | G | G | G | G | G |
| 103 Hazard Management Plan | MGT | G | G | G | G | G |
| 104 Govt Reviews/Audits | MGT | G | G | G | G | G |
| 105 IPT/WG Support | MGT | S | G | G | G | G |
| 106 Hazard Tracking System | MGT | S | G | G | G | G |
| 107 Progress Report | MGT | G | G | G | G | G |
| 108 HMMP | MGT | S | G | G | G | G |
| 201 PHL | ENG | G | G | G | G | G |
| 202 PHA | ENG | S | G | G | G | G |
| 203 SRHA | ENG | N/A | G | G | G | G |
| 204 SSHA | ENG | N/A | S | G | G | G |
| 205 SHA | ENG | N/A | G | G | G | G |
| 206 O&SHA | ENG | S | S | G | G | G |
| 207 HHA | ENG | S | G | G | G | G |
| 208 FHA | ENG | S | S | G | G | S |
| 209 SoSHA | ENG | N/A | S | S | GC | GC |
| 210 EHA | ENG | S | S | G | G | S |
| 301 SAR | ENG | S | G | S | GC | GC |
| 302 HMAR | ENG | S | S | G | GC | GC |
| 303 T&E Participation | ENG | G | G | G | GC | GC |
| 304 ECP/Mishap Review | ENG | N/A | G | G | GC | GC |
| 401 Safety Verification | ENG | N/A | G | G | GC | GC |
| 402 Explosives Hazard Class. | ENG | N/A | G | G | G | S |
| 403 EOD Data | ENG | N/A | G | G | GC | GC |

**Key:** G = Generally Applicable; S = Selectively Applicable; GC = Generally Applicable to Design Changes; N/A = Not Applicable  
**Phases:** MSA = Materiel Solution Analysis; TD = Technology Development; EMD = Engineering & Manufacturing Development; P&D = Production & Deployment; O&S = Operations & Support

---

## Severity Category Quick Reference

| Cat | Label | Key Criteria |
|-----|-------|-------------|
| I | Catastrophic | Death, permanent total disability, irreversible significant environmental impact, or monetary loss >= $10M |
| II | Critical | Permanent partial disability, hospitalisation of >= 3 personnel, reversible significant environmental impact, or monetary loss >= $1M and < $10M |
| III | Marginal | Injury/illness causing >= 1 lost work day, reversible moderate environmental impact, or monetary loss >= $100K and < $1M |
| IV | Negligible | Injury/illness with no lost work day, minimal environmental impact, or monetary loss < $100K |

---

## HTS Minimum Data Elements (Task 106)

Every hazard record must contain:
- Hazard description
- System and subsystem
- Applicability (version-specific hardware/software)
- Requirements references
- System mode(s)
- Causal factor(s)
- Effects
- Mishap description
- Initial RAC
- Target RAC
- Event RAC(s)
- Mitigation measures identified and selected (with version traceability)
- Hazard status
- V&V method
- Action person(s) and organisational element
- Record of risk acceptance(s): authority title/org, date, signed document location
- Hazard management log (full change history)
- HAZMAT data elements (when applicable)

---

## Key Tells & Smells

**Tells (indicators of good practice):**
- HTS has three RAC columns (initial, target, event) populated for every hazard
- SSPP/HMP includes a compliance matrix tracing contractual requirements to SSPP section
- FHA completed before detailed software architecture is frozen
- Design reviews include a hazard status slide with RAC trend data
- Every ECP has a documented system safety review in its approval package
- SwCI assignments are traceable to specific software functions, not just to software items
- Risk acceptance signatures exist for all Serious and High risks with user representative concurrence

**Smells (red flags):**
- Risk acceptance column in HTS is empty for High or Serious hazards
- Probability F assigned to any hazard where only administrative controls have been applied
- Safety assessment report dated after the test event it was supposed to support
- COTS/NDI items listed as "assumed safe from supplier" without system-context analysis
- Software "safety analysis" consists only of functional testing with no fault injection or boundary testing
- Cat I/II hazards mitigated solely by signage, procedures, or PPE
- Life-cycle risk management plan ends at fielding with no O&S phase provisions
- All hazards in HTS show identical probability assessments (sign of bulk-copy rather than individual assessment)
- SSPP calls for applying level 5 mitigations as primary controls for critical hazards
- SwCI 5 (NSI) assigned without documented safety engineering assessment
