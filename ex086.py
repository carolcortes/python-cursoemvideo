from time import sleep
print('\033[4mGERADOR DE MATRIZES\033[m:\n')
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):  #for de linha
    for c in range(0, 3):  #for de coluna
        m[l][c] = int(input(f'Digite um valor para a posição [{l}][{c}]: '))
print('\n ➝ \033[4mGERANDO MATRIZ\033[m:\n')
sleep(1)
for l in range(0, 3):
    for c in ranfrom time import sleep
print('\033[4mGERADOR DE MATRIZES\033[m:\n')
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):  #for de linha
    for c in range(0, 3):  #for de coluna
        m[l][c] = int(input(f'Digite um valor para a posição [{l}][{c}]: '))
print('\n ➝ \033[4mGERANDO MATRIZ\033[m:\n')
sleep(1)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
    sleep(1)
    print()
