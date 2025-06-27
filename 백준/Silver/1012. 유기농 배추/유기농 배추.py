from collections import deque

T = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]


for _ in range(T):
    M, N, K = map(int, input().split())
    bat_list = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(K):
        x, y = map(int,input().split())
        bat_list[y][x] = 1

    bat_que = deque()

    for i in range(N):
        for j in range(M):
            if (bat_list[i][j] == 1 and not visited[i][j]):
                count += 1
                visited[i][j] = 1
                bat_que.append([i,j])

            while bat_que:
                x, y = bat_que.popleft()
                for d in range(4):
                    new_x = dx[d] + x
                    new_y = dy[d] + y
                    if (new_x < 0 or new_x >= N or new_y < 0 or new_y >= M):
                        continue
                    else:
                        if (bat_list[new_x][new_y] == 1 and not visited[new_x][new_y]):
                            bat_que.append([new_x,new_y])
                            visited[new_x][new_y] = 1

    print(count)
                
