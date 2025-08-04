def solution(A, B):
    answer = -1
    
    A.sort()
    B.sort()
    
    # 1 3 5 7
    # 2 2 5 8 
    count = 0
    
    j = 0
    for i in range(len(A)):
        min_num = 1000000001
        min_index = -1
        while j < len(B):
            if B[j] > A[i]:
                j += 1
                count += 1
                break
            else:
                j += 1
        
        # for j in range(len(B)):
        #     if (B[j] > A[i]):
        #         if (min_num > B[j]):
        #             min_num = B[j]
        #             min_index = j
        # if (min_index == -1):
        #     del B[0]
        # else: 
        #     del B[min_index]
        #     count += 1
    
    return count