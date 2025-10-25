import heapq

def solution(stones, k):
    answer = 0
    max_list = []
    
    # 구간 k 중에 가장 큰 값을 어떻게 효과적으로 찾을 수 있지..?
    # 우선순위 큐로 저장하면 자동으로 가장 큰 값이 나오지 않나?
    # 
    start = 0 
    end = k
    answer = max(stones[start:end]) # 초기화
    heap = []
    
    
    for i in range(start, end):
        heapq.heappush(heap, (-stones[i], i))
        
    
    while end < len(stones): # 이동하면서
        # heap.remove(-stones[start])
        # print(answer)
        start += 1
        heapq.heappush(heap, (-stones[end], end))
        
        while heap:
            h = heap[0][1]
            max_num = -heap[0][0]
            # print(heap[0],start)
            if (h < start):
                heapq.heappop(heap)
            else:
                break
          
        # print(start, heap)
        answer = min(-heap[0][0], answer)
        end += 1
    
    
    return answer