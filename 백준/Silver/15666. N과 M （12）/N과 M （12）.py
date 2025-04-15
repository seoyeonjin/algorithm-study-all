
from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = list(map(int, input().split()))

com_arr = combinations_with_replacement(arr, m)
new_com_arr = set()

for com in com_arr:
    com_list = list(com)
    com_list.sort()  
    com_list = tuple(com_list)
    new_com_arr.add(com_list)


set_com_arr = set(new_com_arr)
com_arr = [] 

for com in set_com_arr:
    com_arr.append(com)

com_arr.sort()

for com in com_arr:
    print(*com)