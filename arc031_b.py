n = 10
m = []

sx = 0
sy = 0

found = False
for i in range(n):
    r = list(input())

    # First found "o"
    if "o" in r and not found:
        sx = r.index("o")
        sy = i
        found = True

    m.append(r)

def count(m, t):
    c = 0
    for r in m:
        c += sum([1 if rr == t else 0 for rr in r])

    return c

def dfs(x, y, m, visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if visited[y][x]:
        return

    here = m[y][x]

    if here == "x":
        return

    visited[y][x] = True

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(x + d[0], y + d[1], m, visited)

def judge(sx, sy, m):
    visited = [[False] * n for _ in range(n)]
    dfs(sx, sy, m, visited)
    co = count(m, "o")
    cv = count(visited, True)

    return co == cv

if judge(sx, sy, m):
    print("YES")
    exit()

for i in range(n):
    for j in range(n):
        _map = [[mmm for mmm in mm] for mm in m]
        if _map[i][j] == "x":
            _map[i][j] = "o"

            if judge(sx, sy, _map):
                print("YES")
                exit()

print("NO")
