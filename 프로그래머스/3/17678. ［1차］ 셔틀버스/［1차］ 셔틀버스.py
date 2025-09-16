# 23:59에 집에 돌아간다. 

# 1 - 9시에 도착하면 탐
# 2 - 9시 10분에 도착하면 우선순위에 밀려서 못 탐. 사이에 있는 수중(시간 상 pre 와 current 사이)에 m 번째로 작은 수 -1
# 3 - 9시 1분에 우선순위에 밀려서 못 탐. (n*m) 4번째로 작은 수보다 하나 작으면 돼
# 4 - 우선순위에 밀려서 못감. 5번째로 큰 수보다 하나 작으면 돼.?
# 5 - 셔틀버스가 도착하는 마지막에 가있으면 돼 (우선순위 1순위)
# 마지막 예제 - 셔틀버스가 도착하는 마지막에만 가있으면 돼
from collections import deque

def calc_m(time):
    h, m = map(int, time.split(":"))
    m = h * 60 + m
    return m

def calc_t(m):
    h = str(m // 60)
    m = str(m % 60)
    if (len(h) == 1):
        h = "0" + h
    if (len(m) == 1):
        m = "0" +m
    return h + ":" + m
    
def solution(n, t, m, timetable):
    answer = 0
    timetable.sort()
    timeque = deque()
    for i in range(len(timetable)):
        timeque.append(calc_m(timetable[i]))
        timetable[i] = calc_m(timetable[i])
    
    pre = -1
    start = 540  
    last_t = 540 + (n-1) * t
    
    while (start <= last_t):
        if (start == last_t):
            if (len(timetable) < m):
                answer = start
            else:
                max_m = timetable[m-1]
                if (max_m > start):
                    answer = start
                else:
                    answer = max_m - 1
        else:
            temp = []
            temp2 = []
            for i in range(len(timetable)):
                if (pre < timetable[i] <= start and len(temp) < m):
                    temp.append(timetable[i])
                else:
                    temp2.append(timetable[i])
            timetable = temp2
        start = start + t
            
    # while (start <= last_t):
    #     while timeque:
    #         time = timeque.popleft()
            
#     if (last_t == 540):
#         pre_t = 0
#     else:
#         pre_t = 540 + n * (t-2)
    
#     for i in range(timetable):
    print(answer)
    answer = calc_t(answer)
    return answer