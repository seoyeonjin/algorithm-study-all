
def correct_string(input_str):
    cnt = 0
    for s in input_str:
        if (s == "("):
            cnt += 1
        else: 
            cnt -= 1
        if (cnt < 0):
            return False
    return True

def seperate(input_str):
    cnt = 0
    for i in range(len(input_str)):
        s = input_str[i]
        if (s == "("):
            cnt += 1
        else: 
            cnt -= 1
        if (cnt == 0):
            u = input_str[:i+1]
            v = input_str[i+1:]
            return u,v

def reverse(a):
    v = ""
    for s in a:
        if (s == "("):
            v += ")"
        else:
            v += "("
    return v
        
def recursion(p):
    if (p == ""):
        return ""
    elif (correct_string(p)):
        return p
    else:
        u,v = seperate(p)
        print("u,v", u,v)
        if (correct_string(u)):
            return u + recursion(v)
        else:
            init = "("
            result = recursion(v)
            init += result
            init += ")"
            u = u[1:len(u)-1]
            u = reverse(u)
            init += u
            return init
            
        
def solution(p):
    answer = ''
    answer = recursion(p)
    return answer




