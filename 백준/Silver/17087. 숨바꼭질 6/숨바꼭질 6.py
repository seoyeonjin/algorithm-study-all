import math

N , S = map(int, input().split())   
dg_list = list(map(int, input().split()))

for i in range(N):
    dg_list[i] = abs(S-dg_list[i])

dg_list.sort()
a = math.gcd(*dg_list)
print(a)
