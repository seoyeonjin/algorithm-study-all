import sys
from collections import deque

input = sys.stdin.readline
n, m= map(int,input().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

result = [] 
while queue:
    node = queue.popleft()
    result.append(node)
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
result.pop(0)
for i in result:
    print(i,end = " ")