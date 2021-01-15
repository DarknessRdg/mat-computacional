def _default_min_loop():
    return 6


def _default_media(a, b):
    return (a + b) / 2


def bissecao(a, b, funcao, media=_default_media, tolerancia=None, min_loops=None):
    min_loops = min_loops or _default_min_loop()

    for i in range(min_loops):
        x = media(a, b)

        f_a = funcao(a)
        f_b = funcao(b)
        f_x = funcao(x)

        if f_x * f_a < 0:
            b = x
        else:
            a = x

        feedback = (
            'a = {},  '
            'b = {},  '
            'x = {},  '
            'f(a) = {},  '
            'f(b) = {},  '
            'f(x) = {}'
        )
        feedback = feedback.format(a, b, x, f_a, f_b, f_x)
        print(feedback)
