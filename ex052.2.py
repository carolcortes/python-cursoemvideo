print('\033[1;4m  VERIFICADOR DE NÚMEROS PRIMOS  \033[m')
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {t} vezes.')
ifprint('\033[1;4m  VERIFICADOR DE NÚMEROS PRIMOS  \033[m')
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {t} vezes.')
if t == 2:
    print('Por isso, ele \033[1;4;34mÉ UM NÚMERO PRIMO\033[m.')
else:
    print('Por isso, ele \033[1;4;31mNÃO É UM NÚMERO PRIMO\033[m.')
print('\033[1;4m ' * 32, '\033[m')
