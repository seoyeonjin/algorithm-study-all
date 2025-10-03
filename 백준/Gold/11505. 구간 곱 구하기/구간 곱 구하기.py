# 수정 빈번
import math

N, M, K = map(int, input().split())

temp = math.ceil(math.log(N,2))
# print(temp)

tree = [1] * (2**(temp+1))
# print(tree)

# 초기화 
for i in range(N):
    num = int(input())
    tree[2**temp+i] = num

for i in range(2**temp-1, 0, -1):
    tree[i] = (tree[i*2] * tree[i*2+1])% 1000000007

# print(tree)

def update(b,c):
    rb = b + 2**temp - 1
    tree[rb] = c
    rb //= 2
    while rb:
        tree[rb] = (tree[rb*2] * tree[rb*2+1])  % 1000000007
        rb //= 2

def sub_print(b,c):
    rb =  b + 2**temp -1
    rc =  c + 2**temp -1
    ans = 1
    # selected = []
    while rb <= rc:
        if (rb % 2 == 1):
            # selected.append(tree[rb])
            ans = (ans * tree[rb])  % 1000000007
        if (rc % 2 == 0):
            # selected.append(tree[rc])
            ans = (ans * tree[rc]) % 1000000007
        rb = (rb + 1)//2
        rc = (rc-1)//2
    # print(selected)
    print(ans % 1000000007)



for i in range(M+K):
    a,b,c = map(int, input().split())
    if (a==1): 
        update(b,c)
        # print(tree)
    else:
        sub_print(b,c)
        # 출력