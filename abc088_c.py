c = []
c.append([int(i) for i in input().split(" ")])
c.append([int(i) for i in input().split(" ")])
c.append([int(i) for i in input().split(" ")])

def eq(x, y, z):
    return x == y and y == z

if eq(c[0][0] - c[1][0], c[0][1] - c[1][1], c[0][2] - c[1][2])\
        and eq(c[1][0] - c[2][0], c[1][1] - c[2][1], c[1][2] - c[2][2])\
        and eq(c[2][0] - c[0][0], c[2][1] - c[0][1], c[2][2] - c[0][2]):
            print("Yes")
else:
    print("No")

