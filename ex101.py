print(f'\033[1;4m{"CONTROLE ELEITORAL":^22}\033[m')


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f' - Com {idade} anos o voto é \033[1;4mNEGADO\033[m.'
    elif 16 <= idade < 18 or idade > 65:
        return f' - Com {idade} anos o voto é \033[1;4mOPCIONAL\033[m.'
    else:
        return f' - Com {idade} anos o voto é \033[1;4mOBRIGATÓRIO\033[m.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
   print(f'\033[1;4m{"CONTROLE ELEITORAL":^22}\033[m')


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f' - Com {idade} anos o voto é \033[1;4mNEGADO\033[m.'
    elif 16 <= idade < 18 or idade > 65:
        return f' - Com {idade} anos o voto é \033[1;4mOPCIONAL\033[m.'
    else:
        return f' - Com {idade} anos o voto é \033[1;4mOBRIGATÓRIO\033[m.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
