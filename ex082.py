numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if mais == 'N':
        break
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
print(f'\nOs números digitados foram {numeros}.\n'
      f'Os números pares são {pares}.\n'
      f'Os números ímpares são {impares}.')
                                                                                                                                                                                                               numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if mais == 'N':
        break
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
print(f'\nOs números digitados foram {numeros}.\n'
      f'Os números pares são {pares}.\n'
      f'Os números ímpares são {impares}.')
