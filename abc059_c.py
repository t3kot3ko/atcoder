n = int(input())
a = list(map(int, input().split(" ")))
s = [a[0]]
for i in range(1, n):
    s.append(s[i-1] + a[i])

def f(sign):
    score = 0
    diff = 0
    for i in range(n):
        ss = s[i] + diff
        if (sign == -1 and ss >= 0) or (sign == 1 and ss <= 0):
            d = sign - ss
            diff += d
            score += abs(d)
        sign *= -1

    return score

print(min([f(sign) for sign in [1, -1]]))
