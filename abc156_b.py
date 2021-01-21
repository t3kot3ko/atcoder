n, k = [int(i) for i in input().split(" ")]
r = 0
while n != 0:
    r += 1
    n //= k

print(r)