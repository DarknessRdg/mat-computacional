# Alunos:
#    Luan da Silva Rodrigues
#    Marcelo Augusto Lima Feitosa

import random
from typing import List, Any


SEGUNDA_POSICAO = 1
MEDIANA_11 = 6
MEDIANA_21 = 11
MEDIADA_42 = 21


# ----- questão 1 -----
def busca_primeira_ocorrencia(conjunto: List[Any], alvo: Any) -> int:
    """
    Função que busca o índice da primeira ocorrência de um elemento
    em um determinado conjunto. Se o elemento não estiver no conjunto,
    então é retornado -1.
    """
    tamanho = len(conjunto)

    for index in range(tamanho):
        if conjunto[index] == alvo:
            return index
    return -1


def cria_lista_com_n_elementos(n: int) -> List[int]:
    """
    Função auxiliar para retornar uma lista de tamanho N com os números
    de 1 a N sem repetição embaralhados.
    """
    lista = [i+1 for i in range(n)]
    random.shuffle(lista)
    return lista


# ----- questão 2 e questão 4 -----
lista_com_11 = cria_lista_com_n_elementos(11)
lista_com_21 = cria_lista_com_n_elementos(21)
lista_com_42 = cria_lista_com_n_elementos(42)


if __name__ == '__main__':
    # ----- questão 3 -----

    # segunda posição
    assert busca_primeira_ocorrencia(
        lista_com_11, lista_com_11[SEGUNDA_POSICAO]) == SEGUNDA_POSICAO

    assert busca_primeira_ocorrencia(
        lista_com_21, lista_com_21[SEGUNDA_POSICAO]) == SEGUNDA_POSICAO

    assert busca_primeira_ocorrencia(
        lista_com_42, lista_com_42[SEGUNDA_POSICAO]) == SEGUNDA_POSICAO

    # mediana
    assert busca_primeira_ocorrencia(
        lista_com_11, lista_com_11[MEDIANA_11]) == MEDIANA_11

    assert busca_primeira_ocorrencia(
        lista_com_21, lista_com_21[MEDIANA_21]) == MEDIANA_21

    assert busca_primeira_ocorrencia(
        lista_com_42, lista_com_42[MEDIADA_42]) == MEDIADA_42

    # para valor não existente
    assert busca_primeira_ocorrencia(lista_com_11, 20) == -1
    assert busca_primeira_ocorrencia(lista_com_21, 30) == -1
    assert busca_primeira_ocorrencia(lista_com_42, 50) == -1
