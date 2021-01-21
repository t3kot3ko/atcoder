s = input()

r = 0
for i in range(len(s) - 1, 0, -1):
    if s[i] == "Z":
        r = len(s) - 1 - i
        break

print(len(s) - s.find("A") - r)