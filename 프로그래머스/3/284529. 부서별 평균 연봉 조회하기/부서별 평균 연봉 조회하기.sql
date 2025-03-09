-- 코드를 작성해주세요
-- hr_department 부서정보
-- hr_emplyees 사원정보
-- 평균 연봉, 부서별 => id, 영문 부서명, 평균연봉(소숫점 첫째에서 반올림, 내림)
SELECT d.dept_id, d.dept_name_en, round(avg(e.sal), 0) as avg_sal
FROM hr_department d
JOIN hr_employees e ON d.dept_id=e.dept_id
GROUP BY d.dept_id
ORDER BY avg_sal desc