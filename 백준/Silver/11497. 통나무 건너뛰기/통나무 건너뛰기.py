# 최소가 되는 것. 

T = int(input())


for _ in range(T):
    N = int(input())
    tree_list = list(map(int, input().split()))
    tree_list.sort()
    abs_list = []
    
    start = 0
    end = 2

    while end <= N-1:
        abs_num = abs(tree_list[start] - tree_list[end])
        abs_list.append(abs_num)
        start = end
        end = end + 2

    if (end == N): # 홀수개 일때
        end = N -1
        abs_num = abs(tree_list[start] - tree_list[end])
        abs_list.append(abs_num)
        start = end -2
    else:
        end = start
        start = end-1

    while start > 0:
        abs_num = abs(tree_list[start] - tree_list[end])
        abs_list.append(abs_num)
        end = start
        start = start -2
    print(max(abs_list))