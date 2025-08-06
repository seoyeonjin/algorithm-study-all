# 금메달 수
# 금 = 금 > 은
# 금 = 금, 은 = 은 > 동

N, K = map(int, input().split())
num_list = []

temp_list = []
result_list = [0] * 1001

for i in range(N):
    num, gold, silver, dong = map(int, input().split())
    num_list.append((gold, silver, dong, num))

num_list.sort(key= lambda x : (-x[0], -x[1], -x[2]))

count = 0
i = 0

e,f,g = -1,-1,-1
next_count = 1

for num in num_list:
    a,b,c,d = num
    if ((a,b,c) == (e,f,g)):
        result_list[d] = count
        next_count += 1
    else:
        e,f,g = a,b,c
        count = count + next_count
        next_count = 1
        result_list[d] = count
print(result_list[K])