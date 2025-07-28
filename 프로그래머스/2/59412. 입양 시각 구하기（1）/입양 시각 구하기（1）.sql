SELECT HOUR(datetime) AS 'HOUR', COUNT(datetime) AS 'COUNT'
FROM animal_outs
WHERE HOUR(datetime) between 9 and 19
GROUP BY hour 
ORDER BY hour;