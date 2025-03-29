# Q이면 -> 원하는 곳 모두 이동할 수 있음. 장애물이 있는지만 보면 됨
# K이면 -> 꼭짓점으로 이동할 수 있음.
# P이면 -> 장애물 역할만 할 수 있음. 그 위치만 제외하면 됨

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)] # arr

q_arr = list(map(int, input().split()))

for i in range(q_arr[0]):
    arr[q_arr[i*2+1]-1][q_arr[i*2+2]-1] = "Q"

k_arr = list(map(int, input().split()))

for i in range(k_arr[0]):
    arr[k_arr[i*2+1]-1][k_arr[i*2+2]-1] = "K"
    
p_arr = list(map(int, input().split()))

for i in range(p_arr[0]):
    arr[p_arr[i*2+1]-1][p_arr[i*2+2]-1] = "P"
 

q_direction = [(-1,0), (1,0), (0,1),(0,-1), (1,-1), (-1,1), (1,1), (-1,-1)]
k_direction = [(2, -1), (2, 1), (1, 2), (1, -2), (-2,-1), (-2,1), (-1,2), (-1,-2)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == "Q":
            for d in q_direction: # 모든 방향에 대해서
                count = 1
                while True:
                    new_x = i + d[0] * count
                    new_y = j + d[1] * count
                    count += 1
                    if (0 <= new_x < n and 0 <= new_y < m and (arr[new_x][new_y] == 1 or arr[new_x][new_y] == 0)):
                        arr[new_x][new_y] = 1 # 갈 수 있는 곳
                    else:
                        break
        elif arr[i][j] == "K":
            for k in k_direction:
                new_x = i + k[0] 
                new_y = j + k[1] 
                if (0 <= new_x < n and 0 <= new_y < m and (arr[new_x][new_y] == 1 or arr[new_x][new_y] == 0)):
                    arr[new_x][new_y] = 1 # 갈 수 있는 곳

print(sum(arr, []).count(0))