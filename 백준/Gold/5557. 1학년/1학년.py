N = int(input()) 
num_list = list(map(int, input().split()))

dp = [[0 for i in range(21)] for j in range(N)] # N만큼 갈 수 있음 
dp[0][num_list[0]] = 1

# print(dp)

for i in range(1, N-1):
    for j in range(21): 
        if (dp[i-1][j]):
            sub = j - num_list[i]
            plus =j + num_list[i]
            # print(i,j , dp[i-1][j] , sub, plus)
            if (plus <= 20):
                dp[i][plus] +=  dp[i-1][j]
            if (sub >= 0):
                dp[i][sub] +=  dp[i-1][j]
print(dp[N-2][num_list[-1]])
            
