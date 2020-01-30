import sys
n = int(sys.stdin.readline().rstrip())

s = [[0] * 10 for i in range(10)]

for i in range(1, n+1):
    first = int(str(i)[0])
    end = i % 10
    s[first][end] += 1

r = 0
for i in range(10):
    for j in range(10):
        r += s[i][j] * s[j][i]

print(r)
