N = int(input())
num_list = list(map(int, input().split()))
total = int(input())

result = 0
num_list.sort()

list_of_sum = sum(num_list)
if (list_of_sum <= total):
    print(max(num_list))
else:
    # start = total // N # 시작 bound
    for i in range(N):
        start = total // (N-i)
        # print(start, total)
        if (num_list[i] <= start):
            total = total - num_list[i]
        else:
            break
    print(start)
          