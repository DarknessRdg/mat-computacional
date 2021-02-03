def falsa_posicao(
    a: float,
    b: float,
    funcao: callable,
    torlancia: float
) -> float:
    def get_x(_a, _b, _f_a, _f_b):
        return (_a * _f_b - _b * _f_a) / (_f_b - _f_a)

    primeira = True
    f_x = 1

    while primeira or abs(f_x) > torlancia:
        primeira = False

        f_a = funcao(a)
        f_b = funcao(b)

        x = get_x(a, b, f_a, f_b)

        f_x = funcao(x)

        feedback = (
            'a = {} '
            'b = {} '
            'f(a) = {} '
            'f(b) = {} '
            'x = {} '
            'f(x) = {}'
        )
        print(feedback.format(
            *map(preview, (a, b, f_a, f_b, x, f_x))
        ))

        if f_a * f_x < 0:
            b = x
        else:
            a = x
    return x


def main():
    equacao = input('digite a equacao: ')
    a = float(input('digite o valor de a: '))
    b = float(input('digite o valor de b: '))
    tol = float(input('digite o valor de tolerancia: '))

    equacao = prepare_function(equacao)

    res = trunc(falsa_posicao(a, b, equacao, tol))

    print(res)

    line = '=' * 10
    print('\n'+line+'\n')


# pra executar todods
# faca python3 nome.py < entrada.txt
if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
