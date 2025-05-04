n = int(input())
num_list = list(map(int, input().split()))

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]

m = int(input())

for _ in range(m):
    start , end = map(int ,input().split())
    print(prefix_sum[end] - prefix_sum[start-1])