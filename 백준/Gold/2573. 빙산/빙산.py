from collections import deque

# 빙산의 정보
N, M = map(int, input().split())
bing = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]


for i in range(N):
    temp = list(map(int,input().split()))
    bing.append(temp)

# 덩이가 2덩이가 되는 최초..

# 한번 돌았는데 또 돌 수 있을 때
# 시작은 무조건 한 덩이다 

def check():
    # 만약 2덩이면 return True
    cnt = 0
    visited = set()
    # print(bing)
    
    for i in range(N):
        for j in range(M):
            # print(i,j, visited)
            if (bing[i][j] != 0 and (i,j) not in visited):
                cnt += 1
                # print(i,j)
                que = deque()
                que.append((i,j))
                visited.add((i,j)) 
                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (0<=nx<N and 0<=ny<M and (nx,ny) not in visited and bing[nx][ny] != 0):
                            visited.add((nx,ny))
                            que.append((nx,ny))
    # print(cnt)
    if (cnt == 1):
        return False
    else:
        return True
                    

cnt = 0
while True:


    # cnt += 1
    temp = [[0 for i in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = bing[i][j]

    for i in range(N):
        for j in range(M):
            if (bing[i][j] != 0): 
                bing_cnt = 0
                for k in range(4):
                    # 사방에 있는 0 개수만큼 녹인다
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if (0<=nx<N and 0<=ny<M and bing[nx][ny] == 0):
                        bing_cnt += 1
                temp[i][j] -= bing_cnt
                if (temp[i][j] < 0):
                    temp[i][j] = 0
    cnt += 1 
    
    for i in range(N):
        for j in range(M):
            bing[i][j] = temp[i][j]

    flag = 0
    for i in range(N):
        for j in range(M):
            if (bing[i][j] != 0):
                flag = 1
    
    # 만약 다 녹았으면
    if (flag == 0):
        print(0)
        break

    result = check()
    if (result):
        print(cnt)
        break
    # print(temp)
    # print(bing, cnt)