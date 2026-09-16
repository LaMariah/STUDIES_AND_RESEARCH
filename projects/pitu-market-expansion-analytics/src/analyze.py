"""Validate the reconstructed Pitu market-expansion portfolio metrics."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def roi_value(rows: list[dict[str, str]], label: str) -> float:
    return float(next(row["value"] for row in rows if row["input"] == label))


def main() -> None:
    summary = read_csv("campaign_summary.csv")
    audience = read_csv("audience_test.csv")
    growth = read_csv("distributor_growth.csv")
    roi = read_csv("roi_inputs.csv")

    start_accounts = int(growth[0]["active_distributor_accounts"])
    end_accounts = int(growth[-1]["active_distributor_accounts"])
    net_new_accounts = end_accounts - start_accounts
    distributor_growth_pct = net_new_accounts / start_accounts * 100

    education_rate = float(audience[0]["engagement_rate_pct"])
    comparison_rate = float(audience[1]["engagement_rate_pct"])
    engagement_ratio = education_rate / comparison_rate
    engagement_uplift_pct = (education_rate - comparison_rate) / comparison_rate * 100

    monthly_spend = roi_value(roi, "Monthly campaign investment")
    duration = roi_value(roi, "Campaign duration")
    total_spend = roi_value(roi, "Total campaign investment")
    revenue = roi_value(roi, "Estimated discounted three-year revenue")
    estimated_roi_pct = (revenue - total_spend) / total_spend * 100

    assert monthly_spend * duration == total_spend
    assert net_new_accounts == int(roi_value(roi, "Net new distributor accounts"))
    assert round(distributor_growth_pct, 1) == 266.7
    assert education_rate > comparison_rate
    assert round(estimated_roi_pct, 1) == 58.3
    assert len(summary) == 6

    print("Pitu market-expansion portfolio analysis")
    print(f"Distributor accounts: {start_accounts} to {end_accounts}")
    print(f"Distributor growth: {distributor_growth_pct:.1f}%")
    print(f"Education-led engagement ratio: {engagement_ratio:.2f}x")
    print(f"Relative engagement uplift: {engagement_uplift_pct:.1f}%")
    print(f"Total campaign investment: ${total_spend:,.0f}")
    print(f"Estimated three-year revenue: ${revenue:,.0f}")
    print(f"Estimated three-year ROI: {estimated_roi_pct:.1f}%")


if __name__ == "__main__":
    main()
