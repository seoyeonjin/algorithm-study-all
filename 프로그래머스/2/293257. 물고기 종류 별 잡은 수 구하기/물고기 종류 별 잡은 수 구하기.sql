-- 코드를 작성해주세요

# 잡은 수 기준 내림차순 정렬
# select count(*) as FISH_COUNT, FISH_NAME
select count(ID) as FISH_COUNT, FISH_NAME
from fish_info
natural join fish_name_info
# on fish_info.fish_type = fish_name_info.fish_type
group by FISH_NAME
order by FISH_COUNT desc;