-- Illustrative SQL for a beverage market-entry campaign.

-- 1. Compare engagement by message approach.
SELECT
    content_approach,
    COUNT(DISTINCT post_id) AS posts,
    SUM(impressions) AS impressions,
    SUM(engagements) AS engagements,
    ROUND(100.0 * SUM(engagements) / NULLIF(SUM(impressions), 0), 2)
        AS engagement_rate_pct
FROM campaign_content
GROUP BY content_approach
ORDER BY engagement_rate_pct DESC;

-- 2. Track distributor account growth by quarter.
SELECT
    DATE_TRUNC('quarter', activation_date) AS quarter,
    COUNT(DISTINCT distributor_id) AS new_accounts,
    SUM(COUNT(DISTINCT distributor_id)) OVER (
        ORDER BY DATE_TRUNC('quarter', activation_date)
    ) AS cumulative_accounts
FROM distributor_accounts
WHERE market IN ('New York', 'New Jersey')
GROUP BY 1
ORDER BY 1;

-- 3. Measure retail reorder performance.
SELECT
    retailer_id,
    COUNT(DISTINCT order_id) AS orders,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS latest_order_date,
    CASE WHEN COUNT(DISTINCT order_id) > 1 THEN 1 ELSE 0 END AS reordered
FROM retail_orders
GROUP BY retailer_id;

-- 4. Compare account value with acquisition cost.
SELECT
    channel,
    SUM(campaign_cost) AS acquisition_cost,
    COUNT(DISTINCT new_account_id) AS new_accounts,
    ROUND(
        SUM(campaign_cost) / NULLIF(COUNT(DISTINCT new_account_id), 0),
        2
    ) AS cost_per_new_account,
    SUM(estimated_account_revenue) AS estimated_revenue
FROM channel_performance
GROUP BY channel
ORDER BY estimated_revenue DESC;
