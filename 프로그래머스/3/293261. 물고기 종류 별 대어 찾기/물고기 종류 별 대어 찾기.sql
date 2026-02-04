-- 코드를 작성해주세요
-- 물고기 종류별, 가장큰 물고기 => id(오름), 물고기 이름, 길이
WITH MaxLengthPerType AS (
    SELECT fish_type, MAX(length) AS max_length
    FROM fish_info
    GROUP BY fish_type
)
SELECT i.id, ni.fish_name, i.length
FROM fish_info i
JOIN fish_name_info ni ON i.fish_type = ni.fish_type
JOIN MaxLengthPerType m ON i.fish_type = m.fish_type AND i.length = m.max_length
ORDER BY i.id;
