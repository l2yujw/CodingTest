SET @hour := -1;

SELECT @hour := @hour + 1 hour,
    (SELECT COUNT(HOUR(datetime))
    FROM animal_outs
    WHERE HOUR(datetime) = @hour) count
FROM animal_outs
WHERE @hour + 1 < 24 