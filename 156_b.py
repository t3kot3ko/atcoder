def f(d, k):
    q = d // k
    r = d % k
    if q == 0:
        return str(r)
    else:
        return f(q, k) + str(r)

n, k = [int(e) for e in input().split(" ")]

print(len(f(n, k)))
