a, b = [int(i) for i in input().split(" ")]
r = 0

for i in range(a, b + 1):
    x0 = i // 10000
    x1 = (i // 1000) % 10
    x2 = (i // 100) % 10
    x3 = (i // 10) % 10
    x4 = i % 10

    if x0 == x4 and x1 == x3:
        r += 1

# for i in range(a, b + 1):
#     if str(i) == "".join(reversed(str(i))):
#         r += 1

print(r)
