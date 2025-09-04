def to_base(num, base):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        num, remainder = divmod(num, base)
        result = digits[remainder] + result
    return result

def solution(n, t, m, p):
    answer = ''
    st = ""
    num = 0
    while (len(st) < (t*m)):
        st = st + str(to_base(num, n))
        num += 1
    print(st)
    i = p-1
    while len(answer) != t:
        answer += st[i]
        i = i + m
    return answer