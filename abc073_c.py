import sys
n = int(input())
a = [int(l) for l in sys.stdin.readlines()]

c = {}
for i in a:
    if i not in c.keys():
        c[i] = 0
    c[i] += 1

r = 0
for v in c.values():
    r += v % 2

print(r)
