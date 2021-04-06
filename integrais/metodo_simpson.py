from math import e, sqrt, pi


def metodo_simple(a, b, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 2
    x2 = a + h

    return (h/3) * (funcao(a) + 4*funcao(x2) + funcao(b))


def metodo_compost(a, b, n, funcao):
    n = 2*n
    a, b = sorted([a, b])

    h = (b - a) / (n)

    intervalos = [a + h*it for it in range(n)]
    intervalos.append(b)

    soma = 0
    for i in range(1, n):
        mult = 4 if i % 2 != 0 else 2
        soma += mult * funcao(intervalos[i])

    return (funcao(a) + soma + funcao(b)) * (h/3)


def treis_oitavos(a, b, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 2
    x2 = a + h
    return metodo_simple(a, x2, funcao) + metodo_simple(x2, b, funcao)


def formula(x):
    return e ** (-(x**2) / 2) / (sqrt(2*pi))


if __name__ == '__main__':
    print(metodo_compost(0, 1, 4, lambda x: x * sqrt((x ** 2) + 1)))

    intv = [
        [-1, 1],
        [-2, 2],
        [-3, 3],
    ]
    for (_a, _b) in intv:
        print(_a, _b)
        print(round(metodo_compost(_a, _b, 4, formula), 5))
