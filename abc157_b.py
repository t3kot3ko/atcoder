import sys
lines = sys.stdin.readlines()

a = [[int(e) for e in r.split(" ")] for r in lines[0:3]]
n = lines[3]
b = [int(e) for e in lines[4:]]

patterns = [
    [a[0][0], a[0][1], a[0][2]],
    [a[1][0], a[1][1], a[1][2]],
    [a[2][0], a[2][1], a[2][2]],
    [a[0][0], a[1][0], a[2][0]],
    [a[0][1], a[1][1], a[2][1]],
    [a[0][2], a[1][2], a[2][2]],
    [a[0][0], a[1][1], a[2][2]],
    [a[0][2], a[1][1], a[2][0]]
]

for p in patterns:
    if all([pp in b for pp in p]):
        print("Yes")
        break
else:
    print("No")
