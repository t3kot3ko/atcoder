n = int(input())
t, a = [int(e) for e in input().split(" ")]
h = [int(e) for e in input().split(" ")]
diff = [abs(t - hh * 0.006 - a) for hh in h]

r = 0
m = diff[0]
for i in range(1, n):
    if diff[i] < m:
        m = diff[i]
        r = i

print(r + 1)

