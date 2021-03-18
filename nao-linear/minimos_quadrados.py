from typing import List


def print_polinomio(valores_a: List[float]):
    print('Valores do vetor A:')
    print(valores_a)

    valores_a = valores_a[::-1]

    pot = len(valores_a) - 1
    polinomio = []

    for a in valores_a:
        polinomio.append('+' if a >= 0 else '-')
        a = abs(a)
        if pot == 0:
            polinomio.append(str(a))
        elif polinomio == 1:
            polinomio.append('{}x'.format(a))
        else:
            polinomio.append('{}x^{}'.format(a, pot))
        pot -= 1

    print('Polinômio')
    print(' '.join(polinomio))


def pow(it: float, potencia: int) -> float:
    return round(it**potencia, 2)


def minimos_quadrados(
        x: List[float],
        y: List[float],
        grau: int
) -> List[float]:
    n = len(x)

    matriz = []

    primeira_linha = [
        sum(map(lambda it: pow(it, potencia), x))
        for potencia in range(1, grau+1)
    ]
    primeira_linha.insert(0, n)

    matriz.append(primeira_linha)

    for loop in range(1, grau+1):
        matriz.append([
            sum(map(lambda it: pow(it, potencia), x))
            for potencia in range(loop, grau + loop + 1)
        ])

    b = []
    for loop in range(grau+1):
        valores = [
            x1 ** loop * y1
            for x1, y1 in zip(x, y)
        ]
        b.append(sum(valores))

    return list(map( lambda e: round(e, 5), gaus(matriz, b)))


def pivotagem(matriz: List[List], index_pivo: int):
    i = index_pivo
    while matriz[index_pivo][index_pivo] == 0:
        matriz[i], matriz[i+1] = matriz[i+1], matriz[i]
        i += 1


def gaus(matriz: List[List], b: List) -> List[float]:
    n = len(matriz)

    for index, el in enumerate(b):
        matriz[index].append(el)

    for indice_pivo in range(n):
        pivotagem(matriz, indice_pivo)

        linha_pivo = matriz[indice_pivo]
        pivo = linha_pivo[indice_pivo]

        for linha in matriz[indice_pivo+1:]:
            m = linha[indice_pivo] / pivo

            for temp in range(indice_pivo, len(linha)):
                linha[temp] -= m * linha_pivo[temp]

    for index, linha in enumerate(matriz):
        b[index] = linha.pop()

    return subtituicao_regressiva(matriz, b)


def subtituicao_regressiva(matriz, b):
    resultados_x_acumulados = []

    for index_matriz in range(len(matriz)-1, -1, -1):
        b_atual = b[index_matriz]
        linha_matriz = matriz[index_matriz]

        soma = 0
        for index_rest in range(len(resultados_x_acumulados)):
            index_rest = - (index_rest + 1)

            rest = resultados_x_acumulados[index_rest]
            mult = linha_matriz[index_rest]

            soma += rest * mult

        pos = len(resultados_x_acumulados) + 1
        multiplicador_do_x = linha_matriz[-pos]

        valor_x = (b_atual - soma) / multiplicador_do_x
        resultados_x_acumulados.insert(0, valor_x)

    return resultados_x_acumulados


class Questao3:
    x = [2, 1.09, 3.35, 6.38, 0, 0.33, -1.77, 6.55, 4.2, 10.25, 2.67, 7.23, 0.51, 12.98, -2.51, -5.16, 3.82]
    y = [0, 0.09, 0.86, 2.32, 0, 0.12, -0.63, 2.32, 1.47, 3.49, 0.9, 2.36, 0.16, 3.83, -0.73, -1.49, 1.02]


class Questao4:
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    y = [1, 1, 1, 2, 2, 2, 2, 3, 8, 13, 19, 25, 30, 34, 69, 78, 98, 121, 200, 234, 291, 428, 621, 904, 1128, 1546, 1891,
         2201, 2433, 2915, 3417, 3904, 4256, 4579, 5717, 6836, 7910, 9056, 10278, 11130]

    @classmethod
    def calcula_valor_x(cls, valores_a, x):
        somatorio = 0
        for pot, a in enumerate(valores_a):
            somatorio += a * x ** pot
        return somatorio

    @classmethod
    def error_absoluto(cls, valores_a):
        valores_calculados = [cls.calcula_valor_x(valores_a, x) for x in cls.x]
        return sum([abs(a - b) for a, b in zip(valores_calculados, cls.y)]) / len(cls.x)


if __name__ == '__main__':
    # --------- QUESTAO 3 ---------
    questao_3_letra_a = minimos_quadrados(
        x=Questao3.x,
        y=Questao3.y,
        grau=2
    )
    print_polinomio(questao_3_letra_a)

    questao_3_letra_b = minimos_quadrados(
        x=Questao3.x,
        y=Questao3.y,
        grau=4
    )

    print_polinomio(questao_3_letra_b)

    # --------- QUESTAO 4 ---------
    questao_4_item_1 = minimos_quadrados(x=Questao4.x, y=Questao4.y, grau=30)
    dias = [
        (41, '06/04'),
        (42, '07/04'),
        (43, '08/04'),
        (44, '09/04'),
        (45, '10/04'),
        (46, '11/04'),
        (47, '12/04'),
    ]
    for x_do_dia, dia in dias:
        print('{} = {}'.format(dia, Questao4.calcula_valor_x(questao_4_item_1, x_do_dia)))

    print('Error absoluto item 1')
    print(Questao4.error_absoluto(
        minimos_quadrados(x=Questao4.x, y=Questao4.y, grau=10)
    ))
    print('Error absoluto item 1')
    print(Questao4.error_absoluto(
        minimos_quadrados(x=Questao4.x, y=Questao4.y, grau=20)
    ))
    print('Error absoluto item 1')
    print(Questao4.error_absoluto(
        minimos_quadrados(x=Questao4.x, y=Questao4.y, grau=30)
    ))



