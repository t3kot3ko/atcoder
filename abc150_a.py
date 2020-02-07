import sys
k, x = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
print("Yes" if k * 500 >=x else "No")
