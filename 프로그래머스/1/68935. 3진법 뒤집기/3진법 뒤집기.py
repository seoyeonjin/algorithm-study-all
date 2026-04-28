def solution(n):
    answer = 0
    
    def to_3(a):
        result = ""
        while a:
            b = a % 3
            a = a // 3
            result += str(b)
        return result[::-1]
    
    def to_10(a):
        b = 1
        result = 0
        for aa in a:
            # print(aa, result)
            result += int(aa) * b
            b = b * 3
        return result
    
    t = to_3(n)
    answer = to_10(t)
    
    
    
    # print(t)
    return answer