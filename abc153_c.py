import sys
lines = sys.stdin.readlines()
n, k = [int(i) for i in lines[0].rstrip().split(" ")]
h = [int(i) for i in lines[1].rstrip().split(" ")]

h.sort()
h.reverse()

print(sum(h[k:]))
