n = int(input())
for x in range(1, 10):
    for y in range(1, 10):
        if n == x * y:
            print("Yes")
            exit(0)

print("No")
