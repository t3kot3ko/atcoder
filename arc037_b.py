n, m = map(int, input().split(" "))
uvs = [[False] * n for _ in range(n)]
visited = [False] * n

for i in range(m):
    u, v = map(int, input().split(" "))
    # if u not in uvs.keys():
    #     uvs[u] = []
    # uvs[u].append(v)
    uvs[u-1][v-1] = True
    uvs[v-1][u-1] = True

def dfs(u):
    r = True

    if visited[u]:
        return False

    visited[u] = True

    for v, available in enumerate(uvs[u]):
        if available:
            uvs[v][u] = False
            uvs[u][v] = False

            r &= dfs(v)

    return r


c = 0
while not all(visited):
    u = visited.index(False)
    c += 1
    r = dfs(u)

    if not r:
        c -= 1

print(c)
