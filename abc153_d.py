import math
import sys
h = int(sys.stdin.readline().rstrip())
k = math.floor(math.log2(h))
print(2 ** (k + 1) - 1)
