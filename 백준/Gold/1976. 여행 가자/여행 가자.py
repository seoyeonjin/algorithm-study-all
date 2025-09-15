# 여행 경로가 가능한가? 
# 연결해서 도착하는 게 가능한가? 
# 같은 집합 안에 있는가?

N = int(input())
M = int(input())    

city_list = [i for i in range(N)]

def find(a):
    if (city_list[a] == a):
        return a
    else:
        result = find(city_list[a])
        city_list[a] = result
        return result


def union(a,b):
    one = find(a)
    two = find(b)
    min_n = min(one, two)
    max_n = max(one, two)

    city_list[max_n] = min_n # 더 작은 대표 노드로 변경

for i in range(N):
    temp = list(map(int ,input().split()))
    for j in range(len(temp)):
        if (temp[j] == 1):
            union(i,j)


d_list = list(map(int, input().split()))

num = city_list[d_list[0]-1]

for i in range(M):
    n = d_list[i] -1
    if (find(n) == num):
        continue
    else:
        print("NO")
        exit(0)
print("YES")
