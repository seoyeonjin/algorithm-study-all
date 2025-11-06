# 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터 수.
# 1번과 연결된 컴퓨터 수


# 컴퓨터 수는 100 이하인 양의 정수

N  = int(input())
M = int(input())    

parent = [i for i in range(N+1)] # 컴퓨터수만큼 초기화


def ufind(a):
    if (parent[a] != a):
        parent[a] = ufind(parent[a])
    return parent[a]


def union(a,b):
    ra = ufind(a)
    rb = ufind(b)

    if (ra < rb):
        parent[rb] = ra
    else:
        parent[ra] = rb


for i in range(M):
    a,b = map(int ,input().split())
    union(a,b)
    # 둘을 연결한다.

# print(parent.count(1)-1)

cnt = -1
for i in range(1, N+1):
    r = ufind(parent[i])
    if (r == 1):
        cnt += 1
print(cnt)