-- 코드를 작성해주세요
-- ecoli_data 배양한 대장균 정보
-- 최초의 대장군 개체 parent_id NULL
-- 3세대의 대장균의 id(오름)를 출력
SELECT d1.id
FROM ecoli_data d1
JOIN ecoli_data d2 ON d1.parent_id = d2.id
JOIN ecoli_data d3 ON d2.parent_id = d3.id
WHERE d3.parent_id IS NULL
ORDER BY d1.id