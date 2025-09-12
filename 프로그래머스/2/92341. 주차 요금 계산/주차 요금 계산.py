import math

def calc_s(time):
    m, s= map(int, time.split(":"))
    v = m * 60 + s
    return v

def calc_fee(time,fee):
    # 사용한 초 단위로 나옴
    dtime = fee[0]
    dfee = fee[1]
    m = fee[2]
    f = fee[3]
    if (time <= dtime):
        return dfee
    else:
        v = dfee + math.ceil((time-dtime) /m) * f
        return v

def solution(fees, records):
    answer = []
    cl = []
    time_dict = {}
    
    for r in records:
        a,b,c = r.split(" ")
        if (c == "IN"):
            # time_dict[b] += calc_s(a)
            cl.append((b, calc_s(a)))
        else:
            idx = -1
            for i in range(len(cl)):
                if (cl[i][0] == b):
                    start = cl[i][1]
                    idx = i
            end = calc_s(a)
            time = end - start
            if (b in time_dict):
                time_dict[b] += time
            else:
                time_dict[b] = time
            if (idx >= 0):
                cl.pop(idx)
    for i in range(len(cl)):
        start = cl[i][1]
        end = calc_s("23:59")
        time = end - start
        if (cl[i][0] in time_dict):
            time_dict[cl[i][0]] += time
        else:
            time_dict[cl[i][0]] = time
    
    print(time_dict)
    keys = sorted(time_dict)
    print(keys)
    
    for k in keys:
        answer.append(calc_fee(time_dict[k], fees))
        
    return answer