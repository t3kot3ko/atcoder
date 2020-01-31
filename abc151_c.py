import sys

lines = [l.rstrip() for l in sys.stdin.readlines()[1:]]

ac = []
wa = {}

for l in lines:
    p_raw, s = l.split(" ")
    p = int(p_raw)

    if p in ac:
        continue

    if s == "WA":
        if p not in wa.keys():
            wa[p] = 0
        wa[p] += 1

    elif s == "AC":
        ac += [p]

ac_count = len(ac)
wa_count = 0
for p in ac:
    wa_count += (wa[p] if p in wa.keys() else 0)

print("%d %d" % (ac_count, wa_count))
