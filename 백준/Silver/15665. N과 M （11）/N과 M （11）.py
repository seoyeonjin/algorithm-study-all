n, m = map(int, input().split())
input_list = list(map(int, input().split()))
result_list = []
num_list = []

input_list.sort()

result_set = set()

for i in range(n):
    if input_list[i] not in num_list:
        num_list.append(input_list[i])


def dfs(temp_list):
    if (len(temp_list) == m):
            result_set.add(tuple(temp_list))
    else:
        for num in num_list:
            temp_list.append(num)
            dfs(temp_list)
            temp_list.pop()

dfs([])
result_set = sorted(result_set)
for result in result_set:
    print(*result)