from collections import deque

N = int(input())     # 노드의 개수


gr = [[] for i in range(N+1)]
visited = [0] * (N+1)
tree = [0] * (N+1)


for i in range(N-1):
    a, b = map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)
start = 1

que = deque()
que.append(1)
visited[1] = True

while que:
    node = que.popleft()
    tl = gr[node]
    for t in tl:
        if (not visited[t]):
            tree[t] = node
            visited[t] = True
            que.append(t)


for i in range(2, len(tree)):
    print(tree[i])
