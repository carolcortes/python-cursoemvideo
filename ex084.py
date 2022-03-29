print('-' * 25)
p = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso (kg): ')))
    if len(p) == 0:  #se não cadastrei ninguém ainda
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    p.append(dados[:])
    dados.clear()
    print('-' * 25)
    mais = ' '
    while mais not in 'SN':
        mais = strprint('-' * 25)
p = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso (kg): ')))
    if len(p) == 0:  #se não cadastrei ninguém ainda
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    p.append(dados[:])
    dados.clear()
    print('-' * 25)
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if mais in 'N':
        break
print('-' * 25, f'\nForam cadastradas {len(p)} pessoas.')
print(f'O maior peso é {maior}kg de ', end='')
for i in p:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print(f'\nO menor peso é {menor}kg de ', end='')
for i in p:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')
