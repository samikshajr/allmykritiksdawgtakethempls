import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s = 10**-8
def L(f, c, x):
    return f(c) + ((f(c + s) - f(c - s)) / (2 * s) * (x - c))
def x1_x2(f, c, e):
    n = 0
    delta_x = 10 ** -6
    x1 = c
    x2 = c

    while abs(f(x1) - L(f, c, x1)) < e:
        x1 -= delta_x
        n += 1
        if n > 5000000:
            break
    while abs(f(x2) - L(f, c, x2)) < e:
        x2 += delta_x
        n += 1
        if n > 5000000:
            break
    if n < 5000000:
        return x1, x2
    else:
        return "No such x1 or x2 values cna be found within a reasonable range or iterations"

def f1(x):
    return x ** 2
def f2(x):
    return np.sin(x)
def f3(x):
    return np.exp(x)

print(x1_x2(f1, 1, 0.1))
print(x1_x2(f2, np.pi / 4, 0.05))
print(x1_x2(f3, 0, 0.01))

