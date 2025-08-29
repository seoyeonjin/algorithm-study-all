
from collections import deque

def addA(str):
    str = str + "A"
    return str

def addB(str):
    str = str + "B"
    str = str[::-1]
    return str

S = input()
T = input()

que = deque()
que.append(S)

while que:
    # print(que)
    st = que.popleft()
    if (len(st) > len(T)):
        continue
    else:
        if (st == T):
            print(1)
            exit()
        else:
            a = addA(st)
            b = addB(st)
            if (a in T or a[::-1] in T):
                que.append(a)
            if (b in T or b[::-1] in T):
                que.append(b)
print(0)
