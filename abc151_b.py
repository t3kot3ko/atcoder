import sys
lines = sys.stdin.readlines()
n, k, m = [int(e) for e in lines[0].split(" ")]
a = [int(e) for e in lines[1].split(" ")]

d = n * m - sum(a)
print(str(max([0, d])) if d <= k else "-1")

