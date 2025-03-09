-- 코드를 입력하세요
-- 입양O, 보호기간 가장긴 둘 => 아이디 이름 (보호기간 긴순)
SELECT      ai.animal_id, ai.name
FROM        animal_ins ai 
            JOIN animal_outs ao
            ON ai.animal_id = ao.animal_id
ORDER BY    ao.datetime - ai.datetime desc
LIMIT       2