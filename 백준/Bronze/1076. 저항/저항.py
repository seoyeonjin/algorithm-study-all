

first = input() 
second = input()
third = input()

reg = [
    ["black", 0, 1],
    ["brown", 1, 10],
    ["red", 2, 100],
    ["orange", 3, 1000],
    ["yellow", 4, 10000],
    ["green", 5, 100000],
    ["blue", 6, 1000000],
    ["violet", 7, 10000000],
    ["grey", 8, 100000000],
    ["white", 9, 1000000000]
]

for i in range(len(reg)):
    if (reg[i][0] == first):
        first_num = reg[i][1]
    if (reg[i][0] == second):
        second_num = reg[i][1]
    if (reg[i][0] == third):
        thiird_num = reg[i][2]

str_num = str(first_num) + str(second_num)
num_str = int(str_num)
print(num_str * thiird_num)