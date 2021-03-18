s = input().rstrip()

def f(s, d):
    l = 0
    r = 0

    vs = []
    while d > 0:
        if d % 2 == 1:
            vs.append(s[l:r+1])
            r += 1
            l = r
        else:
            r += 1

        d //= 2

    vs.append(s[l:len(s)])

    return sum(map(int, vs))

print(sum([f(s, i) for i in range(2 ** (len(s) - 1))]))


