import math

n = int(input())
zs = []
for i in range(n):
    zs.append(tuple(map(int, input().split(" "))))

def permutation(x=[]):
    if len(x) == 1:
        yield [x[0]]

    for xx in x:
        left = xx
        right = [e for e in x if e != left]

        for y in permutation(right):
            yield ([left] + y)

def d(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

s = 0
paths = 0
for path in permutation(list(range(n))):
    for i in range(len(path)-1):
        s += d(zs[path[i]], zs[path[i+1]])
    paths += 1

print(s / paths)


