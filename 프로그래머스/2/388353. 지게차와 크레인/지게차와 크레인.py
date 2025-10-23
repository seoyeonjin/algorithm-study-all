from collections import deque

def solution(storage, requests):
    answer = 0
    cons = [[1 for i in range(len(storage[0]))] for j in range(len(storage))]
    
    N = len(storage)
    M = len(storage[0])
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    def jige(i, j):
        que = deque()
        que.append((i,j))
        visited = [(i,j)]
        
        while que:
            x, y = que.popleft()
            if (x == N-1 or y == M-1 or x == 0 or y == 0):
                return True
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if (0<=nx<N and 0<=ny<M and (nx,ny) not in visited and cons[nx][ny] == 0):
                    que.append((nx,ny))
                    visited.append((nx,ny))
        return False
                
            
    
    for r in requests:
        if (len(r) == 2): # 크레인
            for i in range(N):
                for j in range(M):
                    if (storage[i][j] == r[0] and cons[i][j] == 1):
                        cons[i][j] = 0
        else: # 지게차면
            results = []
            for i in range(N):
                for j in range(M):
                    if (storage[i][j] == r[0] and cons[i][j] == 1):
                        result = jige(i,j)
                        if (result):
                            results.append((i,j))
            for res in results:
                a,b = res
                cons[a][b] = 0
                
    answer = (sum(cons, [])).count(1)
    return answer