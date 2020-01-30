import sys
lines = [l.rstrip() for l in sys.stdin.readlines()]
n = int(lines[0])
l = [int(e) for e in lines[1].split(" ")]

min = n
c = 0
for e in l:
    if e < min:
        min = e
    if min >= e:
        c += 1

print(c)
