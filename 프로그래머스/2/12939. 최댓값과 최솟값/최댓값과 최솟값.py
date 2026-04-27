def solution(s):
    answer = ''
    
    # 최소 최대 return
    sList = list(map(int, s.split(" ")))
    print(sList)
    answer = str(min(sList)) + " " + str(max(sList))
    return answer