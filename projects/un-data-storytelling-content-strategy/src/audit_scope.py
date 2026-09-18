"""Audit the stated project hours against the detailed workstream plan."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


STATED_TOTAL_HOURS = 120


@dataclass(frozen=True)
class ScopeAudit:
    workstream_count: int
    allocated_hours: int
    stated_hours: int

    @property
    def difference(self) -> int:
        return self.stated_hours - self.allocated_hours

    @property
    def reconciled(self) -> bool:
        return self.difference == 0


def audit_scope(path: Path) -> ScopeAudit:
    with path.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))

    if not rows:
        raise ValueError("Scope file contains no workstreams")

    allocated_hours = 0
    for line_number, row in enumerate(rows, start=2):
        workstream = (row.get("workstream") or "").strip()
        if not workstream:
            raise ValueError(f"Missing workstream on line {line_number}")
        try:
            hours = int(row["planned_hours"])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"Invalid planned hours on line {line_number}") from error
        if hours < 0:
            raise ValueError(f"Negative planned hours on line {line_number}")
        allocated_hours += hours

    return ScopeAudit(
        workstream_count=len(rows),
        allocated_hours=allocated_hours,
        stated_hours=STATED_TOTAL_HOURS,
    )


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    result = audit_scope(project_root / "data" / "scope_workstreams.csv")
    print(f"Workstreams: {result.workstream_count}")
    print(f"Detailed allocation: {result.allocated_hours} hours")
    print(f"Stated project total: {result.stated_hours} hours")
    print(f"Unallocated difference: {result.difference} hours")
    print(f"Reconciled: {result.reconciled}")


if __name__ == "__main__":
    main()
