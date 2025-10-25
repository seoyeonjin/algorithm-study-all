# import sys
# sys.setrecursionlimit(100000)
def solution(commands):
    answer = []
    values = [["" for i in range(51)] for j in range(51)] # 값을 가지는 것
    roots = [[[i, j] for j in range(51)] for i in range(51)]
    
    
    def ufind(r,c): # union 임 (root만 값 갱신함)
        if (roots[r][c] != [r,c]):
            roots[r][c] = ufind(roots[r][c][0], roots[r][c][1])
        return roots[r][c]
        
    def update_all(v1, v2): # 값 갱신
        for i in range(51):
            for j in range(51):
                if (values[i][j] == v1):
                    values[i][j] = v2
    
    def merge(r1,c1,r2,c2): # merge => 유사 union
        value = values[r1][c1] # 병합되고 저장될 값
        if (value == ""): # 가지고 있는 값이 없으면?
            value = values[r2][c2]
            
        # 각자의 root를 찾는다. 
        root1 = ufind(r1, c1)
        root2 = ufind(r2, c2)
        
        # 어디에 병합할거냐?
        if root1 < root2: # root1이 더 작으면 -> 큰게 바뀌어야지
            roots[root2[0]][root2[1]] = root1
            return root1, value
        elif (root1 > root2):
            roots[root1[0]][root1[1]] = root2
            return root2, value
        else:
            return root1, value
        
        
    def unmerge(r,c):
        # 병합을 해제한다. -> root를 찾는다.
        value = values[r][c]
        root = ufind(r,c) # root를 찾음
        
        for i in range(51):
            for j in range(51):
                if (ufind(roots[i][j][0], roots[i][j][1]) == root):
                    values[i][j] = ""
                    roots[i][j] = [i,j]
        values[r][c] = value
        
    for cmd in commands:
        cmds = list(cmd.split(" "))
        
        if (cmds[0] == "UPDATE" and len(cmds) == 4):
            # r, c 에 value로 업데이트
            r, c = int(cmds[1]), int(cmds[2])
            root = ufind(r,c)
            for i in range(51):
                for j in range(51):
                    if (ufind(roots[i][j][0], roots[i][j][1]) == root):
                        values[i][j] = cmds[3]
        elif (cmds[0] == "UPDATE" and len(cmds) == 3):
            update_all(cmds[1], cmds[2])
        elif (cmds[0] == "MERGE"):
            r1, c1, r2, c2 = int(cmds[1]), int(cmds[2]), int(cmds[3]), int(cmds[4])
            root, value = merge(r1,c1,r2,c2)
            for i in range(51):
                for j in range(51):
                    if (ufind(roots[i][j][0], roots[i][j][1]) == root) :
                        values[i][j] = value
                        roots[i][j] = root
        elif (cmds[0] == "UNMERGE"):
            r, c = int(cmds[1]), int(cmds[2])
            unmerge(r,c)
        elif (cmds[0] == "PRINT"):
            r, c = int(cmds[1]), int(cmds[2])
            value = values[r][c]
            if (value == ""):
                answer.append("EMPTY")
            else:
                answer.append(value)
          
#         print(cmd)
#         for v in roots[:5]:
#             print(v[:5])
        
            
    # UPDATE r c value
    # UPDATE v1 v2 -> 모든 v1을 v2로 변경 -> root에 가서 변경하기만 하면 됨
    # MERGE r1 c1 r2 c2 -> 합친다. -> 둘 중 하나만 값이 있을 경우 그 값을 가짐, 아닌 경우 r1, c1위치의 값을 가지게 됨 r2 c2의 root를 찾아서 r1 c1을 보게 하면 됨
    # UNMERGE r c -> 모든 병합을 해제 -> 값은 r,c 위치에
    # PRINT r c -> 값 출력
    
    
    return answer