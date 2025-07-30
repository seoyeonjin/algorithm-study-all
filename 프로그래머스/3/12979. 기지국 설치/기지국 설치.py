def solution(n, stations, w):
    answer = 0
    ap_list = []
    
    s = 1
    e = n
    
    for st in stations:
        start = st - w 
        if (start < 1):
            start = 1
        end = st + w
        if (end > n):
            end = n
        if (s < start): 
            ap_list.append((s, start))
        s = end + 1
    if (end != n):
        ap_list.append((end+1, n+1))
    print(ap_list)
    
    for ap in ap_list:
        s, e = ap
        num = e - s
        div_num = num // (2*w+1)
        mod_num = num % (2*w+1)
        if (mod_num != 0):
            div_num += 1
        answer += div_num
    

#     ap_list = [0] * (n+1)
    
#     for st in stations:
#         start = st - w 
#         if (start < 0):
#             start = 0
#         end = st + w
#         if (end > n):
#             end = n
#         for i in range(start, end+1):
#             ap_list[i] = 1      
#     start = 1
#     while (start <= n):
#         if (ap_list[start] == 0):
#             answer += 1
#             end = start + (2*w)
#             if (end > n):
#                 end = n
#             start = end + 1
#         else:
#             start += 1

    # for i in range(1, n+1):
    #     if (ap_list[i] == 0):
    #         answer += 1
    #         end = i + (2* w)
    #         if (end > n):
    #             end = n
    #         for j in range(i, end+1):
    #             ap_list[j] = 1

    return answer