import sys

lines = [l.rstrip() for l in sys.stdin.readlines()]
n, m = [int(e) for e in lines[0].split(" ")]
r = [None] * n

for l in lines[1:]:
    s, c = [int(e) for e in l.split(" ")]

    if n != 1 and s == 1 and c == 0:
        print("-1")
        sys.exit(0)

    if r[s - 1] is not None and r[s - 1] != c:
        print("-1")
        sys.exit(0)

    r[s - 1] = c

if n != 1 and r[0] is None:
    r[0] = 1

print("".join([(str(d) if d else "0") for d in r]))

