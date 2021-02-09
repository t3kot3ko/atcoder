a, b, c = list(map(int, input().split(" ")))
M = max([a, b, c])
m = min([a, b, c])

for n in range(1, M + 1):
    if (a + b + c + 2 * n) % 3 == 0:
        x = (a + b + c + 2 * n) / 3
        if x < M:
            continue
        print(n)
        exit()