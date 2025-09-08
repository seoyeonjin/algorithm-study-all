a,b =map(int, input().split())  
S = input() 

A,C,G,T = map(int,input().split())
answer = 0 

start = 0
Acnt = S[start:start+b].count('A')
Ccnt = S[start:start+b].count('C')
Gcnt = S[start:start+b].count('G')
Tcnt = S[start:start+b].count('T')


def correct(Acnt, Ccnt, Gcnt, Tcnt):
    # print(Acnt, Ccnt, Gcnt, Tcnt, A,C,G,T)
    # print(A <= Acnt and C <= Ccnt and G <= Gcnt and  T <= Tcnt)
    if (A <= Acnt and C <= Ccnt and G <= Gcnt and T <= Tcnt):
        return True
    return False

result = correct(Acnt, Ccnt, Gcnt, Tcnt)
if (result ):
    answer += 1

while start + b < a:
    # print(start, start+b, answer)
    temp = S[start]
    if (temp == 'A'):
        Acnt -= 1
    if (temp == 'C'):
        Ccnt -= 1
    if (temp == 'G'):
        Gcnt -= 1
    if (temp == 'T'):
        Tcnt -= 1
    temp = S[start+b]
    if (temp == 'A'):
        Acnt += 1
    if (temp == 'C'):
        Ccnt += 1
    if (temp == 'G'):
        Gcnt += 1 
    if (temp == 'T'):
        Tcnt += 1
    if (correct(Acnt, Ccnt, Gcnt, Tcnt)):
        answer += 1 
    start += 1
print(answer)

