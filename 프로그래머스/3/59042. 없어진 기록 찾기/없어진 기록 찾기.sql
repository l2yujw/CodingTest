-- 코드를 입력하세요
-- 입양 나간 기록o, 보호소 x => id(기준), 이름
SELECT ao.animal_id, ao.name
FROM animal_ins ai
RIGHT JOIN animal_outs ao ON ai.animal_id=ao.animal_id
WHERE ai.animal_id is null
ORDER BY ao.animal_id