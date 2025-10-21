def solution(queue1, queue2):
    answer = -2
    
    que = queue1 + queue2 
    # print(que)
    cnt = 0
    
    start = 0
    end = len(queue1) -1
    target = int(sum(que) // 2 )
    
    init = sum(que[start:end+1]) # 처음 sum
    
    while start <= end and end < len(que)-1:
        if (init < target):
            end += 1
            init += que[end]
            cnt += 1 
        elif (init > target):
            init -= que[start]
            start += 1
            cnt += 1
        else:
            return cnt
    # print(cnt)
    return -1
    # return answer