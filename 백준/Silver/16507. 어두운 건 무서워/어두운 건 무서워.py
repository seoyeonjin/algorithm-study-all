n, m, t = map(int, input().split())
num_list = []

prefix_sum_list = []

prefix_sum_list = [[0 for i in range(m+1)] for j in range(n+1)]


for _ in range(n):
    temp_list = list(map(int, input().split()))
    num_list.append(temp_list)


for i in range(n):
    for j in range(m):
        prefix_sum_list[i][j+1] = prefix_sum_list[i][j] + num_list[i][j]

for _ in range(t):
    a,b,c,d = map(int, input().split())
    div = (c-a+1) * (d-b+1)
    sum = 0
    for i in range(a-1,c):
        sum += prefix_sum_list[i][d] - prefix_sum_list[i][b-1]
    print(sum // div)