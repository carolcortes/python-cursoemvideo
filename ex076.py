p = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, \
    'Mochila', 120.32, 'Canetas', 2.3, 'Livro', 34.9
print('-' * 41)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 41)
for posicao in range(0, len(p)):
    if posicao % 2 == 0:
        print(f'{p[posicao]:.<32}', end='')
    if posicao % 2 != 0:
        print(f'R$ {p[posicao]:>6.2f}')
print('-' * 41)
                                                                                                                                                                                                                                                                                                                                                                                                                                  p = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, \
    'Mochila', 120.32, 'Canetas', 2.3, 'Livro', 34.9
print('-' * 41)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 41)
for posicao in range(0, len(p)):
    if posicao % 2 == 0:
        print(f'{p[posicao]:.<32}', end='')
    if posicao % 2 != 0:
        print(f'R$ {p[posicao]:>6.2f}')
print('-' * 41)
