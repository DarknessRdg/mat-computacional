from math import e, sqrt, pi


def tapezio_simples(a, b, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 2
    return h * (funcao(a) + funcao(b))


def trapezio_compost(a, b, n, funcao):
    a, b = sorted([a, b])
    h = (b - a) / n
    intervalos = [a + h * at for at in range(n)]
    intervalos.append(b)

    soma = 0
    for i in range(n):
        soma += tapezio_simples(intervalos[i], intervalos[i+1], funcao)
    return soma


def formula(x):
    return (e ** (-(x**2) / 2)) / (sqrt(2*pi))


if __name__ == '__main__':
    print(round(tapezio_simples(-1, 1, formula), 5))
    print(round(trapezio_compost(-1, 1, 4, formula), 5))
