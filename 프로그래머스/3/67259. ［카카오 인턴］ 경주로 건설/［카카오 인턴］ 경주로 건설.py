from collections import deque

def solution(board):
    answer = 0
    # 0->비어있음
    # 1-> 벽
    # 직선도로 -> 100원 
    # 코너 -> 500원
    
    dx = [0,0,-1,1] # 오른쪽, 왼쪽, 위쪽, 아래쪽
    dy = [1,-1,0,0]
    
    N = len(board)
    # v -> 25 * 25 이다 -> V^2 이어서 다 돌아도 될듯
    que = deque()
    que.append((0,0,0,0)) # 시작점x, y, direction, 비용
    visited = [[0 for i in range(N)] for j in range(N)]
    visited[0][0] = -1
    
    expan_list = []
    while que: 
        # print(que)
        x, y, direct, expan = que.popleft()

        if (x == N -1 and y == N-1):
            expan_list.append(expan)
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (0<=nx<N and 0<=ny<N and board[nx][ny] == 0): # 갈 수 있으면
                if (x == 0 and y == 0): # 시작점이면 비용 계산
                    newdirect = i // 2
                    newexpan = expan + 100
                else:
                    newdirect = i // 2
                    if (newdirect != direct):
                        newexpan = expan + 600
                    else:
                        newexpan = expan + 100

                if (direct == newdirect): 
                    if (visited[nx][ny] == 0 or visited[nx][ny] >= newexpan):
                        visited[nx][ny] = newexpan
                        que.append((nx,ny,newdirect, newexpan))
                else:
                    if (visited[nx][ny] == 0 or visited[nx][ny] > newexpan - 500):
                        visited[nx][ny] = newexpan
                        que.append((nx,ny,newdirect, newexpan))
                    

    # print(expan_list)
    answer = min(expan_list)
    
    return answer