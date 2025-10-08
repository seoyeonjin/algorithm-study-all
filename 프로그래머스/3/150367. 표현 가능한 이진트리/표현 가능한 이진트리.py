import math
from collections import deque


def solution(numbers):
    answer = []
    # number를 표현하는 데 필요한 최소 자리수
    for num in numbers: 
        binn = bin(num)
        length = len(binn[2:]) # 자릿수
        # print("length: ", length)
        k = math.ceil(math.log(length+1, 2)) 
        min_length = 2**k -1 # 전체 노드 수

        if (min_length > length):
            str_num = "0"*(min_length - length) + (binn[2:])
        else:
            str_num =  str(binn[2:])
        # print(binn[2:], 2**k-1, str_num)
        # print(str_num , binn[2:]) 
        # str_num = "1011111"
        flag = False
        # 하나라도 0이 있으면 절대 못함
        root = int(len(str_num) // 2)
        move = int((root+1) //2 ) 
        # print(root, move)
        que = deque()
        que.append(str_num)
        while que:
            # print(que)
            sub = que.popleft()
            mid = int(len(sub) // 2) # 중간 인덱스
            left = sub[:mid] # 왼쪽
            right = sub[mid+1:] # 오른쪽
            # print(sub, left, right)
            if (sub[mid] == "0"):
                if "1" in left or "1" in right:
                    flag = True
                    break
            else: 
                if (len(left) != 0):
                    que.append(left)
                if (len(right) != 0):
                    que.append(right)
            # if (move == 0): 
            #     continue
            # else:
            #     if (str_num[root] == "0"): # 0이면 양쪽 다 0이어야 함
            #         if (str_num[root-move] != "0" or str_num[root+move] != "0"): #이러면
            #             flag = True
            #             break
            #     else:
            #         que.append((root-move, int(move//2)))
            #         que.append((root+move, int(move//2)))
        
                    
        # for i in range(1, len(str_num), 2):
        #     if (str_num[i] == "0"): 
        #         if (str_num[i-1] != "0" or str_num[i+1] != "0"): 
        #             flag = True
        if (flag == True): 
            answer.append(0)
        else:
            answer.append(1)

    return answer