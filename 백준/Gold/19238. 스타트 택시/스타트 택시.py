# M명의 승객은 빈칸 중 하나에 서 있다. 
# 여러 승객이 같이 탑승하는 경우 없음
from collections import deque

N, M, sfuel = map(int, input().split())
nums = [[0]*(N+1)]
ps = []
visited = set() # 이미 방문한 승객이다

for i in range(N):
    temp = list(map(int, input().split()))
    temp.insert(0,0)
    nums.append(temp)

sx, sy = map(int,input().split())


for i in range(M):
    temp = list(map(int, input().split()))
    x = temp[0]
    y = temp[1]
    nums[x][y] = i + 2
    ps.append(temp)

# 현재 위치 -> 승객이 있는 거리까지의 거리 구하기
# 가장 가까운 거리로 정렬 (dist, 행, 열, pnum) 구조로 하면 정렬되려나? 
# 이동하면서 필요한 연료의 양과 비교 firstD + secondD -> 만약 currentF 가 더 적으면 이동 X 하고 return -1
# 이동 완료 처리: 택시 current위치 이동, 연료 계산 a-b-c+c*2 

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def calc_dist(sx, sy): # 최단거리 계산하기
    que = deque()
    vs = set()
    que.append((sx,sy, 0))
    vs.add((sx,sy))
    temp = []
    while que:
        x, y, cnt = que.popleft() 
        if (nums[x][y] >= 2 and (nums[x][y]-2) not in visited): # 목적지 도착
            temp.append((cnt, x,y, nums[x][y]-2))
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (0<nx<=N and 0<ny<=N and (nx,ny) not in vs and (nums[nx][ny] == 0 or nums[nx][ny] >= 2)):
                que.append((nx,ny, cnt+1))
                vs.add((nx,ny))
    if (len(temp) == 0):
        return -1
    else:
        temp.sort()
        return temp[0]

# ans = calc_dist(sx,sy)
# print(ans)

def calc_dist_two(sx, sy, ax, ay): # 최단거리 계산하기
    que = deque()
    vs = set()
    que.append((sx,sy, 0))
    vs.add((sx,sy))
    while que:
        x, y, cnt = que.popleft() 
        if (x == ax and y == ay): # 목적지 도착
            return cnt 
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (0<nx<=N and 0<ny<=N and (nx,ny) not in vs and (nums[nx][ny] == 0 or nums[nx][ny] >= 2)):
                que.append((nx,ny, cnt+1))
                vs.add((nx,ny))
    return -1 
                
def move(temp, curfuel):
    p = temp[3] # p 넘버
    # sx -> sy 로 이동하는 데 필요한 거리는 person[0]
    dist = calc_dist_two(temp[1], temp[2], ps[p][2],ps[p][3])
    # 필요한 연료 계산
    if (dist == -1):
        return -1 
    fuel = temp[0] + dist
    if (fuel > curfuel):
        return -1
    else:
        return curfuel - fuel + dist * 2 
    

z = 0
while True:
    # 현재 위치로부터 최단 거리 구하기
    temp = calc_dist(sx,sy)

    if (temp == -1):
        if (len(visited) == M):
            print(sfuel)
            exit(0)
        else:
            print(-1)
            exit(0)
    # print(temp)

    curfuel = move(temp, sfuel)
    if (curfuel == -1):
        print(-1)
        exit(0)
    else:
        p = temp[3]
        x = ps[p][0]
        y = ps[p][1]
        nums[x][y] = 0
        visited.add(p)
        sx = ps[p][2]
        sy = ps[p][3]
        sfuel = curfuel
    # print(sx, sy, sfuel)
    
    # z += 1
    # if (z == 2):
    #     break
