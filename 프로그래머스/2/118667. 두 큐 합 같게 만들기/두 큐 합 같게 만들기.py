from collections import deque

def solution(queue1, queue2):
    answer = -2
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    que = deque()
    cnt = 0
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    que.append((q1,q2,cnt, q1_sum, q2_sum))
      
    while que:
        # print(que)
        q1, q2, cnt,s1,s2 = que.popleft()
        if (q1 == queue1 and cnt != 0):
            return -1   
        if (len(q1) == 0 or len(q2) == 0):
            return -1
        
        if (s1 < s2):
            num = q2.popleft()
            q1.append(num)
            s1 = s1 + num
            s2 = s2 - num
            que.append((q1,q2, cnt+1, s1,s2))
        elif (s2 < s1):
            num = q1.popleft()
            q2.append(num)
            s1 -= num
            s2 += num
            que.append((q1,q2, cnt+1, s1, s2))
        else:
            return cnt
        
        
#     total_que = queue1 + queue2
#     # sum_total = sum(total_que)
#     half = len(queue1)
    
#     prefix_sum = [0] * (half * 2 + 1)
#     for i in range(half*2):
#         prefix_sum[i+1] = prefix_sum[i] + total_que[i]
#     print(prefix_sum)
    
#     total_sum = prefix_sum[-1]
    
#     for i in range(half+1):
#         half_sum = prefix_sum[i+half] - prefix_sum[i]
#         print(half_sum)
#         if (half_sum == total_sum // 2):
#             print(i+1)
#             return (i+1)
#     return -1
        
    return answer