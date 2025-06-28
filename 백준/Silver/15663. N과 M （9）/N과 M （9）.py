from itertools import permutations

n, m = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
result_list = list(permutations(num_list,m))
result_list = list(set(result_list))
result_list.sort()
for result in result_list:
    print(*result)