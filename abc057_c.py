import math

n = int(input())
m = 11

for a in range(1, int(math.sqrt(n))+1):
    if n % a != 0:
        continue

    b = n // a
    len_a = len(str(a))
    len_b = len(str(b))

    f = max(len_a, len_b)
    if m > f:
        m = f

print(m)
