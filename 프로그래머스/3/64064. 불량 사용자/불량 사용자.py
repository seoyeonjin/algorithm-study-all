final_result  = []

def is_equal(id, str):
    flag = True
    if (len(id) == len(str)):
        for i in range(len(str)):
            if (str[i] == "*"):
                continue
            else:
                if (str[i] != id[i]):
                    flag = False
    else:
        flag = False     
    return flag

def dfs(b_i, visited, user_id, result, banned_id):
    if (b_i >= len(banned_id)):
        # result.sort()
        # if (result not in final_result):    
        final_result.append([*result])
        return result
    for i in range(len(user_id)):
        id = user_id[i]
        if (is_equal(id, banned_id[b_i]) and not visited[i] and id not in result):
            result.append(id)
            visited[i] = 1
            dfs(b_i+1, visited, user_id, result, banned_id)
            visited[i] = 0
            result.pop()


# 몇가지 경우의 수가 가능하냐? 
def solution(user_id, banned_id):
    answer = 0
    visited = [0] * len(user_id)
    
    ban_index = 0
    result = dfs(ban_index, visited, user_id, [], banned_id)
    # print(final_result)
    temp = []
    
    for fr in final_result:
        fr.sort()
        if (fr not in temp):
            temp.append(fr)
    answer = len(temp)
    
    return answer