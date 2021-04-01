n = int(input())

r = 0
for nn in range(1, n+1):
    if nn % 2 == 0:
        continue

    i = 1
    c = 0
    while i <= nn:
        if nn % i == 0:
            c += 1
        i += 1

    if c == 8:
        r += 1

print(r)
