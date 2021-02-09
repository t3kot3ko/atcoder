import sys
# lines = [l.rstrip() for l in sys.stdin.readlines()]
lines = """3
1 3 2
3 1 2
""".split("\n")
n = int(lines[0])
ps = [int(i) for i in lines[1].split(" ")]
qs = [int(i) for i in lines[2].split(" ")]

def factorial(n):
    r = 1
    for i in range(n):
       r *= i 
    return r

a = 0
for p in ps:
    a += factorial(n - 1) * (n - p)

print(r + 1)


