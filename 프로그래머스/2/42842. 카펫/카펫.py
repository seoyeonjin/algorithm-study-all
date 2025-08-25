from math import sqrt

def divv(total):
    results = [] 
    for i in range(1,int(sqrt(total))+1) :
        if (total % i == 0):
            results.append((i, total//i))
    return results
            

def solution(brown, yellow):
    answer = []
    # 두개 더하면 총 타일 수 
    # 인수분해 해서
    # 1 2 3 4 6 12 만든다음에 -> 짝 지어서 -2씩 곱한 게 yellow랑 같으면 돼
    total = brown + yellow
    results = divv(total)
    print(results)
    for r in results:
        a,b = r
        if ((a-2) * (b-2) == yellow):
            answer.append(a)
            answer.append(b)
    answer.sort(reverse=True)
    return answer