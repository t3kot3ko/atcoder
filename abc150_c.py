import itertools

n = int(input())
ps = list(map(int, input().split(" ")))
qs = list(map(int, input().split(" ")))

c = 0
for perm in itertools.permutations(list(range(1, n+1)), n):
    if all([ps[i] == perm[i] for i in range(n)]):
        a = c

    if all([qs[i] == perm[i] for i in range(n)]):
        b = c

    c += 1

print(a - b if a > b else b - a)
