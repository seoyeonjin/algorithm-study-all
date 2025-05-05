# 두 수의 합이 일치하는 거.. 찾기.. 

n = int(input())
num_list = list(map(int, input().split()))
result = int(input())   

# 정렬을 해볼까.
num_list.sort() 

start = 0
end = len(num_list)-1
count = 0

while start < end:
    sum =num_list[start] + num_list[end]
    if (sum == result):
        count += 1
        start += 1
        end -= 1
    elif (sum < result):
        start += 1
    elif (sum > result):
        end -= 1
print(count)