def solution(dirs):
    answer = 0
    
    # 0,1,2,3 -> 왼 위 오 아
    visited = [[[0 for _ in range(4)] for i in range(11)] for j in range(11)] 

    # 시작 좌표
    a, b = 5, 5

    for d in dirs:
        if (d == "U"): # 위로 가면
            na,nb = a,b+1
            if (nb <= 10): # 갈 수 있는 곳
                if (visited[a][b][1] == 0):
                    answer += 1
                visited[a][b][1] = 1
                a,b = na,nb
                visited[a][b][3] = 1
        elif (d == "D"): # 아래로 가면
            na,nb = a,b-1
            if (nb >= 0): # 갈 수 있으면
                if (visited[a][b][3] == 0):
                    answer += 1
                visited[a][b][3] = 1
                a,b = na,nb
                visited[a][b][1] = 1
        elif (d == "R"): # 오른쪽이면
            na,nb = a+1, b
            if (na <= 10): 
                if (visited[a][b][2] == 0):
                    answer += 1
                visited[a][b][2] = 1
                a,b = na,nb
                visited[a][b][0] = 1
        elif (d == "L"):
            na,nb = a-1, b
            if (na >= 0):
                if (visited[a][b][0] == 0):
                    answer += 1
                visited[a][b][0] = 1 
                a,b = na,nb
                visited[a][b][2] = 1
        
                
        
    return answer