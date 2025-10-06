import math

def solution(board, skill):
    answer = 0
    row = len(board)
    col = len(board[0])
    
    temp = [[0 for i in range(col)] for j in range(row)]
    # print(temp)

    for s in skill:
        types, a,b,c,d, degree = s
        if (types == 1):
            degree = -degree
        temp[a][b] += degree
        if (c+1 < row):
            temp[c+1][b] -= degree
        if (d+1 < col):
            temp[a][d+1] -= degree
        if (c+1 < row and d+1 < col):
            temp[c+1][d+1] += degree
    
    # print(temp)
    for i in range(row):
        for j in range(col-1):
            temp[i][j+1] += temp[i][j]

    # print(temp)
    for i in range(col):
        for j in range(row-1):
            temp[j+1][i] += temp[j][i]
    # print(temp)
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if (board[i][j] >0):
                answer += 1
    # print(board)
    
    return answer