n, m = list(map(int, input().split(" ")))
nodes = {}

for i in range(m):
    a, b = list(map(int, input().split(" ")))
    if a not in nodes.keys():
        nodes[a] = []
    if b not in nodes.keys():
        nodes[b] = []

    nodes[a].append(b)
    nodes[b].append(a)


def search(node, nodes, visited=[], result=[]):
    visited = visited + [node]

    if len(visited) == len(nodes):
        result.append(visited)
        
    
    if node not in nodes.keys():
        print(node)
    else:
        for link in nodes[node]:
            if link in visited:
                continue

            search(link, nodes, visited)

    return result

print(len(search(1, nodes)))

