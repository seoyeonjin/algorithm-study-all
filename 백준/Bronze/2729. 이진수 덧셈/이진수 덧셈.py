n = int(input())

for _ in range(n):
    a, b = input().split() 
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    result = int_a + int_b
    bin_result = bin(result)
    print(bin_result[2:])