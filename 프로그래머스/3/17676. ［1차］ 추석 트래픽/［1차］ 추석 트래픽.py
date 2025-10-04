def solution(lines):
    answer = 0
    point = []
    
    def to_time(S):
        A, ms = S.split(".") 
        h, m, s = map(int,A.split(":"))
        time = h * 3600 + m * 60 + s 
        time *= 1000
        time += int(ms)
        return time
    
    def calc_start(et, T):
        T = T * 1000
        st = et - T  + 1      
        return int(st) 
    
    for l in lines:
        date, S, T = l.split(" ")
        end_time = to_time(S)
        start_time = calc_start(end_time, float(T[:-1]))
        point.append((start_time, end_time))
        # 후보를 다 모았다. 
            
    # print(point)
    max_ans = 1
    for i in range(len(point)):
        for t in [point[i][0], point[i][1]]:
            cnt = 0
            for (s, e) in point:
                if s <= t+999 and e >= t:  # 겹치면 카운트
                    cnt += 1
            max_ans = max(max_ans, cnt)
                
    answer = max_ans
    
    return answer
