

N = int(input())    
M = int(input()) # s의 길이 
S = input()

bits = ""

for i in range(len(S)):
    if (S[i] == "O"):
        bits += "0"
    else:
        bits += "1"
    
# print(bits)

com = ""

cnt = 0

for i in range(2*N+1):
    if (i % 2):
        com += "0"
    else:
        com += "1"
# print("com " , com)

for i in range(len(S)-(2*N)):
    temp = bits[i:i+(2*N+1)]

    if (temp[0] == "0"):
        continue
    else:
        if (int(temp) + int(com) == int(com) * 2):
            cnt += 1
print(cnt)


# 더하면 20202가 된다? -> 그러면 더해서 확인해보면 되는 거 아닌가?