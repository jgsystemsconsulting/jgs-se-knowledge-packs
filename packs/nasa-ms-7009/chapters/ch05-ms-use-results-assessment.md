# Chapter 5: M&S Use, Inputs, and Results Assessment

## Core Idea
In operations, teams record proposed uses, judge appropriateness against permissible uses and V&V domains, control input pedigree, document setup and utilization, either stay inside envelopes or explicitly manage excursions, capture runtime messages, and assess M&S results across structured factors before risk and reporting.

## Frameworks Introduced
- **Proposed use record**: The actual analysis purpose for this run or campaign.
- **Use appropriateness assessment**: Accept or reject the M&S for that proposed use versus permissible use and domains.
- **Input pedigree**: Provenance and quality of inputs feeding the run (Appendix E concepts).
- **Setup and utilization rationale**: How the M&S was configured and exercised.
- **Envelope compliance option**: Ensure uses stay within permissible uses and domains, or apply the standard alternate control path when they do not.
- **Runtime message log**: Warnings/errors and explanations from execution.
- **M&S results assessment**: Multi-factor evaluation (use assessment, input pedigree, uncertainty, sensitivity, reviews, and related factors).

## Key Concepts
- **Proposed vs permissible vs intended use**: Three linked statements across life-cycle stages.
- **Use assessment is a gate**: Not automatic just because the model exists.
- **Inputs are part of credibility**: Garbage-in is a first-class failure mode.
- **Messages are evidence**: Silently ignoring warnings undermines results claims.
- **Results assessment is not capability assessment**: One judges this analysis product; the other judged the developed M&S.
- **Handbook user guidance**: Operator practices and expected phase outcomes support clean use.

## Mental Models
- Every analysis is a claim that this M&S plus these inputs plus this setup answer this question.
- Staying inside the envelope is the default path to credibility.
- Results assessment packages the operational story the same way capability packaged development.
- Configuration of the run is as important as the code revision.

## Anti-patterns
- **Repurposing a model without a new use assessment**: Classic credibility breach.
- **Untracked spreadsheet inputs**: No pedigree, no defense.
- **Clearing warnings without root-cause notes**: Hides instability.
- **Skipping results assessment because V&V passed years ago**: Capability is not results.

## Key Takeaways
1. Record proposed use and assess appropriateness before relying on outputs.
2. Maintain input pedigrees and setup/utilization rationales.
3. Prefer execution inside permissible uses and V&V domains.
4. Log and explain runtime warnings and errors.
5. Perform a structured M&S results assessment for the analysis.
6. Keep use evidence ready for risk and decision reporting.

## Connects To
- **ch02**: Permissible uses and capability baseline.
- **ch03-ch04**: Domains and uncertainty that bound use.
- **ch06**: Risk assessment and mandatory report contents.
- **ch01**: Criticality that justified applying the standard.
