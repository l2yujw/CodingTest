-- 코드를 입력하세요
SELECT  ingredient_type, sum(total_order) as "total_order"
FROM    first_half f 
JOIN icecream_info i ON f.flavor = i.flavor
GROUP BY    ingredient_type