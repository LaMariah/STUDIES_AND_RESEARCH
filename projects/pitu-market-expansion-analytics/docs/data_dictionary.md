# Data dictionary

## campaign_summary.csv

| Field | Type | Definition |
| --- | --- | --- |
| metric | Text | Business measure tracked in the case study |
| baseline | Number | Reconstructed starting value |
| outcome | Number | Reconstructed campaign outcome |
| unit | Text | Unit of measurement |
| status | Text | Evidence classification for the value |

## audience_test.csv

| Field | Type | Definition |
| --- | --- | --- |
| content_approach | Text | Education-led or brand-led campaign approach |
| audience_share_pct | Number | Reconstructed share assigned to the approach |
| language | Text | Primary campaign language |
| primary_message | Text | Main communication idea |
| engagement_rate_pct | Number | Reconstructed engagement rate |
| interpretation | Text | Directional reading of the result |

## distributor_growth.csv

| Field | Type | Definition |
| --- | --- | --- |
| period | Text | Campaign milestone |
| active_distributor_accounts | Integer | Active account count at the milestone |
| retail_locations_estimate | Integer | Estimated stores stocking the product |

## roi_inputs.csv

| Field | Type | Definition |
| --- | --- | --- |
| input | Text | ROI variable |
| value | Number | Numeric input |
| unit | Text | Currency, time, or account unit |
| classification | Text | Reported, calculated, assumed, or estimated value |
