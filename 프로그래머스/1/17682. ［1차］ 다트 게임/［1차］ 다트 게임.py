import math

def calc_star(num_list):
    if (len(num_list) == 1):
        num_list[0] *= 2
    elif (len(num_list) > 1):
        num_list[-1] *= 2
        num_list[-2] *= 2
    return num_list

def calc_sharp(num_list):
    num_list[-1] *= (-1)
    return num_list


def solution(dartResult):
    answer = 0
    # 스타상 -> 이번, 저번 점수가 *2
    # 중첩될 수 있음..
    # 아차상 -> 이번이 -1 배
    num_list = []
    point = 0
    for i in range(len(dartResult)):
        if (dartResult[i] == "S"):
            temp = dartResult[point:i]
            if (temp[0] == "*"):
                num_list = calc_star(num_list)
                temp = temp[1:]
            elif (temp[0] == "#"):
                num_list = calc_sharp(num_list)
                temp = temp[1:]
            num = int(temp)
            num_list.append(num)
            point = i+1
        elif (dartResult[i] == "D"):
            temp = dartResult[point:i]
            if (temp[0] == "*"):
                num_list = calc_star(num_list)
                temp = temp[1:]
            elif (temp[0] == "#"):
                num_list = calc_sharp(num_list)
                temp = temp[1:]
            num = math.pow(int(temp),2)
            num_list.append(num)
            point = i+1
        elif (dartResult[i] == "T"):
            temp = dartResult[point:i]
            if (temp[0] == "*"):
                num_list = calc_star(num_list)
                temp = temp[1:]
            elif (temp[0] == "#"):
                num_list = calc_sharp(num_list)
                temp = temp[1:]
            num = math.pow(int(temp),3)
            num_list.append(num)
            point = i+1
    if (dartResult[-1] == "*"):
        num_list = calc_star(num_list)
    elif (dartResult[-1] == "#"):
        num_list = calc_sharp(num_list)
    print(num_list)
    
    for num in num_list:
        answer += int(num)
    return answer