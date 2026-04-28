import heapq

N = int(input())
total = []

for i in range(N):
    temp = list(map(int, input().split()))
    # total.append(temp)
    for t in temp:
        heapq.heappush(total, t)
        if len(total) > N:
            heapq.heappop(total)

print(total[0])