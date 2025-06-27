from collections import deque

N, M, R = map(int, input().split())
saved_list = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    saved_list[start].append(end)
    saved_list[end].append(start)

for i in range(N+1):
    saved_list[i].sort()

visited_list = [0 for _ in range(N+1)]

def bfs():
    count = 1
    visited_list[R] = count
    count += 1
    que = deque()
    que.append(R)
    
    while que:
        start_node = que.popleft()
        for node in saved_list[start_node]:
            if (not visited_list[node]):
                visited_list[node] = count
                count += 1
                que.append(node)

bfs()

for visited in visited_list[1:]:
    print(visited)