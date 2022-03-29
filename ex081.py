numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if mais == 'N':
        break
numeros.sort(reverse=True)
print(f'\nForam digitados {len(numeros)} números.')
print(f'Os números digitados, em ordem decrescente, são {numeros}.')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista', end=' ')
    if numeros.count(5) == 1:
        print(f'na posição {numeros.index(5)}.')
  numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if mais == 'N':
        break
numeros.sort(reverse=True)
print(f'\nForam digitados {len(numeros)} números.')
print(f'Os números digitados, em ordem decrescente, são {numeros}.')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista', end=' ')
    if numeros.count(5) == 1:
        print(f'na posição {numeros.index(5)}.')
    else:
        print('nas posições', end=' ')
        for i, n in enumerate(numeros):
            if n == 5:
                print(f'{i}', end='  ')
else:
    print('O número 5 não faz parte da lista.')
