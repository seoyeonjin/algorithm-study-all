def solution(sticker):
    answer = 0
    
    # [7,3,100,400,1,1] 그러면 이거 dp인가?
    dp = [[0 for i in range(2)] for i in range(len(sticker)+1)]
    dp[0][0] = 0
    dp[0][1] = 0 # 처음 걸 포함하지 않음
    
    dp2 = [[0 for i in range(2)] for i in range(len(sticker)+1)]
    dp2[0][0] = 0
    dp2[0][1] = sticker[0] # 처음 걸 항상 포함함
    
    for i in range(1,len(sticker)):
        dp[i][0] = max(dp[i-1][1],dp[i-1][0])
        dp[i][1] = dp[i-1][0] + sticker[i]
        
        dp2[i][0] = max(dp2[i-1][1],dp2[i-1][0])
        dp2[i][1] = dp2[i-1][0] + sticker[i]
    
    answer = max(dp[len(sticker)-1][1], dp2[len(sticker)-1][0])
    if (len(sticker) == 1):
        answer = sticker[0]
    return answer