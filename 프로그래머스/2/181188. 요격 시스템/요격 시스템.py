def solution(targets):
    
    answer = 0
    targets.sort(key=lambda x: x[1])
    
    cnt = 0
    end = 0
    for s, e in targets:
        if s >= end:
            cnt += 1
            end = e
    answer = cnt
#     # 경계값을 포함하지 않음
#     MAX_NUM = 100000001
#     prefix_sum = [0 for i in range(MAX_NUM+2)]
#     temps = [0 for i in range(MAX_NUM+1)]
    
    
#     def calc():
#         prefix_sum[0] = temps[0]
#         for i in range(1, len(temps)):
#             prefix_sum[i] = prefix_sum[i-1] + temps[i]
        
    
#     for t in targets:
#         s, e = t
#         temps[s] += 1
#         temps[e] -= 1
        
#     calc()
    
#     # print(temps)
#     # print(prefix_sum)
    
#     while True:
#         num = max(prefix_sum)
#         if (num == 0):
#             break
#         answer += 1 
#         max_index = prefix_sum.index(num)
#         # print(max_index)

#         for t in targets:
#             s, e= t
#             if (s <= max_index < e):
#                 temps[s] -= 1
#                 temps[e] += 1
#         calc()

    return answer

