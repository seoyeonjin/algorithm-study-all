from itertools import product

def solution(users, emoticons):
    answer = []
    temp = [10,20,30,40]
    sales = product(temp, repeat=len(emoticons))
    
    for sl in sales: # 순서대로 각 이모티콘 할인율
        total_sub = 0
        total_price = 0
        for u in users:
            user_price = 0
            persent, price = u
            for i in range(len(sl)):
                s = sl[i] # i번째 이모티콘 할인율
                if (s >= persent): # 생각한거보다 높으면 산다
                    user_price += (emoticons[i] * (100-s) / 100)
            if (price <= user_price):
                user_price = 0
                total_sub += 1
            else:
                total_price += user_price
        answer.append((total_sub, total_price))
                    
    
    answer.sort(key=lambda x: (-x[0], -x[1]))        
        
    answer = answer[0]

    return answer