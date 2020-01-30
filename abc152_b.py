import sys
a, b = [int(e) for e in sys.stdin.readline().rstrip().split(" ")]
print(str(min([a, b])) * max([a, b]))
