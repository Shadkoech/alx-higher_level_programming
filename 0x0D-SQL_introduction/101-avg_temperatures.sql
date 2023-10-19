-- SQL script that displays average Temperature by city and ordered by temperature

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
