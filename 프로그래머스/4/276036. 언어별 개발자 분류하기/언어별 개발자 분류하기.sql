WITH
frontend_code AS (
    SELECT SUM(code) AS total FROM skillcodes WHERE category = 'Front End'
),
python_code AS (
    SELECT code AS value FROM skillcodes WHERE name = 'Python'
),
csharp_code AS (
    SELECT code AS value FROM skillcodes WHERE name = 'C#'
)

SELECT
    CASE
        WHEN d.skill_code & fc.total AND d.skill_code & pc.value THEN 'A'
        WHEN d.skill_code & cc.value THEN 'B'
        WHEN d.skill_code & fc.total THEN 'C'
    END AS grade,
    d.id,
    d.email
FROM developers d
CROSS JOIN frontend_code fc
CROSS JOIN python_code pc
CROSS JOIN csharp_code cc
WHERE 
    (d.skill_code & fc.total AND d.skill_code & pc.value) OR
    (d.skill_code & cc.value) OR
    (d.skill_code & fc.total)
ORDER BY grade, id;