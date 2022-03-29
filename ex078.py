lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f' • Você digitou os valores {lista}.')
print(f' • O maior valor digitado foi o {max(lista)} ', end='')
print(f'na posição {lista.index(max(lista))}.' if lista.counlista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f' • Você digitou os valores {lista}.')
print(f' • O maior valor digitado foi o {max(lista)} ', end='')
print(f'na posição {lista.index(max(lista))}.' if lista.count(max(lista)) == 1 else 'nas posições ', end='')
if lista.count(max(lista)) > 1:
    for i, v in enumerate(lista):
        if v == max(lista):
            print(f'{i}', end='  ')
print(f'\n • O menor valor digitado foi o {min(lista)} ', end='')
print(f'na posição {lista.index(min(lista))}.' if lista.count(min(lista)) == 1 else 'nas posições ', end='')
if lista.count(min(lista)) > 1:
    for i, v in enumerate(lista):
        if v == min(lista):
            print(f'{i}', end='  ')
