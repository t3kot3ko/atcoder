n = int(input())

c = 0
for nn in range(1, n+1):
    k = 0
    while nn > 0:
        nn //= 10
        k += 1

    if k % 2 == 1:
        c += 1

print(c)