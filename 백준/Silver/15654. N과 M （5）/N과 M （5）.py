from itertools import permutations

n, m = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
result_list = list(permutations(num_list,m))
for result in result_list:
    print(*result)