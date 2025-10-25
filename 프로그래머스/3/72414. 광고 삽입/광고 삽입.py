def solution(play_time, adv_time, logs):
    answer = ''
    # 가장 많이 보는 구간에 공익광고를 넣는다.
    # 파란색 - 동영상 전체 재생 구간
    # 검은색 - 재생 기록, 각 재생 기록을 구분하는 ID
    # 빨간색 - 최적의 구간. 누적 재생시간이 가장 크다. 재생시간 * 보고 있는 시청자 수
    # play_time: 동영상 재생 시간
    # adv_time: 공익광고 재생시간
    
    def tts(time):
        h, m, s = map(int, time.split(":"))
        seconds = h * 3600 + m * 60 + s
        return seconds
    
    def stt(seconds):
        h = str(seconds // 3600)
        m = str((seconds % 3600) // 60)
        s = str((seconds % 3600) % 60)
        
        if (len(h) == 1):
            h = "0" + h
        if (len(m) == 1):
            m = "0" + m
        if (len(s) == 1):
            s = "0" + s
        return h + ":" + m + ":" + s
    
    play_s = tts(play_time)
    times = [0 for i in range(play_s+2)]
    start_list = [0]
    for l in logs:
        start, end = l.split("-")
        ss = tts(start)
        start_list.append(ss)
        se = tts(end)
        times[ss] += 1
        times[se] -= 1
    
    for i in range(1,len(times)):
        times[i] += times[i-1]
    
    
    # print(tts("1:20:15"))
    # print(tts("02:03:55"))
    # print(times[5458:6314+2])
    # log 는 문자열 배열
    
    # for i in range(len(times)):
    #     times[i] += times[i-1] 

    psum = [0] * (play_s + 2)
    for i in range(play_s):
        psum[i+1]=psum[i]+times[i]
    adv_s = tts(adv_time)
    
    start_list.sort()
    
    max_viewer = 0
    max_start = 0

    # 모든 시작점마다 돌면서
    for s in range(0, play_s-adv_s+1):
        viewer = 0
        if (s + adv_s <= play_s): # 그 안에 끝나면
            viewer = psum[s+adv_s] - psum[s]
        else:
            continue
            # viewer = times[play_s] - times[play_s-adv_s]
        # print(stt(s+adv_s), stt(s), viewer, stt(viewer))
        if (viewer > max_viewer):
            max_viewer = max(viewer, max_viewer)
            max_start = s
        # elif (viewer == max_viewer):
        #     if (s < max_start):
        #         max_start = s
        
    answer = (stt(max_start))
    return answer