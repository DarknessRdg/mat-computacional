from utils import trunc


def newton(inicial, funcao, derivada, tolerancia):
    x0 = inicial
    x1 = x0

    f_x0 = 1

    it = 0
    primeira = True
    todos = []
    while primeira or abs(f_x0) > tolerancia or f_x0 != 0:
        primeira = False
        it += 1

        f_x0 = funcao(x0)
        todos.append(f_x0)

        f_derivada_x0 = derivada(x0)

        x1 = x0 - f_x0 / f_derivada_x0
        x0 = x1

    return todos



def bissecao(a, b, funcao, tolerancia, max_loops=50):
    """
    Cálculo numéro da bisseção.
    """
    x = funcao((a + b) / 2)

    stop = False

    todos_x = []
    for i in range(1, max_loops + 1):
        if stop:
            break

        x = (a + b) / 2

        f_a = funcao(a)
        f_x = funcao(x)
        todos_x.append((b - a) / 2)

        if abs((b - a) / 2) < tolerancia or f_x == 0:
            stop = True

        if f_x * f_a < 0:
            b = x
        else:
            a = x

    return todos_x


def falsa_posicao(a, b, funcao, tolerancia):
    def get_x(_a, _b, _f_a, _f_b):
        return (_a * _f_b - _b * _f_a) / (_f_b - _f_a)

    primeira = True
    f_x = 1

    todos_x = []
    while primeira or abs(f_x) > tolerancia:
        primeira = False

        f_a = funcao(a)
        f_b = funcao(b)

        x = get_x(a, b, f_a, f_b)

        f_x = funcao(x)
        todos_x.append(f_x)

        if f_a * f_x < 0:
            b = x
        else:
            a = x
    return todos_x


def secante(x1, x2, funcao, tolerancia):
    f_x1 = 0
    loop = 0

    todos_x = []
    while loop == 0 or abs(f_x1) > tolerancia:
        loop += 1

        f_x1 = funcao(x1)
        todos_x.append(f_x1)

        f_x2 = funcao(x2)

        x3 = x2 - ((f_x2 * (x1 - x2)) / (f_x1 - f_x2))

        x1, x2 = x2, x3

    return todos_x


planilha = open('planilha.csv', 'w')


# def f(j):
#     return (p * (1 - (1 + j) ** -n)) / j - q0


def f(x):
    return x**3 - 9*x + 3

def f_(x):
    return 3*x**2 - 9

#
# q0 = 60000
# n = 36
# p = 2000


def normaliza(*arg):

    arg = list(arg)

    for i in arg:
        for j in range(len(i)):
            i[j] = trunc(i[j])

    for i in arg:
        while len(i) > 15:
            i.pop()

        while len(i) < 15:
            i.append('')


if __name__ == '__main__':
    tolerancia = 10**(-3)

    res = [
        secante(1, 2, f, tolerancia),
        falsa_posicao(1, 2, f, tolerancia),
        bissecao(1, 2, f, tolerancia),
        newton(2, f, f_, tolerancia)
    ]

    planilha.write('secante;falsa posicao;bissecao;newton\n')

    def s(s):
        return str(s).replace('.', ',')

    normaliza(*res)
    for i in range(15):
        planilha.write(';'.join(map(s, (res[0][i], res[1][i], res[2][i], res[3][i]))))
        planilha.write('\n')
    planilha.close()
