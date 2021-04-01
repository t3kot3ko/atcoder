a, b, k = list(map(int, input().split(" ")))
c = 0
r = []
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        r.append(i)

print(r[-k])