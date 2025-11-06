import heapq

T = int(input())

INF = float('inf')
for _ in range(T):

    n, d, c = map(int, input().split())
    coms = [INF for i in range(n+1)]
    coms[c] = 0
    heap = []
    heapq.heappush(heap, (0, c)) # start node
    edges = [[] for i in range(n+1)]
    for i in range(d):
        a,b,s = map(int ,input().split())
        edges[b].append((a,s))
    while heap:
        dist, node = heapq.heappop(heap)
        if (dist > coms[node]):
            continue
        for e in edges[node]:
            nn ,ns = e
            if (dist + ns < coms[nn]):
                coms[nn] = dist + ns
                heapq.heappush(heap, (dist+ns, nn))
    cnt = 0
    time = 0
    for i in range(1, n+1):
        if (coms[i] != INF): 
            cnt += 1
            if (coms[i] > time): 
                time = coms[i]
    print(cnt, time)
    