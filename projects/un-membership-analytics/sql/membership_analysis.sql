-- Portfolio examples for a membership lifecycle dataset.
-- Table and field names are illustrative.

-- 1. Assign a lifecycle segment to each member.
SELECT
    member_id,
    CASE
        WHEN last_renewal_date >= CURRENT_DATE - INTERVAL '12 months' THEN 'Active'
        WHEN renewal_count > 1 THEN 'Lapsed'
        ELSE 'Never renewed'
    END AS lifecycle_segment
FROM membership_records;

-- 2. Summarize the membership base.
WITH segmented AS (
    SELECT
        member_id,
        CASE
            WHEN last_renewal_date >= CURRENT_DATE - INTERVAL '12 months' THEN 'Active'
            WHEN renewal_count > 1 THEN 'Lapsed'
            ELSE 'Never renewed'
        END AS lifecycle_segment
    FROM membership_records
)
SELECT
    lifecycle_segment,
    COUNT(*) AS members,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS share_pct
FROM segmented
GROUP BY lifecycle_segment
ORDER BY members DESC;

-- 3. Calculate reactivation conversion stages.
SELECT
    COUNT(*) FILTER (WHERE contacted_at IS NOT NULL) AS contacted,
    COUNT(*) FILTER (WHERE opened_at IS NOT NULL) AS opened,
    COUNT(*) FILTER (WHERE attended_at IS NOT NULL) AS attended,
    COUNT(*) FILTER (WHERE renewed_at IS NOT NULL) AS renewed,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE renewed_at IS NOT NULL)
        / NULLIF(COUNT(*) FILTER (WHERE contacted_at IS NOT NULL), 0),
        1
    ) AS reactivation_rate_pct
FROM reactivation_events
WHERE lifecycle_segment = 'Lapsed';

-- 4. Rank content themes with one consistent metric.
SELECT
    content_theme,
    SUM(saves + shares + comments) AS engagement_index,
    DENSE_RANK() OVER (
        ORDER BY SUM(saves + shares + comments) DESC
    ) AS performance_rank
FROM content_posts
GROUP BY content_theme
ORDER BY performance_rank;
