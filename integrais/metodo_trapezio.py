from math import e


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


if __name__ == '__main__':
    print(tapezio_simples(3, 1, lambda x: e**(-x**2)))
    print(trapezio_compost(3, 1, 4, lambda x: e**(-x**2)))
