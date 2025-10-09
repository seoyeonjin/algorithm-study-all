from collections import deque

def solution(info, query):
    answer = []
    info_dict = {
        'cpp': '0', 'java': '1', 'python':'2',
        'backend': '0', 'frontend': '1', 
        'junior': '0', 'senior':'1',
        'chicken':'0', 'pizza': '1'
    }
    
    p_dict = dict()
    
    for i in info:
        info_list = list(i.split(" ")) # 공백으로 나누고
        key = ""
        for temp in info_list[:-1]:
            key += info_dict[temp]
        num =  int(info_list[-1]) # 가장 마지막
        if (key not in p_dict):
            p_dict[key] = [num]
        else:
            p_dict[key].append(num)
    
    for p in p_dict:
        p_dict[p].sort()
    
    # print(p_dict)
    
    for q in query:
        ql = list(q.split(" "))
        num = int(ql[-1]) # 마지막 거
        
        key_list = []
        key = ""
        cnt = 0
        
        for temp in ql[:-1]:
            if (temp == 'and'):
                continue
            if (temp == '-'): # 상관없다는 어떻게 처리하지?
                key += '-'
            else:
                key += info_dict[temp]
        # dfs(0, key, num)
        
        
        que = deque()
        
        if (key[0] == "-"):
            que.append("0")
            que.append("1")
            que.append("2")
        else:
            que.append(key[0])
        
        while que:
            temp = que.popleft() # 하나 뽑아
            index = len(temp) # 1 에 가서 추가해야돼
            if (index == 4):
                key_list.append(temp)
            else:
                if (key[index] == "-"): 
                    que.append(temp+"0")
                    que.append(temp+"1")
                else:
                    que.append(temp+key[index])       
        
        
        def search(num_list, num): # 기준이 되는 num 보다 크거나 같은 것의 개수
            start = 0
            end = len(num_list)
            # cnt = 0
    
            while start < end:
                # print(num_list, num, start, end)
                mid = int((start+end) // 2 ) # 중간 인덱스 
                if (num_list[mid] < num):
                    start = mid + 1
                elif (num_list[mid] >= num):
                    end = mid
            return len(num_list) - end
            
                
            
        
        for key in key_list:
            # print(key, key_list)
            # print(key in p_dict)
            if key in p_dict:
                p_list = p_dict[key]
                # print(p_list)
                # 이진 탐색?
                cnt += search(p_list, num)
                # for p in p_list:
                #     if (p >= num):
                #         cnt += 1
        answer.append(cnt)

    return answer