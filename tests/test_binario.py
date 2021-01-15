import pytest

from binarios.bin import binario_para_inteiro, int_to_bin


def _python_int_to_bin_str(numero):
    binario = str(bin(numero))
    _, binario = binario.split('b')
    return binario


class TestBinarioParaInteiro:
    """
    Teste da função `binario_para_inteiro`
    """

    @pytest.mark.parametrize(
        'binario', map(_python_int_to_bin_str, range(1000))
    )
    def test_somente_resultados_inteiros(self, binario):
        expected_value = int(binario, 2)
        assert binario_para_inteiro(binario) == expected_value

    @pytest.mark.parametrize('binario, esperado', [
        ('1.1001', 1.5625),
        ('1.010001', 1.265625),
        ('11000101.101', 197.625),
    ])
    def test_somente_valores_fracionados(self, binario, esperado):
        assert binario_para_inteiro(binario) == esperado


class TestInteiroParaBinario:
    """
    Teste da função `int_to_bin`
    """

    @pytest.mark.parametrize(
        'inteiro', range(1000)
    )
    def test_somente_numeros_interios(self, inteiro):
        expected = _python_int_to_bin_str(inteiro)
        assert int_to_bin(str(inteiro)) == expected

    @pytest.mark.parametrize('fracionado, esperado', [
        ('1.5625', '1.1001')
    ])
    def test_somente_numeros_interios(self, fracionado, esperado):
        # assert int_to_bin(fracionado) == esperado
        pass
