from collections import deque


n = int(input())    

dol_list = list(map(int, input().split()))
start, end = map(int ,input().split())  
start -= 1
end -= 1

que = deque()

que.append((start, 0))

while que:
    new_start, count = que[0]
    que.popleft()
    if (new_start == end):
        print(count)
        exit()
    next_start = new_start
    while 0 <= next_start < n:
        next_start += dol_list[new_start]
        que.append((next_start, count+1))
    next_start = new_start
    while 0 <= next_start < n:
        next_start -= dol_list[new_start]
        que.append((next_start, count +1))

print(-1)