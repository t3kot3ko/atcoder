n, r = [int(e) for e in input().split(" ")]

if n >= 10:
    print(r)
else:
    print(r + 100 * (10 - n))

