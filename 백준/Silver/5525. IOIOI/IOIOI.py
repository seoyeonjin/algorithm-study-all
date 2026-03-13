# 문자열 s와 정수 n 
# n은 o의 개수
# s안에 pn이 몇 군데 포함?

N = int(input())    
M = int(input()) # s의 길이 
S = input()

# 문자열 안에 O가 N개 나오고 I가 N+1개 나오는 쌍이 몇 개 있는지 구하기
# I로 시작하고 I로 끝나야 함

# Pn을 구해서 매칭되는 거 확인하면 되지 않을까?
# -> 이러면 n^2만큼 돌아야 함
# # 일단 Pn을 구한다.
# P = ""

# for i in range(N):
#     P += "IO"
# P += "I"

# 비교를 이렇게 하면 안 되는데.. 흐음.. 무슨 방법이 없을까?

# 2N + 1 이 P의 길이임
# 약간 비트마스킹으로 비교를 해야할 거 같은데?
# 2N+1 길이의 1이랑 합쳤을 때 -> 기존이랑 같은지 확인하기?
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
com = int(com)


for i in range(len(S)-(2*N)):
    temp = bits[i:i+(2*N+1)]
    temp = int(temp)
    if (temp + com == com * 2):
        cnt += 1
print(cnt)


# 더하면 20202가 된다? -> 그러면 더해서 확인해보면 되는 거 아닌가?