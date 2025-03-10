-- 코드를 작성해주세요
-- ecoli_data 배양 대장균 정보
-- 최초 parent_id null
-- 크기 <=100 low, 100<zmrl<=1000 medium, 1000<size high
SELECT id, 
    CASE
        WHEN size_of_colony <= 100 THEN 'LOW'
        WHEN size_of_colony <= 1000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END as size
FROM ecoli_data
ORDER BY id