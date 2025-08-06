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
# print(num_list)

num_list.sort(key= lambda x : (-x[0], -x[1], -x[2]))

# print(num_list)
count = 0

for num in num_list:
    a,b,c,d = num
    if ((a,b,c) in temp_list):
        result_list[d] = count
        count += 1
    else:
        temp_list.append((a,b,c))
        count += 1
        result_list[d] = count
print(result_list[K])