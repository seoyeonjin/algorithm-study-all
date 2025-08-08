N, S = map(int, input().split())
num_list = list(map(int, input().split()))

start = 0
end = 0
sum = 0
result_list = []

while end < len(num_list):
    if (sum >= S):
        result_list.append(end-start)
        sum = sum - num_list[start]
        start += 1
    else:
        sum = sum + num_list[end]
        end += 1

curr = sum
while curr >= S and start < end:
    result_list.append(end - start)
    curr -= num_list[start]
    start += 1

if (len(result_list) == 0):
    print(0)
else:
    print(min(result_list))