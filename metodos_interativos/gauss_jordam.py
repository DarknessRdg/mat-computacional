from typing import List


def pivotagem(matriz: List[List[float]], index_pivo: int):
    """
    Funcao auxiliar para realizar pivotagem para não permitir
    o pivô ter valor 0.
    """
    i = index_pivo
    while matriz[index_pivo][index_pivo] == 0:
        matriz[i], matriz[i+1] = matriz[i+1], matriz[i]
        i += 1


def get_pivo(linha: List[float], index_pivo: int) -> float:
    """Retorna o elemento da linha que é o pivô da linha"""
    return linha[index_pivo]


def gauss_jordam(
    matiz: List[List[float]],
    valores_b: List[float]
) -> List[float]:
    """
    Calcula as raizes de uma matriz utilizando método de Gaus-Jordan.
    Ao final é retornado um vetor com as raízes: [x1, x2, x3, x4 , ...]
    """
    for index, el in enumerate(valores_b):
        matiz[index].append(el)

    for index_pivo in range(len(matiz)):
        pivotagem(matiz, index_pivo)

        linha_pivo = matiz[index_pivo]
        pivo = get_pivo(linha_pivo, index_pivo)

        for i in range(len(linha_pivo)):
            linha_pivo[i] /= pivo

        for index_para_sub in range(len(matiz)):
            if index_para_sub == index_pivo:
                continue

            linha_sub = matiz[index_para_sub]
            pivo = get_pivo(linha_sub, index_pivo)

            for j in range(len(linha_sub)):
                linha_sub[j] -= linha_pivo[j] * pivo

    return list(map(lambda linha: linha.pop(), matiz))


if __name__ == '__main__':
    m = [
        [4, -2, -3, 6],
        [-6, 7, 6.5, -6],
        [1, 7.5, 6.25, 5.5],
        [-12, 22, 15.5, -1]
    ]
    b = [12, -6.5, 16, 17]

    raizes = gauss_jordam(m, b)

    for i, x in enumerate(raizes):
        print(f'x{i+1} = {x}')
