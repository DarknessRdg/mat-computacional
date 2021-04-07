from math import e, sqrt, pi


def metodo_simple(a, b, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 2
    x2 = a + h

    return (h/3) * (funcao(a) + 4*funcao(x2) + funcao(b))


def metodo_compost(a, b, n, funcao):
    n = 2*n
    a, b = sorted([a, b])

    h = (b - a) / n

    intervalos = [a + h*it for it in range(n)]
    intervalos.append(b)

    soma = 0
    for i in range(1, n):
        mult = 4 if i % 2 != 0 else 2
        soma += mult * funcao(intervalos[i])

    return (funcao(a) + soma + funcao(b)) * (h/3)


def treis_oitavos(a, b, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 3
    x2 = a + h
    x3 = a + 2*h

    return (funcao(a) + 3 * funcao(x2) + 3 * funcao(x3) + funcao(b)) * ((3 * h) / 8)


def formula(x):
    return e ** (-(x**2) / 2) / (sqrt(2*pi))


if __name__ == '__main__':
    print(round(metodo_compost(0, 180, 4.5, formula), 5))
