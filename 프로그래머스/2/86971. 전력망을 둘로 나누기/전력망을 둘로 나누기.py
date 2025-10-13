def solution(n, wires):
    answer = 1e9
    
    edges = [[] for i in range(n+1)] # 연결
    # visited = [0 for i in range(n+1)] 
    
    def dfs(node, visited):
        visited[node] = True
        cnt = 1 
        for a in edges[node]:
            if not visited[a]:
                cnt += dfs(a, visited)
        return cnt
        
    
    for w in wires:
        a,b = w
        edges[a].append(b)
        edges[b].append(a)
    
    for w in wires:
        a,b = w  # 제거할 엣지
        edges[a].remove(b)
        edges[b].remove(a)
        
        visited = [False] * (n+1)
        acnt = dfs(a, visited)
        bcnt = dfs(b, visited)

        sub = abs(acnt - bcnt) # 가능한 비슷하도록 나눈다
        # print("b: ", visited)
        answer = min(answer, sub)
        
        edges[a].append(b)
        edges[b].append(a)
        
    # print(edges)
    return answer