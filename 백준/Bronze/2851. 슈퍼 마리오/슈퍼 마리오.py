# 받은 점수의 합을 최대한 100에 가깝게 해야 함

nl = []
for i in range(10): 
    nl.append(int(input()))


psum = [0] * 11

for i in range(1,11):
    psum[i] = psum[i-1] + nl[i-1]

# print(psum)

min_i = 11
min_n = psum[10]

answer = []

for i in range(1, len(psum)):
    answer.append((abs(psum[i] - 100), -i))

answer.sort()
print(psum[-answer[0][1]])