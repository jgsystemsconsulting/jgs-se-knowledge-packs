# Spec: OG share cards (P9)

- Date: 2026-09-15
- Package: P9, visual website cut
- Status: ready for implementation
- Owner: jgs-se-knowledge-packs maintainers

## Problem

Public pages ship text-only Open Graph and Twitter cards. `docs/index.html` and the
`tooling/gen_packs_page.py` head template carry `og:title`, `og:description`, and
`og:url`, but neither page has `og:image` or `twitter:image`. `twitter:card` is
`summary` rather than `summary_large_image`. There is no self-hosted image tree under
`docs/` for share previews (fonts and HTML only). Every external link preview is text
only, and an index-only meta fix drifts on the next `gen_packs_page.py` regen
(RR-B-00: do not hand-edit `docs/packs.html`).

## Evidence

- `docs/index.html` head: OG/Twitter meta without images; `twitter:card` = `summary`.
- `tooling/gen_packs_page.py` head template: same pattern; packs.html is generated.
- P12 `[html-assets]` already classifies `og:image` / `twitter:image` content and
  allowlists exact first-party hosts `github.com` and `jgsystemsconsulting.github.io`.
- Self-host convention from P12: images under `docs/assets/`, fonts under `docs/fonts/`,
  relative references for page body assets; absolute first-party HTTPS URLs are required
  for crawler-facing OG/Twitter image meta.
- Brand: dark drafting (ink `#0a0a0b`, paper `#f4f2ec`), section mark `§`, mono labels.

## Goal

Ship a self-hosted 1200x630 OG card under `docs/assets/`, wire absolute first-party
`og:image` + dimensions + `twitter:image` + `summary_large_image` on `docs/index.html`
and the packs generator template, regenerate `docs/packs.html`, and keep
`python tooling/check_release.py`, `tooling/test_html_assets.py`, and
`tooling/test_ci_gate.py` green.

## Non-goals

- Landing hero still (P10) and labelled body stills (P11).
- CDN or third-party image hosts.
- Hand-editing `docs/packs.html` body (RR-B-00).
- Visual-regression CI.
- Changing brand tokens (P13 already owns the marker contract); preserve
  `BRAND-TOKENS:BEGIN` / `END` markers.
- P8 ledger work.
- Product YAML or pack Markdown content.

## Requirements

1. `docs/assets/og-default.png` exists at 1200x630, dark drafting brand (ink ground,
   paper accent, `§` mark, title "JGS SE Knowledge Packs", short subtitle). Optional
   companion SVG may ship beside it; crawlers use the PNG.
2. Absolute image URL on both pages:
   `https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/assets/og-default.png`
3. Meta on `docs/index.html` and the `gen_packs_page.py` template head:
   - `og:image` (absolute URL above)
   - `og:image:width` = `1200`
   - `og:image:height` = `630`
   - `twitter:card` = `summary_large_image`
   - `twitter:image` (same absolute URL)
4. Regenerate `docs/packs.html` via `python tooling/gen_packs_page.py`; never hand-edit
   the generated body.
5. No CDN. Image host must stay on the first-party allowlist so `[html-assets]` stays clean.
6. Preserve brand-token markers in `docs/index.html`.
7. Gates pass: `python tooling/test_html_assets.py`, `python tooling/test_ci_gate.py`,
   `python tooling/check_release.py`.

## Design

### Asset

Create `docs/assets/` if missing. Produce `og-default.png` (1200x630 RGB) with a small
local generator using available tooling (Pillow if present; otherwise solid-frame PNG
via stdlib). Brand layout: ink background, thin drafting frame, paper left spine,
large `§`, title and subtitle in mono, footer strip with the public pages path and
PUBLIC / MIT labels. Optional `og-default.svg` mirrors the same composition for
source/editability; meta points at PNG only.

One default card is enough for index and packs (same product surface). A packs-only
variant is out of scope unless a later package needs distinct copy.

### Meta wiring

Edit `docs/index.html` head after existing `og:url`. Edit the f-string head in
`tooling/gen_packs_page.py` to use `{PAGES}/assets/og-default.png` so the absolute
base stays single-sourced with the existing `PAGES` constant. Run the generator.
Do not touch BRAND-TOKENS markers or body chrome beyond the head meta block.

### Gate posture

P12 already fails closed on non-allowlisted `og:image` / `twitter:image` hosts.
First-party absolute URLs are required and must scan clean. No new scanner code in
this package unless a gate regression appears.

## Acceptance criteria

1. `docs/assets/og-default.png` is tracked, 1200x630.
2. `docs/index.html` and `docs/packs.html` both carry `og:image`, `og:image:width`,
   `og:image:height`, `twitter:card=summary_large_image`, and `twitter:image` with the
   absolute first-party PNG URL.
3. `docs/packs.html` head matches a fresh `gen_packs_page.py` render (RR-B-30).
4. `python tooling/test_html_assets.py` exits 0.
5. `python tooling/test_ci_gate.py` exits 0.
6. `python tooling/check_release.py` exits 0 (PASS).
7. Brand-token markers still present and exclusive-slice intact in `docs/index.html`.
8. No CDN host appears in either page's asset scan.

## Risks

| Risk | Mitigation |
|------|------------|
| SVG-only OG image ignored by major crawlers | Ship PNG as the meta target; SVG optional companion only |
| Relative `og:image` breaks some crawlers | Absolute first-party HTTPS URL only |
| Hand-edit packs.html drifts | Always regenerate via `gen_packs_page.py` |
| Non-allowlisted host trips `[html-assets]` | URL host must be `jgsystemsconsulting.github.io` |
| Brand-token markers broken while editing head | Head-only edit; markers live in `<style>` |

## Research

research: skipped (in-repo static OG card and meta wiring; no external API or platform choice beyond the existing GH Pages host already used for `og:url`)
