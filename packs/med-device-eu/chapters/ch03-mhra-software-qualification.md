# Where the MHRA qualification boundary for apps sits and how it diverges from the EU reading

The MHRA guidance (Medical device stand-alone software including apps, including IVDMDs) decides whether an app or stand-alone package is a medical device, an IVD, or an accessory for the Great Britain market, where qualified software must be UKCA or CE marked under UK MDR 2002.
This chapter covers that boundary and the document's app examples; the UKCA-era obligations that follow qualification are ch08's subject.

## The boundary test

S6's flow chart starts by sorting the product: a computer program, or a "functional document" such as a macro spreadsheet, an interactive web page, or a treatment flow chart PDF that needs a separate application to run.
Freeware and open-source count, and the regulations attach to placing on the market rather than to sale.
The second question is medical purpose, read from labelling, instructions for use, promotional material, app store descriptions, landing pages, and the manufacturer's social media.
The guidance lists the medical purposes in two groups: the general device purposes (prevention, diagnosis, monitoring, treatment and alleviation, compensation for injury or handicap, investigation or modification of anatomy or physiological process, control of conception) and the IVD purposes (information on a physiological or pathological state, a congenital abnormality, recipient safety and compatibility, or monitoring of therapeutic measures), the latter only where the data comes from in vitro examination of specimens.

Non-device side of the line, as S6 draws it: general fitness, health, and wellbeing monitoring; professional or patient medical education; storing or transmitting medical data unchanged; reference information that lets a clinician apply their own knowledge; administrative booking, prescription requests, and virtual consultations; an electronic patient record that only replaces the paper file.
Multipurpose tools (a word processor, a plain database) are not devices, though a macro-driven spreadsheet with a specific clinical purpose can be.
Disclaimers do not move the line: S6 notes that "for information only" or "not a medical device" statements fail where medical claims appear elsewhere, and testimonials in product literature count as implied claims.
The manufacturer's own view is not decisive; the regulator or an averagely informed consumer can read a product as a device from its circumstances.

Decision support gets its own page, and it is the sharpest part of the boundary.
Software is unlikely to be a device when it reproduces a paper document, follows a fixed procedure path, explains options while the clinician chooses, or offers only lifestyle or referral advice.
It is most likely to be a device when it is tied to a specific medicine or device, influences actual treatment parameters, or produces a diagnosis, prognosis, or individual risk figure.
Automated reasoning (a calculation, an algorithm) pushes it toward device, especially where the clinician will not review the raw data.

## App examples the guidance uses

- Dose calculators, including insulin dosing from carbohydrate intake, and drug dosing driven by IVD results such as blood glucose, creatinine, or genomic variants.
- Symptom checkers: a device when they narrow conditions by likelihood, recommend treatment, or filter by severity; not a device when they only list matches alphabetically, give reference information, or signpost to care. Class I unless they allow direct diagnosis, which lifts them to class IIa.
- Skin assessment from photos, patient-specific disease risk scores, remote monitoring with alarm filtering, and text magnification or sound amplification tied to a named impairment.
- Fertility and contraception apps based on basal body temperature qualify; a plain cycle diary does not.
- Blastocyst selection software for IVF is a medical device, not an IVD, because the specimen is intended for reintroduction into the body.
- An app that is the only way to interact with a hardware device (a display-less thermometer) may be a component of the device; an app that records data from a monitor may be an accessory.
- Clinical calculators split by verifiability, covered below.

## Where the UK reading diverges from the MDCG one

Three divergences, all stated in S6.
First, lineage and framing: the MHRA document presents itself as the UK's interpretation of MEDDEV 2.1/6 and keeps the term "stand-alone software" in its title and flow chart, while MDCG 2019-11 rev.1 explicitly retires that term and insists qualification depends on intended purpose alone, regardless of location.
Second, the calculator carve-out: S6 applies a verifiability discretion, where a calculation the intended user can easily check (simple scores, four-function arithmetic) is unlikely to be a device, and states: "If the calculation cannot be easily verified by the intended user then it is likely to be a device."
The MDCG document has no verifiability test; under its flow, a calculator with a medical purpose and individual-patient benefit qualifies as MDSW whatever the arithmetic.
Third, S6 treats intermediate and complex calculators, lookup-table tools, and anything pulling unverified data from a patient record as likely devices, and asks for user-study evidence of verifiability where the manufacturer claims the user can check the result; the EU guidance reaches similar software through its action-on-data step without the verifiability language.

Sources: S6
