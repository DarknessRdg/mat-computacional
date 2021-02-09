from typing import List

from funcoes_professor import matriz_b


def pivotagem(matriz: List[List], index_pivo: int):
    """
    Funcao auxiliar para realizar pivotagem para não permitir
    o pivô ter valor 0.
    """
    i = index_pivo
    while matriz[index_pivo][index_pivo] == 0:
        matriz[i], matriz[i+1] = matriz[i+1], matriz[i]
        i += 1


def gaus(matriz: List[List], b: List):
    """
    Método de gaus. O método recebe uma matriz quadrada de tamanho N
    e uma lista de valores da igualdade de tamanho N.

    Os calculos são realizados nos endereçoes da prórpia matriz,
    dessa forma, ao final o método a matriz original está modificada
    de modo que agora é uma matriz triangular superior e B com os novos
    valores calculados.
    """
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
    """
    Faz substituicao regressiva de uma matriz um e vetor b.
    Retorna lista com os valores de X em ordem crescente: [x1, x2, x3, x4 ...]
    """
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


if __name__ == '__main__':
    resultados_obtidos = gaus(*matriz_b())
    print(resultados_obtidos)
