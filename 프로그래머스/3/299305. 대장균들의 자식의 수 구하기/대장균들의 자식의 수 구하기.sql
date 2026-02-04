-- ECOLI_DATA 배양 대장균 정보
-- id(오름)와 자식의 수, 자식x(0)
SELECT d1.id, COUNT(d2.id) AS child_count
FROM ecoli_data d1
LEFT JOIN ecoli_data d2 ON d1.id=d2.parent_id
GROUP BY d1.id
ORDER BY d1.id