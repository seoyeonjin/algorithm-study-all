import math

def solution(n, m):
    answer = []
    # 최대 공약수 찾기
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    gg = gcd(n,m)
    mg = m * n  // gg
    
    answer = [gg,mg]
    return answer