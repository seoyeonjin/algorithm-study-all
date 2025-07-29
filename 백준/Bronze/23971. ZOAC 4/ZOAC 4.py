# 강의실을 예약한다 

# 무조건 앉아야 함.
H, W, N, M = map(int, input().split())

a = 0
count_a = 0
while a < W:
    a += (M+1)
    count_a += 1

b = 0
count_b = 0
while b < H:
    b += (N+1)
    count_b += 1

print(count_a * count_b)