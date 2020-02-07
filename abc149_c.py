def is_prime(n):
    if n == 1:
        return False

    i = 2
    while True:
        if i ** 2 >= n:
            return True
        if n % i == 0:
            return False
        i += 1

x = int(input())
for i in range(x, x ** 2):
    if is_prime(i):
        print(i)
        break
