import sys

input = sys.stdin.readline
N, M = map(int, input().split())
word_list = []
word_dict = dict()

len_list = [[] for _ in range(11)]

for i in range(N):
    word = input().rstrip()
    if (len(word) >= M): 
        if (word in word_dict.keys()):
            word_dict[word] += 1
        else:
            word_dict[word] = 1

for word in word_dict:
    word_list.append([word_dict[word], len(word), word])
word_list.sort(key = lambda x: (-x[0], -x[1], x[2]))

for word in word_list:
    print(word[2])
