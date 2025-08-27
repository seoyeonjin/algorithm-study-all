from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        a,b = e
        graph[a].append(b)
        graph[b].append(a)
    # print(node_list)
    
    result = [0 for i in range(n+1)]
    
    result[1] = 1
    
    start = 1
    count = 1
    que = deque()
    que.append((start, count))
    while que:
        node, count = que.popleft()
        for node in graph[node]:
            if (result[node] == 0):
                result[node] = count
                que.append((node, count+1))
                
    print(result)
    max_num = max(result)
    print(max_num)
    for i in range(1,n+1):
        if (result[i] == max_num):
            answer += 1
    # print(answer)
    return answer