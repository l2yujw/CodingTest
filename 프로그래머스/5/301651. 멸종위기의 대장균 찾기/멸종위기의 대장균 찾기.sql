WITH RECURSIVE generations AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA 
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT e.ID, e.PARENT_ID, g.GENERATION + 1
    FROM ECOLI_DATA e
    INNER JOIN generations g 
    ON e.PARENT_ID = g.ID
)

SELECT COUNT(*) AS COUNT, g.GENERATION
FROM generations g
WHERE NOT EXISTS (
    SELECT 1 
    FROM ECOLI_DATA child 
    WHERE child.PARENT_ID = g.ID
)
GROUP BY g.GENERATION
ORDER BY g.GENERATION;