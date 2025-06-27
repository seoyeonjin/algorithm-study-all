from collections import deque

def is_comparable(begin, target):
    different_count = 0
    length = len(begin)
    for i in range(length):
        if (begin[i] != target[i]):
            different_count += 1
    if (different_count == 1):
        return True
    else:
        return False
    
    
def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    
    word_que = deque()
    word_que.append([begin, answer])
    
    while word_que:
        flag = 0
        target_word, answer = word_que.popleft()
        answer += 1
        for i in range(len(words)):
            if (is_comparable(target_word, words[i]) and not visited[i]):
                print(target_word, words[i])
                if (words[i] == target):
                    return answer
                word_que.append([words[i], answer])
                visited[i] = 1
                flag = 1
        if (flag == 0):
            return 0