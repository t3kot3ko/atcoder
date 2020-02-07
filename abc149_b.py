a, b, k = [int(i) for i in input().split(" ")]
if a >= k:
    print("%d %d" % (a - k, b))
else: # a < k
    print("%d %d" % (0, b + (a - k)))

