#диалог
def dialogue(name):
    return 'I purple your, ' + name
#Числа Фиббоначи
def fibon(n):
    a = 1
    b = 1
    yield a
    yield b
    while a + b < n:
        f = a + b
        a = b
        b = f
        yield f
#сумма
def add(a, b, c, d):
    return a + b + c + d
def mul(k, w, q, l):
    return k * w * q * l
def sub(e, f, g):
    return e - f - g
def div(p, m):
    return p / m