def aumentar(v, a, form=False):
    return moeda(v + (v*a/100)) if form else v + (v*a/100)


def diminuir(v, d, form=False):
    return moeda(v - (v*d/100)) if fdef aumentar(v, a, form=False):
    return moeda(v + (v*a/100)) if form else v + (v*a/100)


def diminuir(v, d, form=False):
    return moeda(v - (v*d/100)) if form else v - (v*d/100)


def dobro(v, form=False):
    return moeda(v*2) if form else v * 2


def metade(v, form=False):
    return moeda(v/2) if form else v / 2


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(v=0, a=0, d=0):
    print(f'{"-" * 30}\n{"RESUMO DO VALOR":^30}\n{"-" * 30}\n'
          f'{"PREÇO ANALISADO:":<15}{moeda(v):>14}\n'
          f'{"DOBRO DO PREÇO:":<15}{dobro(v, True):>15}\n'
          f'{"METADE DO PREÇO:":<15}{metade(v, True):>14}\n'
          f'{f"{a}% DE AUMENTO:":>15}{aumentar(v, a, True):>15}\n'
          f'{f"{d}% DE REDUÇÃO:":>15}{diminuir(v, d, True):>15}\n'
          f'{"-"*30}')
