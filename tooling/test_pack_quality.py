#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for the pack-quality gate (no framework).

Run:  python tooling/test_pack_quality.py
Exits 0 when the demo matrix (orphan, depth floor, topic resolution,
en-dash range expansion, clean pack, kind skip) and the real-tree clean
state all hold. Any failed assert raises and exits nonzero.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_pack_quality  # noqa: E402


def _pack(
    root: Path,
    slug: str,
    body: str,
    chapters: dict[str, int],
    kind: str | None = None,
) -> Path:
    """Write a mini pack: SKILL.md plus chapters sized in lines."""
    kind_line = f"kind: {kind}\n" if kind else ""
    d = root / slug
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(
        f"---\nname: {slug}\n{kind_line}description: x\n---\n# {slug}\n{body}",
        encoding="utf-8",
    )
    for name, lines in chapters.items():
        ch = d / "chapters" / name
        ch.parent.mkdir(parents=True, exist_ok=True)
        ch.write_text("line\n" * lines, encoding="utf-8")
    return d


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        packs = Path(td)

        # 1. orphan negative: chapter on disk, basename nowhere in SKILL.md;
        #    the ch01 token resolves via glob so only the orphan check fires
        p = _pack(
            packs,
            "orphan",
            "\n## Topic Index\n\n- **Intro** \u2192 ch01\n",
            {"ch01-intro.md": 30},
        )
        errs = check_pack_quality.check_pack(p)
        assert errs, errs
        assert all("[orphan-chapter]" in e for e in errs), errs

        # 2. depth negative: linked 25-line chapter, only the floor fires
        p = _pack(
            packs,
            "thin",
            "Read chapters/ch01-thin.md first.\n\n## Topic Index\n\n- **Thin** \u2192 ch01\n",
            {"ch01-thin.md": 25},
        )
        errs = check_pack_quality.check_pack(p)
        assert len(errs) == 1, errs
        assert "[chapter-depth]" in errs[0] and "25" in errs[0], errs

        # 3. topic negative: index token with no chapter behind it
        p = _pack(
            packs,
            "ghost",
            "See chapters/ch01-intro.md.\n\n## Topic Index\n\n- **Ghost** \u2192 ch09\n",
            {"ch01-intro.md": 30},
        )
        errs = check_pack_quality.check_pack(p)
        assert len(errs) == 1, errs
        assert "[topic-index]" in errs[0] and "ch09" in errs[0], errs

        # 4. range positive: ch02\u2013ch04 must expand to all three chapters
        #    (a single-token parser would leave ch03 unresolvable and fail)
        p = _pack(
            packs,
            "span",
            (
                "See chapters/ch02-part.md, chapters/ch03-part.md, chapters/ch04-part.md.\n"
                "\n## Topic Index\n\n- **Span** \u2192 ch02\u2013ch04\n"
            ),
            {"ch02-part.md": 30, "ch03-part.md": 31, "ch04-part.md": 32},
        )
        assert check_pack_quality.check_pack(p) == []

        # 5. clean positive: full mini-pack
        p = _pack(
            packs,
            "clean",
            "Read chapters/ch01-intro.md.\n\n## Topic Index\n\n- **Intro** \u2192 ch01\n",
            {"ch01-intro.md": 30},
        )
        assert check_pack_quality.check_pack(p) == []

        # 6. kind skip: signpost frontmatter bypasses all three checks
        p = _pack(
            packs,
            "sign",
            "Read chapters/ch01-intro.md.\n\n## Topic Index\n\n- **Intro** \u2192 ch01\n",
            {"ch01-intro.md": 30},
            kind="signpost",
        )
        assert check_pack_quality.check_pack(p) == []
        # skip proof: break the tree under the kind line; still clean
        (p / "chapters" / "ch01-intro.md").unlink()
        assert check_pack_quality.check_pack(p) == []

        # 6b. mixed-case kind skip: same bypass, same broken-tree proof
        p = _pack(
            packs,
            "sign-mixed",
            "Read chapters/ch01-intro.md.\n\n## Topic Index\n\n- **Intro** \u2192 ch01\n",
            {"ch01-intro.md": 30},
            kind="Signpost",
        )
        assert check_pack_quality.check_pack(p) == []
        (p / "chapters" / "ch01-intro.md").unlink()
        assert check_pack_quality.check_pack(p) == []

        # 6c. mixed-case orchestrator skip; the signpost unlink above proves the skip
        p = _pack(
            packs,
            "orch-mixed",
            "Read chapters/ch01-intro.md.\n\n## Topic Index\n\n- **Intro** \u2192 ch01\n",
            {"ch01-intro.md": 30},
            kind="Orchestrator",
        )
        assert check_pack_quality.check_pack(p) == []

    # 7. real tree: every shipped pack passes and main() exits 0
    for p in sorted((ROOT / "packs").iterdir()):
        if p.is_dir():
            assert check_pack_quality.check_pack(p) == [], p
    assert check_pack_quality.main(["--all"]) == 0

    print("pack-quality probe: OK (demo matrix, real-tree clean)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
