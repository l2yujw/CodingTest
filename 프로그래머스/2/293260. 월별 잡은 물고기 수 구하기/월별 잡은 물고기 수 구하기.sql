-- 코드를 작성해주세요
SELECT      COUNT(*) AS fish_count, month(time) AS month
FROM        fish_info
GROUP BY    month
ORDER BY    month