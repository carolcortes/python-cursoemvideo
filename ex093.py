gols = []
j = {'nome': str(input('Nome do jogador: ')).strip().title()}
p = int(input(f'Quantas partidas {j["nome"]} jogou? '))
for c in range(0, p):
    gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
j['gols'] = gols[:]
j['gtotal'] = sum(gols)
print('-' * 30, f'\nO jogador {j["nome"]} jogou {p} partidas.')
for i, v in enumerate(j["gols"]):
    print(f' → {i+1}ª partida: {v} gols')
print(f'• Foi um total de {j["gtotal"]} gols durante o campeonato.')
print('\n', j)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        gols = []
j = {'nome': str(input('Nome do jogador: ')).strip().title()}
p = int(input(f'Quantas partidas {j["nome"]} jogou? '))
for c in range(0, p):
    gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
j['gols'] = gols[:]
j['gtotal'] = sum(gols)
print('-' * 30, f'\nO jogador {j["nome"]} jogou {p} partidas.')
for i, v in enumerate(j["gols"]):
    print(f' → {i+1}ª partida: {v} gols')
print(f'• Foi um total de {j["gtotal"]} gols durante o campeonato.')
print('\n', j)
