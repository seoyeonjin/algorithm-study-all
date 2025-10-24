from collections import deque

T = int(input())


for t in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    con_list = []

    # print(sx,sy)

    for _ in range(N):
        x, y = map(int, input().split())
        con_list.append((x,y))

    ends = list(map(int, input().split()))
    ex, ey = ends
    con_list.append((ex,ey))

    que  = deque()
    que.append((sx,sy))
    visited = [(sx,sy)]

    result = False
    while que:
        x, y = que.popleft()
        if (x == ex and y == ey):
            result = True
            break
        for i in range(N+1): # 편의점
            cx,cy = con_list[i]
            # print(abs(x-cx) + abs(y-cy) <= 10000 and (cx,cy) not in visited)
            if (abs(x-cx) + abs(y-cy) <= 1000 and (cx,cy) not in visited): # 갈 수 있으면
                visited.append((cx,cy))
                que.append((cx,cy))
    
    if (result):
        print("happy")
    else:
        print("sad")