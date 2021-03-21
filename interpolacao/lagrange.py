from functools import reduce


def mult(iterable):
    return reduce(lambda acc, x: acc * x, iterable)


class Item(object):
    def __init__(self, cima, baixo, y):
        self.cima, self.baixo, self.y = cima, baixo, y

    def __str__(self):
        cima = []

        for x in self.cima:
            cima.append('(x - {})'.format(x))

        return '[ {} / {} ] * {}'.format(
            ' * '.join(cima),
            mult(self.baixo),
            self.y
        )

    def calc_x(self, x):
        baixo = mult(self.baixo)

        cima = mult(map(lambda it: x - it, self.cima))
        return (cima / baixo) * self.y


def get_polinomio(array_x, array_y):
    items = []
    for index, (x, y) in enumerate(zip(array_x, array_y)):

        cima = []
        baixo = []
        for sub_index, sub_x in enumerate(array_x):
            if sub_index == index:
                continue

            cima.append(sub_x)
            baixo.append(x - sub_x)

        items.append(Item(cima, baixo, y))

    return items


def calc_x(items, x):
    return sum(map(lambda it: it.calc_x(x), items))


i = get_polinomio(
    array_x=[1, 2.5, 2, 3, 4, 5],
    array_y=[1, 7, 5, 8, 2, 1]
)


if __name__ == '__main__':

    for y in i:
        print(y)

    print(calc_x(i, 3.5))
