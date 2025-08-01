import heapq

def solution(operations):
    answer = []
    num_list = []
    max_heap = []
    min_heap = []
    
    for op in operations:
        a, b = op.split()
        b = int(b)
        if (a == "I"):
            # heapq.heappush(max_heap, b)
            # heapq.heappush(min_heap, -b)
            num_list.append(b)
            num_list.sort()
        elif (a == "D"):
            if (b == -1):
                if (len(num_list) > 0):
                    del num_list[0]
            else:
                if (len(num_list) > 0):
                    num_list.pop()
    if (len(num_list) == 0):
        return([0,0])
    else:
        return([num_list[-1], num_list[0]])
    # return answer