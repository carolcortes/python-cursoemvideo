from random import randint
from time import sleep
jogada = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Suas opções:\n'
                    '[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n'
                    'Informe sua jogada: '))
if jogador >= 3:
    print('Jogada inválida. Tente novamente.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(0.5)
    print('\033[1m-=-' * 8, f'\nComputador jogou {jogada[computador]}\n'
                  f'Jogador jogou {jogada[jogador]}\n' + '-=-' * 8, '\033[m')
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')

    elif computador == 1:
        if jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')
    elif computador == 2:
        if jogador == 2:
            print('EMPATE!')
        elif jogador == 0:
            print('JOGADOR VENCE!')
        else:
            print('from random import randint
from time import sleep
jogada = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Suas opções:\n'
                    '[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n'
                    'Informe sua jogada: '))
if jogador >= 3:
    print('Jogada inválida. Tente novamente.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(0.5)
    print('\033[1m-=-' * 8, f'\nComputador jogou {jogada[computador]}\n'
                  f'Jogador jogou {jogada[jogador]}\n' + '-=-' * 8, '\033[m')
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')

    elif computador == 1:
        if jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')
    elif computador == 2:
        if jogador == 2:
            print('EMPATE!')
        elif jogador == 0:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')
