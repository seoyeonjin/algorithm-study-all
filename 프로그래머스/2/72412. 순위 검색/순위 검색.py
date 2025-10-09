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
    # print(p_dict)
    
    for q in query:
        ql = list(q.split(" "))
        num = int(ql[-1]) # 마지막 거
        
        key_list = []
        key = ""
        cnt = 0
        
        def dfs(i, key, num):
            if (i == 4):
                key_list.append(key)
                # if (key in info_dict): 
                #     p_list = info_dict[key]
                #     for p in p_list:
                #         if (p >= num):
                #             cnt += 1 
            else:
                if (i == 0):
                    if (key[i] == '-'): # 아무거나면
                        dfs(i+1, "0"+key[1:], num)
                        dfs(i+1, "1"+key[1:], num)
                        dfs(i+1, "2"+key[1:], num)
                    else:
                        dfs(i+1, key,num)
                else:  # 나머지는
                    if (key[i] == '-'): # 아무거나면
                        dfs(i+1, key[:i] + "0" + key[i+1:], num)
                        dfs(i+1, key[:i] + "1" + key[i+1:], num)
                    else:
                        dfs(i+1, key,num)
            
        
        for temp in ql[:-1]:
            if (temp == 'and'):
                continue
            if (temp == '-'): # 상관없다는 어떻게 처리하지?
                key += '-'
            else:
                key += info_dict[temp]
        dfs(0, key, num)
        
#         while '-' not in key:
            
        
        for key in key_list:
            # print(key, key_list)
            # print(key in p_dict)
            if key in p_dict:
                p_list = p_dict[key]
                # print(p_list)
                for p in p_list:
                    if (p >= num):
                        cnt += 1
        answer.append(cnt)
                
            # print(temp)
    
#     if ('01010' not in p ):
#         p['01010'] = [1]    
#     else:
#         p['01010'].append(2)
#     print(p)
    # for i in info:
    #     for j in query:
    #         answer.append((i,j))
    return answer