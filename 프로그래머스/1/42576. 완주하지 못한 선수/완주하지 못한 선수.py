from collections import Counter

def solution(participant, completion):
    answer = ''
    pc = Counter(participant)
    cc= Counter(completion)
    rc = pc - cc
    # print(rc, pc,cc)
    for r in rc:
        answer += r
    return answer