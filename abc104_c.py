d, g = map(int, input().split(" "))
pcs = []

for i in range(d):
    p, c = map(int, input().split(" "))
    pcs.append((p, c))


def f(b, g):
    s = 0
    r = 0
    cursor = 0
    mc = 0

    while b > 0:
        p, c = pcs[cursor]

        if b % 2 == 1:

            for _ in range(p-1):
                s += (cursor + 1) * 100
                r += 1

                if s >= g:
                    return r, s

            s += (cursor + 1) * 100 + c
            r += 1

            if s >= g:
                return r, s

        else:
            mc = cursor

        b //= 2
        cursor += 1

    p, c = pcs[mc]
    for _ in range(p-1):
        s += (mc + 1) * 100
        r += 1

        if s >= g:
            return r, s

    return 0, s

print(min([e for e in [f(b, g)[0] for b in range(2 ** d)] if e > 0]))