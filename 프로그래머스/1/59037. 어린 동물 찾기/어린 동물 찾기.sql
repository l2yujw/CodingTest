-- 코드를 입력하세요
SELECT animal_id, name 
FROM animal_ins 
WHERE intake_condition NOT LIKE 'Aged' 
ORDER BY animal_id