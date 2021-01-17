def eh_divisivel(numero, divisor):
    return numero % divisor == 0


def eh_primo(numero):
    intervalo_de_teste = range(2, numero // 2 + 1)

    if 0 <= numero <= 1:
        return False

    for divisor in intervalo_de_teste:
        if eh_divisivel(numero, divisor):
            return False

    return True
