-- 코드를 작성해주세요
-- skillcodes
-- developers
-- grade별 개발자의 정보
-- A: Front, Python B:C# C: 그외 Front
WITH f AS (
    SELECT SUM(code)
    FROM skillcodes
    WHERE category = 'Front End'
)

SELECT CASE
            WHEN skill_code & (SELECT * FROM f) AND skill_code & (SELECT code FROM skillcodes WHERE name = 'Python') THEN 'A'
            WHEN skill_code & (SELECT code FROM skillcodes WHERE name = 'C#') THEN 'B'
            WHEN skill_code & (SELECT * FROM f) THEN 'C'
        END AS grade, id, email
FROM developers
HAVING grade IS NOT NULL
ORDER BY grade, id