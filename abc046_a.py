a, b, c = input().split(" ")
if a == b == c:
    print(1)
elif a == b or b == c or c == a:
    print(2)
else:
    print(3)
