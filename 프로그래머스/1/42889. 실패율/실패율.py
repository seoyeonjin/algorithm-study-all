def solution(N, stages):
    answer = []
    people = len(stages)
    temp = [0] * (N+2)
    
    for i in range(people):
        num = stages[i]
        temp[num] += 1
    
    for i in range(1, N+1):
        cnt = temp[i]
        total = sum(temp[i:])
        if (total == 0):
            result = 0
        else:
            result = cnt/total
        answer.append((result, i))
        
    answer.sort(key=lambda x: (-x[0], x[1]))
    for i in range(len(answer)):
        answer[i] = answer[i][1]
    return answer