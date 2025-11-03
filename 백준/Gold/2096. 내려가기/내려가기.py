N = int(input())
nums = []
maxs = [0,0,0]
mins = [0,0,0]

for i in range(N):
    temp = list(map(int ,input().split()))
    a = max(maxs[0], maxs[1]) + temp[0]
    b = max(maxs[0], maxs[1], maxs[2]) + temp[1]
    c = max(maxs[2], maxs[1]) + temp[2]
    maxs = [a,b,c]
    d = min(mins[0], mins[1]) + temp[0]
    e = min(mins[0], mins[1], mins[2]) + temp[1]
    f = min(mins[2], mins[1]) + temp[2]
    mins = [d,e,f]

print(max(maxs), min(mins))