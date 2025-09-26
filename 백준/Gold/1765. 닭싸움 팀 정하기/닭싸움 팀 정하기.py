
def ufind(a, rl):
    if (a == rl[a]):
        return a
    else:
        root = ufind(rl[a], rl)
        rl[a] = root
        return root
    

def union(a,b,rl):
    ar = ufind(a, rl)
    br = ufind(b, rl) 
    if (ar < br):
        rl[ar] = br
    else:
        rl[br] = ar

n = int(input())
m = int(input())

rl = [i for i in range(n+1)]
dislikel = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c= input().split()  
    b = int(b)
    c = int(c)
    if (a == 'E'):
        # 원수
        # 원수의 원수는 친구이다. 
        # A와 B가 원수라고 하면
        for f in dislikel[b]:
            union(c, f, rl)
        for f in dislikel[c]:
            union(b, f, rl)
        dislikel[b].append(c)
        dislikel[c].append(b)
    else:
        # 친구
        union(b,c,rl)
        # 작은 거 e에 d 저장

rl = rl[1:]
rs = set(rl)
print(len(rs))