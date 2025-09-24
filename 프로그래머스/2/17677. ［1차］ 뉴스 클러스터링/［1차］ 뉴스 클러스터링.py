def make_set(str):
    temp = []
    for i in range(len(str)-1):
        sub = str[i:i+2]
        if (sub.isalpha()):
            temp.append(sub.upper())
    return temp

def solution(str1, str2):
    answer = 0
    # 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
    a = make_set(str1)
    b = make_set(str2)
    inter = 0
    inter_list = []
    for i in range(len(a)):
        if (a[i] in b and a[i] not in inter_list):
            inter += min(a.count(a[i]), b.count(a[i]))
            inter_list.append(a[i])
    union = len(a) + len(b) - inter
    
    if (union == 0):
        answer = 1
    else:
        answer = inter / union
    
    answer = int(answer * 65536)
    return answer