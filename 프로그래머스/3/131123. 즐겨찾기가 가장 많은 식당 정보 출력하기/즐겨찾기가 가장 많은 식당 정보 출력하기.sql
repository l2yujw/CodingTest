-- 코드를 입력하세요
-- rest_info 식당
-- 음식종류별, 즐겨찾기수 가장 많 => 음식종류(내림), id, 식당이름, 즐겨찾기수
SELECT  food_type, rest_id, rest_name, favorites
FROM    rest_info
WHERE   (food_type, favorites) IN ( SELECT food_type, MAX(favorites)
                                    FROM rest_info
                                    GROUP BY food_type)
ORDER BY food_type DESC