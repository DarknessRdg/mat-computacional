def binario_para_inteiro(numero: str, show_steps: bool = False):
    spited = numero.split('.')
    parte_fracionada = []

    parte_inteira = spited[0]
    if len(spited) == 2:
        parte_fracionada = spited[1]

    potencia = 0
    somatoria = 0
    passos_binario = []
    passos_inteiro = []

    for numero in map(int, parte_inteira[::-1]):
        somatoria += numero * 2 ** potencia

        if numero != 0:
            passos_binario.insert(0, f'2**{potencia}')
            passos_inteiro.insert(0, f'{2 ** potencia}')
        potencia += 1

    potencia = 0
    for numero in map(int, list(parte_fracionada)):
        potencia += 1
        if numero == 0:
            continue

        somatoria += 1 / (2 ** potencia)

        passos_binario.append(f'1/2**{potencia}')
        passos_inteiro.append(f'{1 / (2 ** potencia)}')

    if show_steps:
        print(', '.join(passos_binario))
        print(', '.join(passos_inteiro))
    return somatoria


def int_to_bin(numero: str):
    separado = numero.split('.')

    resultado = str(bin(int(separado.pop(0)))).split('b')[1]

    if separado:
        resultado += _int_frac_to_bin(int(separado.pop()))

    return resultado


def _int_frac_to_bin(fracao_interia: int) -> str:
    resultados = []

    while fracao_interia not in (1, 0):
        fracao_interia *= 2
        resultados.append(int(fracao_interia))

        if resultados[-1] == 1:
            fracao_interia -= 1

    return ''.join(resultados)
