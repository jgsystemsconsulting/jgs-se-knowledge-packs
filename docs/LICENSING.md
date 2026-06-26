<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Licensing & Reconstitution Justification

This document explains **why every pack in this catalogue is lawful to reconstitute,
redistribute, and install**, and why that remains true even though the packs do not
hyperlink to the original source documents. The short version: we only ever package
sources whose licence *expressly permits* what we do, and we honour every condition
those licences attach.

## 1. The two-layer licensing model

A knowledge pack has two separable layers, licensed independently:

| Layer | What it is | Licence |
|-------|-----------|---------|
| **Tooling & scaffolding** | The repo: `tooling/`, installers, docs, CI, pack structure | **MIT** (JG Systems Consulting Ltd.) |
| **Pack content** | The reconstructed reference notes inside `packs/<slug>/` | **The upstream source's own licence** (see each `packs/<slug>/LICENSE` and the root `NOTICE`) |

The machinery is permissively licensed; the *knowledge* keeps whatever obligations its
open source attached. A CC BY-NC-SA source (e.g. SEBoK) yields a CC BY-NC-SA pack:
non-commercial, attribution and share-alike carried forward.

## 2. We only package sources that permit it

Every pack's source is vetted to **Tier 1 or Tier 2** of [SOURCE-VETTING.md](SOURCE-VETTING.md)
before any content is produced. Sources that are merely "free to read" but
all-rights-reserved (ISO/IEC/IEEE standards, SWEBOK, the MITRE SE Guide, the INCOSE SE
Handbook, TOGAF, PMBOK) are on a hard **Excluded** list and are never packaged. So no
pack can carry restricted text in the first place.

### Tier 1: Public domain (e.g. NASA SE Handbook, DoDAF)

Works of the US Government are **not subject to copyright** in the United States
(17 U.S.C. § 105). There is no exclusive right to infringe: anyone may reproduce,
transform, and redistribute them for any purpose. We add an attribution courtesy line in
`NOTICE`, but no permission is needed and none is implied to be withheld.

### Tier 2: Open licence (e.g. SEBoK, OMG SysML, MIT OpenCourseWare)

These carry licences that **expressly grant the right to redistribute and to create
derivative works**:

- **Creative Commons BY-NC-SA** (SEBoK, MIT OCW): the licence grants the rights to
  *"Share: copy and redistribute"* and *"Adapt: remix, transform, and build upon the
  material."* Reconstituting the source into reference notes is precisely an exercise of
  the **Adapt** right. We satisfy every condition: **BY** (we attribute the creator),
  **NC** (packs are non-commercial), **SA** (pack content is released under the same
  licence; see each pack `LICENSE`).
- **OMG Specification Licence** (SysML): grants a royalty-free, worldwide right to copy,
  modify, and distribute modified versions, provided the copyright notice is reproduced,
  modifications are noted, and the trademarked spec name is not applied to the modified
  work. Our packs comply with all three.

In every Tier-2 case, reconstitution is **the licensed use, not a grey area**.

## 3. We transform, we do not reproduce

Independently of the licence grant, the packs minimise any copyright exposure by design:
chapters are **synthesised reference notes** (frameworks, definitions, decision rules in
our own structure and words), not transcriptions. Long verbatim passages are never
reproduced (it is both a quality rule and a licence-safety rule, enforced in
[PACK-SPEC.md](PACK-SPEC.md) and reviewed in CONTRIBUTING). What we publish is a
*transformative derivative*, exactly what the **Adapt** right covers for CC sources, and
a non-issue for public-domain sources.

## 4. Why not linking to the source is still squeaky-clean

The packs deliberately **do not hyperlink to the original source documents**. This does
not affect licence compliance:

- **Attribution is identification, not a download link.** The CC attribution requirement
  is satisfied by naming the creator, the copyright/licence notice, and indicating that
  changes were made. We do all of this in each pack's `LICENSE`, in the root `NOTICE`, and
  in `PACK.yaml` (title, publisher, version, licence, and a "reconstructed as reference
  notes" change indication). The CC term to provide a URI to the material applies only
  *"to the extent reasonably practicable"* and is met by **fully and unambiguously
  identifying a well-known public work** (exact title, version, publisher); a reader can
  locate it trivially. A clickable download link is not required by the licence.
- **The licence deed is still linked.** Where a licence (e.g. CC) asks for a link to the
  licence, each pack `LICENSE` links the **licence deed** (creativecommons.org). That is
  the licence, not the source material, and it is retained.
- **Public-domain sources require no attribution at all**, so omitting a link to them
  raises no question whatsoever.

The result: full, licence-compliant attribution travels with every pack, while the docs
stay free of links to the source files themselves.

## 5. Conclusion

Every pack in this catalogue is **redistributable by construction**:

1. its source cleared Tier 1 or Tier 2 vetting (Excluded sources are never packaged);
2. the source licence expressly permits redistribution and derivative works (or is public
   domain);
3. the content is transformative, not a reproduction;
4. all attribution, non-commercial, and share-alike obligations are carried forward in the
   pack `LICENSE`, the root `NOTICE`, and `PACK.yaml`.

This is why the catalogue can be installed, shared, and published without a copyright or
licence breach, with or without links to the source material.

> This document is an engineering/compliance rationale, not legal advice. Where a specific
> downstream use (e.g. commercial use of an NC pack) is contemplated, consult the named
> source licence directly.
