import sys
lines = [l.rstrip() for l in sys.stdin.readlines()]
n = int(lines[0])
s = lines[1]

r = 0
for c in range(len(s) - 2):
    if s[c] == "A" and s[c+1] == "B" and s[c+2] == "C":
        r += 1
        c += 2

print(r) 

