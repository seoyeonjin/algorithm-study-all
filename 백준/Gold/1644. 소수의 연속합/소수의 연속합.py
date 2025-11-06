n = int(input())

# 소수 리스트 만들기 (에라토스테네스의 체)
primes = [True] * (n + 1)
primes[0] = primes[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, n + 1, i):
            primes[j] = False

prime_list = [i for i in range(2, n + 1) if primes[i]]

# 투 포인터로 연속된 소수의 합 구하기
cnt = 0
start, end = 0, 0
current_sum = 0

while True:
    if current_sum >= n:
        if current_sum == n:
            cnt += 1
        current_sum -= prime_list[start]
        start += 1
    elif end == len(prime_list):
        break
    else:
        current_sum += prime_list[end]
        end += 1

print(cnt)
