-- 코드를 작성해주세요

# select SUBSTR(time, 6, 2
select count(*) as "FISH_COUNT", month(time) as "MONTH"
from fish_info
group by MONTH
having count(*) > 0
order by MONTH asc