N = int(input())

words = []
count = 0

for i in range(N):
    words.append(input())
words.sort()

for i in range(N):
    if i == N-1 or not words[i+1].startswith(words[i]):
        count += 1
print(count)