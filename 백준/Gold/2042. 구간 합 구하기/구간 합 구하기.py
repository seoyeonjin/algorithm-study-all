# 세그먼트 트리 
import math

def change(b,c):
    real_b = 2**temp + b -1
    # print(temp, real_b)
    plus = c - tree[real_b]
    while real_b:
        # print(real_b, plus)
        tree[real_b] += plus
        real_b = real_b // 2 

def sub_print(b,c):
    rb =  2**temp + b -1
    rc =  2**temp + c -1
    selected = []
    while rb <= rc:
        if (rb % 2 == 1):
            selected.append(tree[rb])
        if (rc % 2 == 0):
            selected.append(tree[rc])
        rb = (rb + 1) // 2
        rc = (rc -1) // 2
    sum_s = sum(selected)
    # print(selected)
    print(sum_s)

N, M, K = map(int, input().split())


temp = math.ceil(math.log2(N))
tree = [0 for i in range(2**(temp+1))]
# print(tree)


for i in range(N):
    num = int(input())
    tree[2**(temp)+i] = num
# print(tree)

for i in range(len(tree)-1, 1, -1): 
    tree[i//2] += tree[i]
# print(tree)

for i in range(M+K):
    a,b,c = map(int ,input().split())
    if (a == 1):
        change(b,c)
        # print(tree)
    else:
        sub_print(b,c)
        # b부터 c까지의 합을 출력한다
