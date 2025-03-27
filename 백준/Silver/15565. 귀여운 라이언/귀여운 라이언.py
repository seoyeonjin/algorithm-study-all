n, k = map(int, input().split())
arr = list(map(int, input().split()))


lion_list = [i for i in range(n) if arr[i] == 1]

min_list = []

if len(lion_list) < k:
    print(-1)
    exit()

# min_length = float('inf')
left, right = 0, k - 1  

while right < len(lion_list):
    length = lion_list[right] - lion_list[left] + 1
    min_list.append(length)
    left += 1
    right += 1  

print(min(min_list))
