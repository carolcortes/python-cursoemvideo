from random import sample
from time import sleep
x = '-*' * 13
print(f'{x}\n     \033[1;4mMEGA-SENA DO NENI\033[m\n{x}')
jogos = []
q = int(input('Quantos jogos deseja sortear? '))
print('-' * 33)
for j in range(0, q):
    jogos.append(sample(range(1, 61), 6))
    jogos[j].sort()
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
print('\nBOA SORTE!')
                                                                                                                                                                                                                                                                                                                                               from random import sample
from time import sleep
x = '-*' * 13
print(f'{x}\n     \033[1;4mMEGA-SENA DO NENI\033[m\n{x}')
jogos = []
q = int(input('Quantos jogos deseja sortear? '))
print('-' * 33)
for j in range(0, q):
    jogos.append(sample(range(1, 61), 6))
    jogos[j].sort()
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
print('\nBOA SORTE!')
