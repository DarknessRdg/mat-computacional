def get_polinomio_newton(array_x, array_y):
    ordens = [array_y]

    for n_ordem_atual in range(1, len(array_x)):
        ordem_atual = ordens[-1]

        prox_ordem = []
        for index in range(len(ordem_atual) - 1):
            cima = ordem_atual[index + 1] - ordem_atual[index]
            baixo = array_x[index + n_ordem_atual] - array_x[index]

            if baixo == 0:
                prox_ordem.append(0)
            else:
                prox_ordem.append(cima / baixo)

        ordens.append(prox_ordem)

    return [ordem.pop(0) for ordem in ordens]


def get_x(ordem, valores_x, x):
    valores = []

    for i in range(len(ordem)):
        atual = ordem[i]

        for j in range(i):
            xi = valores_x[j]
            atual *= x - xi
        valores.append(atual)

    return sum(valores)


def print_polinomio(ordem, valores_x):
    itens = []
    for i in range(len(ordem)):
        d = round(ordem[i], 4)

        x_formatados = ''
        for j in range(i):
            x_formatados += '(x - {})'.format(valores_x[j])

        itens.append('{}{}'.format(d, x_formatados))

    print('f(x) =', ''.join(itens))


if __name__ == '__main__':
    array_x = [1, 2.5, 2, 3, 4, 5],
    array_y = [1, 7, 5, 8, 2, 1]

    ordens = get_polinomio_newton(
        array_x=array_x,
        array_y=array_y
    )

    print_polinomio(ordens, array_x)

    print(get_x(ordens, array_x, 3.5))
