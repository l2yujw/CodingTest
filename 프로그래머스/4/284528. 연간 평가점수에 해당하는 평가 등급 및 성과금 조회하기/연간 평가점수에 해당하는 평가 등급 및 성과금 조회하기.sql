-- 코드를 작성해주세요
-- hr_department 부서정보
-- hr_employees 사원정보
-- hr_grade 2022년 사원 평가 정보
-- 사원별 성과금
-- 96>=S, 90>=A, 80>=B, C
SELECT e.emp_no, e.emp_name, s.grade, 
    CASE s.grade
        WHEN 'S' THEN e.sal*0.2
        WHEN 'A' THEN e.sal*0.15
        WHEN 'B' THEN e.sal*0.1
        ELSE e.sal*0
    END
        as bonus
FROM hr_employees e
JOIN (SELECT emp_no, 
        CASE
            WHEN avg(score) >= 96 THEN 'S'
            WHEN avg(score) >= 90 THEN 'A'
            WHEN avg(score) >= 80 THEN 'B'
            ELSE 'C'
        END as grade
      FROM hr_grade
      GROUP BY EMP_NO) as s ON e.emp_no = s.emp_no
ORDER BY emp_no