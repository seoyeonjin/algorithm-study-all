import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = []

for _ in range(N):
    arr = list(map(int, input().split()))
    num_list.append(arr)

prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]


for i in range(N):
    for j in range(N):
        prefix_sum[i][j+1] = prefix_sum[i][j] + num_list[i][j]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())  
    sum = 0
    for i in range(x1-1, x2):
        sum += prefix_sum[i][y2] - prefix_sum[i][y1-1]

    print(sum)