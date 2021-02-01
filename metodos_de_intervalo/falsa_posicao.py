import math
from decimal import Decimal, localcontext, ROUND_DOWN

N_TRUC = 4


def math_doted(equacao_input, operador):
    return equacao_input.replace(operador, f'math.{operador}')


PARSE_STRATEGY = {
    'sin': math_doted,
    'cos': math_doted,
    'e': math_doted,
    '^': lambda equacao_input, operador: equacao_input.replace(operador, '**'),
    'x': lambda equacao_input, operador: equacao_input.replace(operador, '{x}')
}


def trunc(numero: float) -> float:
    """
    Trunca um número float em N casas decimais sem arredondamento
    """
    numero = str(numero)
    inteira, decimal = numero.split('.')

    decimal += '0' * N_TRUC

    return float('{}.{}'.format(inteira, decimal[:N_TRUC]))


def preview(numero: float) -> str:
    numero = str(trunc(numero))
    inteira, decimal = numero.split('.')

    decimal += '0' * 5
    return '{}.{}'.format(inteira, decimal[:N_TRUC])


def prepare_function(funcao_do_usuario: str) -> callable:
    for operador, strategy in PARSE_STRATEGY.items():
        print('formando o opeardor', operador)
        funcao_do_usuario = strategy(funcao_do_usuario, operador)

    print('a funcao ficou assim: ', funcao_do_usuario)

    def executador_do_meu_eval(x):
        return trunc(eval(funcao_do_usuario.format(x=x)))

    return executador_do_meu_eval


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
