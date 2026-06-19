import json
import subprocess
import sys
import unittest
from pathlib import Path

EVAL = Path(__file__).resolve().parent.parent / "eval.py"
ROOT = Path(__file__).resolve().parent.parent.parent.parent


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


if __name__ == "__main__":
    unittest.main()
