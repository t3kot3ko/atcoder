s = input()
n = len(s)

m = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        ss = s[i:j]
        if all([sss == "A" or sss == "C" or sss == "G" or sss == "T" for sss in ss]):
            if m < (j - i):
                m = j - i

print(m)
