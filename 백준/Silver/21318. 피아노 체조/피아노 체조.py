N = int(input())    # 악보의 개수
paper_arr = list(map(int, input().split()))
query_num = int(input())    
sum_arr = [0] * (N-1)

if (N > 1): 
    for i in range(N-1):
        if (paper_arr[i]-paper_arr[i+1] > 0):
            sum_arr[i] = 1

    prefix_sum = [0] * N
    prefix_sum[0] = sum_arr[0]

    for i in range(N-1):
        prefix_sum[i+1] = prefix_sum[i] + sum_arr[i]
else:
    prefix_sum = [0] * N

for _ in range(query_num):
    start, end = map(int, input().split())
    print(prefix_sum[end-1] - prefix_sum[start-1])