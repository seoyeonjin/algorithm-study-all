def zip(s, match_str, start):
    # print(s, match_str, start)
    end = start + len(match_str)
    cp_str = s[start:end]
    count = 0
    while (match_str == cp_str):
        count += 1
        start = end
        end = end + len(match_str)
        cp_str = s[start:end]
    return count

def solution(s):
    answer = 0
    count_list = []
    for i in range(1, len(s)+1): 
        result_list = []
        result_count = 0
        j = 0
        while (j < len(s)):
            match_str = s[j:j+i]
            start = j + i
            count = zip(s, match_str, start)
            if (count == 0):
                # result_list.append(len(match_str))
                result_count += len(match_str)
            else:
                # result_list.append(1)
                # result_list.append(len(match_str))
                count_str = str(count+1)
                # print(count_str)
                result_count += len(match_str) +len(count_str)
            j = j + (count * i) + len(match_str)
        
        count_list.append(result_count)
    # print(count_list)
    return (min(count_list))
    
    # return answer