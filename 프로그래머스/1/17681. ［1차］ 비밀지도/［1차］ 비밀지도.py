def convert(n):
    answer = ""
    while n > 0:
        n, m = divmod(n, 2)
        answer += str(m)
    return answer[::-1]
        

def solution(n, arr1, arr2):
    answer = []
    s1 = []
    s2 = []
    for a in arr1:
        a = convert(a)
        if (len(a) < n):
            a = "0" * (n-len(a)) + a
        s1.append(a)
    for b in arr2:
        b= convert(b)
        if (len(b) < n):
            b = "0" * (n-len(b)) + b
        s2.append(b)
    for i in range(n):
        temp = ""
        for j in range(n):
            if (s1[i][j] == "1" or s2[i][j] == "1"):
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    
    return answer