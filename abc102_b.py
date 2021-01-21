n = input()
a = sorted([int(e) for e in input().split(" ")])
print(max(a[-1], a[0]) - min(a[-1], a[0]))
