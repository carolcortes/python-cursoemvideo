print(f'\033[1;4m{"FICHA DO JOGADOR":^20}\033[m')


def ficha(jog='<não informado>', gol=0):
    print(f' - O jogador {jog} fez {gol} gol(s) no campeonato.')


j = str(input('Nome do jogador: ')).strip().title()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j == '':
    ficha(gol=g)
else:
    ficha(j, g)
                                                                                                                                                                                                                                                                                print(f'\033[1;4m{"FICHA DO JOGADOR":^20}\033[m')


def ficha(jog='<não informado>', gol=0):
    print(f' - O jogador {jog} fez {gol} gol(s) no campeonato.')


j = str(input('Nome do jogador: ')).strip().title()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j == '':
    ficha(gol=g)
else:
    ficha(j, g)
