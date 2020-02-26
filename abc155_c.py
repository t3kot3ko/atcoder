import sys

lines = [l.rstrip() for l in sys.stdin.readlines()]
d = {}

n = int(lines[0])
for l in lines[1:]:
    if l in d.keys():
        d[l] += 1
    else:
        d[l] = 1

s = sorted(d.items(), key=lambda x: -x[1])
l = sorted([e for e in s if e[1] == s[0][1]], key=lambda x: x[0])

for k, _ in l:
    print(k)
