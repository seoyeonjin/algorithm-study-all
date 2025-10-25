# N개 학급
# M명으로 구성

# 모든 학생들의 능력치 중 최댓값과 최솟값의 차이가 최소가 되도록
N, M = map(int, input().split())
stus = []
ans_list = []

stu_dict = {}

for i in range(N):
    m_list = list(map(int, input().split()))
    for m in m_list:
        stus.append((m, i))

stus.sort()


s, e = 0,0

while e < len(stus):

    if (stus[e][1] in stu_dict ):
        stu_dict[stus[e][1]] += 1
    else:
        stu_dict[stus[e][1]] = 1
    # print(stu_dict )
    if (len(stu_dict) == N): # 학급의  수와 같아졌을 때
        while len(stu_dict) == N:
            stu_dict[stus[s][1]] -= 1
            if (stu_dict[stus[s][1]] == 0):
                del stu_dict[stus[s][1]]
            s += 1
        ans_list.append((s-1,e))
    e += 1
    
# print(stus)

# print(ans_list)
min_ans = float('inf')

for ans in ans_list:
    a,b = ans
    temp = sorted(stus[a:b+1])
    max_m = temp[-1][0]
    min_m = temp[0][0]
    min_ans = min(min_ans, abs(max_m - min_m))

print(min_ans)
