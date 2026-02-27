# 수빈, 동생
# 수빈은 X -> X-1, X+1, 2*X 로 이동

# 수빈과 동생으 ㅣ위치 -> 가장 빠른 시간 몇 초?
from collections import deque

N,M= map(int, input().split())

ml = 150000

dist = [1e9] * (ml)

que = deque()
que.append(N)
dist[N] = 0

while que:
    node = que.popleft()
    if (node == M):
        print(dist[node])
        break
    if (node + 1 < ml and dist[node+1] == 1e9):
        dist[node+1] = dist[node] + 1
        que.append(node+1)
    if (node - 1 >= 0 and dist[node-1] == 1e9):
        dist[node-1] = dist[node] + 1
        que.append(node-1)
    if (node * 2 < ml and dist[node*2] == 1e9):
        dist[node*2] = dist[node] + 1
        que.append(node*2)

# print(dp[M])
    