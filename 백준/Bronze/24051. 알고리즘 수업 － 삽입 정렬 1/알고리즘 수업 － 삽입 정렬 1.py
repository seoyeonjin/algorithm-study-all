
N, K = map(int, input().split())
num_list = list(map(int, input().split()))

def insertion_sort(num_list):
    count = 0
    for i in range(N):
        loc = i -1
        new_item = num_list[i]

        while (0 <= loc and new_item < num_list[loc]):
            num_list[loc+1] = num_list[loc]
            loc -= 1            
            count += 1
            if (count == K):
                print(num_list[loc+1])
        if (loc + 1 != i):
            num_list[loc+1] = new_item
            count += 1
            if (count == K):
                print(num_list[loc+1])
    return count



count = insertion_sort(num_list)
if (count < K):
    print(-1)