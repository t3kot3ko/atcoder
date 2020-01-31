import sys
import math

h, a = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
print(math.ceil(h / a))
