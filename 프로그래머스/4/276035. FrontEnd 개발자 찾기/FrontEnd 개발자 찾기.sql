-- 코드를 작성해주세요
-- skillcodes 개발언어 스킬코드 2진수
-- developers 개발자 스킬 정보
-- front end 가능 개발자, id 오름
SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S
ON S.CODE & D.SKILL_CODE
WHERE S.CATEGORY = 'Front End'
ORDER BY ID ASC;