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
    
# # print(bits)

# com = ""

# cnt = 0

# for i in range(2*N+1):
#     if (i % 2):
#         com += "0"
#     else:
#         com += "1"
# com = int(com)


# for i in range(len(S)-(2*N)):
#     temp = bits[i:i+(2*N+1)]
#     temp = int(temp)
#     if (temp == com):
#         cnt += 1
# print(cnt)

cnt = 0
temp = 0
result = 0
for i in range(len(S)):
    # 만약에 1 이면 + 1 0이면 -1 하면서 가다가 cnt가 n이랑 같아지면 + 1 하고 계속 간다. 다시 0이 되면 + 1하면서 간다
    # 만약에 음수가 되거나 2가 되면, 그 자리부터 다시 간다.
    # print(bits[:i+1])
    if (bits[i] == "1"):
        temp += 1
        cnt += 1
    else:
        temp -= 1
        cnt += 1

    # print(temp, cnt, result)
    if (temp == 1 and cnt >= (2*N+1)):
        result += 1
    elif (temp < 0): # 이렇게 되면
        cnt = 0
        temp = 0
    elif (temp >= 2):
        cnt = 1
        temp = 1
print(result)

