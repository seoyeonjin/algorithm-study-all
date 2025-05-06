n = int(input())
arr = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        index = stack.pop()
        answer[index] = arr[i]
    stack.append(i)

print(' '.join(map(str, answer)))