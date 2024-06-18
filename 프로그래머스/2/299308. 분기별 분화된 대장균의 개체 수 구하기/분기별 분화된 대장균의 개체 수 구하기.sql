-- 코드를 작성해주세요
select  concat(ceil(month(differentiation_date) / 3), 'Q') as quarter, count(id) as ecoli_count
from    ecoli_data
group by    quarter
order by    quarter