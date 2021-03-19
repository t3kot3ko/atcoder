n = int(input())
ts = []

for i in range(n):
    ts.append(int(input()))

def f(b, ts):
    c = 0
    t = 0   # Takahashi-kun
    s = sum(ts)

    while b > 0:
        if b % 2 == 1:
            t += ts[c]

        b //= 2
        c += 1

    return max(t, s - t)

print(min([f(b, ts) for b in range(2 ** n)]))