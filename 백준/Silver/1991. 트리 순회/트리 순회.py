n = int(input())
ch_list = {}

for _ in range(n):
    pa, ch1, ch2 = input().split()
    ch_list[pa] = [ch1, ch2]


def pre(ch):
    if ch != ".":
        print(ch, end="")
        pre(ch_list[ch][0])
        pre(ch_list[ch][1])


def inorder(ch):
    if ch != ".":
        inorder(ch_list[ch][0])
        print(ch, end="")
        inorder(ch_list[ch][1])


def post(ch):
    if ch != ".":
        post(ch_list[ch][0])
        post(ch_list[ch][1])
        print(ch, end="")


pre('A')
print()
inorder('A')
print()
post('A')
print()
