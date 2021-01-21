s = input()
t = input()
n = len(s)
m = len(t)

if n < m and s == t[:n]:
    print("Yes")
else:
    print("Yes" if min(s) < max(t) else "No")
