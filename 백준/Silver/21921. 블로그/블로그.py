# 누적합이 최대가 되는? 부분들이 몇개가 있냐.. 0개면 SAD

N, X = map(int ,input().split())

visitor_list = list(map(int ,input().split()))

prefix_list = [0] * (N+1)   

for i in range(N):
    prefix_list[i+1] = prefix_list[i] + visitor_list[i] 

# print(prefix_list)
result_list = []
end = X
while end <= N:
    start = end - X
    result_list.append(prefix_list[end] - prefix_list[start])
    end += 1

if (result_list and max(result_list)):
    print(max(result_list))
    print(result_list.count(max(result_list)))
else:
    print("SAD")