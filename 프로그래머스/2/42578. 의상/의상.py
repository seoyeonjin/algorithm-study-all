from collections import defaultdict

def solution(clothes):
    answer = 1
    wears = defaultdict(int)
    
    # 가능한 조합의 개수를 가져온다
    
    for c, kind in clothes:
        wears[kind] += 1
        
    # print(wears)
    
    for w in wears:
        answer *= (wears[w] + 1)
        
    return answer -1