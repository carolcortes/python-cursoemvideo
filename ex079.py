valores = []
while True:
    v = int(input('Digite um número: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Não é permitido valores duplicados na lista.')
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja adicionar mais um valor? [S/N]: ')).upper().split()[0]
    if mais == 'N':
        break
print('-=' * 20)
print(f'Você digitou os valores {sorted(valores)}')
                                                                                                                                                                                                                                                                                                             valores = []
while True:
    v = int(input('Digite um número: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Não é permitido valores duplicados na lista.')
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja adicionar mais um valor? [S/N]: ')).upper().split()[0]
    if mais == 'N':
        break
print('-=' * 20)
print(f'Você digitou os valores {sorted(valores)}')
