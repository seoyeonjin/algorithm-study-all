 
t = int(input())

for _ in range(t):
    n = int(input())
    stock_list = list(map(int, input().split()))
    max_number_index = -1
    account = 0
    while max_number_index < n -1:
        temp_max_number_index = max_number_index
        # print("temp_max_number_index: ", temp_max_number_index)
        max_index_list = []
        max_number = 0
        for i in range(n-1, max_number_index, -1):
            if (max_number < stock_list[i]):
                max_number = stock_list[i]
        for i in range(n):
            if (stock_list[i] == max_number):
                max_index_list.append(i)
        max_number_index = max(max_index_list)

        # print("max_number_index", max_number_index)
        count = max_number_index - temp_max_number_index -1
        # print("count: ", count)
        for i in range(temp_max_number_index+1, max_number_index):
            # print("i: ", i)
            # print("account: ", account)
            account -= stock_list[i] # 계속 산다.
        account += count * max_number
        # print(account)
    print(account)

    