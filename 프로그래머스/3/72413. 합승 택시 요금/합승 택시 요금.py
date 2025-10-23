def solution(n, s, a, b, fares):
    
    INF = float('inf')
    answer = INF
    # 플로이드 워샬
    root = [[INF for i in range(n+1)] for j in range(n+1)]
    
    for f in fares:
        e,d,c = f
        root[e][d] = c
        root[d][e] = c
        
    for i in range(n+1):
        for j in range(n+1):
            if (i == j):
                root[i][j] = 0
    
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                root[i][j] = min(root[i][j], root[i][k] + root[k][j])
                
    # a는 a도착
    # b는 b도착
    # s는 출발
    # 어디까지 합승하는 게 좋을까? 
    for i in range(1, n+1): # 하나씩 합승 지점이다
        dis = root[s][i] + root[i][a] + root[i][b]
        answer = min(answer, dis)
    # print(root)
    return answer