import sys
input = sys.stdin.readline

n = int(input())
input_list = []

for _ in range(n):
    a = input().strip()
    if ("push" in a):
        a, b = a.split()
        input_list.append(int(b))
    elif (a == "front"):
        if (len(input_list) == 0):
            print(-1)
        else:
            print(input_list[0])
    elif (a == "back"):
        if (len(input_list) == 0):
            print(-1)
        else:
            print(input_list[-1])
    elif (a == "empty"):
        if (len(input_list) == 0):
            print(1)
        else: 
            print(0)
    elif (a == "size"):
        print(len(input_list))
    elif (a == "pop"):
        if (len(input_list) == 0):
            print(-1)   
        else:
            print(input_list[0])
            input_list.remove(input_list[0])