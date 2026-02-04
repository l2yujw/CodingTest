SELECT      YEAR(ym) AS 'YEAR', ROUND(AVG(pm_val1), 2) AS 'PM10', ROUND(AVG(pm_val2), 2) AS "PM2.5"
FROM        air_pollution
GROUP BY    year, location1, location2
HAVING      location2 = "수원"
ORDER BY    YEAR