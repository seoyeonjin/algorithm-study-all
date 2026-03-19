# 초콜릿 막대 정사각형 N개
# 초콜릿 크기는 2의 제곱 형태

# 상근이는 적어도 K개 정사각형을 먹어야 한다. 
# 선영이는 상근이가 주는 초콜릿만 먹는다.

# 상근이는 K개 정사각형이 디도록 자른다. -> 남은 것 선영이 

# K개 정사각형 만들려면 몇 번 쪼개야돼? 

# 6개가 되려면 어떻게 되어야 하는가?

# 4 + 2 + 2
# 8이어야 하고, 2번 쪼개야 한다. 

# 어떻게 생각? 6에서 가장 작은 2의 제곱수를 찾는다.
# 그리고 뺀 나머지를 본다. -> 나머지를 구하기 위해 
import math

num = int(input())

cnt = 0
max_size = 2 ** int(math.log(num, 2))

if (max_size == num):
    print(max_size, 0)
    exit(0)

size = max_size * 2
# print(size)

while num > 0:
    if (size < num):
        temp = 2 ** int(math.log(num,2))
        num = num - temp
        cnt += 1
        size = size // 2
        # print(cnt, temp, num, size)
    elif (size == num):
        break
    else:
        # 작을 때
        size = size // 2
        cnt += 1
        # print(cnt, size)

    
print(max_size * 2, cnt)