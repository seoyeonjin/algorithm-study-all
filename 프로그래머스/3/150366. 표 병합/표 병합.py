# import sys 
# sys.setrecursionlimit(1000)

def solution(commands):
    answer = []
    root = [[[i,j] for j in range(51)] for i in range(51)]
    values = [["" for i in range(51)] for j in range(51)]
    
    def ufind(r,c, value):
        values[r][c] = value
        if (root[r][c][0] == r and root[r][c][1] == c):
            return [r,c]
        else:
            result = ufind(root[r][c][0], root[r][c][1], value)
            root[r][c][0] = result[0]
            root[r][c][1] = result[1]
            return result
        
    def ufind_wo_value(r,c):
        if (root[r][c][0] == r and root[r][c][1] == c):
            return [r,c]
        else:
            result = ufind_wo_value(root[r][c][0], root[r][c][1])
            root[r][c][0] = result[0]
            root[r][c][1] = result[1]
            return result
    
    def merge(a,b,c,d):
        # union을 구현한다. 
        # if (a == c and b ==d):
        #     return
        
        if (values[a][b]):
            value = values[a][b]
        else:
            value = values[c][d]
        
        root1 = ufind(a,b, value)
        root2 = ufind(c,d, value)
        
        # print(root1, root2)
        
        minr = min(root1, root2)
        maxr = max(root1, root2)
        # print(minr, maxr)
        
        for i in range(51):
            for j in range(51):
                if (root[i][j] == maxr or root[i][j] == minr):
                    root[i][j] = minr
                    values[i][j] = value
        
        # if (root1[0] < root2[0]): # 더 작은 거에 담아둔다
        #      root[root2[0]][root2[1]] = root1
        # elif (root1[0] == root2[0]):
        #     if (root1[1] <= root2[1]): # 둘이 같을 때는?
        #         root[root2[0]][root2[1]] = root1
        #     else: 
        #         root[root1[0]][root1[1]] = root2
        # else:
        #     root[root1[0]][root1[1]] = root2
            
            
        # print(root[1][2], root[1][3])
        
    # def ufind(r,c,value):
    def update_all(v1, v2):  # v1을 찾는다
        for i in range(51):
            for j in range(51):
                if (values[i][j] == v1):
                    values[i][j] = v2
        
    
    def update(r,c,value):
        values[r][c] = value
        r = ufind(r,c,value)
        # print(r[0], r[1])
        for i in range(51):
            for j in range(51):
                if (root[i][j] == [r[0], r[1]]):
                    values[i][j] = value
    def unmerge(r,c):
        # 셀의 모든 병합을 해제한다. 
        value = values[r][c]
        root1 = ufind_wo_value(r,c) # 이 root를 가지고 있는 애 찾아서 다 value ""으르 변경하기 root도 자기자신으로 변경
        # a, b = root1
        
        for i in range(51):
            for j in range(51):
                if (root[i][j] == root1):
                    values[i][j] = ""
                    root[i][j] = [i,j]
        values[r][c] = value
        

    for c in commands:
        cmds = c.split(" ")
        if (cmds[0] == "UPDATE" and len(cmds) == 4): #  셀 업데이트
            r= int(cmds[1])
            c = int(cmds[2])
            update(r,c,cmds[3])
        elif (cmds[0] == "UPDATE" and len(cmds) == 3):
            v1 = cmds[1]
            v2 = cmds[2]
            update_all(v1, v2)
            # print()
        elif (cmds[0] == "MERGE"):
            r1 = int(cmds[1])
            c1 = int(cmds[2])
            r2 = int(cmds[3])
            c2 = int(cmds[4])
            merge(r1,c1,r2,c2)
        elif (cmds[0] == "UNMERGE"):
            r = int(cmds[1])
            c = int(cmds[2])
            unmerge(r,c)
        else: # print
            r = int(cmds[1])
            c = int(cmds[2])
            if (values[r][c] == ""):
                answer.append("EMPTY")
            else:
                answer.append(values[r][c])
    
        # for v in values[:6]:
        #     print(v[:6])
            
    return answer