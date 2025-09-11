import math

def is_prime(n):
    if (n == 1):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):    
            return False
    return True

def convert(n, k):
    answer = ""
    while n > 0:
        n,b = divmod(n,k)
        answer += str(b)
    return answer[::-1]

def solution(n, k):
    answer = 0
    result = convert(n,k)
    result = result.split("0")
    for r in result:
        if (r == ""):
            continue
        if (is_prime(int(r))):
            answer += 1
    return answer