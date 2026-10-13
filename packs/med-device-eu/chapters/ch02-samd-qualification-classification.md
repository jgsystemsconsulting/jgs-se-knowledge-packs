# How MDCG 2019-11 rev.1 qualifies and classifies medical device software

MDCG 2019-11 rev.1 (the June 2025 revision of the October 2019 document) answers two questions for software manufacturers: is this software covered by the EU Medical Devices Regulations at all (qualification), and if so, which risk class applies (classification).
Its criteria cover apps on phones, server-side software, embedded code, and cloud services alike; S1 defines software as "a set of instructions that processes input data and creates output data", and repeats that where the software runs changes neither its qualification nor its class.
The rev.1 text also states that its criteria reach medical device artificial intelligence and MDR Annex XVI products.

## The qualification decision

S1 runs qualification as a five-step decision.
Step 1: is the product software at all by the definition above?
Step 2: is it an Annex XVI product, an accessory for a medical device, or software that drives or influences the use of a hardware device?
Any of those puts it under the regulations, treated as part of that device or, for accessories, in its own right.
Step 3: does it act on data beyond storage, archival, communication, simple search, or lossless compression?
Step 4: is that action for the benefit of individual patients?
Tools that only aggregate population data, provide generic pathways, or serve epidemiology fail this step.
Step 5: does the software have a medical purpose of its own under the device definition?

The decisive own-purpose test: software qualifies as medical device software (MDSW) when its manufacturer intends a medical purpose for it, such as diagnosis, prevention, monitoring, prediction, prognosis, treatment, or alleviation.
Software with no medical purpose (invoicing, word processing, wellness and fitness apps, general communication) does not qualify.
Altering data representation for cosmetic or compatibility reasons does not qualify; doing it to serve a diagnostic or therapeutic purpose can.
S1 adds two negatives worth remembering: the risk of harm from malfunction is not a qualification criterion, and the operating system, server, or virtual environment the software runs on is irrelevant.

Software that only drives or influences a hardware device, with no medical purpose of its own, is still covered: as a component of that device or as an accessory.
If it has a medical purpose and also drives a device, it is MDSW.
Examples S1 uses include insulin dosing software that commands a pump in a closed loop, melanoma analysis software that controls a laser scanner, and smartwatch apps that alert on irregular heartbeats.

IVD MDSW is the parallel track.
Software providing information of the kind the IVDR covers (physiological or pathological state, predisposition to disease, treatment monitoring, donor compatibility) qualifies as IVD MDSW.
When the software mixes data from IVDs and other medical devices, S1 applies a weighting: the applicable regulation follows whichever data source substantially drives the intended purpose.

## The classification decision

For MDSW under the MDR, the document's central rule is Rule 11 of Annex VIII, which S1 breaks into three sub-rules.
Sub-rule 11a: software providing information used for diagnostic or therapeutic decisions starts at class IIa; it rises to class IIb when decisions based on wrong information could cause serious deterioration or a surgical intervention, and to class III when they could cause death or irreversible deterioration.
Sub-rule 11b: software intended only to monitor physiological processes is class IIa, rising to class IIb for vital parameters whose variations could put the patient in immediate danger.
Sub-rule 11c: all other software is class I.
S1 maps these outcomes onto the IMDRF risk categorization framework in an annex, with the caveat that class I software sits outside that table.

Around Rule 11, S1 applies the implementing rules.
Software that drives or influences a device falls in that device's class; independent software is classified in its own right; where several rules apply, the strictest wins; and software sold in combination with a device may not land below the device's own class.
Rule 15 puts contraception software at class IIb.
Rule 22 puts closed-loop therapeutic systems with integrated diagnostics at class III.
Rules 12 and 13 mostly resolve to the residual class I, since software cannot physically administer or remove substances.
IVD MDSW classifies under the IVDR's own Annex VIII instead, with the same own-right and same-class logic in its implementing rules.

## What rev.1 changed and how software reaches the market

The revision page lists the changes against the 2019 original: a scope clarification; more weight on crafting a clear intended purpose and on modular software; a clarified Annex XVI scope; new examples including software intended to treat; a clarified Rule 11 sub-rule a covering devices that prevent the risk of illness; an expanded modules section; an updated EHR annex reflecting the European Health Data Space; and a new class I example in the classification annex.

On market placement, S1 gives two routes: as a device in its own right with its own conformity assessment, or as an integral component of a hardware device assessed through that device's process.
Modular products are assessed per module: modules claiming a medical purpose must individually conform, and the manufacturer must delineate module boundaries, dependencies, and interfaces.
Any change to function, intended use, or design can re-open qualification and classification, including for the combination with another device.

Sources: S1
