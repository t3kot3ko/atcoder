import sys

n = int(input())
z = [[None] * n for i in range(n)]

lines = sys.stdin.readlines()

i = -1
for l in lines:
    splitted = l.split(" ")

    if len(splitted) < 2:
        i += 1
        continue

    x, y = [int(s) for s in splitted]
    z[i][x-1] = y

def f(x, n):
    # proved
    p = [None] * n

    # honest
    h = [0] * n

    # cursor
    c = 0

    xx = x
    while x > 0:
        if x % 2 == 1:
            h[c] = 1

            # Statement picked up
            v = z[c]

            # print(v)
            for i in range(len(p)):
                if (p[i] == 0 and v[i] == 1) or (p[i] == 1 and v[i] == 0):
                    # Not consistent
                    return 0

            for i in range(len(p)):
                if v[i] is not None:
                    p[i] = v[i]

        c += 1
        x //= 2

    r = 0
    for pp, hh in zip(p, h):
        if (pp == 0 and hh == 1) or (pp == 1 and hh == 0):
            return 0

        if hh == 1 and (pp is None or pp == 1):
            r += 1
        elif pp == 1 and (hh is None or hh == 1):
            r += 1

    return r

print(max([f(i, n) for i in range(2 ** n)]))