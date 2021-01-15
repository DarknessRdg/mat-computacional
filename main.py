def funcao(x):
    return round(x**3 - 9*x + 3, 2)


def media(a, b):
    return round((a+b) / 2, 2)


if __name__ == '__main__':
    a, b = 2, 3.5

    for i in range(6):
        x = media(a, b)

        value = funcao(x)
        value_a = funcao(a)

        if value * value_a < 0:
            b = x
        else:
            a = x

        print(f'a = {a},  b = {b},   x = {x},  value = {value}')
