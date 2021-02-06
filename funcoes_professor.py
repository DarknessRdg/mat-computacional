import math

from utils import trunc


def letra_a(x):
    return trunc(x**3 - 9*x + 3)


def derivada_letra_a(x):
    return trunc(3*x**2 - 9)


def letra_b(x):
    return trunc(x**4 - 14*x**2 + 24*x - 10)


def derivada_letra_b(x):
    return trunc(4*x**3 - 28*x + 24)


def letra_c(x):
    return trunc(math.e**x - math.sin(x) - 2)


def derivada_letra_c(x):
    return trunc(math.e**x - math.cos(x))


def letra_d(x):
    return trunc(math.e**(-x) - x)


def derivada_letra_d(x):
    return trunc(-(math.e**(-x)) - 1)


def letra_e(x):
    return trunc(math.sin(x)**2 - x * math.sin(x) + 0.25*x**2)


def derivada_letra_e(x):
    return trunc(math.sin(2*x) - math.sin(x) - x*math.cos(x) + 0.5*x)


def letra_f(x):
    return trunc(x**5 - 6*x**4 - 14*x**3 + 72*x**2 + 44*x - 180)


def derivada_letra_f(x):
    return trunc(5*x**4 - 24*x**3 - 4*x**2 + 144*x + 44)


def letra_g(x):
    return trunc(math.e**x + x**2 - 2)


def derivada_letra_g(x):
    return trunc(2*x + math.e**x)
