
def solution(n, k, cmd):
    answer = ''
    nl = [[i-1,i+1] for i in range(n)]
    result = ["O" for i in range(n)]
    nl[n-1][1] = -1
    remove_list = []
    
    def up(k, num): # k부터 num만큼 위로 가야함
        node = nl[k]
        num = int(num)
        while num:
            n = node[0] # next node
            node = nl[n]
            num -= 1
        return n
    
    def down(k, num):
        node = nl[k]
        num = int(num)
        while num:
            n = node[1]
            node = nl[n]
            num -=1
        return n
    
    def cut(k): # k를 지워야함 
        remove_list.append(k)
        pre = nl[k][0]
        post = nl[k][1]
        if (pre != -1):
            nl[pre][1] = nl[k][1]
        if (post != -1):
            nl[post][0] = nl[k][0]
        result[k] = "X"
        
        if (nl[k][1] == -1):
            k = nl[k][0]
        else:
            k = nl[k][1]
        return k 
        
    def z():
        node = remove_list.pop() # 마지막 거 꺼내기
        pre = nl[node][0]
        post = nl[node][1]
        
        if pre != -1:
            nl[pre][1] = node
        if post != -1:
            nl[post][0] = node
        result[node] = "O"

    for c in cmd:
        if (c == "C"):
            k = cut(k)
        elif (c == "Z"):
            z()
        else:
            c, num = c.split(" ")
            if (c == "U"):
                k = up(k, num)
            else:
                k = down(k, num)

    return "".join(result)
    # return answer