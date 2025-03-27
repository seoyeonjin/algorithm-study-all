import math

A, B = map(int, input().split())
count = 0

prime_list = []

def is_prime(n):
    for i in range(2,int(math.sqrt(n)) +1):
        if (n % i == 0):
            return False
    return True

for num in range(2, 100000):
    if (is_prime(num)):
        prime_list.append(num)

for num in range(A, B+1):
    result_list = []
    i = 0
    while num > 1 and i < len(prime_list):
        if (num % prime_list[i] == 0):
            num  = num // prime_list[i]
            result_list.append(prime_list[i])
        else:
            i += 1
    if (len(result_list) > 1 and is_prime(len(result_list))):
        count +=1

print(count)