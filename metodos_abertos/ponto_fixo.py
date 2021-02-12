from math import *


def f(r):
    s = pi * r * sqrt((r ** 2) + (20 ** 2))
    return round(s, 4)


def calc_r(r):
    return 1200 / (pi * sqrt((r ** 2) + (20 ** 2)))


def ponto_fixo(x, it, funcao):
    for i in range(it):
        x = calc_r(x)
        print("f(x) = {}, x = {}".format(funcao(x), x))


if __name__ == '__main__':
    s = 1200
    h = 20
    pi = 3.1415

    ponto_fixo(17, 5, f)
