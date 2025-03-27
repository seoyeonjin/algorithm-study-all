import math 

R, G = map(int, input().split())

gcd_number =  math.gcd(R,G)
gcd_list = []

for i in range(1, gcd_number+1):
    if (gcd_number % i == 0): 
        gcd_list.append(i)

for gcd in gcd_list:
    print(gcd, int(R/gcd), int(G/gcd))
