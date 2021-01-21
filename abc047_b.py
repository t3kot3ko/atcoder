import sys
w, h, n = [int(i) for i in input().split(" ")]
xm, xM, ym, yM = w, 0, h, 0
for line in sys.stdin:
    x, y, a = [int(i) for i in line.split(" ")]

    if a == 1 and xM < x:
        xM = x
    elif a == 2 and xm > x:
        xm = x
    elif a == 3 and yM < y:
        yM = y
    elif a == 4 and ym > y:
        ym = y

print(max(xm - xM, 0) * max(ym - yM, 0))


