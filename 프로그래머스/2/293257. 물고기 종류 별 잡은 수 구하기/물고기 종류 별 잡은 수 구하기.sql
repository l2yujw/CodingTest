-- 코드를 작성해주세요
SELECT      COUNT(*) AS 'fish_count', n.fish_name
FROM        fish_info i, fish_name_info n
WHERE       i.fish_type = n.fish_type
GROUP BY    n.fish_name
ORDER BY    fish_count DESC