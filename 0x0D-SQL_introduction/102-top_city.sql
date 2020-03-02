-- Average Temperature calculator
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month between 07 and 08 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
