import math

from utils import trunc


def _default_media(a: float, b: float) -> float:
    """
    Função que retorna média de dois números
    """
    return (a + b) / 2


def bissecao(
        a: float,
        b: float,
        funcao: callable,
        media: callable = _default_media,
        tolerancia: float = None,
        max_loops: int = 50
) -> float:
    """
    Cálculo numéro da bisseção.
    """
    x = funcao(m(a, b))

    stop = False

    for i in range(1, max_loops + 1):
        if stop:
            break

        feedback = (
            'loop = {},  '
            'a = {},  '
            'b = {},  '
        )
        print(feedback.format(i, a, b), end='')
        x = media(a, b)

        f_a = funcao(a)
        f_x = funcao(x)

        if abs((b - a) / 2) < tolerancia or f_x == 0:
            stop = True

        if f_x * f_a < 0:
            b = x
        else:
            a = x

        feedback = (
            'x = {},  '
            'f(x) = {},  '
            'f(a) = {},  '
        )
        feedback = feedback.format(x, f_x, f_a)
        print(feedback)

    return x


if __name__ == '__main__':
    def f(value):
        def wrapper(x):
            return x**3 + 12*x**2 - 100*x -6

        return trunc(wrapper(value))


    def m(a, b):
        return trunc(_default_media(a, b))

    resultado = trunc(
        bissecao(
            a=5,
            b=6,
            funcao=f,
            media=m,
            tolerancia=10 ** (-3)
        )
    )
    print('resultado', resultado)
    print('f(resultado) =', f(resultado))
