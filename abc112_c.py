import sys
n = int(input())
d = [list(map(int, l.split(" "))) for l in sys.stdin.readlines()]

for cx in range(0, 101):
    for cy in range(0, 101):
        hs = [dd[2] + abs(dd[0] - cx) + abs(dd[1] - cy) for dd in d if dd[2] != 0]

        if hs[0] >= 1 and all([h == hs[0] for h in hs]):
            if all([hs[0] - abs(dd[0] - cx) - abs(dd[1] - cy) <= 0 for dd in d if dd[2] == 0]):
                print("{} {} {}".format(cx, cy, hs[0]))
                exit()
            else:
                continue
