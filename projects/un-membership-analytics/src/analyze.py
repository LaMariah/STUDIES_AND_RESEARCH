"""Validate and summarize the reconstructed UN Latin Club portfolio data."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def main() -> None:
    segments = read_csv("membership_segments.csv")
    funnel = read_csv("reactivation_funnel.csv")
    content = read_csv("content_performance.csv")
    weekly = read_csv("weekly_engagement.csv")

    total_members = sum(int(row["members"]) for row in segments)
    total_share = sum(float(row["share_pct"]) for row in segments)
    assert total_members == 500, "Membership records must total 500"
    assert total_share == 100, "Segment shares must total 100%"

    funnel_counts = [int(row["members"]) for row in funnel]
    assert all(
        earlier >= later for earlier, later in zip(funnel_counts, funnel_counts[1:])
    ), "Funnel counts must be non-increasing"

    lapsed = next(
        int(row["members"]) for row in segments if row["segment"] == "Lapsed"
    )
    active = next(
        int(row["members"]) for row in segments if row["segment"] == "Active"
    )
    renewed = next(
        int(row["members"]) for row in funnel if row["stage"] == "Renewed"
    )
    reactivation_rate = renewed / lapsed * 100
    active_base_growth = renewed / active * 100

    best_content = min(content, key=lambda row: int(row["rank"]))
    final_engagement_change = float(weekly[-1]["cumulative_change_pct"])
    assert final_engagement_change == 15.0

    print("UN Latin Club portfolio analysis")
    print(f"Membership records: {total_members}")
    print(f"Lapsed members: {lapsed} ({lapsed / total_members:.1%})")
    print(f"Renewed members: {renewed}")
    print(f"Reactivation rate: {reactivation_rate:.1f}% of lapsed members")
    print(f"Active-base increase: {active_base_growth:.1f}% versus starting active base")
    print(f"Top content theme: {best_content['content_theme']}")
    print(f"Seven-week engagement change: {final_engagement_change:.1f}%")


if __name__ == "__main__":
    main()
