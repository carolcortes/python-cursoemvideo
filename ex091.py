from random import randint
from time import sleep
from operator import itemgetter
j = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
ranking = []
print('-' * 30, '\n → \033[1;4mVALORES SORTEADOS:\033[m')
sleep(1)
for k, v in j.items():
    print(f'{k}: {v}')
    sleep(1)
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)  # ordenar os itens, na posição do from random import randint
from time import sleep
from operator import itemgetter
j = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
ranking = []
print('-' * 30, '\n → \033[1;4mVALORES SORTEADOS:\033[m')
sleep(1)
for k, v in j.items():
    print(f'{k}: {v}')
    sleep(1)
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)  # ordenar os itens, na posição do itemgetter, decrescente.
print('-' * 30, f'\n → \033[1;4mRANKING:\033[m')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
