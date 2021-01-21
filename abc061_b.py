import sys
n, m = [int(i) for i in input().split(" ")]
r = [0] * n

for l in sys.stdin:
    a, b = [int(i) for i in l.split(" ")]
    r[a-1] += 1
    r[b-1] += 1

for rr in r:
    print(rr)

