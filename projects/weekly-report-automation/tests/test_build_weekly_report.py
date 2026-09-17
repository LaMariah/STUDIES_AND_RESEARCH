"""Tests for the weekly activity report builder."""

from __future__ import annotations

import csv
import tempfile
import unittest
from datetime import date
from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from build_weekly_report import build_report, load_activities, select_reporting_window


class WeeklyReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_weekly_log.csv"

    def test_sample_data_is_synthetic(self) -> None:
        activities = load_activities(self.sample_path)
        self.assertTrue(all(item.data_status == "synthetic" for item in activities))

    def test_reporting_window_selects_four_records(self) -> None:
        activities = load_activities(self.sample_path)
        selected = select_reporting_window(activities, date(2026, 9, 11))
        self.assertEqual(len(selected), 4)

    def test_report_includes_review_warning_and_hours(self) -> None:
        activities = load_activities(self.sample_path)
        report = build_report(activities, date(2026, 9, 11))
        self.assertIn("Review required before forwarding", report)
        self.assertIn("Hours logged: 10.0", report)

    def test_duplicate_ids_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate_path = Path(directory) / "duplicate.csv"
            with self.sample_path.open(encoding="utf-8", newline="") as source:
                rows = list(csv.DictReader(source))
            fieldnames = list(rows[0])
            with duplicate_path.open("w", encoding="utf-8", newline="") as target:
                writer = csv.DictWriter(target, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(rows[0])
                writer.writerow(rows[0])
            with self.assertRaisesRegex(ValueError, "Duplicate activity_id"):
                load_activities(duplicate_path)


if __name__ == "__main__":
    unittest.main()
