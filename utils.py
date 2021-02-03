N_TRUNC = 4


def trunc(numero: float) -> float:
    """
    Trunca um número float em N casas decimais sem arredondamento
    """
    numero = str(float(numero))
    inteira, decimal = numero.split('.')

    decimal += '0' * N_TRUNC

    return float('{}.{}'.format(inteira, decimal[:N_TRUNC]))


def preview(numero: float) -> str:
    """
    Formata um número em N casas decimais, de acordo com o valor
    de N_TRUNC
    """
    numero = str(trunc(numero))
    inteira, decimal = numero.split('.')

    decimal += '0' * 5
    return '{}.{}'.format(inteira, decimal[:N_TRUNC])


def math_doted(equacao_input: str, operador: str) -> str:
    """
    Remove o operador e adicionar `math.operador` da equação
    """
    return equacao_input.replace(operador, f'math.{operador}')


PARSE_STRATEGY = {
    'sin': math_doted,
    'cos': math_doted,
    'e': math_doted,
    '^': lambda equacao_input, operador: equacao_input.replace(operador, '**'),
    'x': lambda equacao_input, operador: equacao_input.replace(operador, '{x}')
}


def prepare_function(funcao_do_usuario: str) -> callable:
    """
    Recebe uma função como string de input do usuário e retorna uma
    função python que calcula f(x).
    """
    for operador, strategy in PARSE_STRATEGY.items():
        print('formando o opeardor', operador)
        funcao_do_usuario = strategy(funcao_do_usuario, operador)

    print('a funcao ficou assim: ', funcao_do_usuario)

    def f(x):
        return trunc(eval(funcao_do_usuario.format(x=x)))

    return f
