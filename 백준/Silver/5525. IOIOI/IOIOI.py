# 문자열 s와 정수 n 
# n은 o의 개수
# s안에 pn이 몇 군데 포함?

N = int(input())    
M = int(input()) # s의 길이 
S = input()

cnt = 0
temp = 0
result = 0
for i in range(len(S)):
    # 만약에 1 이면 + 1 0이면 -1 하면서 가다가 cnt가 n이랑 같아지면 + 1 하고 계속 간다. 다시 0이 되면 + 1하면서 간다
    # 만약에 음수가 되거나 2가 되면, 그 자리부터 다시 간다.
    # print(bits[:i+1])
    if (S[i] == "I"):
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

