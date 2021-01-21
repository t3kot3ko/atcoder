n = int(input())
s = []
t = []
for _ in range(n):
    s.append(input().rstrip())

m = int(input())
for _ in range(m):
    t.append(input().rstrip())

print(max(max([sum([1 if si == ss else 0 for ss in s]) - sum([1 if si == tt else 0 for tt in t]) for si in s]), 0))