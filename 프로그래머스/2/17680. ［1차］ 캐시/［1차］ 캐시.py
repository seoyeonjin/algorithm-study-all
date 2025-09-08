from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cnt = 0
    caches = deque()
    
    for c in cities:
        c = c.upper()
        if c not in caches:
            if (len(caches) < cacheSize):
                caches.append(c)
                answer += 5
            else:
                if (cacheSize != 0):
                    caches.popleft()
                    caches.append(c)
                    answer += 5
                else: 
                    answer += 5
        else:
            caches.remove(c)
            caches.append(c)
            answer += 1
    return answer