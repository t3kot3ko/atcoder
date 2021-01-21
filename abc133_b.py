import sys
import math
n, d = [int(i) for i in input().split(" ")]
x = [[int(i) for i in l.split(" ")] for l in sys.stdin.readlines()]

r = 0
for i in range(n - 1):
    for j in range(i+1, n):
        d = sum([(x1 - x2) ** 2 for x1, x2 in zip(x[i], x[j])])
        if math.sqrt(d) == int(math.sqrt(d)):
            r += 1

print(r)
