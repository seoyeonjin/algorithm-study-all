import heapq

# k가 2500?

def solution(n, m, x, y, r, c, k):
    answer = ''
    dx = [1,0, 0, -1]
    dy = [0,-1,1,0]
    move = ["d", "l", "r", "u"]
    
    def add_route(temp):
        move_cnt = (k - len(temp)) // 2  # temp (나눈 몫만큼 이동 가능 1 만큼 이동하면서)
        move_list = []
        result = temp
        a = r
        b = c
        na = a
        nb = b
        
        for i in range(4):
            while move_cnt:
                a += dx[i]
                b += dy[i]

                if (1 <= a <= n and 1 <= b <= m):
                    move_list.append(i)
                    move_cnt -= 1
                else:
                    a -= dx[i]
                    b -= dy[i]
                    break
        # print(move_list)
#             
        for i in range(len(move_list)):
            result += (move[move_list[i]])
        for i in range(len(move_list)-1, -1, -1):
            if (move_list[i] == 0):
                result += move[3]
            elif (move_list[i] == 1):
                result += move[2]
            elif (move_list[i] == 2):
                result += move[1]
            else:
                result += move[0]
        # print(result)
        return result
        
    

    result = ""
    
    visited = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
    visited[x][y][k] = 1
    
    rl = []
    heap = []
    heapq.heappush(heap, (result, x,y,k))
    while heap:
        # print(heap)
        result, a,b, cnt = heapq.heappop(heap)
        remains = abs(r-a) + abs(c-b)
        
        if a == r and b == c and cnt == 0:
            return result
        
        if (cnt == 0):
            continue
        
        if (cnt >= remains):
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                
                if (1 <= na <= n and 1 <= nb <= m and not visited[na][nb][cnt-1]):
                    newresult = result + move[i]
                    visited[na][nb][cnt-1] = 1
                    heapq.heappush(heap, (newresult, na,nb, cnt-1))
                    # if (na == r and nb == c):
                    #     if (cnt == 1):
                    #         return newresult
                    #     else:
                    #         if ((k-len(newresult)) % 2 == 0):
                    #             # 부족한 만큼 어딜 다녀와야 함
                    #             full_result = add_route(newresult)
                    #             return full_result
                    # else:
                        
    
    return("impossible")

