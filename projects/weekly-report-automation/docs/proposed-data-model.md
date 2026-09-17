# Proposed data model

## Purpose

This document defines a normalized logical data model for a future database-backed version of the weekly reporting workflow.

The current public prototype reads synthetic records from a CSV file. No production database, organization data, personal data, credentials, or real communications appear in this repository.

## Design goals

- Keep activity records separate from report-generation history.
- Preserve the exact records included in each report run.
- Record validation failures without changing the source activity.
- Require a documented human decision before external delivery.
- Support audit metrics such as record counts, total hours, validation issues, and review status.
- Use stable identifiers to prevent duplicate processing.

## Entity definitions

| Entity | Purpose | Primary key |
| --- | --- | --- |
| `ACTIVITY_RECORD` | Stores one structured operational activity | `activity_id` |
| `REPORT_RUN` | Stores one report-generation event and its totals | `run_id` |
| `REPORT_RUN_ACTIVITY` | Preserves which activities were included in each report | `run_id` + `activity_id` |
| `VALIDATION_ISSUE` | Records missing, invalid, or review-sensitive data | `issue_id` |
| `REVIEW_DECISION` | Records the human approval outcome for a report run | `review_id` |

## Relationship rules

1. One activity record can appear in zero or more report runs.
2. One report run can include zero or more activity records.
3. The `REPORT_RUN_ACTIVITY` junction resolves this many-to-many relationship and supports safe reruns.
4. An activity record can produce zero or more validation issues.
5. A report run can record zero or more validation issues.
6. A report run requires a review decision before its status changes to approved for delivery.

## Key controls

| Control | Data-model support |
| --- | --- |
| Duplicate prevention | Unique `activity_id` and composite key on `REPORT_RUN_ACTIVITY` |
| Reporting-window traceability | `reference_date`, `window_start`, and `window_end` on `REPORT_RUN` |
| Reconciliation | `record_count` and `total_hours` stored with the run |
| Validation history | Separate `VALIDATION_ISSUE` records preserve errors and resolutions |
| Human approval | `REVIEW_DECISION` stores decision, role, time, and notes |
| Privacy | Public examples use synthetic records and role labels instead of personal identifiers |

## Current implementation mapping

| Logical entity | Public prototype equivalent |
| --- | --- |
| `ACTIVITY_RECORD` | Rows in `data/sample_weekly_log.csv` and the Python `Activity` model |
| `REPORT_RUN` | Generated run ID, reference date, record count, and total hours |
| `REPORT_RUN_ACTIVITY` | Activities selected by the reporting-window function |
| `VALIDATION_ISSUE` | Required-field, duplicate-ID, date, hours, and review-status checks |
| `REVIEW_DECISION` | Approval checklist in the generated Markdown report |

## Implementation boundary

The ERD describes the proposed logical structure. The repository does not claim that a relational database or production integration has been deployed. A production implementation would require approved access controls, encrypted secrets, retention rules, backups, and organization-owned infrastructure.
