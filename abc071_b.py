s = input()
a = "abcdefghijklmnopqrstuvwxyz"
for c in a:
    if c not in s:
        print(c)
        exit(0)
else:
    print("None")