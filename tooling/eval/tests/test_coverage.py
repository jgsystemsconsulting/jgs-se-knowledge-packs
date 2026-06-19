import json
import subprocess
import sys
import unittest
from pathlib import Path

EVAL = Path(__file__).resolve().parent.parent / "eval.py"
ROOT = Path(__file__).resolve().parent.parent.parent.parent

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


class TestCli(unittest.TestCase):
    def test_validate_runs_and_reports_pass_on_a_good_bank(self):
        tmp = ROOT / "results" / "_t_bank.json"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps({"slug": "demo", "status": "complete", "questions": [
            {"id": "d-01", "type": "topic", "prompt": "p",
             "routing": {"any_of": ["ch01"], "all_of": []},
             "must_include": ["x"], "provenance": "s ch01"}]}), encoding="utf-8")
        r = subprocess.run([sys.executable, str(EVAL), "validate", str(tmp)],
                           capture_output=True, text=True)
        tmp.unlink()
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertIn("PASS", r.stdout)

    def test_validate_fails_on_bad_bank(self):
        tmp = ROOT / "results" / "_t_bad.json"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps({"status": "complete", "questions": []}), encoding="utf-8")
        r = subprocess.run([sys.executable, str(EVAL), "validate", str(tmp)],
                           capture_output=True, text=True)
        tmp.unlink()
        self.assertEqual(r.returncode, 1)


class TestCoverage(unittest.TestCase):
    def test_coverage_counts_seeded_vs_stub(self):
        manifest = {"packs": [
            {"slug": "nasa-risk", "status": "seeded"},
            {"slug": "sebok", "status": "stub"}]}
        summary = ev.coverage_summary(manifest)
        self.assertEqual(summary["seeded"], 1)
        self.assertEqual(summary["stub"], 1)
        self.assertEqual(summary["total"], 2)
        self.assertEqual(summary["suite"], "INCOMPLETE")

    def test_coverage_all_seeded_is_complete(self):
        manifest = {"packs": [{"slug": "a", "status": "seeded"}]}
        self.assertEqual(ev.coverage_summary(manifest)["suite"], "COMPLETE")


if __name__ == "__main__":
    unittest.main()
