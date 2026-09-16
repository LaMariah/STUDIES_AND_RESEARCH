# Data dictionary

## membership_segments.csv

| Field | Type | Definition |
| --- | --- | --- |
| segment | Text | Membership lifecycle category |
| members | Integer | Number of records in the segment |
| share_pct | Number | Segment share of all reconstructed membership records |
| priority | Text | Recommended lifecycle action |
| rationale | Text | Reason for the recommended action |

## reactivation_funnel.csv

| Field | Type | Definition |
| --- | --- | --- |
| stage | Text | Step in the reactivation journey |
| members | Integer | People reaching the stage |
| share_of_contacted_pct | Number | Stage count divided by 235 contacted lapsed members |

## content_performance.csv

| Field | Type | Definition |
| --- | --- | --- |
| content_theme | Text | Editorial category |
| engagement_index | Integer | Reconstructed normalized measure used for category comparison |
| rank | Integer | Performance order, with 1 as the best result |

## weekly_engagement.csv

| Field | Type | Definition |
| --- | --- | --- |
| week | Integer | Reporting week |
| cumulative_change_pct | Number | Reconstructed cumulative change from the starting engagement baseline |
