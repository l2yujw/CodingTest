-- 코드를 작성해주세요
select  id, email, first_name, last_name
from    developers
where   skill_code & (select code from skillcodes where name = "python") or
        skill_code & (select code from skillcodes where name = "c#")
order by    id