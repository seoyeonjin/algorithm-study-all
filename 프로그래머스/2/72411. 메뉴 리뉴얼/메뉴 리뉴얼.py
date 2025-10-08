from itertools import combinations

def solution(orders, course):
    answer = []
    
    alpha = set()
    for o in orders:
        for a in o:
            alpha.add(a)
    alpha = sorted(alpha)
    # print(alpha)
    
    def is_exist(com, order): 
        # 모든 com에 있는 요소들이 order에 들어가 있어? 
        flag = True
        order = set(order)
        for c in com:
            if (c not in order): 
                flag = False
                return False
        return flag 
    
    for c in course:
        combos = []
        for order in orders:
            order = sorted(order)
            combos += combinations(order, c)
        com_dict = dict() 
        max_cnt = -1
        for com in combos:
            # print(com)
            # 각 조합에 대해서 모든 원소가 orders의 o 안에 있는지 확인한다
            cnt = 0 # 주문 횟수가 가장 많은 거 찾아야 하는데 ... 
            for o in orders: 
                exist = is_exist(com, o)
                if (exist):
                    cnt += 1 
            com_dict["".join(com)] = cnt
            max_cnt = max(cnt, max_cnt) # 가장 큰 cnt를 찾는다 
        # print(max_cnt)
        if (max_cnt >= 2):
            for c in com_dict:
                if (com_dict[c] == max_cnt):
                    answer.append(c)
    
#     com_list = combos
#     for c in course: # 코스 개수마다 가장 max_cnt 에 대해서만 메뉴를 넣으면 됨
#         # com_list = combinations(alpha, c)
        
        
        # 각 코스에 대해서
    answer.sort()
    return answer