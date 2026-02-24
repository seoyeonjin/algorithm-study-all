import math

N, K = map(int, input().split())

ps = list(map(int,input().split())) # 인형을 선호하는 사람의 수

# 연속 K개의 표준편차를 구해야 하는 건가?

# 표준 편차가 최소가 되도록 연속된 K개를 구하는 문제
# 연속된 K마다 다시 표준 편차를 구할 필요가 있나? 

# 처음 거 평균이 2이다
# 1 + 1 => 2 / 3 이다. (분산)
# 표준 편차는 2/3의 양의 제곱근이다.

# 처음 거 평균에서 (a+b+c)/N - a/N + d/N 이면 구할 수 있음 m'
# 처음 거 분산에서 - (a1-m)^2/N + (a4-m)^2/N 이면 구할 수 있음
# 표준 편차는 분산에서 루트해서 최솟값 구하기

def init():
    tsum = 0
    for i in range(K):
        tsum += ps[i]
    return tsum / K

def calc_m(a,b,m, k):
    # newm = m - 
    tsum = 0
    for i in range(K):
        tsum += ps[i]
    return tsum / K

def calc_var(a,b,m,k): # 범위랑 평균이 들어왔을 때 분산 구하기
    tsum = 0
    for i in range(a,b+1):
        tsum += pow(ps[i]-m, 2)
    return tsum/k
    

result = []

for i in range(K, N+1):
    for j in range(N-i+1): # i개 만큼 0,K 0,K+1
        tsum = sum(ps[j:j+i])
        tm = tsum/i
        tvar = calc_var(j, j+i-1, tm, i)
        # print(i,j,j+i-1, tsum, tm, tvar)
        te = math.sqrt(tvar)
        result.append(te)
        
    
print(min(result))
