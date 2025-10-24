def solution(edges):
    answer = []
    
    # edges를 인접 리스트로 표현
    # max_n = max(sum(edges, []))
    
    max_n = -1
    for e in edges:
        a,b = e
        max_n = max(max_n, a,b)

    # print(max_n)
    redges = [[0,0] for i in range(max_n+1)] # 들어오는 거, 나가는 거
    
    # print(redges)
    for e in edges: # 들어오는 거 나가는 거 표시
        a,b = e
        redges[a][1] += 1
        redges[b][0] += 1
        
    
    for i in range(1, len(redges)): # root 찾기
        r = redges[i] 
        if (r[0] == 0 and r[1] >= 2):
            root = i
            total = r[1]
        if (r[0] == 0 and r[1] == 0):
            redges[i] = None
    # print(root, total)
    
    for e in edges: #
        if (e[0] == root):
            redges[e[1]][0] -= 1
        
    # print(redges)
    
    eight = 0
    donut = 0
    bar = 0
    
    for r in redges[1:]:
        if (r == None):
            continue
        if (r[0] == 2 and r[1] == 2): 
            eight += 1
        if (r[1] == 0):
            bar += 1
    
    # bar -= 1 # root는 빼줌
    
    answer = [root, total - bar -eight, bar, eight]
    return answer