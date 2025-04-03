N, Q = map(int, input().split())     # 땅 개수, 오리 수

ground_list = []
result_list = [0] * (N+1) # 땅 개수만큼 초기화 1번 땅부터 시작함...

for _ in range(Q):
    n = int(input())
    ground_list.append(n)   # 원하는 땅 번호

for ground in ground_list: # Q
    temp_list = []
    temp = ground
    while temp > 1: # 원하는 땅 a까지 가면서 
        if (result_list[temp]):
            temp_list.append(temp)
        temp = int(temp /2)
    if (temp_list):
        print(min(temp_list))
    else: 
        result_list[ground] = 1
        print(0)
    # print(ground ,result_list)

