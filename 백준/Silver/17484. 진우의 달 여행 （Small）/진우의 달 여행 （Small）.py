# 수가 작음 -> 완탐 
from collections import deque

dx = [1,1,1]
dy = [-1,0,1]

N, M = map(int, input().split())
way_list = []
result_list = []

for _ in range(N):
    temp_list = list(map(int, input().split()))
    way_list.append(temp_list)

que= deque()

for i in range(M):
    que.append((0,i,-1, way_list[0][i]))

while que:
    x, y, d, w = que.popleft()
    # print(x, y, que)
    if (x == N-1):
        # print(x,y,w)
        result_list.append(w)
    else: 
        for i in range(3):
            if (d != i):
                new_x = x + dx[i]
                new_y = y + dy[i] 
                if (new_x < N and new_y < M and new_y >= 0):
                    new_w =  w + way_list[new_x][new_y]
                    que.append((new_x, new_y, i, new_w))

print(min(result_list))
