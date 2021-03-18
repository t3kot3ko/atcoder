s = input().rstrip()

for d in range(2 ** (len(s) - 1)):
    r = int(s[0])
    c = 1
    e = s[0]

    while d > 0:
        if d % 2 == 1:
            r += int(s[c])
            e += "+" + s[c]

        else:
            r -= int(s[c])
            e += "-" + s[c]

        c += 1
        d //= 2

    for i in range(c, len(s)):
        r -= int(s[i])
        e += "-" + s[i]

    if r == 7:
        print(e + "=7")
        break
