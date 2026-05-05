import heapq

def solution(scoville, K):
    answer = 0
    
    # 섞은 음식의 스코빌 지수 = 가장 안 매운 + (두번째로 안 매운 * 2)
    
    # K 이상이 될 때까지 섞는다. 
    # heap?
    
    heapq.heapify(scoville) 
    sc = 0
    while scoville:
        # print(heap)
        # 만약 heap 에서 뺄 수 있는 게 1면?
        if (len(scoville) == 1):
            if (scoville[0] >= K):
                return answer
            else:
                answer = -1
                return answer
        
        temp1 = heapq.heappop(scoville)
        
        if (temp1 >= K):
            return answer
        
        temp2 = heapq.heappop(scoville)
        
        new = temp1 + temp2 * 2
        heapq.heappush(scoville, new)
        
        answer += 1
    
    # answer = heapq.heappop(heap)
    
    return -1