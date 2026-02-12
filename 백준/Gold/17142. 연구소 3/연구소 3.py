# 복제에 1초 걸린다.
# 바이러스 M개를 활성 상태로 변경한다

# 0은 빈칸, 1은 벽, 2는 바이러스다
# 활성 바이러스 -> 비활성 바이러스 칸

# 활성칸 정보 찾기

from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
nums = []
vis = []

for i in range(n):
    nums.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if (nums[i][j] == 2):
            vis.append((i,j))


coms = combinations(vis, m)
min_cnt = 1e9

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(ns, coms):
   
    # cnt = 0
    que = deque()
    visited = set()
    zero = 0

    for i in range(n):
        for j in range(n):
            if (ns[i][j] == 0):
                zero += 1
    for c in coms:
        que.append((c[0],c[1], 0))
        visited.add(c)

    # visited.add(coms)
    # print(visited)

    while que:  
        # print(que)
        x, y, cnt = que.popleft()
        if (zero == 0):
            return cnt
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if (0<=nx<n and 0<=ny<n and (nx,ny) not in visited):
                if (ns[nx][ny] == 0):
                    zero -= 1
                    if (zero == 0):
                        return cnt +1
                    que.append((nx,ny,cnt+1))
                    visited.add((nx,ny))
                    ns[nx][ny] = 3
                elif(ns[nx][ny] == 2 or ns[nx][ny] == 3):
                    que.append((nx,ny,cnt+1))
                    visited.add((nx,ny))
                    # ns[nx][ny] = 3
    return 1e9
            
                            
                



for com in coms:
    # print(com)
    dnums = deepcopy(nums)
    for m in com:
        x, y = m
        dnums[x][y] = 3 # 활성 바이러스
    cnt = bfs(dnums, com)
    # print(cnt)
    min_cnt = min(min_cnt, cnt)

if (min_cnt == 1e9):
    print(-1)
else:
    print(min_cnt)