# Chapter 3: Risk Assessment — Severity, Probability, the Matrix & Acceptance Authorities

## Core Idea
MIL-STD-882E Section 4.3.3 formalises risk as a two-dimensional quantity: severity of the potential mishap crossed with probability that the mishap occurs. A Risk Assessment Code (RAC) encodes both dimensions in a single alphanumeric label (e.g., 1A = Catastrophic/Frequent). The Risk Assessment Matrix (Table III) maps every RAC to one of four risk levels — High, Serious, Medium, or Low — which then determines the required acceptance authority level under DoDI 5000 series.

## Frameworks Introduced

- **Risk Assessment Matrix (Table III)**: 4x5 grid of Severity (I–IV) crossed with Probability (A–F) producing risk levels High/Serious/Medium/Low.
  - When to use: mandatory for every identified hazard at every risk assessment point (initial, target, event); tailored alternatives require formal DoD Component policy approval.

- **Severity Categories (Table I)**: four categories based on worst-case mishap consequence — death/total disability/severe environmental impact/large monetary loss at the severe end, down to minor injuries and minimal environmental impact at the low end.
  - When to use: applied at Element 3 for each hazard; re-applied after each design change.

- **Probability Levels (Table II)**: six levels from Frequent (A) to Eliminated (F), assessed qualitatively or quantitatively; Eliminated (F) is reserved for hazards that have been physically removed from the system — procedures, PPE, and training cannot achieve F.
  - When to use: applied concurrently with severity assessment; quantitative data preferred over qualitative when available.

## Key Concepts

- **Severity Category I — Catastrophic**: could result in death, permanent total disability, irreversible significant environmental impact, or monetary loss >= $10M.
- **Severity Category II — Critical**: permanent partial disability, hospitalisation of >= 3 personnel, reversible significant environmental impact, or monetary loss >= $1M and < $10M.
- **Severity Category III — Marginal**: injury or illness causing >= 1 lost work day, reversible moderate environmental impact, or monetary loss >= $100K and < $1M.
- **Severity Category IV — Negligible**: injury or illness with no lost work day, minimal environmental impact, or monetary loss < $100K.
- **Probability A — Frequent**: likely to occur often in the life of an item; continuously experienced in fleet. Quantitative: >= 10^-1.
- **Probability B — Probable**: will occur several times in item life; frequent in fleet. Quantitative: >= 10^-2 and < 10^-1.
- **Probability C — Occasional**: likely to occur sometime in item life; will occur several times in fleet. Quantitative: >= 10^-3 and < 10^-2.
- **Probability D — Remote**: unlikely but possible in item life; unlikely but can reasonably be expected in fleet. Quantitative: >= 10^-6 and < 10^-3.
- **Probability E — Improbable**: so unlikely it can be assumed not to occur in item life; unlikely to occur but possible in fleet. Quantitative: < 10^-6.
- **Probability F — Eliminated**: incapable of occurrence; used when a hazard has been physically eliminated. Cannot be achieved through doctrine, training, warning, cautions, or PPE alone.
- **RAC (Risk Assessment Code)**: alphanumeric combining severity (1–4) and probability (A–F); e.g., 2C = Critical severity, Occasional probability.
- **Risk Level — High**: RACs 1A, 1B, 1C, 2A, 2B. Requires highest-level acceptance authority.
- **Risk Level — Serious**: RACs 1D, 2C, 3A, 3B. Requires elevated acceptance authority; user representative concurrence required.
- **Risk Level — Medium**: RACs 1E, 2D, 3C, 3D, 4A, 4B. Requires programme-level acceptance.
- **Risk Level — Low**: RACs 2E, 3E, 4C, 4D, 4E. Can typically be accepted at lower authority levels.
- **Monetary Loss**: sum of estimated costs for equipment repair/replacement, facility repair/replacement, environmental cleanup, personal injury or illness costs, environmental liabilities, and known fines or penalties.

## The Risk Assessment Matrix

```
               Severity
               Cat I         Cat II        Cat III       Cat IV
Prob           (Catastrophic)(Critical)    (Marginal)    (Negligible)
A (Frequent)   HIGH          HIGH          SERIOUS       MEDIUM
B (Probable)   HIGH          SERIOUS       MEDIUM        LOW
C (Occasional) SERIOUS       MEDIUM        MEDIUM        LOW
D (Remote)     MEDIUM        MEDIUM        LOW           LOW
E (Improbable) LOW           LOW           LOW           LOW
F (Eliminated) ---           ---           ---           ---
```

## Mental Models

- **"Eliminated (F) requires physical removal"** — no amount of training, warnings, cautions, or PPE can move a mishap probability to F. This prevents administrative wishful thinking from inflating risk reduction claims.
- **"Severity drives the floor"** — for Cat I (Catastrophic) hazards, even Improbable (E) probability still generates a Low risk level requiring formal acceptance; there is no "ignore" threshold for Catastrophic severity.
- **"Quantitative data beats qualitative"** — when frequency/rate of occurrence data are available, use them; fall back to qualitative text descriptions only in their absence. The SSPP must document all numerical probability definitions used.

## Anti-patterns

- **Setting probability to F via PPE or procedures**: the standard explicitly states "No amount of doctrine, training, warning, caution, or Personal Protective Equipment (PPE) can move a mishap probability to level F."
- **Treating the matrix as static after initial assessment**: risk must be re-assessed at initial, target, and each event (DT, OT, fielding, post-fielding) — the HTS must hold all three sets of RACs.
- **Accepting tailored matrices without formal approval**: the standard permits tailored alternatives but requires formal DoD Component policy approval; informal "programme adjustments" are non-compliant.

## Key Takeaways

1. Every hazard receives three RACs over its life: initial (baseline), target (post-planned mitigation), and event (configuration-specific at each test/fielding event).
2. Catastrophic (I) severity combined with any non-Eliminated probability always produces a High or Serious risk — there is no low-risk path for Cat I without physical hazard elimination or confirmed F probability.
3. Monetary loss thresholds ($100K / $1M / $10M) were updated in Change 1; always use the current Table I values.
4. Quantitative probability levels are provided in Appendix A Table A-II: Improbable = < 10^-6; Remote = 10^-6 to 10^-3; Occasional = 10^-3 to 10^-2; Probable = 10^-2 to 10^-1; Frequent = >= 10^-1.
5. Risk acceptance authority is defined in applicable DoDI 5000 series — the standard delegates this determination to acquisition policy, not to the standard itself.
6. User representative concurrence is required before all Serious and High risk acceptance decisions throughout the life-cycle.

## Connects To

- **Chapter 4 (Software Safety)**: Table VI extends the risk level framework to software via SwCI, using the same H/S/M/L levels.
- **Chapter 5 (Task 100)**: Tasks 101 and 102 require the HTS to record initial, target, and event RACs for every hazard.
- **Chapter 7 (Task 300)**: Tasks 301 and 302 require assessment reports to cite the specific risk matrix used and to summarise all RACs.
- **NASA System Safety Handbook**: uses comparable severity/probability matrices; DoD and NASA conventions are similar enough for cross-standard comparison in programme contexts.
