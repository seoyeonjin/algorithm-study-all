# 누적합이 최대가 되는 지점 찾기

n, m = map(int, input().split())
nl = list(map(int ,input().split()))

psum = [0] * (n+1)

for i in range(1, n+1):
    psum[i] = psum[i-1] + nl[i-1]

# print(psum)

answer = []

for i in range(n-m+1): # 2
    answer.append(psum[i+m] - psum[i])
print(max(answer))