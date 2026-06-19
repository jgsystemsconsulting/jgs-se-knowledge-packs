# Source Vetting

This is the integrity document for the repository. **No pack is accepted unless its
source clears this rubric.** The whole value of `jgs-se-knowledge-packs` is that every pack
is redistributable by construction, so a colleague can install it, and we can publish it,
without a copyright or licence breach.

The governing principle:

> **"Free to download" is not "free to redistribute."**

A document you can read for free on a website may still be all-rights-reserved. A
knowledge pack *reproduces and transforms* a source into new files that we then publish.
That is redistribution plus derivative work. It needs an actual grant.

---

## The eligibility tiers

A source must land in **Tier 1 or Tier 2** to be packaged. Tier 3 is case-by-case and
needs a written rationale in the pack's `PACK.yaml`. The Excluded tier is a hard stop.

### 🟢 Tier 1 — Public domain (maximum freedom)

Works with no copyright, or an explicit public-domain dedication. Reproduce, transform,
and redistribute freely. Attribution is courtesy, not obligation.

- **US Government works** — not subject to copyright in the US (17 U.S.C. § 105).
  Examples: NASA, NIST, US DoD, FAA publications.
- Look for a **Distribution Statement A** ("Approved for public release; distribution is
  unlimited") on defense documents, or a US-gov-authorship statement.
- CC0 / explicit public-domain dedication.

### 🟡 Tier 2 — Open licence (shareable with conditions)

A licence that grants redistribution and (ideally) derivative works. The pack **must
carry the source's conditions forward**: attribution, share-alike, non-commercial,
trademark limits.

- **Creative Commons** BY, BY-SA, BY-NC, BY-NC-SA. (NC and SA propagate to the pack —
  see "Carrying conditions forward" below.)
- **OMG specification licence** — grants copy, modify, and redistribute of modified
  versions, provided you reproduce the copyright notice, add a prominent modification
  notice, and do not use the trademarked spec name on the modified work.
- Permissive software/content licences (MIT, Apache-2.0, BSD) where they cover the text.

### 🟠 Tier 3 — Caution (verbatim-only or unclear grant)

Package only with an explicit written justification in `PACK.yaml` and, where the grant
is ambiguous, a note that the maintainers judged it defensible (or sought permission).

- **No-derivatives clauses** (e.g. CC BY-ND, or OMG specs with a "no modifications"
  condition such as UAF). A knowledge pack transforms the source, so a strict
  no-derivatives source is normally **not** packageable — at most a verbatim excerpt
  with heavy citation. Prefer to exclude.
- **"Freely available" with no stated licence.** Free download ≠ redistribution grant.
  Treat as Excluded until a real grant is found or permission is obtained.

### 🔴 Excluded — read-only, not redistributable (hard stop)

These are valuable and you may *read and cite* them, but you may **not** package them.
This list exists so the repo never ships something that triggers a takedown.

| Source | Why excluded |
|---|---|
| **ISO / IEC / IEEE standards** (e.g. 15288, 42010, 12207) | Paywalled, all-rights-reserved. Licensed per-user, often via BSI/Accuris/IHS. |
| **INCOSE SE Handbook** | Copyrighted (Wiley). Not redistributable. |
| **SWEBOK v4** (IEEE) | Free download, but licence says "may not alter the text in any way," individual & non-commercial only. |
| **MITRE SE Guide** | "© The MITRE Corporation. All rights reserved." |
| **The Open Group TOGAF / ArchiMate** | Evaluation/member licence; not redistributable. |
| **PMI PMBOK** | PMI copyright. |
| **INCOSE SE Vision 2035** | Freely downloadable but no stated redistribution/derivative grant (Tier 3 → treat as excluded pending permission). |

> If you are licensed to read one of these (e.g. an employer's BSI/Accuris seat for an
> ISO standard), that licence is **yours**, not the repo's. Building a pack from it for
> your own private use may be fine; **publishing that pack here is not.** Keep
> source-restricted packs in a private/local skills directory, never in this repo.

---

## Carrying conditions forward

When a source is Tier 2, the pack inherits its obligations:

- **Attribution (BY)** — `PACK.yaml` records title, author/publisher, version, URL; the
  pack `LICENSE` file reproduces the source notice.
- **Share-alike (SA)** — the pack's *content* is released under the same licence as the
  source (not the repo's MIT). State this in the pack `LICENSE`.
- **Non-commercial (NC)** — the pack is flagged `commercial_use: false` in `PACK.yaml`.
  The repo tooling (MIT) is separate from pack *content* licences.
- **Trademark / no-endorsement** — do not imply the source's authors endorse the pack;
  do not use a trademarked spec name on a transformed work (OMG rule).

The repository tooling and scaffolding are MIT. **Pack content licences are independent
and per-pack** — a pack folder always contains its own `LICENSE`.

---

## The vetting checklist (run before opening a pack PR)

1. [ ] Identified the exact source document, version, and publisher. (Read the source's
   own licence to vet it — the source URL is used for vetting only, never published.)
2. [ ] Found the **licence statement** in the source itself (not a third-party claim).
3. [ ] Assigned a tier (1 / 2 / 3) with the licence named.
4. [ ] Source is **not** on the Excluded list.
5. [ ] If Tier 2: NC / SA / BY / trademark conditions recorded in `PACK.yaml`.
6. [ ] If Tier 3: written justification present.
7. [ ] Pack folder contains a `LICENSE` reproducing the source's terms.
8. [ ] `PACK.yaml` `title`, `publisher`, `license`, `license_tier`, `commercial_use`
   filled — textual attribution, **no source-material URL published** (see LICENSING.md).

CI enforces 4, 7, and 8 mechanically (`tooling/validate_pack.py`). Tiers 1–3 judgement
is human and reviewed on the PR.

> **Link policy.** Source-material URLs are recorded during vetting but are **not**
> published anywhere in a pack or the docs. Attribution travels as text (title +
> publisher + version + licence) plus the licence-deed link — which the licences accept.
> See [LICENSING.md](LICENSING.md) §4.
