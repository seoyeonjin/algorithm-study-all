N, M = map(int, input().split())
num_list = list(map(int ,input().split()))

# 누적 합

prefix_sum = [0] * (N +1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]

# print(prefix_sum)


for _ in range(M): 
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])
