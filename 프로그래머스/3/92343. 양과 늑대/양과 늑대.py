# import sys
# sys.setrecursionlimit(1000)

def solution(info, edges):
    answer = 0
    al = []
    
    tree = [[] for i in range(len(info))] 
    
    for e in edges:
        a, b = e
        tree[a].append(b)
    
    def dfs(node, scnt, wcnt, possible): 
        nonlocal answer
        answer = max(answer, scnt)
    
        next_possible = possible.copy()
        for c in tree[node]:
            next_possible.append(c)
        
        for n in next_possible:
            new_possible = next_possible.copy()
            new_possible.remove(n)
            if (info[n] == 0): # 양이면
                dfs(n, scnt+1, wcnt,new_possible)
            else: # 늑대면
                if (wcnt + 1 < scnt):
                    dfs(n, scnt, wcnt+1, new_possible)
    
    dfs(0, 1, 0, [])
    print(al)
    return answer