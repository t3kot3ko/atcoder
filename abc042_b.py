import sys
n, l = [int(i) for i in input().split(" ")]
s = [l.rstrip() for l in sys.stdin.readlines()]

for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if s[j] > s[j + 1]:
            x = s[j+1]
            y = s[j]
            s[j+1] = y
            s[j] = x

print("".join(s))
