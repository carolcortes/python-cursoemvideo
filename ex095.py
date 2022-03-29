gols, jogadores = [], []
while True:
    j = {'nome': str(input('Nome do jogador: ')).strip().title()}
    p = int(input('Quantas partidas o jogador jogou? '))
    for c in range(0, p):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    j['gols'] = gols[:]
    j['gtotal'] = sum(gols)
    jogadores.append(j.copy())
    j.clear()
    gols = []
    print('-' * 30)
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar? ')).upper().strip()[0]
    if mais == 'N':
        break
print(f'\n{"JOGADORES CADASTRADOS":^43}\n{"CÓD.":^5}{"NOME":^20}{"JOGOS":^10}{"GOLS":^10}')
for c in range(0, len(jogadores)):
    print(f'{c+1:^5}{jogadores[c]["nome"]:^20}{len(jogadores[c]["gols"]):^10}{jogadores[c]["gtotal"]:^10}')
print('-' * 43, '\n Deseja mostrar os dados de qual jogador?\n'
                'Digite o código do jogador ou \"0\" para finalizar a consulta.\n'+'-' * 43)
while True:
    cod = int(input('Digite o código do jogador: '))-1
    if cod < 0:
        break
    elif cod >= len(jogadores):
        print('Código inválido. Tente novamente.')
    else:
        print(f'  → \033[1;4mLEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"].upper()}:\033[m')
        for i, g in enumerate(jogadores[cod]['gols']):
  gols, jogadores = [], []
while True:
    j = {'nome': str(input('Nome do jogador: ')).strip().title()}
    p = int(input('Quantas partidas o jogador jogou? '))
    for c in range(0, p):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    j['gols'] = gols[:]
    j['gtotal'] = sum(gols)
    jogadores.append(j.copy())
    j.clear()
    gols = []
    print('-' * 30)
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar? ')).upper().strip()[0]
    if mais == 'N':
        break
print(f'\n{"JOGADORES CADASTRADOS":^43}\n{"CÓD.":^5}{"NOME":^20}{"JOGOS":^10}{"GOLS":^10}')
for c in range(0, len(jogadores)):
    print(f'{c+1:^5}{jogadores[c]["nome"]:^20}{len(jogadores[c]["gols"]):^10}{jogadores[c]["gtotal"]:^10}')
print('-' * 43, '\n Deseja mostrar os dados de qual jogador?\n'
                'Digite o código do jogador ou \"0\" para finalizar a consulta.\n'+'-' * 43)
while True:
    cod = int(input('Digite o código do jogador: '))-1
    if cod < 0:
        break
    elif cod >= len(jogadores):
        print('Código inválido. Tente novamente.')
    else:
        print(f'  → \033[1;4mLEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"].upper()}:\033[m')
        for i, g in enumerate(jogadores[cod]['gols']):
            print(f'No {i+1}º jogo ele fez {g} gols.')
        print('\nDeseja realizar nova consulta?')
print('\nConsulta finalizada!')
