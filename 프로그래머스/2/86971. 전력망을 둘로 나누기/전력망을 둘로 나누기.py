from collections import deque

def solution(n, wires):
    answer = -1
    min_ans = 1e9
    
    edges = [[] for i in range(n+1)]
    
    
    for w in wires:
        a, b = w
        edges[a].append(b)
        edges[b].append(a)
        
    for w in wires:
        a, b = w
        visited = [0 for i in range(n+1)]
        edges[a].remove(b)
        edges[b].remove(a) 
        
        que = deque()
        cnt = 1
        que.append(a)
        visited[a] = 1
        
        while que:
            node = que.popleft()
            for e in edges[node]:
                if (not visited[e]):
                    cnt += 1
                    que.append(e)
                    visited[e] = 1
                    
        bcnt = n - cnt
        ans = abs(bcnt - cnt)
        min_ans = min(min_ans, ans)
        
        
        edges[a].append(b)
        edges[b].append(a)
    answer = (min_ans)
    return answer