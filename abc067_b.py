n, k = [int(i) for i in input().split(" ")]
l = [int(i) for i in input().split(" ")]
print(sum(sorted(l, reverse=True)[0:k]))