def solution(places):
    answer = []
    
    def calc_d(a,b):
        d = abs(a[0] - b[0]) + abs(a[1]-b[1])
        return d
    
    def is_partition(p, x,y): 
        a,b= x
        c,d = y
        if (a == c): # 일직선 상에 있다면
            newy = int((b+d) // 2)
            point = p[a][newy]
            if (point == 'X'):
                return True
            else:
                return False
        elif (b == d): # 일직선 상에
            newx = int((a+c)//2)
            point = p[newx][d]
            if (point == 'X'):
                return True
            else:
                return False
        else:
            # 일직선 상에 없다면 2개 좌표를 봐야함
            point1 = p[a][d]
            if (point1 == 'X'):
                point2 = p[c][b]
                if (point2 == 'X'):
                    return True
                else:
                    return False
            else:
                return False    
            
            
    
    for p in places:
        p_list = []
        for i in range(5):
            for j in range(5):
                if (p[i][j] == 'P'):
                    p_list.append((i,j))
        flag = False
        for i in range(len(p_list)):
            for j in range(len(p_list)):
                # 맨허튼 거리 계산하기
                if (i != j and not flag):    
                    d = calc_d(p_list[i],p_list[j])
                    if (d == 1):
                        answer.append(0)
                        flag = True
                    elif (d==2):
                        # 사이에 파티션이 있는건지 확인하기 
                        exist = is_partition(p, p_list[i],p_list[j])
                        if (not exist): # 있다면 true
                            answer.append(0)
                            flag = True
        if (flag == False):
            answer.append(1)
                        
                    
    return answer