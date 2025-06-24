n, b = map(int, input().split())

result_list = []

while (n>=1):
    a = n % b
    result_list.insert(0, a)
    n = n // b 

dict_list = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
    17: "H",
    18: "I",
    19: "J",
    20: "K",
    21: "L",
    22: "M",
    23: "N",
    24: "O",
    25: "P",
    26: "Q",
    27: "R",
    28: "S",
    29: "T",
    30: "U",
    31: "V",
    32: "W",
    33: "X",
    34: "Y",
    35: "Z"
}

for result in result_list:
    if (result >= 10):
        print(dict_list[result], end='')
    else: 
        print(result, end='')
