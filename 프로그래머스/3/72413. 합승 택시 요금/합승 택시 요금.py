import heapq

def solution(n, s, a, b, fares):
    
    INF = float('inf')
    answer = 0
    dist = [[INF for i in range(n+1)] for j in range(n+1)]

    for i in range(1, n+1):
        dist[i][i] = 0

    for (c, d, w) in fares:
        dist[c][d] = w
        dist[d][c] = w

   
    for k in range(1,n+1):        
        for i in range(1,n+1):   
            for j in range(1,n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_cnt = float('inf')
    for i in range(1,n+1):
        cnt = dist[s][i] + dist[i][a] + dist[i][b]
        min_cnt = min(cnt, min_cnt)
        # print(i, cnt)
    answer = min_cnt
        
        
    
    return answer