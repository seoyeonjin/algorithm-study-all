n, m = map(int, input().split())
num_list = list(map(int, input().split()))
result_set = set()
num_list.sort()

def dfs(k, temp_list):
    if (len(temp_list) == m):
        result_set.add(tuple(temp_list))
    else:
        for i in range(k, n):
            temp_list.append(num_list[i])
            dfs(i, temp_list)
            temp_list.pop() 

dfs(0, [])
result_list = sorted(result_set)
for re in result_list:
    print(*re)