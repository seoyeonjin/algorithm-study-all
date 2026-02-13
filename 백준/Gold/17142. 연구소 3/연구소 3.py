# N,M

# 모든 바이러스는 비활성 상태

# 활성 상태로 변경한다.
from itertools import combinations
from collections import deque
from copy import deepcopy


N,M = map(int,input().split())
nums = []
vs = []


for i in range(N):
    nums.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if (nums[i][j] == 2):
            vs.append((i,j))

coms = combinations(vs, M) # M개 뽑아서 활성 상태로 변경하기

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# zero 개수 세기
zcnt = sum(nums, []).count(0)
# print(zcnt)
ans = []


# 활성 상태는 3으로 표시한다.
for com in coms:
    # 활성 상태로 놓고 시작하기
    que = deque()
    visited = set()
    zero = zcnt
    dnums = deepcopy(nums)

    if (zero == 0):
        ans.append(zero)
        break

    for c in com:
        que.append((c[0], c[1], 0))
        dnums[c[0]][c[1]] = 3
    while que:
        x, y, cnt = que.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if (0<=nx<N and 0<=ny<N and (nx,ny) not in visited):
                if (dnums[nx][ny] == 0):
                    dnums[nx][ny] = 3
                    visited.add((nx,ny))
                    que.append((nx,ny,cnt+1))
                    zero -= 1
                    if (zero == 0):
                        ans.append(cnt+1)
                        break
                elif (dnums[nx][ny] == 2):
                    dnums[nx][ny] = 3
                    visited.add((nx,ny))
                    que.append((nx,ny,cnt+1))

if (len(ans) == 0):
    print(-1)
else:
    ans.sort()
    print(ans[0])
                
    