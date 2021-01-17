from primos.primo import eh_primo
import pytest


@pytest.mark.parametrize('primo', [
    2, 3, 5, 7, 11, 13, 17, 19,
    23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79,
    83, 89, 97
])
def test_primos(primo):
    assert eh_primo(primo)


@pytest.mark.parametrize('nao_primo', [
    0, 1, 4, 6, 8, 9, 10, 12, 14, 15,
    16, 18, 20, 21, 24
])
def test_nao_sao_primos(nao_primo):
    assert not eh_primo(nao_primo)
