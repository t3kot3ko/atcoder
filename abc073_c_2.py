import sys
n = int(input())
a = [int(l) for l in sys.stdin.readlines()]

c = 0
r = 0
cur = -1
for i in sorted(a) + [-1]:
    if cur == i:
        c += 1
    else:
        cur = i
        r += (c % 2)
        c = 1

print(r)
