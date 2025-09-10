def calc_s(time):
    h,m,s= map(int, time.split(":"))
    seconds = h * 60 * 60 + m * 60 + s
    return seconds
    
def calc_time(seconds):
    h, div = divmod(seconds, 3600)
    m, s = divmod(div, 60)
    h = str(h)
    m = str(m)
    s = str(s)
    if (len(h) == 1):
        h = "0" + h
    if (len(m) == 1):
        m = "0"  + m
    if (len(s) == 1):
        s = "0" + s
    return ":".join((h,m,s))

def solution(play_time, adv_time, logs):
    ep = calc_s(play_time)
    at = calc_s(adv_time)

    result = [0] * (ep+2)

    for l in logs:
        s, e = l.split("-")
        ss = calc_s(s)
        es = calc_s(e)
        result[ss] += 1
        result[es] -= 1

    for i in range(1, ep+1):
        result[i] += result[i-1] # 펼치기
        
    prefix = [0] * (ep+2)
    for i in range(1, ep+1):
        prefix[i] = prefix[i-1] + result[i-1]

    max_time = 0
    answer_start = 0
    for start in range(0, ep - at + 1):
        total = prefix[start+at] - prefix[start]
        if total > max_time:
            max_time = total
            answer_start = start

    return calc_time(answer_start)

