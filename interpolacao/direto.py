from metodos_interativos.gauss import gaus


def get_matrix(array_x, array_y, grau):
    matriz = []
    for x in array_x:
        matriz.append(
            [1] + [x ** i for i in range(1, grau+1)]
        )

    return gaus(matriz, array_y)


def calc_x(valores_x, x):
    s = 0
    for pot, a in enumerate(valores_x):
        s += a * (x ** pot)
    return s


def print_polinomio(x):
    v = [
        '{} x^{}'.format(i, index)
        for index, i in enumerate(x)
    ]
    v = v[::-1]
    print(' + '.join(v))


if __name__ == '__main__':

    r = get_matrix(
        array_x=[16, 40, 64, 88, 112],
        array_y=[4.2, 9.2, 10, 10.7, 8.6],
        grau=4
    )
    print_polinomio(map(lambda it: round(it, 4), r))

    print(calc_x(r, 105))
