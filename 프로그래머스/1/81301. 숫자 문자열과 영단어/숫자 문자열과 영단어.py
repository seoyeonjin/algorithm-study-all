def is_num(a):
    if (a == "0" or a == "1" or a == "2" or a == "3" or a =="4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9"):
        return True
    else:
        return False
    
def solution(s):
    answer = ""
    dic = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    i = 0
    while i < len(s):
        a = s[i]
        if (is_num(a)):
            answer += a
            i += 1
        else:
            if (a == "z"):
                answer += "0"
                i += 4
            elif (a == "o"):
                answer += "1"
                i += 3
            elif (a == "t"):
                if (s[i+1] == "w"):
                    answer += "2"
                    i += 3
                else:
                    answer += "3"
                    i += 5
            elif (a == "f"):
                if (s[i+1] == "o"):
                    answer += "4"
                    i += 4
                else:
                    answer += "5"
                    i += 4
            elif (a == "s"):
                if (s[i+1] == "i"):
                    answer += "6"
                    i += 3
                else:
                    answer += "7"
                    i += 5
            elif (a == "e"):
                answer += "8"
                i += 5
            else:
                answer += "9"
                i += 4
            # temp = ""
            # b = i
            # while (b < len(s) and not is_num(s[b])):
            #     temp += s[b]
            #     b += 1
            #     if (temp in dic):
            #         answer += str(dic[temp])
            #         i = b
            #         break
    return int(answer)