import heapq

# 포함했을 때 안 했을 때 비교를 해야 하는건가?? 
# 규칙을 찾아보면, 작은 수부터 합쳐야한다.

#최소 비교 횟수를 구하는 문제

# 매번 가장 작은 두 묶음을 합쳐야 함!! 
N = int(input())
num_list = []
sum = 0
total_sum = 0

for _ in range(N):
    heapq.heappush(num_list, int(input()))

if (N > 2):
    while (len(num_list) > 1):
        num1 = heapq.heappop(num_list)
        num2 = heapq.heappop(num_list)
        sum = num1 + num2
        total_sum = total_sum + sum
        heapq.heappush(num_list, sum)
    print(total_sum)
else:
    print(0)
