from random import randint
x = '\033[1;4m*=\033[m' * 16
xx = '-' * 33
print(f'{x}\n   Vamos jogar! PAR OU ÍMPAR?\n{x}')
cont = 0
while True:
    j = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P / I]: ')).strip().upper()[0]
    c = randint(0, 10)
    print(f'{xx}\nVocê from random import randint
x = '\033[1;4m*=\033[m' * 16
xx = '-' * 33
print(f'{x}\n   Vamos jogar! PAR OU ÍMPAR?\n{x}')
cont = 0
while True:
    j = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P / I]: ')).strip().upper()[0]
    c = randint(0, 10)
    print(f'{xx}\nVocê jogou {j} e o computador {c}.\nA soma de {j} + {c} é {j+c}.\nO RESULTADO É', end='')
    print(f' \033[1;4mPAR\033[m!\n{xx}' if (j+c) % 2 == 0 else f' \033[1;4mIMPAR\033[m!\n{xx}')
    if pi == 'P' and (j+c) % 2 == 0:
        print('Você GANHOU!\nVamos jogar novamente!\n')
    elif pi == 'I' and (j+c) % 2 != 0:
        print('Você GANHOU!\nVamos jogar novamente!\n')
    else:
        break
    cont += 1
print(f'Você perdeu!  -X-! \033[4mGAME OVER\033[m !-X-\n{xx}')
if cont > 1:
    print(f' ▶   Você venceu {cont} vezes.')
elif cont == 1:
    print(f' ▶   Você venceu {cont} vez.')
else:
    print(' ▶   Você não ganhou nenhuma vez.')
