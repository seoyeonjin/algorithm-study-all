n = int(input())
num_list = []

for i in range(n):
    a = int(input())
    num_list.append(a)

# num_list안에 제일 작은 거 * n개 -> 최대 중량
num_list.sort()
result_list = [] 

for i in range(n):
    a = num_list[i]
    weight = a * (n-i)
    result_list.append(weight)
print(max(result_list))