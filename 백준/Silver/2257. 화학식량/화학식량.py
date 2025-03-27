
input_str = input()
stack = []

for input in input_str:
    if (input == "("):
        stack.append(input) 
    elif (input == "C"):
        stack.append(12)
    elif (input == "H"):
        stack.append(1)
    elif (input == "O"):
        stack.append(16)
    elif (input == ")"):
        temp = 0
        while True:
            if (stack[-1] == "("):
                stack.pop()
                stack.append(temp)
                break
            else: 
                temp += stack.pop()
    else:
        stack.append(stack.pop() * int(input))
    
print(sum(stack))

# stack