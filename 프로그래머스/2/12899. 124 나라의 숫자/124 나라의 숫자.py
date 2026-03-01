def solution(n):
    
    result = []
    while n:
        mod = n % 3
        if mod == 0:
            result.append("4")
            n = n // 3 - 1  
        elif mod == 1:
            result.append("1")
            n //= 3
        else: 
            result.append("2")
            n //= 3
            
    return "".join(reversed(result))