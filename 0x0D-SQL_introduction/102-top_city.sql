-- Select top 3 hottest cities in summer
SELECT city, AVG(value) FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
