import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


class TestBaseline(unittest.TestCase):
    def test_no_change_is_clean(self):
        base = {"slug": "s", "expected": {"a": "PASS", "b": "PASS"}}
        cur = {"a": "PASS", "b": "PASS"}
        self.assertEqual(ev.baseline_diff(base, cur), {"regressions": [], "fixed": [], "new": []})

    def test_regression_detected(self):
        base = {"slug": "s", "expected": {"a": "PASS"}}
        cur = {"a": "FAIL"}
        self.assertEqual(ev.baseline_diff(base, cur)["regressions"], ["a"])

    def test_fixed_detected(self):
        base = {"slug": "s", "expected": {"a": "FAIL"}}
        cur = {"a": "PASS"}
        self.assertEqual(ev.baseline_diff(base, cur)["fixed"], ["a"])

    def test_new_question_not_in_baseline_is_flagged_new(self):
        base = {"slug": "s", "expected": {"a": "PASS"}}
        cur = {"a": "PASS", "z": "PASS"}
        self.assertEqual(ev.baseline_diff(base, cur)["new"], ["z"])

    def test_gate_fails_on_regression(self):
        base = {"slug": "s", "expected": {"a": "PASS"}}
        self.assertFalse(ev.baseline_gate_ok(ev.baseline_diff(base, {"a": "FAIL"})))

    def test_gate_ok_when_only_fixed_or_new(self):
        base = {"slug": "s", "expected": {"a": "FAIL"}}
        self.assertTrue(ev.baseline_gate_ok(ev.baseline_diff(base, {"a": "PASS", "z": "PASS"})))
