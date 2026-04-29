-- Top Revenue Categories

SELECT
    category,
    SUM(total_amount) AS revenue
FROM processed_transactions
GROUP BY category
ORDER BY revenue DESC;

-- Average Fuel Margin By Grade

SELECT
    fuel_grade,
    AVG(margin_per_gallon) AS avg_margin
FROM fuel_margin_analysis
GROUP BY fuel_grade
ORDER BY avg_margin DESC;
