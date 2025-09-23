from collections import deque

def solution(board):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    answer = 0
    
    que = deque()

    cnt = 0
    cnt_list = [[0 for i in range(25)] for j in range(25)] 
    que.append((0,0,-1, cnt))
    visited = [[0 for i in range(25)] for j in range(25)] 
    visited[0][0] = 1
    
    n = len(board)
    
    while que:
        print(que)
        for c in cnt_list[:3]:
            print(c[:3])
        a,b, direct, cnt = que.popleft()
        if (a == n-1 and b == n-1):
            print(cnt)
        #     cnt_list.append(cnt)
        # else:
        for i in range(2): # 세로로 움직일 때
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0):
                if (direct == 0 or direct == -1):
                    cnt_list[nx][ny] = min(cnt_list[a][b] +100, cnt+100)
                    if not visited[nx][ny]:
                        que.append((nx, ny, 0, cnt_list[nx][ny]))
                        visited[nx][ny] = 1
                else:
                    cnt_list[nx][ny] = min(cnt_list[a][b] +600, cnt+600)
                    
                    if not visited[nx][ny]:
                        que.append((nx, ny, 0, cnt_list[nx][ny]))
                        visited[nx][ny] = 1
        for i in range(2,4): # 가로로 움직일 때
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0):
                if (direct == 1 or direct == -1):
                    cnt_list[nx][ny] = min(cnt_list[a][b] +100, cnt+100)
                    if not visited[nx][ny]:
                        que.append((nx, ny, 1, cnt_list[nx][ny]))
                        visited[nx][ny] = 1
                else:
                    cnt_list[nx][ny] = min(cnt_list[a][b] +600, cnt+600)
                    
                    if not visited[nx][ny]:
                        que.append((nx, ny, 1, cnt_list[nx][ny]))
                        visited[nx][ny] = 1

        # for i in range(2, 4): # 가로로 움직일 때
        #     nx = a + dx[i]
        #     ny = b + dy[i]
        #     if (0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny]):
        #         if (direct == 1 or direct == -1):
        #             que.append((nx, ny, 1, cnt + 100))
        #         else:
        #             que.append((nx, ny, 1, cnt + 600))
        #         visited[nx][ny] = 1
    # print(cnt_list)
    # print(cnt_list[n-1][n-1])
  
    return answer