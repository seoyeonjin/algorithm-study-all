def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    def find():
        result = [[0 for i in range(n)] for i in range(m)] #없어질 수 있는 칸에 -1 표시하기 
        
        for i in range(m-1):
            for j in range(n-1): # 돌면서
                if (board[i][j] != "0"):
                    a = board[i][j]
                    b = board[i+1][j]
                    c = board[i][j+1]
                    d = board[i+1][j+1] 
                    if (a == b and c == d and a ==c ): 
                        result[i][j] = -1
                        result[i+1][j] = -1
                        result[i][j+1] = -1
                        result[i+1][j+1] = -1
        return result
    
    # result = find()
    # print(result)
    total_cnt = 0
    while True:
        result = find() # 찾기
        
        # 종료 조건
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt += result[i][j]
        if (cnt == 0):
            break
        
        # 보드 업데이트하기
        total_cnt += cnt
        for i in range(m):
            for j in range(n):
                if (result[i][j] == -1):
                    board[i][j] = "0" 
        for i in range(n):
            temp = []
            temp_cnt = 0
            for j in range(m): 
                # print(j,i, board[j][i])
                if (board[j][i] != "0"): 
                    temp.append(board[j][i]) # 있는 것만 모아둔 temp 리스트를 만든닫 
                else:
                    temp_cnt += 1
            for j in range(m):
                if (j < temp_cnt): 
                    board[j][i] = "0"
                else: 
                    board[j][i] = temp[j-temp_cnt]
        
                    
                    
    # print(total_cnt)
    # print(board)
       
    for i in range(m):
        for j in range(n):
            if (board[i][j] == "0"): 
                answer += 1


    
    return answer