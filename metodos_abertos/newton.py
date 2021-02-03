from funcoes_professor import letra_a, derivada_letra_a
from utils import preview


def newton(inicial, funcao, derivada, tolerancia):
    x0 = inicial
    x1 = x0

    f_x0 = 1

    it = 0
    primeira = True
    while primeira or abs(f_x0) > tolerancia or f_x0 != 0:
        primeira = False
        it += 1

        f_x0 = funcao(x0)
        f_derivada_x0 = derivada(x0)

        x1 = x0 - f_x0 / f_derivada_x0

        feedback = (
            'it: {} '
            'xi: {} '
            'f(xi) {} '
            "f'(xi): {} "
            'xi+1: {}'
        )
        print(feedback.format(
            it, *map(preview, (x0, f_x0, f_derivada_x0, x1))
        ))

        x0 = x1

    return x1


if __name__ == '__main__':
    res = newton(3.5, letra_a, derivada_letra_a, 0.001)
    print(res)
