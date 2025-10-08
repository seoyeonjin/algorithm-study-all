from itertools import permutations
from collections import deque


def solution(expression):
    answer = 0
    eList = []
    al = []
    
    start = 0
    end = 0
    
    op_list = ["*", "-", "+"]
    op_per = permutations(op_list)
    
    # for p in op_per:
    #     print(p)
    while end < len(expression):
        if (expression[end].isdigit()): # 숫자면
            end += 1
        else:
            num = expression[start:end]
            eList.append(int(num))
            eList.append(expression[end])
            start = end + 1
            end += 1
    eList.append(int(expression[start:end]))
    
    
    for opp in op_per: # 각 연산자 우선순위 마다
        s_que = deque(eList)
        d_que = s_que # 다 초기화한다음에
        
        for op in opp: # 하나씩 꺼내서 먼저 연산한다 그리고 결과의 절댓값을 al에 저장한다
            s_que = d_que
            d_que = deque() # 얘는 초기화해 
            while s_que:
                e = s_que.popleft()
                if (e == op): 
                    num1 = d_que.pop()
                    num2 = s_que.popleft()
                    if (op == "*"):
                        result = num1 * num2
                    elif (op == "-"):
                        result = num1 - num2
                    else:
                        result = num1 + num2
                    d_que.append(result)
                else:
                    d_que.append(e)
        final_result = d_que.popleft() # 최종 값
        al.append(abs(final_result))
                    
    answer = (max(al))
    # print(start, end, len(expression))
    # print(eList)
    return answer