import math
a, b, c, x, y = list(map(int, input().split(" ")))

ps = []
for i in range(max(x*2+1, y*2+1)):
    xx = max(math.ceil(x - i / 2), 0)
    yy = max(math.ceil(y - i / 2), 0)

    ps.append(i * c + a * xx + b * yy)

print(ps)
print(min(ps))
    
    
