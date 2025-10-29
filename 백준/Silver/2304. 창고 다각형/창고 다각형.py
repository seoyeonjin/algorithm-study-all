import heapq

N = int(input())
bar_list = []
heap = []
ans = 0

for _ in range(N):
    l, h = map(int,input().split())
    bar_list.append((h, l)) 
    heapq.heappush(heap, (h,l))
bar_list.sort(reverse=True)

# print(bar_list)

ans += bar_list[0][0] # 높이 

lefts =[]
rights = [] 

for i in range(1, N):
    if (bar_list[i][1] < bar_list[0][1]): # 더 작으면
        lefts.append(bar_list[i])
    else:
        rights.append(bar_list[i])

# print(lefts, rights)
def left_sub(bars, end):
    if (len(bars) == 0):
        return 0
    # 현재 bars의 최댓값 찾기
    bars.sort(reverse=True)
    max_h = bars[0][0] 
    # 여기까지 면적 계산하기
    temp = (end - bars[0][1]) * max_h
    # x 좌표가 더 작은 것듦만 구하기
    sub_bars = []
    for i in range(1, len(bars)):
        if (bars[i][1] < bars[0][1]):
            sub_bars.append((bars[i][0], bars[i][1]))
    return temp + left_sub(sub_bars, bars[0][1])


def right_sub(bars, start):
    if (len(bars) == 0):
        return 0
    # 현재 bars의 최댓값 찾기
    bars.sort(reverse=True)
    max_h = bars[0][0] 
    # 여기까지 면적 계산하기
    temp = (bars[0][1]+1-start) * max_h
    # print(temp,bars[0][1], start, max_h)
    sub_bars = []
    for i in range(1, len(bars)):
        if (bars[i][1] > bars[0][1]):
            sub_bars.append((bars[i][0], bars[i][1]))
    return temp + right_sub(sub_bars, bars[0][1]+1)

ans += left_sub(lefts, bar_list[0][1])
# print(result1) 
ans += right_sub(rights, bar_list[0][1]+1)
print(ans)