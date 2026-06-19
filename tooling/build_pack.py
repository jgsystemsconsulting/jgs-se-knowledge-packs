#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
build_pack.py — scaffold a new knowledge pack and record its provenance.

This is the *orchestration entry point* for the build method documented in the
README ("How a pack is built"). It does the deterministic, mechanical parts:

  1. Verifies the source has been vetted (you pass the licence + tier explicitly,
     which forces you to have read docs/SOURCE-VETTING.md first).
  2. Creates packs/<slug>/ with chapters/ and a pre-filled PACK.yaml + LICENSE stub.
  3. Prints the next manual steps (extraction + agent generation).

The *content generation* steps (text extraction, chapter-offset mapping, and the
per-chapter reference-depth synthesis) are performed by an agent following
docs/PACK-SPEC.md, using the MIT-licensed book-to-skill engine for extraction:
    https://github.com/virgiliojr94/book-to-skill

Why this split: licence vetting and provenance must be deterministic and auditable;
the synthesis is a judgement task best done by an agent reading the source slices.
This script guarantees no pack is created without a tier and licence on record.

Usage:
    python tooling/build_pack.py \
        --slug nasa-se-handbook \
        --title "NASA Systems Engineering Handbook (SP-2016-6105 Rev 2)" \
        --publisher "NASA" \
        --version "Rev 2 (2016)" \
        --license "Public Domain (US Government work)" \
        --tier 1 \
        --commercial-use true
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VALID_TIERS = {"1", "2", "3"}

PACK_YAML_TEMPLATE = """\
slug: {slug}
title: "{title}"
publisher: "{publisher}"
source_version: "{version}"
license: "{license}"
license_tier: {tier}
commercial_use: {commercial_use}
share_alike: {share_alike}
attribution_required: {attribution_required}
build:
  method: "book-to-skill extraction + offset-mapped parallel chapter generation"
  source_pages: 0
  chapters: 0
  built_on: "TODO"
notes: >
  TODO: record how the source licence's conditions (attribution / non-commercial /
  share-alike / trademark) are carried forward into this pack.
"""

LICENSE_STUB = """\
{slug} pack — content licence
{underline}

This pack is derived from:
    {title}
    {publisher}, {version}

Source licence: {license}  (tier {tier} — see ../../docs/SOURCE-VETTING.md)
No source-material download link is published (see ../../docs/LICENSING.md).

TODO: reproduce the source's full licence text / terms here. For public-domain
(US Government) works, state that and keep an attribution courtesy note. For CC or
OMG sources, reproduce the licence summary and the obligations carried forward.

NOTE: This licence governs the CONTENT of this pack and is independent of the
repository's MIT licence (which covers tooling only).
"""


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--publisher", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--license", required=True, help="exact source licence name")
    ap.add_argument("--tier", required=True, choices=sorted(VALID_TIERS),
                    help="1=public domain, 2=open licence, 3=caution (justify in PACK.yaml)")
    ap.add_argument("--commercial-use", default="false", choices=["true", "false"])
    ap.add_argument("--share-alike", default="false", choices=["true", "false"])
    ap.add_argument("--attribution-required", default="true", choices=["true", "false"])
    args = ap.parse_args(argv[1:])

    pack_dir = REPO_ROOT / "packs" / args.slug
    if pack_dir.exists():
        print(f"ERROR: packs/{args.slug} already exists.", file=sys.stderr)
        return 1

    (pack_dir / "chapters").mkdir(parents=True)

    (pack_dir / "PACK.yaml").write_text(PACK_YAML_TEMPLATE.format(
        slug=args.slug, title=args.title, publisher=args.publisher, version=args.version,
        license=args.license, tier=args.tier,
        commercial_use=args.commercial_use, share_alike=args.share_alike,
        attribution_required=args.attribution_required,
    ), encoding="utf-8")

    (pack_dir / "LICENSE").write_text(LICENSE_STUB.format(
        slug=args.slug, underline="=" * (len(args.slug) + 24), title=args.title,
        publisher=args.publisher, version=args.version,
        license=args.license, tier=args.tier,
    ), encoding="utf-8")

    print(f"Created packs/{args.slug}/ with PACK.yaml + LICENSE stub and chapters/.")
    print("\nNext (manual / agent-driven — see docs/PACK-SPEC.md):")
    print("  1. Extract source text with book-to-skill.")
    print("  2. Map structure to chapter offsets.")
    print("  3. Generate chapters/chNN-*.md (reference depth), glossary/patterns/cheatsheet.")
    print("  4. Write SKILL.md (index + core frameworks).")
    print("  5. Fill the TODOs in PACK.yaml + LICENSE.")
    print(f"  6. Validate:  python tooling/validate_pack.py packs/{args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
