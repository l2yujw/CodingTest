-- 코드를 입력하세요
-- places 공간 정보
-- 공간 둘 이상 (헤비유저), => id순
SELECT id, name, host_id
FROM places
WHERE host_id IN (SELECT host_id
            FROM places
            GROUP BY host_id
            HAVING count(*) >= 2)
ORDER BY id 