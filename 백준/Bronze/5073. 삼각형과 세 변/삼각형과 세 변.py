
while True:
    a, b,c = map(int , input().split())
    if (a == 0 and b == 0 and c ==0):
        break

    max_num = max(a,b,c)
    if (max_num == a and a >= b + c):
        print("Invalid")
    elif (max_num == b and b >= a + c):
        print("Invalid")
    elif (max_num == c and c >= a + b):
        print("Invalid")
    else: 
        if (a == b == c):
            print("Equilateral")
        elif (a == b or b == c or a == c ):
            print("Isosceles")
        else: 
            print("Scalene")
