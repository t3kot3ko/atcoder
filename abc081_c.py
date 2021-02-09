n, k = [int(i) for i in input().split(" ")]
a = [int(i) for i in input().split(" ")]
r = [0] * n

for aa in a:
    r[aa-1] += 1

print(sum(sorted(r, reverse=True)[k:]))


