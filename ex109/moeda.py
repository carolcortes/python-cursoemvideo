def aumentar(v, a, form=False):
    return moeda(v + (v*a/100)) if form else v + (v*a/100)


def diminuir(v, d, form=False):
    return moeda(v - (v*d/100)) if form else v - (v*d/100)


def dobro(v, form=False):
    return moeda(v*2) if form else v * 2


def metade(v, form=False):
    return moeda(v/2) if form else v / 2


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
                                                                                                                                                                                                                                                                                                                                                         def aumentar(v, a, form=False):
    return moeda(v + (v*a/100)) if form else v + (v*a/100)


def diminuir(v, d, form=False):
    return moeda(v - (v*d/100)) if form else v - (v*d/100)


def dobro(v, form=False):
    return moeda(v*2) if form else v * 2


def metade(v, form=False):
    return moeda(v/2) if form else v / 2


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
