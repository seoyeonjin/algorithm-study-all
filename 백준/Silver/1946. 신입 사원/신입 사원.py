import sys
input = sys.stdin.readline

T = int(input())    

for _ in range(T):
    n = int(input())
    grade_list = []
    count = 0
    for i in range(n):
        first, second = map(int, input().split())
        grade_list.append((first, second))
    grade_list.sort()

    # print(grade_list)

    grade_min = grade_list[0][1]

    for i in range(1,n):
        if (grade_list[i][1] < grade_min):
            grade_min = grade_list[i][1]
        else:
            count +=1
    print(n-count)