-- 코드를 입력하세요
-- animal_ins 동물 보호소에 들어온 동물들의 정보
-- animal_outs 입양 보낸 동물들의 정보
-- ins (입양 못간 애, 가장 오래 3마리,) => 이름, 보호시작일(시작일 순)
SELECT  ai.name, ai.datetime
FROM    animal_ins ai
WHERE   ai.animal_id NOT IN (
            SELECT  ao.animal_id
            FROM    animal_outs ao
        )
ORDER BY    ai.datetime
LIMIT   3