import math
import sys
input = sys.stdin.readline



def is_prime(n):
    if (n < 4):
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

primes = [True for _ in range(1000001)]
for i in range(2, 1000001):
    if primes[i] == True:
        for j in range(i*2, 1000001, i):
            primes[j] = False

n = int(input())
for _ in range(n): 
    count = 0 
    num = int(input())
    for i in range(2,(num // 2) + 1):
        if (primes[i] and primes[num-i]):
            count += 1
    print(count)
