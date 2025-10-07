def solution(record):
    answer = []
    user_dict = dict()
    # 가상 닉네임 사용
    # 관리자 창
    # 
    result_stack = []
    
    for r in record:
        cmd_list = list(r.split(" "))
        # print(cmd_list)
        if (cmd_list[0] == "Enter"): # 들어오는 경우 
            user_dict[cmd_list[1]] = cmd_list[2]
            result_stack.append((1, cmd_list[1])) 
        elif (cmd_list[0] == "Leave"): # 떠나는 경우 
            result_stack.append((2, cmd_list[1]))
        elif (cmd_list[0] == "Change"): # 이름 바꾸는 경우 
            user_dict[cmd_list[1]] = cmd_list[2]
    
    for r in result_stack: 
        a,b = r
        if (a == 1): 
            answer.append(user_dict[b] + "님이 들어왔습니다.")
        else:
            answer.append(user_dict[b] +"님이 나갔습니다.")
    return answer