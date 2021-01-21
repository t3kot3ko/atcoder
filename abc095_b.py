import sys
n, x = [int(x) for x in input().split(" ")]
m = [int(l.rstrip()) for l in sys.stdin.readlines()]

x -= sum(m)
r = n

for mm in sorted(m):
    if x < mm:
        continue

    r += x // mm
    x -= mm * (x // mm)

print(r)