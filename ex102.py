print(f'\033[1;4m{"CALCULADORA DE FATORIAL":^25}\033[m')


def fatorial(n, show=False):
    """
    -> Função para calcular o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: Opção para mostrar ou não o cálculo.
    :return: Resultado do fatorial de um número n.
    """
    from math import factorial
    f = factorial(n)
    if show:
        print(f'{n}! = ', end='')
        for c in range(n, 0, -1):
            print(c, end='')
            print(' x ' if c > 1 else ' =print(f'\033[1;4m{"CALCULADORA DE FATORIAL":^25}\033[m')


def fatorial(n, show=False):
    """
    -> Função para calcular o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: Opção para mostrar ou não o cálculo.
    :return: Resultado do fatorial de um número n.
    """
    from math import factorial
    f = factorial(n)
    if show:
        print(f'{n}! = ', end='')
        for c in range(n, 0, -1):
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f


print(fatorial(int(input('Digite um número: ')), show=True))
help(fatorial)
