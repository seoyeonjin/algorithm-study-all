def solution(number, k):
    answer = ''
    # nCk 라고 하면 이 경우의 수를 다 해보는 건 말이 안 됨
    
    # 앞에서부터 K개까지 최대인 부분까지 지운다. 
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    if k > 0:
        stack = stack[:-k]
        
    answer = "".join(stack)
    
    # 슬라이딩 윈도우 마냥 하면 될 거 같은데
    start = 0
    end = k
    ans = []
    
    # while end < len(number):
    #     ans = []
    #     for i in range(k):
    #         ans.append()
    
#     if (start == end -1):
#         answer = max(number)
#     else: 
#         while start < end-1:
#             # 이 범위에서 최댓값을 찾는다.
#             max_num = max(number[start:end]) 
#             # 최댓값을 ans 에 추가한다.
#             answer += max_num
#             # max_num의 index 찾기
#             idx = number[start:end].index(max_num) 
#             # 최댓값까지 가야하는 거리를 k에서 뺀다.(k 갱신)
#             k -= idx
#             # k != 0이면 더 간다. 
#             if (k == 0):
#                 if (end != len(number)):
#                     answer += "".join(number[end:])
#                 break
#             start = idx + start + 1
#             end = start + k + 1

#             print(start, end)
        # 최댓값 위치 이후로 k개 만큼 가서 또 최댓값을 계산한다.
        
    return answer