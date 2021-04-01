n, m = list(map(int, input().split(" ")))
ks = []
for i in range(m):
    ks.append(list(map(int, input().split(" ")))[1:])
ps = list(map(int, input().split(" ")))

bits = [0] * n
cur = 0
r = 0

while True:
    found = True
    for i in range(m):
        s = 0
        for si in ks[i]:
            s += bits[si-1]
        if s % 2 != ps[i]:
            found = False

    if found:
        r += 1

    if all([b == 1 for b in bits]):
        break

    bits[0] += 1
    for i in range(n-1):
        if bits[i] == 2:
            bits[i] = 0
            bits[i+1] += 1


print(r)