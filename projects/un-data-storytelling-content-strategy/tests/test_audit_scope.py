import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from audit_scope import audit_scope  # noqa: E402


class ScopeAuditTests(unittest.TestCase):
    def test_documented_scope_flags_ten_unallocated_hours(self) -> None:
        result = audit_scope(PROJECT_ROOT / "data" / "scope_workstreams.csv")
        self.assertEqual(result.workstream_count, 6)
        self.assertEqual(result.allocated_hours, 110)
        self.assertEqual(result.difference, 10)
        self.assertFalse(result.reconciled)

    def test_invalid_hours_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.csv"
            sample.write_text("workstream,planned_hours\nResearch,unknown\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Invalid planned hours"):
                audit_scope(sample)


if __name__ == "__main__":
    unittest.main()
