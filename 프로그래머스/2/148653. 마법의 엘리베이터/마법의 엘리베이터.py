# 50분까지
# from collections import deque

def solution(storey):
    answer = 0
    # 마법 엘리베이터 10의 제곱수가 있다. +-
    # 더한 층으로 이동하는데 더한 결과가 0보다 작으면 이동하지 않는다.
    # 0ㅊㅇ이 가장 아래 층이다.
    # 최소이동 횟수 구하기
    # 민수가 있는 층 -> storey이다. 0층ㅇ로 가기 위한 최소 이동횟수?
    
#     que = deque()
#     que.append((storey, 0))
#     result = [] 
    
#     while que:
#         x,cnt = que.popleft()
#         num = x % 10 
#         x = x // 10
#         if (x == 0): 
#             result.append(cnt+num)
#         else:
#             que.append((x, cnt+num))
#             que.append((x+1, cnt+(10-num)))
        
    
    cnt = 0
    while storey > 0:
        # print(storey)
        num = storey % 10 # 10으로 나눈 나머지
        if (num > 5):
            num = 10 - num
            cnt += num
            storey = storey // 10 + 1
        elif (num < 5):
            cnt += num
            storey = storey // 10
        else:  # 5 일때
            next_num = (storey // 10) % 10
            
            if next_num >= 5:
                cnt += 5
                storey = storey // 10 + 1
            else:
                cnt += 5
                storey //= 10
            

    return cnt