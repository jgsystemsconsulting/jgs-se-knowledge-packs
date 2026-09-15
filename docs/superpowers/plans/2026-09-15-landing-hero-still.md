# Landing Hero Still (P10) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one primary self-hosted hero brand still on `docs/index.html` only (dark drafting taste, alt text, reduced-motion safe, minimal inline CSS), keep OG meta and packs body untouched, preserve BRAND-TOKENS markers, and leave html-assets / CI / release gates green.

**Architecture:** Commit a wide brand still under `docs/assets/` matching the P9 OG drafting language. Wire a two-column hero (copy + figure) with a narrow-viewport stack. Relative image path only. No generator or packs.html body change.

**Tech Stack:** Python 3 + Pillow for one-shot PNG, optional SVG companion, plain HTML/CSS in `docs/index.html`. No CDN. No new runtime dependency.

**Spec:** docs/superpowers/specs/2026-09-15-landing-hero-still.md

**Research:** research: skipped (in-repo static hero still and HTML wire-up; no external API)

## Global Constraints

- No CDN. Self-hosted assets under `docs/assets/` only.
- Dark drafting brand: ink `#0a0a0b`, paper `#f4f2ec`, mono drafting aesthetic, `§` mark.
- Index only. No OG meta changes (P9 done). No packs.html body redesign.
- Preserve `/* BRAND-TOKENS:BEGIN` / `/* BRAND-TOKENS:END` markers.
- Gates must pass: `test_html_assets.py`, `test_ci_gate.py`, `check_release.py`.
- Em-dash-free durable prose (RR-B-28).

## Codebase context

- `docs/index.html` hero is text + CTA only today.
- P9 landed `docs/assets/og-default.png` (+ SVG) and OG meta.
- P12 allowlists relative `assets/` paths; absolute first-party hosts only for OG meta.
- Existing `@media (prefers-reduced-motion:reduce)` zeros transitions/animations.

---

### Task 1: Create branded hero still assets

**Files:**
- Create: `docs/assets/hero-still.png` (required)
- Create (optional): `docs/assets/hero-still.svg`

**Model:** standard

- [ ] **Step 1: Ensure `docs/assets/` exists**

```bash
mkdir -p docs/assets
```

- [ ] **Step 2: Generate PNG**

Use Pillow to paint ink ground, drafting frame, paper spine, large `§`, title
"SE Knowledge Packs", subtitle, labelled sheet callout, footer path strip. Save RGB PNG
(e.g. 1600x720) to `docs/assets/hero-still.png`.

- [ ] **Step 3: Optional SVG companion**

Mirror composition in `docs/assets/hero-still.svg` for editability. Page `<img>` uses PNG.

- [ ] **Step 4: Verify file exists**

```bash
python -c "from PIL import Image; im=Image.open('docs/assets/hero-still.png'); print(im.size, im.mode)"
```

---

### Task 2: Wire hero figure on index.html only

**Files:**
- Modify: `docs/index.html` (hero CSS + hero markup only)

**Model:** flash

- [ ] **Step 1: Add minimal hero media CSS** outside BRAND-TOKENS markers: grid layout,
  figure border, responsive image, stack at 860px. Keep reduce-motion rule.

- [ ] **Step 2: Add figure markup** with relative `src="assets/hero-still.png"`, width/height,
  descriptive alt, `decoding="async"`.

- [ ] **Step 3: Confirm constraints**

```bash
rg -n "BRAND-TOKENS|og:image|hero-still|prefers-reduced-motion" docs/index.html
```

OG meta unchanged. Markers intact. packs.html untouched.

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
- Spec already under `docs/superpowers/specs/`
- Update: packages ledger P10 status to done when work lands

**Model:** flash

- [ ] Write EXECUTED (`done`)
- [ ] FCL triage Track 3 (no-world-claims)
- [ ] ARL triage Track 1 clean
- [ ] IVL triage Track 1 or 3 clean after gate run
- [ ] Mark P10 done in packages doc

## Commit plan

Prefer two commits if helpful:

1. `feat(docs): add self-hosted landing hero still asset`
2. `feat(docs): wire hero still on index landing (P10)`

Or one combined commit if the diff is small:

- `feat(docs): self-hosted landing hero still (P10)`

Closeout:

- `docs(superpowers): close P10 landing-hero-still track`
