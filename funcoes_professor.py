import math


def letra_a(x):
    return x**3 - 9*x + 3


def derivada_letra_a(x):
    return 3*x**2 - 9


def letra_b(x):
    return x**4 - 14*x**2 + 24*x - 10


def letra_c(x):
    return math.e**x - math.sin(x) - 2


def letra_d(x):
    return math.e**(-x) - x


def letra_e(x):
    return math.sin(x)**2 - x * math.sin(x) + 0.25*x**2


def letra_f(x):
    return x**5 - 6*x**4 - 14*x**3 + 72*x**2 + 44*x - 180


def letra_g(x):
    return math.e**x + x**2 - 2
