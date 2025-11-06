N, M = map(int , input().split())
T = []

start = 0
end = 10**18 # 초기화

for _ in range(N):
    a = int(input())
    T.append(a)

# print(T)
def check(t): 
    # a의 시간에 모든 사람이 통과할 수 있는지 확인
    # 어떻게 확인하지?
    result = 0
    for k in T:
        temp = (t // k)
        result += temp
    if (result >= M):
        return True
    else:
        return False
        


while start < end:
    mid = (start + end) // 2
    if (check(mid)): # 통과가능이면
        end = mid
    else:
        start = mid + 1
print( end)
