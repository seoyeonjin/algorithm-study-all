# 보석은 M가지 색상
# N명의 학생에게 나누어주려고 함

# 학생은 항상 같은 색상의 보석만 가져감
# 가장 많은 보석을 가져간 학생이 가진 보석의 개수 == 질투심
# 질투심이 최소가 되어야 함

N, M = map(int, input().split())
KList = []

for i in range(M):
    K = int(input())
    KList.append(K) 


# 한 학생은 같은 수의 보석만 가져갈 수 있음
# 만약에 최대 4개씩 가진다고 하면 -> 가져갈 수 있음
# 만약에 2개 가져간다고 하면 -> 모두가 나눠가질 수 없음
# 만약에 3개 가져간다고 하면 -> 3 1 3 3 1 -> 나눠가질 수 있음 -> 최소 3이어야 함

min_k = max(KList)
left = 1
right = min_k
ans = 1e9 + 1

while left <= right:
    mid = (left + right) // 2 
    cnt = 0

    # print(left, right, mid)
    for i in range(M):
        a = KList[i]
        cnt += a // mid
        if (a % mid != 0):
            cnt += 1

    if (cnt > N): # 더 많은 양씩 가져가야 함
        left = mid + 1
    else:
       ans = min(ans, mid)
       right = mid -1 
print(ans)