import sys
lines = sys.stdin.readlines()
h, n = [int(i) for i in lines[0].rstrip().split(" ")]
a = [int(i) for i in lines[1].rstrip().split(" ")]

print("Yes" if sum(a) >= h else "No")

