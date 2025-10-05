from string import ascii_uppercase

def solution(msg):
    
    def find_w(msg):
        cnt = 1
        msg_list = [] 
        while cnt <= len(msg):
            m = msg[:cnt]
            if m in dict:
                msg_list.append(m)
                cnt += 1
            else:
                break
        msg_list.sort(key=len)
        return msg_list[-1]
    
    answer = []
    dict = {}
    for i, alpha in enumerate(ascii_uppercase):
        dict[alpha] = i + 1
    # print(dict)
    max_dict = 26
    
    while msg:
        w = find_w(msg) # w를 찾았다
        answer.append(dict[w])
        msg = msg[len(w):]
        if (len(msg)):
            max_dict += 1
            neww = w + msg[0]
            dict[neww] = max_dict
        
    return answer