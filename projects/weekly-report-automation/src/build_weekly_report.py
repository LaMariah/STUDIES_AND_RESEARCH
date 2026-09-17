"""Build a review-ready Nonprofit weekly report from a CSV export."""

from __future__ import annotations

import argparse
import csv
import hashlib
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path


REQUIRED_FIELDS = {
    "activity_id",
    "week",
    "week_of",
    "work_done",
    "hours_spent",
    "improvements_made",
    "ideas_opportunities",
    "possible_outcomes",
    "status",
    "data_status",
}


@dataclass(frozen=True)
class Activity:
    activity_id: str
    week: str
    week_of: date
    work_done: str
    hours_spent: float
    improvements_made: str
    ideas_opportunities: str
    possible_outcomes: str
    status: str
    data_status: str


def load_activities(path: Path) -> list[Activity]:
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        missing = REQUIRED_FIELDS.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(sorted(missing))}")

        activities: list[Activity] = []
        seen_ids: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            activity_id = row["activity_id"].strip()
            if activity_id in seen_ids:
                raise ValueError(f"Duplicate activity_id on line {line_number}: {activity_id}")
            seen_ids.add(activity_id)
            try:
                activity_date = datetime.strptime(row["week_of"], "%Y-%m-%d").date()
                hours = float(row["hours_spent"])
            except ValueError as error:
                raise ValueError(f"Invalid date or hours on line {line_number}") from error
            if hours < 0:
                raise ValueError(f"Hours cannot be negative on line {line_number}")
            activities.append(
                Activity(
                    activity_id=activity_id,
                    week=row["week"].strip(),
                    week_of=activity_date,
                    work_done=row["work_done"].strip(),
                    hours_spent=hours,
                    improvements_made=row["improvements_made"].strip(),
                    ideas_opportunities=row["ideas_opportunities"].strip(),
                    possible_outcomes=row["possible_outcomes"].strip(),
                    status=row["status"].strip(),
                    data_status=row["data_status"].strip(),
                )
            )
    return activities


def select_reporting_window(activities: list[Activity], reference_date: date) -> list[Activity]:
    start_date = reference_date - timedelta(days=4)
    return [activity for activity in activities if start_date <= activity.week_of <= reference_date]


def build_report(activities: list[Activity], reference_date: date) -> str:
    run_source = reference_date.isoformat() + "|" + "|".join(
        activity.activity_id for activity in activities
    )
    run_id = hashlib.sha256(run_source.encode()).hexdigest()[:12]
    total_hours = sum(activity.hours_spent for activity in activities)
    needs_review = [activity for activity in activities if activity.status == "Needs Review"]

    lines = [
        "# Nonprofit weekly activity report",
        "",
        f"Reporting date: {reference_date.isoformat()}",
        f"Run ID: `{run_id}`",
        f"Records: {len(activities)}",
        f"Hours logged: {total_hours:.1f}",
        f"Items needing review: {len(needs_review)}",
        "",
    ]
    if needs_review:
        lines.extend([
            "> Review required before forwarding this report.",
            "",
        ])
    if not activities:
        lines.extend(["No activities were recorded for this reporting window.", ""])
        return "\n".join(lines)

    for number, activity in enumerate(activities, start=1):
        lines.extend(
            [
                f"## {number}. {activity.work_done}",
                "",
                f"- Activity ID: `{activity.activity_id}`",
                f"- Date: {activity.week_of.isoformat()}",
                f"- Hours: {activity.hours_spent:.1f}",
                f"- Status: {activity.status}",
                f"- Improvement: {activity.improvements_made}",
                f"- Idea or opportunity: {activity.ideas_opportunities}",
                f"- Possible outcome: {activity.possible_outcomes}",
                "",
            ]
        )
    lines.extend(
        [
            "## Approval",
            "",
            "- [ ] Reviewed by workflow owner",
            "- [ ] Sensitive information removed",
            "- [ ] Approved for forwarding",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--reference-date", type=date.fromisoformat, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    activities = load_activities(args.input)
    selected = select_reporting_window(activities, args.reference_date)
    report = build_report(selected, args.reference_date)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Created {args.output} with {len(selected)} records")


if __name__ == "__main__":
    main()
