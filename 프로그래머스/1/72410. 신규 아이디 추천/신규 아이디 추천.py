def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for n in new_id:
        if (n.isalpha() or n == "-" or n == "_" or n == "." or n.isdigit()):
            answer += n
    fs = ".."
    while fs in answer:
        idx= answer.find(fs)
        answer = answer[:idx] + answer[idx+1:]
    
    if (len(answer) > 0 and answer[0] == "."):
        answer = answer[1:]
    if (len(answer) > 0 and answer[-1] == "."):
        answer = answer[:len(answer)-1]
        

    if (len(answer) == 0):
        answer += "a"

    if (len(answer) >= 16): 
        answer = answer[:15]
        if (answer[-1] == "."):
            answer = answer[:-1]

    while (len(answer) <= 2):
        answer = answer + answer[-1]
    return answer