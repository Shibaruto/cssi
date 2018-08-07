def longest_word(x,y,z):
    print len(x), len(y), len(z)
    if lx >= ly and lx >= lz:
        return x
    elif ly >= lx and ly >= lz:
        return y
    else:
        return z

def reverse_string(T):
    o = ""
    for i in T:
        o = i + o
    return o

def sum_to_n(n):
    c = 0
    for i in range(1, n+1):
        c = c + i
    return c

def is_triangle(a,b,c):
    sabc = a + b > c
    sacb = a + c > b
    sbca = b + c > a
    if sabc and sacb and sbca:
        return True
    else:
        return False

def roll_dice(num):
    g = 0
    for i range(num):
        g = g + i
        random.randint(1,6)
        return g
