import math

x, y = map(int, input().split())

gcd = math.gcd(x, y)
print(x+y-gcd)