valores = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print('\n ⇨ \033[1;4mValores declarados em ordem crescente:\033[m'
      f'\n • Pares: {valores[0]}'
      f'\n • Ímpares: {valores[1]}')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     valores = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print('\n ⇨ \033[1;4mValores declarados em ordem crescente:\033[m'
      f'\n • Pares: {valores[0]}'
      f'\n • Ímpares: {valores[1]}')
