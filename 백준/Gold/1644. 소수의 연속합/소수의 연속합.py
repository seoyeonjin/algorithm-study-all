# 소수 리스트를 만들면 좋겠다. 

n = int(input())

primes = [True for _ in range(n+1)]
for i in range(2, n+1):
    if primes[i] == True:
        for j in range(i*2, n+1, i):
            primes[j] = False

prime_list = []

for i in range(2,n+1):
    if (primes[i]):
        prime_list.append(i)

if (len(prime_list) != 0):
    
    start = 0
    end = 1
    sum = prime_list[start]
    cnt = 0

    # print(prime_list, len(prime_list))
    while start < end and end <= len(prime_list):
        if (end == len(prime_list)):
            while start < end:
                if (sum == n):
                    cnt += 1
                    break
                elif (sum > n ):
                    sum -= prime_list[start]
                    start += 1
                else:
                    break
            break
        else:
            if (sum == n): # 같으면
                cnt += 1
                sum += prime_list[end]
                end += 1
            elif (sum < n):
                sum += prime_list[end]
                end += 1
            else:
                sum -= prime_list[start]
                start += 1 
            # print(sum, start, end)
    print(cnt)
else:
    print(0)