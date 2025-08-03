# 가방 무게가 작은 것부터 돌면서, 가능한 후보 중 가장 비싼 걸 선택하려고 한다. (아이디어)

# 결정 순간에서 내가 뭘 최대화(또는 최소화)해야 하는지 정한다.
# -> 내가 최대화 해야 하는 가격

# 제약 조건이 많은 것부터 처리한다.
# -> 제약 조건: 무게

# 처리 순서를 정렬로 만든다.
# -> 둘다 정렬하긴 해야 하는데... 

"""
1. 보석 (무게, 가치) → 무게 오름차순 정렬
2. 가방 → 무게 오름차순 정렬
3. 가방 하나씩 처리:
   - 현재 가방이 담을 수 있는 모든 보석을 후보 힙에 넣음 (가치 최대 힙)
   - 후보 힙에서 가장 비싼 보석을 선택
"""

import heapq

N, K = map(int, input().split())

mv_list = []
k_list = []

max_v = 0

for _ in range(N):
    m,v = map(int, input().split())
    mv_list.append((m,v))

mv_list.sort()

for _ in range(K):
    k_list.append(int(input()))
k_list.sort()

j = 0

heap = []
        
for i in range(K):
    bag = k_list[i]
    while (j < N and mv_list[j][0] <= bag):
        heapq.heappush(heap, (-mv_list[j][1], mv_list[j][0]))
        j += 1
    if (len(heap) > 0):
        v,m = heapq.heappop(heap)
        v = -v
        max_v += v
print(max_v)