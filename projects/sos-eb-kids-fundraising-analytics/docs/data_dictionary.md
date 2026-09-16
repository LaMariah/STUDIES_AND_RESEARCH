# Data dictionary

## illustrative_donor_funnel.csv

| Field | Type | Definition |
| --- | --- | --- |
| stage | Text | Donor-journey stage |
| illustrative_count | Integer | Synthetic count used for demonstration |
| previous_stage_conversion_pct | Number | Stage count divided by the prior-stage count |
| data_status | Text | Identifies the row as illustrative |

## institutional_funding_pipeline.csv

| Field | Type | Definition |
| --- | --- | --- |
| stage | Text | Institutional fundraising stage |
| measurement_definition | Text | Operational definition of the stage |
| recommended_kpi | Text | Metric recommended for future reporting |
| data_status | Text | Framework or verified-outcome classification |

## verified_project_evidence.csv

| Field | Type | Definition |
| --- | --- | --- |
| evidence | Text | Claim or project fact |
| source | Text | Public URL or professional experience statement |
| status | Text | Publicly documented or user-reported classification |
| portfolio_use | Text | Appropriate use in the case study |
