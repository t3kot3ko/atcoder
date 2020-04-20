n = int(input())
xs = [int(e) for e in input().split(" ")]

print(min([sum([(x - p) ** 2 for x in xs]) for p in range(1, 101)]))
    
