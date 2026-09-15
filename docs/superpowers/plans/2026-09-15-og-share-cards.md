# OG Share Cards (P9) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a self-hosted 1200x630 OG/share card under `docs/assets/`, wire absolute first-party `og:image` / `twitter:image` / `summary_large_image` on `docs/index.html` and `tooling/gen_packs_page.py`, regenerate `docs/packs.html`, and keep the html-assets / CI / release gates green.

**Architecture:** One default PNG card (dark drafting brand) is enough for both public pages. Meta URLs use the existing first-party GH Pages base already present as `og:url` / `PAGES`. Packs page stays generated (RR-B-00). P12 `[html-assets]` already classifies image meta; no new scanner.

**Tech Stack:** Python 3, Pillow if available for the one-shot PNG, plain HTML meta, existing `gen_packs_page.py`. No CDN. No new runtime dependency in repo tooling (Pillow is local generation only; the PNG bytes are committed).

**Spec:** docs/superpowers/specs/2026-09-15-og-share-cards.md

**Research:** research: skipped (in-repo static OG card and meta wiring; no external API)

## Global Constraints

- No CDN. Self-hosted assets under `docs/assets/` only.
- Absolute OG/Twitter image URLs:
  `https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/assets/og-default.png`
- Dark drafting brand: ink `#0a0a0b`, paper `#f4f2ec`, mono drafting aesthetic, `§` mark, title "JGS SE Knowledge Packs".
- Do not hand-edit `docs/packs.html` body; regenerate with `python tooling/gen_packs_page.py`.
- Preserve `/* BRAND-TOKENS:BEGIN` / `/* BRAND-TOKENS:END` markers in `docs/index.html`.
- Gates must pass: `test_html_assets.py`, `test_ci_gate.py`, `check_release.py`.
- Em-dash-free durable prose (RR-B-28).

## Codebase context

- `docs/index.html` head already has `og:type|title|description|url` and `twitter:card=summary`.
- `tooling/gen_packs_page.py` defines `PAGES = "https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs"` and mirrors the head block.
- P12 `scan_html_external_assets` allowlists exact hosts `github.com` and `jgsystemsconsulting.github.io` for `og:image` / `twitter:image`.
- `docs/assets/` may not exist yet; create it with the PNG.

---

### Task 1: Create branded OG card assets

**Files:**
- Create: `docs/assets/og-default.png` (required, 1200x630)
- Create (optional): `docs/assets/og-default.svg`

**Model:** standard

- [ ] **Step 1: Ensure `docs/assets/` exists**

```bash
mkdir -p docs/assets
```

- [ ] **Step 2: Generate PNG**

Use Pillow (or equivalent one-shot) to paint ink ground, drafting frame, paper spine, large `§`, title "JGS SE Knowledge Packs", subtitle about licence-vetted SE skills, footer path strip. Save RGB PNG 1200x630 to `docs/assets/og-default.png`.

- [ ] **Step 3: Verify dimensions**

```bash
python -c "from PIL import Image; im=Image.open('docs/assets/og-default.png'); assert im.size==(1200,630), im.size; print('ok', im.size)"
```

---

### Task 2: Wire meta on index and generator; regenerate packs.html

**Files:**
- Modify: `docs/index.html` (head only)
- Modify: `tooling/gen_packs_page.py` (head template only)
- Regenerate: `docs/packs.html`

**Model:** flash

- [ ] **Step 1: Edit index.html head**

After `og:url`, add:

```html
<meta property="og:image" content="https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/assets/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

Change `twitter:card` to `summary_large_image` and add matching `twitter:image`.

- [ ] **Step 2: Edit gen_packs_page.py template head**

Same tags using `{PAGES}/assets/og-default.png`.

- [ ] **Step 3: Regenerate**

```bash
python tooling/gen_packs_page.py
```

- [ ] **Step 4: Confirm markers intact**

```bash
rg -n "BRAND-TOKENS" docs/index.html
```

---

### Task 3: Gates

**Model:** standard

- [ ] **Step 1: Run probes and release gate**

```bash
python tooling/test_html_assets.py
python tooling/test_ci_gate.py
python tooling/check_release.py
```

All must exit 0.

---

### Task 4: Superpowers closeout artifacts

**Files:**
- Create: EXECUTED, ARL triage, FCL triage, IVL triage logs under `docs/superpowers/plans/`
- Update: packages ledger P9 status to done when work lands

**Model:** flash

- [ ] Write EXECUTED (`done`)
- [ ] FCL triage Track 3 (no-world-claims)
- [ ] ARL triage Track 1 clean
- [ ] IVL triage Track 1 or 3 clean after gate run

## Commit plan

Prefer two commits if helpful:

1. `feat(docs): add self-hosted OG share card asset`
2. `feat(docs): wire og:image and summary_large_image on public pages`

Or one combined commit if the diff is small:

- `feat(docs): self-hosted OG share cards (P9)`
