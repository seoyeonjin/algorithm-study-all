# 배열 x -> 45 의 배수만큼 시계 / 반시계로 돌린다.
# X 의 대각선을 가운데열로 옮긴다.
# X의 가운데 열을 X의 부 대각선으로 옮긴다.(반대 대각선)
# X의 부 대각선을 X의 가운데 행으로 옮긴다.
# X의 가운데 행 -> X의 주 대각선
# 원소의 기존 순서는 유지
# 다른 원소 위치는 변경 X 

T = int(input())

def rotate(n, l):
    # 대각선을 가운데열로 옮긴다.
    temp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = l[i][j] # 복제해두고
    # 대각선 옮기기
    for i in range(n):
        num = l[i][i]
        temp[i][n//2] = num
    # 가운데 열 부 대각선으로 옮기기
    for i in range(n):
        num = l[i][n//2]
        temp[i][n-i-1] = num
    # 부대각선
    for i in range(n):
        num = l[n-i-1][i]
        temp[n//2][i] = num
    for i in range(n):
        num = l[n//2][i]
        temp[i][i] = num
    for i in range(n):
        for j in range(n):
            l[i][j] = temp[i][j]
        
    # print(temp)
    # l[0][0] = rn



for _ in range(T):
    N,D = map(int, input().split()) # 45로 나누면 몇 번 돌려야 하는지 알 수 있음
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    if (D < 0): D = D + 360
    rn = D // 45 # 몫
    for i in range(rn):
        rotate(N, l)
        # print(l[0][0])
    # result = rotate(rn, N, l)
    for i in range(N):
        for j in range(N):
            print(l[i][j], end = " ")
        print()

