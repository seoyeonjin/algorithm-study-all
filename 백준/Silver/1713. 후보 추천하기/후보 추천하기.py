
photo_num = int(input())
recom_num = int(input())

recom_list = map(int, input().split())
result_list = []

for stu in recom_list:
    if (photo_num > len(result_list)):
        is_exist = False
        for result in result_list:
            if (stu == result[0]):
                result[1] += 1
                is_exist = True
        if (not is_exist):
            result_list.append([stu,1])
    else: #누군가는 탈락
        is_exist = False
        for result in result_list:
           if (stu == result[0]):
               result[1] += 1
               is_exist = True
        if (not is_exist):
            min = [0,1000]
            for result in result_list:
                if (min[1] > result[1]):
                    min = result
            result_list.remove(min)
            result_list.append([stu, 1])
result_list.sort()

for result in result_list:
    print(result[0], end = ' ')