import heapq

def solution(n, paths, gates, summits):
    answer = []
    al = []
    
    gr = [[] for i in range(n+1)]
    INF = float('inf')
     # 방문 배열
    
    for i,j,w in paths:
        gr[i].append((j,w))
        gr[j].append((i,w)) # 양방향이니까

    # 중간에 만난 애가 gates에 있으면 그 길은 안 간다
    # dfs로 가야하는 거 같은데, 항상 최소 길을 먼저 넣고 나오게 한다. 
    # 전체 최소가 아니어서, 다익스트라는 아닌듯
    # 현재까지의 최소를 저장해서 계속 이동한다. 
    # 모든 gate로부터 모든 dist에 대해서 이동해본다. 
    # 다익스트라로 이 지점까지의 최소를 저장해둔다? 합이 아니라 ..
    
    # 다익스트라로 gate마다 -> 다른 좌표까지의 이동까지 최소를 기록해둔다. 
    # 결론적으로 summit에 있으면 추가한다. 
    # 근데 중간에 gate가 끼어있는 경로면 안 됨

    distance = [INF for i in range(n+1)] # 각지점까지 거리 
    heap = []
    for g in gates:
        heapq.heappush(heap, (0,g))
        distance[g] = 0
#     for i in range(len(gates)): 
#         g = gates[i] 

#         heap =  [(0,g)]
        
        # distance[g] = 0 # 현재지점까지 거리

    gates = set(gates)
    summits = set(summits)
    while heap:
        intensity, start = heapq.heappop(heap)
        
        if distance[start] < intensity:
            continue
        if start in summits: 
            continue          

        for nxt, w in gr[start]:
            if nxt in gates:   
                continue
            new_intensity = max(intensity, w)
            if distance[nxt] > new_intensity:
                distance[nxt] = new_intensity
                heapq.heappush(heap, (new_intensity, nxt))
        # 현재 게이트에서 갈 수 있는 길
        # for node, d in gr[start]:
        #     if (node in gates):
        #         continue
        #     if (node in summits):
        #         # 현재까지 최소 거리를 al 에 넣는다
        #         continue
        #         # al.append((node, max(max_dist, d)))
        #     else:
        #         # 일단은 간다
        #         temp_min = max(distance[start], d)
        #         if (distance[node] > temp_min):
        #             distance[node] = temp_min
        #             heapq.heappush(heap, (max(max_dist,d), node))
        #                 # que.append((node, max(max_dist, d)))
        #         # if (not visited[node]):
        #             # if (distance[node] < distance[start])

    answer =0
    result = sorted([(distance[s], s) for s in summits])
    answer = ([result[0][1], result[0][0]])
    # answer = min([(distance[s], s) for s in summits])
    # al.sort(key=lambda x: (x[1], x[0]))
    # answer = al[0]
    
    return answer