# 연속된 자연수의 합으로 나타내는 가지수가 알고싶다. 

N = int(input())


num_list = [i for i in range(1,N+1)]

start = 0
end = 0
sum = num_list[0]
count = 0 
while end < N-1:
    if (sum == N):
        count += 1
        sum = sum - num_list[start] + num_list[end+1]
        start += 1
        end += 1
    elif (sum < N):
        sum = sum + num_list[end+1]
        end += 1
    else:
        sum = sum - num_list[start]
        start += 1
print(count+1)