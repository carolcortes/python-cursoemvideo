from random import randint
x = '\033[1;4m¨\033[m' * 23
print(f'{x}\n  SORTERIO DE NUMEROS\n{x}')
n = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Os valores sorteados foram: ', end='')
for c in range(0, len(n)):
    print(f'{n[c]}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}.')
print(f'O menor valor sorteado foi {min(n)}.')
                                                                                                                                                                                                     from random import randint
x = '\033[1;4m¨\033[m' * 23
print(f'{x}\n  SORTERIO DE NUMEROS\n{x}')
n = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Os valores sorteados foram: ', end='')
for c in range(0, len(n)):
    print(f'{n[c]}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}.')
print(f'O menor valor sorteado foi {min(n)}.')
