x = '\033[1;4m#\033[m' * 23
print(f'{x}\n  LOJÃO SUPER XANDÃO\n{x}')
total = mil = 0
barato = []
preco = []
while True:
    p = str(input('Nome do produto: ')).title()
    v = float(input('Preço: R$'))
    mais = ' '
    total += v
    if v > 1000:
        mil += 1
    barato.append(p)
    preco.append(v)
    while mais not in 'SN':
        mais = str(input('Deseja incluir mais produtos? [S / N]: ')).strip().upper()[0]
    print('-' * 15)
    if mais == 'N':
        break
print('{:^50}'.format('\033[1;4mCOMPRA FINALIZADA!\033[m'))
print(f' • O total da compra foi R${total:.2f}.\n • Temos {mil} produtos custando mais de R$1.000.00.\n'
      f' • O produto mais barato foi \"{barato[preco.index(min(preco))]}\" e custa R${min(preco):.2f}.')
         x = '\033[1;4m#\033[m' * 23
print(f'{x}\n  LOJÃO SUPER XANDÃO\n{x}')
total = mil = 0
barato = []
preco = []
while True:
    p = str(input('Nome do produto: ')).title()
    v = float(input('Preço: R$'))
    mais = ' '
    total += v
    if v > 1000:
        mil += 1
    barato.append(p)
    preco.append(v)
    while mais not in 'SN':
        mais = str(input('Deseja incluir mais produtos? [S / N]: ')).strip().upper()[0]
    print('-' * 15)
    if mais == 'N':
        break
print('{:^50}'.format('\033[1;4mCOMPRA FINALIZADA!\033[m'))
print(f' • O total da compra foi R${total:.2f}.\n • Temos {mil} produtos custando mais de R$1.000.00.\n'
      f' • O produto mais barato foi \"{barato[preco.index(min(preco))]}\" e custa R${min(preco):.2f}.')
