n = int(input())
a = list(map(int, input().split(" ")))

m = 0
for x in range(min(a) - 1, max(a) + 2):
    r = sum([aa == x or aa + 1 == x or aa - 1 == x for aa in a])
    if m < r:
        m = r
print(m)