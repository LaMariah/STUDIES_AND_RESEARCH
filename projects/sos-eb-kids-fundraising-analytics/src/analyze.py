"""Validate the illustrative SOS EB Kids donor-funnel dataset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def main() -> None:
    funnel = read_csv("illustrative_donor_funnel.csv")
    pipeline = read_csv("institutional_funding_pipeline.csv")
    evidence = read_csv("verified_project_evidence.csv")

    counts = [int(row["illustrative_count"]) for row in funnel]
    assert all(row["data_status"] == "illustrative" for row in funnel)
    assert all(
        earlier >= later for earlier, later in zip(counts, counts[1:])
    ), "Funnel counts must not increase"

    completed = counts[-1]
    awareness = counts[0]
    donation_starts = counts[-2]
    visitor_to_donor_pct = completed / awareness * 100
    completion_pct = completed / donation_starts * 100

    funding_rows = [
        row for row in pipeline if row["stage"] == "Funding secured"
    ]
    assert len(funding_rows) == 1
    assert funding_rows[0]["data_status"] == "verified outcome without amount"
    assert len(evidence) == 5

    print("SOS EB Kids fundraising portfolio analysis")
    print("Dataset status: illustrative, not organizational performance")
    print(f"Illustrative awareness visitors: {awareness:,}")
    print(f"Illustrative completed donations: {completed}")
    print(f"Illustrative visitor-to-donor rate: {visitor_to_donor_pct:.1f}%")
    print(f"Illustrative donation completion rate: {completion_pct:.1f}%")
    print(f"Institutional funding stages: {len(pipeline)}")
    print(f"Evidence records: {len(evidence)}")


if __name__ == "__main__":
    main()
