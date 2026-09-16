# Methodology

## Scope

This case study recreates an analytics workflow completed during a 2024 internship. The public version uses aggregate figures from the portfolio dashboard. It excludes member names, contact information, internal reports, and raw institutional data.

## Segmentation logic

Membership records were assigned to one of three mutually exclusive lifecycle groups:

- Active: renewed within the analysis period
- Lapsed: previously active and no longer renewed
- Never renewed: joined once without a later renewal

The lapsed group became the primary audience because prior participation signals awareness and interest.

## Funnel logic

The funnel uses the contacted lapsed population as its denominator.

| Stage | Formula |
| --- | --- |
| Open rate | Opened divided by email sent |
| Attendance rate | Attended event divided by email sent |
| Reactivation rate | Renewed divided by lapsed base |

Each rate answers a different question. Mixing denominators would create misleading comparisons.

## Content comparison

Content themes use a reconstructed engagement index. The index supports relative comparison inside this case study. It should not be compared with metrics from another platform or organization unless both use the same definition.

## Quality checks

- Membership segment counts must sum to 500.
- Segment percentages must sum to 100%.
- Funnel counts must never increase after the contacted stage.
- The renewal count must not exceed the event attendance count.
- Weekly cumulative engagement must end at 15%.

## Limitations

- The dataset is reconstructed and does not support causal claims.
- The funnel does not include a randomized control group.
- The engagement index does not expose platform-level weighting.
- External factors such as event timing and seasonality are unavailable.

## Recommended next analysis

1. Track renewal by invitation channel and event type.
2. Compare personalized and general email subject lines.
3. Measure 30-day and 90-day retention after reactivation.
4. Calculate cost per reactivated member.
5. Record consent and lawful-use fields beside each contact record.
