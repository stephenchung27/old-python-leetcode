def power(x, y):
    if y == 0: return 1
    temp = power(x, y // 2)
    if y % 2 == 0: return temp * temp
    else: return temp * temp * x

def multiply(x, y):
    p, c = 0, 0
    while y > 0:
        if y % 2 == 1: p += x << c
        c += 1
        y >>= 1
    return p

def divide(x, y):
    if x < y: return 0
    r, i, z = 0, 1, y
    while x > (z << 1):
        z <<= 1
        i <<= 1
    return divide(x - z, y >> i) + i

def add(x, y):
    while y != 0:
        c = x & y
        x ^= y
        y = c << 1
    return x

def subtract(x, y):
    while y != 0:
        c = (~x) & y
        x ^= y
        y = c << 1
    return x
