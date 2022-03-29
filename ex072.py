x = '\033[1;4m¨\033[m' * 23
print(f'{x}\n  NÚMEROS POR EXTENSO\n{x}')
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente, ', end='')
    print(f'Você digitou o número {extenso[n]}.')
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if mais == 'N':
        break
print('\nPROGRAMA Fx = '\033[1;4m¨\033[m' * 23
print(f'{x}\n  NÚMEROS POR EXTENSO\n{x}')
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente, ', end='')
    print(f'Você digitou o número {extenso[n]}.')
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if mais == 'N':
        break
print('\nPROGRAMA FINALIZADO!')