-- 코드를 작성해주세요
-- fish_info 잡은 물고기 정보
-- 평균 길이 33이상, 종류별로 분류(오름차순), 10이하 = 10
WITH filtered_fish_info AS (
    SELECT id, fish_type, 
           CASE 
               WHEN length <= 10 THEN 10
               ELSE length
           END AS adjusted_length
    FROM fish_info
)
SELECT 
    COUNT(id) AS fish_count, 
    MAX(adjusted_length) AS max_length, 
    fish_type
FROM filtered_fish_info
GROUP BY fish_type
HAVING AVG(adjusted_length) >= 33
ORDER BY fish_type;
