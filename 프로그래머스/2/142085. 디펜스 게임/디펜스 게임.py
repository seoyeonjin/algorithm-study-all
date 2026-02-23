import heapq

def solution(n, k, enemy):
    heap = []

    for i in range(len(enemy)):
        e = enemy[i]

        # 일단 병사로 막는다고 가정
        n -= e

        # 현재 라운드도 "무적권 후보"에 포함
        heapq.heappush(heap, -e)

        # 병사가 부족할 때
        if n < 0:
            if k == 0: # 더 이상 사용할 수 있는 무적권이 없으면
                return i 
            n += -heapq.heappop(heap) # 무적권 사용
            k -= 1

    return len(enemy)