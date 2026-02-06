from itertools import combinations, chain
import copy

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
lab_list = []
cnt_list = []

for i in range(n):
    lab_list.append(list(map(int, input().split())))

# 0의 좌표 중 3가지를 골라서 조합
zero = [(x, y) for x in range(n) for y in range(m) if lab_list[x][y] == 0]
combi = list(combinations(zero, 3))

# lab_list2 = copy.deepcopy(lab_list)
# lab_list2[0][0] = 3

for com in combi:
    # lab_list2 초기화?
    lab_list2 = copy.deepcopy(lab_list)
    # print(lab_list2)
    for i in range(3):
        x, y = com[i]
        lab_list2[x][y] = 1

    virus = [(x, y) for x in range(n)
             for y in range(m) if lab_list2[x][y] == 2]
    while virus:
        x_v, y_v = virus.pop()
        for dx, dy in direction:
            nx = x_v + dx
            ny = y_v + dy
            if 0 <= nx < n and 0 <= ny < m and lab_list2[nx][ny] == 0:
                lab_list2[nx][ny] = 2
                virus.append((nx, ny)) 
    cnt = sum(lab_list2, []).count(0)
    cnt_list.append(cnt)

print(max(cnt_list))
