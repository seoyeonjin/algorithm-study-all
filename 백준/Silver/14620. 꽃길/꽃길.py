import itertools
import math
# 꽃을 심기 위한 최소 비용
# 씨앗이 3개 있음 -> 총 15 공간을 대여해야함 근데 십자 모양으로 5칸 대여해야 함

n = int(input())
dan_list = []
price_list = [[0 for _ in range(n)] for _ in range(n)]
flower_list = []
result_list = []

for i in range(n):
    dan_list.append(list(map(int, input().split())))

direction = [(0,-1), (0,1), (-1,0), (1,0)] # 위치 이동 가능해야 함

def calc_distance(a, b):
    a_x = a[0]
    b_x = b[0]
    a_y = a[1]
    b_y = b[1]

    distance = math.sqrt(pow((a_x - b_x), 2) + pow((a_y - b_y), 2))
    return distance

for i in range(1, n-1):
    for j in range(1, n-1):
        price = dan_list[i][j]
        flower_list.append((i,j))  # 후보
        for d in direction:
            price += dan_list[i+d[0]][j+d[1]]
        price_list[i][j] = price

flower_com_list = itertools.combinations(flower_list,3) # 3개 뽑아서 돌거야

for flower in flower_com_list:
    a = flower[0]
    b = flower[1]
    c = flower[2] 
    
    if (calc_distance(a,b) > 2 and calc_distance(a,c) > 2 and calc_distance(b,c) > 2):
        result_list.append(price_list[a[0]][a[1]] + price_list[b[0]][b[1]] + price_list[c[0]][c[1]])


result_list.sort()

print(result_list[0])