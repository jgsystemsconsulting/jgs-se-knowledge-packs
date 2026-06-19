# Chapter 7: Transparency Obligations for Certain AI Systems (Chapter IV, Article 50)

## Core Idea
Chapter IV imposes targeted disclosure obligations on providers and deployers of AI systems that interact with humans, generate synthetic content, or categorise/recognise emotions — even when those systems are not high-risk. The core principle is that humans must know when they are dealing with AI, and AI-generated content must be machine-detectably labelled.

## Frameworks Introduced
- **Article 50 — Four transparency obligations**:
  1. **Human-AI interaction disclosure** (Art 50(1)): Providers must design systems interacting with natural persons to inform those persons they are talking to an AI, unless this is obvious to a reasonably well-informed observer. Exception: law-enforcement-authorised systems (with safeguards).
  2. **Synthetic content machine-readability labelling** (Art 50(2)): Providers of AI systems generating synthetic audio, image, video, or text must ensure outputs are marked in a machine-readable format detectable as artificially generated or manipulated. Must be effective, interoperable, robust, and reliable as far as technically feasible.
  3. **Emotion recognition and biometric categorisation disclosure** (Art 50(3)): Deployers must inform persons exposed to emotion recognition or biometric categorisation systems of the operation; processing must comply with GDPR/law enforcement data protection rules.
  4. **Deep fake disclosure** (Art 50(4)): Deployers of AI generating or manipulating image/audio/video constituting a deep fake must disclose that content has been artificially generated or manipulated. Exception: law enforcement authorised use and (limited) artistic/satirical works. Deployers of AI generating text on public-interest matters must disclose AI generation (unless human review/editorial control and legal responsibility are in place).
  - When to use: For any AI system interacting with end users or generating synthetic media, regardless of high-risk status.

## Key Concepts
- **Deep fake** (Art 3(60)) — AI-generated or manipulated image, audio, or video content that resembles existing persons, objects, places, entities, or events and would falsely appear to a person to be authentic or truthful.
- **Machine-readable format labelling** — synthetic content outputs must carry technically detectable markers; human-visible disclaimers alone do not satisfy Art 50(2). The Act anticipates watermarking, metadata embedding, or equivalent technical solutions.
- **Reasonably well-informed, observant, and circumspect person** — the standard used in Art 50(1) to determine whether human-AI interaction disclosure is already obvious; a higher standard than the average consumer, aligned with EU consumer law.
- **Editorial control exception** (Art 50(4)) — AI-generated text published on public-interest matters is exempted from the deep fake disclosure rule if it undergoes human review/editorial control AND a natural or legal person holds editorial responsibility for publication. Both conditions must be met.
- **Artistic/satirical work limitation** — for deep fake content forming part of evidently artistic, creative, satirical, fictional, or analogous work, the disclosure obligation is limited to appropriate disclosure that does not hamper the display or enjoyment of the work.

## Mental Models
- **"Transparency obligations are a floor for non-high-risk AI"**: Art 50 applies to chatbots, synthetic media generators, emotion detectors, and biometric categorisers that may not be high-risk under Chapter III; it is a separate, lighter-touch but mandatory layer.
- **"Labelling must be machine-readable, not merely human-visible"**: A human-visible watermark or disclaimer on synthetic content is insufficient; Art 50(2) requires machine-detectable marking, enabling automated detection downstream.

## Anti-patterns
- Assuming Art 50 only applies to high-risk AI systems: it applies to any AI system in its four categories, regardless of risk classification.
- Treating the artistic exception as broad: the artistic/satirical carve-out for deep fake disclosure is limited to disclosure that does not hamper the work; full non-disclosure is not permitted.
- Assuming law-enforcement exception eliminates disclosure entirely: the Art 50(1) exception for law-enforcement-authorised systems applies to identity detection, not to all law-enforcement AI systems.

## Key Takeaways
1. Art 50 creates four separate disclosure obligations; each covers a different AI system type and may apply independently.
2. Machine-readable synthetic content labelling is a technical requirement on providers; deployers' disclosure of deep fakes is a parallel obligation.
3. The chatbot disclosure obligation applies at design level (provider builds it in); the deep fake disclosure obligation falls on deployers at distribution.
4. Emotion recognition disclosure is a deployer obligation; providers must build emotion recognition capability declarations into instructions for use (Art 13).
5. The Commission may adopt implementing acts approving codes of practice for synthetic content detection and labelling (Art 50(7)).
6. Art 50 obligations do not replace, but supplement, Chapter III high-risk obligations where both apply.

## Connects To
- **Chapter I (Art 3(60))**: Deep fake definition.
- **Chapter III Section 3 (Art 26(11))**: Deployers of high-risk Annex III systems must also inform affected persons; Art 50 extends this to non-high-risk systems.
- **Chapter X (Art 95-96)**: Codes of conduct and Commission guidelines may further specify Art 50 implementation.
- **Chapter XII (Art 99(4)(g))**: Violation of Art 50 by providers or deployers carries fines up to EUR 15 million or 3% of turnover.
