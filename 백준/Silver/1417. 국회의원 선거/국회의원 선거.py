# 국회의원 선거 
# 가장 많은 표를 받으면 당선된다. 

# 다솜이는 기호 1번이다 

# 1번이 가장 높은 득표수를 가져야 한다. 

import heapq


N = int(input())

heap  = []
dasom = int(input())
count = 0
for _ in range(N-1):
    a = int(input())
    heapq.heappush(heap,-a)

while True:
    if (len(heap) != 0): 
        other = heapq.heappop(heap)
        other = -other
        if (other < dasom):
            break
        else:
            dasom += 1
            other -= 1 
            count += 1
            heapq.heappush(heap, -other)
    else:
        break
    
print(count )

