-- 코드를 작성해주세요
select  sum(score) as score, g.emp_no, e.emp_name, e.position, e.email
from    hr_employees e, hr_grade g
where   e.emp_no = g.emp_no
group by    year, emp_no
having      g.year = '2022'
order by    1 desc
limit   1
        