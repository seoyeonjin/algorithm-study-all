
A, B, C, M = map(int, input().split())

# 피로도가 M이 넘지 않는지 확인한다.

work = 0
hard = 0 
total = 0

for i in range(24):
    if (hard + A <= M): # 일을 할 수 있으면
        work += B
        hard += A
    else:
        hard -= C
        if (hard < 0):
            hard = 0

print(work)

        