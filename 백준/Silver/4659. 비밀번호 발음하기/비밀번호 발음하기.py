dic = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'w':22,
    'v':23,
    'x':24,
    'y':25,
    'z':26
}

def rule_one(l):
    if (1 in l or 5 in l or 9 in l or 15 in l or 21 in l):
        return True
    else:
        return False

def rule_two(l):
    a_count = 0
    b_count = 0
    for i in range(len(l)):
        if (l[i] == 1 or l[i] == 5 or l[i] == 9 or l[i] == 15 or l[i] == 21):
            a_count += 1
            b_count = 0
            if (a_count >= 3):
                return False
        else:
            b_count += 1
            a_count = 0
            if (b_count >= 3):
                return False
    return True

def rule_three(l):
    for i in range(len(l)-1):
        if (l[i] == l[i+1]):
            if (l[i] == 15 or l[i] == 5):
                return True
            else:
                return False
    return True


while True:
    pw = input()
    if (pw == "end"):
        break
    npw = list(pw)
    for i in range(len(npw)):
        npw[i] = dic[npw[i]] 
    result = rule_one(npw)
    if (not result):
        print("<", *pw, "> is not acceptable.", sep="")
    else:
        result = rule_two(npw)
        if (not result):
            print("<", *pw, "> is not acceptable.", sep="")
        else: 
            result = rule_three(npw)
            if (not result):
                print("<", *pw, "> is not acceptable.", sep="")
            else:
                print("<", *pw, "> is acceptable.", sep="")
    