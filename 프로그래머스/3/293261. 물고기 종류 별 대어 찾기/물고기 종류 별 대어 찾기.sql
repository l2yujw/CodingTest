-- 코드를 작성해주세요
-- 물고기 종류별, 가장큰 물고기 => id(오름), 물고기 이름, 길이
SELECT i.id, ni.fish_name, IFNULL(i.length, 0) AS length
FROM fish_info i
JOIN fish_name_info ni ON i.fish_type=ni.fish_type
WHERE i.fish_type IN (SELECT fish_type
                      FROM fish_info
                      GROUP BY fish_type
                      HAVING length = max(length))
ORDER BY i.id