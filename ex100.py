from random import randint
from time import sleep
num, pares = [], []


def sorteio():
    print('  \033[1;4mSORTEANDO 5 VALORES:\033[m ', end='')
    for c in range(0, 5):
        num.append(randint(1, 10))
        print(num[c], end=' ')
        sleep(0.5)


def somapar():
    for valor in num:
        if valor % 2 == 0:
            pares.append(valor)
    print(f'\n → Os números pares informados são {pares}.\n'
          f' → A soma dos números pares é de {sum(pares)}.')


sfrom random import randint
from time import sleep
num, pares = [], []


def sorteio():
    print('  \033[1;4mSORTEANDO 5 VALORES:\033[m ', end='')
    for c in range(0, 5):
        num.append(randint(1, 10))
        print(num[c], end=' ')
        sleep(0.5)


def somapar():
    for valor in num:
        if valor % 2 == 0:
            pares.append(valor)
    print(f'\n → Os números pares informados são {pares}.\n'
          f' → A soma dos números pares é de {sum(pares)}.')


sorteio()
somapar()
