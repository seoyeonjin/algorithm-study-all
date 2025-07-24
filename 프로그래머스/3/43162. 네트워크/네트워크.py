# 방문한적 없으면 바로 고
def dfs(start, visited, computers, n):
    for i in range(n):
        if (i != start and not visited[i] and computers[start][i]):
            visited[i] = 1
            dfs(i, visited, computers, n)
    

def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if (not visited[i]):
            answer += 1
            dfs(i, visited, computers, n)
    return answer