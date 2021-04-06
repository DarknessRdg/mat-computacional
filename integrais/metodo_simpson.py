from math import e


def metodo_simple(a, b, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 2
    x2 = a + h

    return (h/3) * (funcao(a) + 4*funcao(x2) + funcao(b))


def metodo_compost(a, b, n, funcao):
    a, b = sorted([a, b])

    h = (b - a) / 2

    intervalos = [a + h*it for it in range(n)]
    intervalos.append(b)

    soma = 0
    for i in range(n):
        soma += metodo_simple(intervalos[i], intervalos[i+1], funcao)
    return soma


if __name__ == '__main__':
    print(metodo_simple(1, 3, lambda x: e**(-x**2)))
    print(metodo_compost(1, 3, 2, lambda x: e**(-x**2)))

