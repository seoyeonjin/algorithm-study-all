import math

def solution(numbers):
    answer = []
    
    def dfs(temp):
        # print(temp)
        if (len(temp) > 1):   
            mid = len(temp) // 2
            if (temp[mid] == "0" and "1" in temp):
                return 0
            else: # 1이면 나머지에 대해 검사
                r1 = dfs(temp[:mid])
                r2 =  dfs(temp[mid+1:])
                if (r1 == 0 and "1" in temp[:mid]): # 자식 중 0이 있으면서 0이면
                    return 0
                if (r2 == 0 and "1" in temp[mid+1:]):
                    return 0
                return 1
        else:
            return 1
                
    # 중위 순회
    for n in numbers:
        # 몇자리 필요한지 a확인
        bin_n = bin(n)[2:]
        k = 1
        while (2 ** k - 1) < len(bin_n):
            k += 1
        full_bin = bin_n.zfill(2 ** k - 1)
        # k = math.ceil(math.log(len(bin_n), 2))
        # full_bin = "0" * (2**k-1-(len(bin_n))) + bin_n
        # print(full_bin)
        # 중위 순회하는데 
        
        result = dfs(full_bin)
        # print(result)
        if (result == 0):
            answer.append(0)
        else: 
            answer.append(1)
    
    return answer