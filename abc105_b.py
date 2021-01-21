n = int(input())
for x in range(n // 4 + 1):
    if (n - 4 * x) % 7 == 0:
        print("Yes")
        break
else:
    print("No")