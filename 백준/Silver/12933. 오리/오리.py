
answer_str = "quack"

input_str = input() 
answer_list = []
max_quack= -1

for str in input_str:
    if (str == "q"):
        answer_list.append("q")
    elif (str == "u"):
        if ("q" in answer_list):
            answer_list.remove("q")
            answer_list.append("qu")
        else: 
            print(-1)
            exit(0)
    elif (str == "a"):
        if ("qu" in answer_list):
            answer_list.remove("qu")
            answer_list.append("qua")
        else: 
            print(-1)
            exit(0)   
    elif (str == "c"):
        if ("qua" in answer_list):
            answer_list.remove("qua")
            answer_list.append("quac")
        else: 
            print(-1)
            exit(0)
    elif (str == "k"):
        if ("quac" in answer_list):
            answer_list.remove("quac")
            answer_list.append("quack")
            max_quack = max(max_quack, len(answer_list))
            answer_list.remove("quack")
        else: 
            print(-1)
            exit(0)

if (len(answer_list) == 0):
    print(max_quack)
else: 
    print(-1)