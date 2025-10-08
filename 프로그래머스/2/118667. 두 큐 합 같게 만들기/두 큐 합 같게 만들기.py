def solution(queue1, queue2):
    answer = -2 
    all_que = queue1 + queue2
    # print(all_que)
    start = 0
    end = len(queue1) 
    
    qsum = sum(queue1)
    target = qsum + sum(queue2)
    if (target % 2 == 1): 
        return -1
    target = int(target//2)
    cnt = 0
    flag = False
    # print(target)
    while start <= end and end < len(all_que):
        if (qsum < target):
            qsum += all_que[end]
            end += 1
            cnt += 1
        elif (qsum > target): 
            qsum -= all_que[start]
            start += 1
            cnt += 1
        else:
            flag = True
            break
    
    if (flag):
        answer = cnt
    else: 
        answer = -1
        
            
    # 실제로 하면 안 되나? 
    return answer