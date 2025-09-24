import heapq

N, M, X = map(int, input().split())

INF = int(1e9)
graph = [[] for j in range(N+1)]
distance = [[INF for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    s, e, t = map(int,input().split())
    graph[s].append((e,t))


for i in range(1, N+1): 
    heap = []
    heapq.heappush(heap, (0, i))
    distance[i][i] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if (dist > distance[i][node]):
            continue
        for e, t in graph[node]:
            new_dist = dist + t
            if (new_dist < distance[i][e]):
                distance[i][e] = new_dist
                heapq.heappush(heap, (new_dist, e))
# print(distance)

answer = [0] * (N+1)

for i in range(1, N+1):
    if distance[i][X] != INF and distance[X][i] != INF:
        answer[i] = distance[i][X] + distance[X][i]

print(max(answer[1:]))

# 시작점 각 점에서 모두 다익스트라 실행! 