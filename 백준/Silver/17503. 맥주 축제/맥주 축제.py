import heapq

N, M, K = map(int, input().split())
beer_list = []

for i in range(K):
    v, c = map(int, input().split()) # 선호도, 도수
    # N개의 맥주를 모두 마셔야 함 -> N개.... 
    # K개 중에 뭐부터 먹어야 돼? 도수가 작은 것부터 N개
    beer_list.append((v,c)) 
    # 선호도 합을 채울 때까지 먹는다

# 도수가 낮은 순으로 정렬 
beer_list.sort(key=lambda x: (x[1]))

heap = []
total_v = 0
answer = -1
# print(beer_list)
for beer in beer_list:
    v,c =beer
    total_v += v
    heapq.heappush(heap, v)

    # print(heap, total_v)
    if (len(heap) > N): # 그 이상으로 먹었으면 선호도가 가장 낮은 거 하나 빼기
        v = heapq.heappop(heap)
        total_v -= v
    # print(heap)
    if (total_v >= M and len(heap) == N): # 먹었으면 
        answer = c
        break

print(answer)