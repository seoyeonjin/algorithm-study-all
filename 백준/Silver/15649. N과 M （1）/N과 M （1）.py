import itertools

n, m = map(int,input().split())
num_list = []

for i in range(1,n+1):
    num_list.append(i)
# print(num_list)
    
result = itertools.permutations(num_list, m)
for i in result:
    print(*i)