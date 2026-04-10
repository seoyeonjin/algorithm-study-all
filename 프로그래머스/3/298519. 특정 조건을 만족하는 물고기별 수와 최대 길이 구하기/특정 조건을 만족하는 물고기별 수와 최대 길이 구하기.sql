-- 코드를 작성해주세요

# 평균 길이가 33 이상인 물고기 종류별 분류
# 잡은 수, 최대 길이, 물고기 종류 출력
# 종류 오름차순
# 10이하는 10으로 취급해서 평규 길이 구하기

select count(id) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE
from fish_info
group by fish_type
having avg(
    case
        when length is null or length < 10 then 10
        else length
    end
) > 33
order by fish_type asc