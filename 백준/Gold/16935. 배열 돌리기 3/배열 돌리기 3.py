# 1번 상하 반전 
# 2번 좌우 반전
# 3번 오른쪽 90도 회전
# 4번 왼쪽 90도 회전
# 5번 4등분해서 1번 -> 2번 -> 3번 -> 4번 -> 1번
# 6번 4등분해서 1번 -> 4번 -> 3번 -> 2번 -> 1번


N, M, R = map(int, input().split())

nums = [[] for i in range(N)] 

for i in range(N):
    temp = list(map(int, input().split()))
    nums[i] = temp

r_list = list(map(int, input().split()))

def up_down():
    for i in range(N // 2):
        # 절반까지 가면서
        nums[i], nums[N-1-i] = nums[N-1-i], nums[i]
    
def right_left():
    for i in range(N):
        for j in range(M//2):
            nums[i][j], nums[i][M-1-j] = nums[i][M-1-j], nums[i][j]

def rotate_right():
    new_nums = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            num = nums[i][j]
            new_nums[j][N-1-i] = num
    return new_nums

def rotate_left():
    new_nums = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            num = nums[i][j]
            new_nums[M-1-j][i] = num
    return new_nums

def change_one():
    new_nums = [[0 for i in range(M)] for j in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            new_nums[i][M//2 +j] = nums[i][j]
            new_nums[i+N//2][j+M//2] = nums[i][j+M//2]
            new_nums[i+N//2][j] = nums[i+N//2][j+M//2]
            new_nums[i][j] = nums[i+N//2][j]
    return new_nums

def change_two():
    new_nums = [[0 for i in range(M)] for j in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            new_nums[i+N//2][j] = nums[i][j]
            new_nums[i+N//2][j+M//2] = nums[i+N//2][j]
            new_nums[i][j+M//2] = nums[i+N//2][j+M//2]
            new_nums[i][j] = nums[i][j+M//2]
    return new_nums


for r in r_list:
    if (r == 1):
        up_down()
    elif (r == 2):
        right_left()
    elif (r == 3):
        nums = rotate_right()
        N, M = M, N
    elif (r == 4):
        nums = rotate_left()
        N, M = M, N
    elif (r == 5):
        nums = change_one()
    elif (r == 6):
        nums = change_two()


for num in nums:
    print(*num)
