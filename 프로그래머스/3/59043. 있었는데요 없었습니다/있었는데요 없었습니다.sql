-- 코드를 입력하세요
-- 보호시작일 < 입양일 => 동물의 아이디, 이름 (보호 시작일 빠른순)
SELECT  ai.animal_id, ai.name
FROM    animal_ins ai JOIN animal_outs ao ON ai.animal_id = ao.animal_id
WHERE   ai.datetime - ao.datetime > 0
ORDER BY    ai.datetime