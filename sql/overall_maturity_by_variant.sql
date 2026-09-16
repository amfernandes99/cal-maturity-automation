SELECT
    Variant,
    COUNT(*) AS parameter_count,
    ROUND(AVG(Score), 1) AS average_score,
    ROUND(AVG(Score) / 25 * 100, 1) AS maturity_percentage
FROM `cal-maturity-portfolio.cal_analytics.cal_maturity`
GROUP BY
    Variant
ORDER BY
    maturity_percentage DESC;