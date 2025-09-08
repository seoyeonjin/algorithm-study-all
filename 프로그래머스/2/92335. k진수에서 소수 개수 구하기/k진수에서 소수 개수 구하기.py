import math

def is_prime(a):
    a = int(a)
    if (a == 1):
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if (a % i == 0):
            return False
    return True
    

def convert(n,k):
    result = ""
    while (n > 0):
        a,b = divmod(n,k)
        n = a
        result += str(b)
    return result[::-1]
    

def solution(n, k):
    answer = 0
    result = convert(n,k)
    result = result.split("0")
    for r in result:
        if (r != "" and is_prime(r)):
            answer += 1
    return answer