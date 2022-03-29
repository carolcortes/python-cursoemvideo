from time import sleep
print('\033[4mGERADOR DE MATRIZES\033[m:\n')
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para a posição [{l}][{c}]: '))
        if m[l][c] % 2 == 0:
            pares += m[l][c]
print('\n ➝ \033[4mGERANDO MATRIZ\033[m:\n')
sleep(1)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}from time import sleep
print('\033[4mGERADOR DE MATRIZES\033[m:\n')
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para a posição [{l}][{c}]: '))
        if m[l][c] % 2 == 0:
            pares += m[l][c]
print('\n ➝ \033[4mGERANDO MATRIZ\033[m:\n')
sleep(1)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
    sleep(1)
    print()
print(f'\n ◦ A soma dos valores pares digitados é {pares}.'
      f'\n ◦ A soma dos valores da 3ª coluna é {m[0][2] + m[1][2] + m[2][2]}.'
      f'\n ◦ O maior valor da segunda linha é {max(m[1])}')

