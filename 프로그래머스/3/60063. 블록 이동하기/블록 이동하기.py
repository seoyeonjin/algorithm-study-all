from collections import deque

def is_moved(car, blen, board):
    a,b,c,d = car[0][0], car[0][1], car[1][0], car[1][1]
    if (0 <= a < blen and 0 <= b < blen and 0<=c<blen and 0<=d<blen):
        if (board[a][b] == 0 and board[c][d] == 0):
            return True
    return False

def is_rotate(car, blen, board, checked_cd):
    a,b,c,d = car[0][0], car[0][1], car[1][0], car[1][1]
    # print(a,b,c,d, is_left)
    if (0 <= a < blen and 0 <= b < blen and 0<=c<blen and 0<=d<blen):
        if (board[a][b] == 0 and board[c][d] == 0):
            if (0 <= checked_cd[0] < blen and 0 <= checked_cd[1] < blen):
                if (board[checked_cd[0]][checked_cd[1]] == 0):
                    return True
    return False
    
    
def solution(board):
    answer = 0
    carcd = [[0,0], [0,1]]
    carque = deque()
    cnt = 0
    carque.append((carcd,cnt))
    blen = len(board)
    visited = []
    visited.append(carcd)
    visited.append([carcd[1], carcd[0]])

    while carque:
        # print(carque)
        cd,cnt = carque.popleft()
        temp, temp2 = cd
        a,b = temp[0], temp[1]
        c,d = temp2[0], temp2[1]
        if (cd[0] == [blen - 1,blen- 1] or cd[1] == [blen-1, blen-1]): 
            return cnt
        else:
            if (a == c):
                n1 = [[a,b-1], [c,d-1]]
                n2 = [[a,b+1], [c,d+1]]
                n3 = [[a,b], [a-1, b]]
                n4 = [[a,b], [a+1,b]]
                n5 = [[c-1, d], [c,d]]
                n6 = [[c+1,d], [c,d]]
                n7 = [[a-1, b], [c-1, d]]
                n8 = [[a+1, b], [c+1, d]]
                
                if (is_rotate(n3, blen, board, [c-1, d]) and n3 not in visited):
                    carque.append((n3, cnt+1))
                    visited.append(n3)
                    visited.append([n3[1], n3[0]])
                if (is_rotate(n4, blen, board, [c+1,d]) and n4 not in visited):
                    carque.append((n4, cnt+1))
                    visited.append(n4)
                    visited.append([n4[1], n4[0]])
                if (is_rotate(n5, blen, board, [a-1,b]) and n5 not in visited):
                    carque.append((n5, cnt+1))
                    visited.append(n5)
                    visited.append([n5[1], n5[0]])
                if (is_rotate(n6, blen, board, [a+1,b]) and n6 not in visited):
                    carque.append((n6, cnt+1))
                    visited.append(n6)
                    visited.append([n6[1], n6[0]])
                if (is_moved(n1, blen, board) and n1 not in visited):
                    carque.append((n1, cnt+1))
                    visited.append(n1)
                    visited.append([n1[1], n1[0]])
                if (is_moved(n2, blen, board) and n2 not in visited):
                    carque.append((n2, cnt+1))
                    visited.append(n2)
                    visited.append( [n2[1], n2[0]])
                if (is_moved(n7, blen, board) and n7 not in visited):
                    carque.append((n7, cnt+1))
                    visited.append(n7)
                    visited.append([n7[1], n7[0]])
                if (is_moved(n8, blen, board) and n8 not in visited):
                    carque.append((n8, cnt+1))
                    visited.append(n8)
                    visited.append( [n8[1], n8[0]])
            else:
                n1 = [[a-1,b], [c-1,d]]
                n2 = [[a+1,b], [c+1,d]]
                n3 = [[a,b], [a, b-1]]
                n4 = [[a,b], [a,b+1]]
                n5 = [[c, d-1], [c,d]]
                n6 = [[c, d+1], [c,d]]
                n7 = [[a, b-1], [c, d-1]]
                n8 = [[a, b+1], [c, d+1]]
                if (is_rotate(n3, blen, board, [c,d-1]) and n3 not in visited):
                    carque.append((n3, cnt+1))
                    visited.append(n3)
                    visited.append([n3[1], n3[0]])
                if (is_rotate(n4, blen, board, [c,d+1]) and n4 not in visited):
                    carque.append((n4, cnt+1))
                    visited.append(n4)
                    visited.append([n4[1], n4[0]])
                if (is_rotate(n5, blen, board, [a,b-1]) and n5 not in visited):
                    carque.append((n5, cnt+1))
                    visited.append(n5)
                    visited.append([n5[1], n5[0]])
                if (is_rotate(n6, blen, board, [a,b+1]) and n6 not in visited):
                    carque.append((n6, cnt+1))
                    visited.append(n6)
                    visited.append([n6[1], n6[0]])
                if (is_moved(n1, blen, board) and n1 not in visited):
                    carque.append((n1, cnt+1))
                    visited.append(n1)
                    visited.append([n1[1], n1[0]])
                if (is_moved(n2, blen, board) and n2 not in visited):
                    carque.append((n2, cnt+1))
                    visited.append(n2)
                    visited.append( [n2[1], n2[0]])
                if (is_moved(n7, blen, board) and n7 not in visited):
                    carque.append((n7, cnt+1))
                    visited.append(n7)
                    visited.append([n7[1], n7[0]])
                if (is_moved(n8, blen, board) and n8 not in visited):
                    carque.append((n8, cnt+1))
                    visited.append(n8)
                    visited.append( [n8[1], n8[0]])

            
    return answer