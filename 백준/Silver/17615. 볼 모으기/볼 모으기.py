N = int(input())
bl = list(input())

# target이 R일 때 처음으로 나오는 B를 찾아야 함

bindex = -1
rindex = - 1
rcnt = 0
bcnt = 0

for i in range(len(bl)-1, -1, -1):
    if (bl[i] == 'B'): 
        bindex = i
        break
for i in range(len(bl)-1, -1, -1):
    if (bl[i] == 'R'):
        rindex = i
        break


if (bindex == -1 or rindex == -1):
    print(0)
else:
    for i in range(bindex):
        if (bl[i] == 'R'):
            rcnt += 1
    for i in range(rindex):
        if (bl[i] == 'B'):
            bcnt += 1
    answer = min(rcnt, bcnt)
    print(answer)
