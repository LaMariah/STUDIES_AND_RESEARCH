-- Illustrative SQL for a privacy-conscious nonprofit fundraising system.

-- 1. Measure conversion between donor-journey stages.
WITH stage_counts AS (
    SELECT
        funnel_stage,
        stage_order,
        COUNT(DISTINCT anonymous_supporter_id) AS supporters
    FROM donor_events
    GROUP BY funnel_stage, stage_order
),
with_previous AS (
    SELECT
        funnel_stage,
        stage_order,
        supporters,
        LAG(supporters) OVER (ORDER BY stage_order) AS previous_supporters
    FROM stage_counts
)
SELECT
    funnel_stage,
    supporters,
    ROUND(100.0 * supporters / NULLIF(previous_supporters, 0), 1)
        AS previous_stage_conversion_pct
FROM with_previous
ORDER BY stage_order;

-- 2. Compare completed donations by acquisition channel.
SELECT
    acquisition_channel,
    COUNT(DISTINCT donor_id) AS donors,
    COUNT(*) AS completed_donations,
    SUM(donation_amount) AS donation_value,
    ROUND(AVG(donation_amount), 2) AS average_donation
FROM donations
WHERE donation_status = 'completed'
GROUP BY acquisition_channel
ORDER BY donation_value DESC;

-- 3. Measure donor retention without exposing identities.
WITH donor_years AS (
    SELECT
        donor_id,
        EXTRACT(YEAR FROM donation_date) AS donation_year
    FROM donations
    WHERE donation_status = 'completed'
    GROUP BY donor_id, EXTRACT(YEAR FROM donation_date)
)
SELECT
    current_year.donation_year,
    COUNT(DISTINCT current_year.donor_id) AS donors,
    COUNT(DISTINCT next_year.donor_id) AS retained_next_year,
    ROUND(
        100.0 * COUNT(DISTINCT next_year.donor_id)
        / NULLIF(COUNT(DISTINCT current_year.donor_id), 0),
        1
    ) AS next_year_retention_pct
FROM donor_years current_year
LEFT JOIN donor_years next_year
    ON current_year.donor_id = next_year.donor_id
    AND next_year.donation_year = current_year.donation_year + 1
GROUP BY current_year.donation_year
ORDER BY current_year.donation_year;

-- 4. Review the institutional funding pipeline.
SELECT
    pipeline_stage,
    COUNT(*) AS opportunities,
    SUM(requested_amount) AS requested_value,
    AVG(CURRENT_DATE - stage_entered_date) AS average_days_in_stage
FROM funding_opportunities
GROUP BY pipeline_stage
ORDER BY MIN(stage_order);
