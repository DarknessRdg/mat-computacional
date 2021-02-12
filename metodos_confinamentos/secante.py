import math

from utils import trunc


def secante(x1, x2, funcao, tolerancia):
    f_x1 = 0
    loop = 0
    while loop == 0 or abs(f_x1) > tolerancia:
        loop += 1

        f_x1 = funcao(x1)
        f_x2 = funcao(x2)

        x3 = x2 - ((f_x2 * (x1 - x2)) / (f_x1 - f_x2))

        feedback = (
            'loop = {} '
            'x1 = {} '
            'x2 = {} '
            'f(x1) = {} '
            'f(x2) = {} '
            'x3 = {} '
            'f(x3) {} '
        )
        print(feedback.format(
           loop, *map(trunc, (x1, x2, f_x1, f_x2, x3, funcao(x3)))
        ))

        x1 = x2
        x2 = x3

    return x1


if __name__ == '__main__':

    print(secante(
        x1=1,
        x2=2,
        funcao=f,
        tolerancia=10 ** -3
    ))
