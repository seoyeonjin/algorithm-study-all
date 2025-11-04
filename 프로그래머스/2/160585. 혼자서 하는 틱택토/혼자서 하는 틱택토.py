def solution(board):
    answer = 1
    # 3개가 같은 표시 가로, 세로, 대각선 O, X
    # 9칸이 다 칠해지면 무승부
    
    # 머쓱이 혼자한다.
    # 규칙을 어겼을 수도 있다. 
    # O,X 순서 헷갈림 or 이겼는데도 게임 진행
    # 혼자 진행했을 때 나올 수 있는 상황인지 판단
    
    # 선공이 O다 -> O의 개수보다 X의 개수가 항상 적거나 같아야 함
    # X가 더 많으며 안 됨
    
    # 만약에 개수가 같으면 -> 마지막에 X까지 놓고 끝난 상황
    # O가 3개 있으면 안 됨
    
    # 만약에 개수가 다르면 -> 마지막에 O까지 놓고 끝난 상황
    # X가 3개 있으면 안 됨
    def tic(tg):
        # 각 상황에 대해서 어떻게 효율적으로 확인하지?
        # 가로, 세로
        for i in range(3):
            cnt = 0
            cnt2 = 0
            for j in range(3):
                if (board[i][j] == tg):
                    cnt += 1
                if (board[j][i] == tg):
                    cnt2 += 1
            if (cnt == 3 or cnt2 == 3):
                return 1
        # 대각선
        if (board[0][0] == tg and board[1][1] == tg and board[2][2] == tg):
            return 1
        if (board[0][2] == tg and board[1][1] == tg and board[2][0] == tg):
            return 1
        
        return 0
        
    
    cntO, cntX = 0,0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "O"):
                cntO += 1
            elif (board[i][j] == "X"):
                cntX += 1
    
    if (cntO < cntX):
        return 0
    
    if (cntO == cntX):
        # O가 연속 3개 있는지 확인
        result = tic("O")
        # print(cntO, cntX, result)
        if (result == 1): return 0
    else:
        if (cntO == cntX + 1): 
            # X가 연속 3개 있는지 확인
            result = tic("X")
            if (result == 1): return 0
        else:
            return 0
    
    return answer